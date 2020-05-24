Analyzing text in a Google Sheet using Cloud Natural Language API and Apps Script | Google Cloud Big Data and Machine Learning Blog  |  Google Cloud Platform

 ![](../_resources/6c87978deeaace9b956c3205f1927ee7.png)

## Analyzing text in a Google Sheet using Cloud Natural Language API and Apps Script

Friday, December 1, 2017

*By [Alicia Williams](https://twitter.com/presactlyalicia), Cloud Advocate*

There are many formulas in Google Sheets for analyzing quantitative data, but spreadsheets often capture valuable text data as well. Text data in Google Sheets can come from many sources: Google Form responses, notes columns, descriptions, and more. As humans we can make sense of this data by reading it, but this becomes difficult as your data grows into hundreds or thousands of rows.

[Cloud Natural Language](https://cloud.google.com/natural-language/) (Cloud NL) takes the machine learning technology used by Google Search and Google Assistant and makes it possible for anyone to perform syntax analysis, sentiment analysis, and entity analysis with their own data. Cloud NL is accessible from Google Sheets with a few lines of [Apps Script](https://www.google.com/script/start/), and can help extract meaning from text data in a scalable way.

In this post, we’ll import a Kaggle dataset into Google Sheets, write some Apps Script to send our text data to Cloud NL, and visualize the results in Data Studio.

![](../_resources/dd6b120c1bad742be2acc68c7668a061.png)

### Importing data into Sheets

The [Boston Airbnb Open Data dataset](https://www.kaggle.com/airbnb/boston) on [Kaggle](https://www.kaggle.com/datasets) includes a snapshot of guest reviews for thousands of Airbnb listings in Boston. One listing can have hundreds of reviews, which makes this data an ideal candidate for Cloud NL.

Due to the large size of [the dataset files](https://www.kaggle.com/airbnb/boston/data), we’ll select just one listing for this analysis, listing_id=66288. From reviews.csv, we’ll load the 400+ reviews for the selected listing into a Google Sheets spreadsheet. Then we’ll [import and insert the listings.csv data as an additional sheet](https://support.google.com/docs/answer/40608) in this same spreadsheet.

### Pre-processing data with the Google Sheets' built-in translation function

For our analysis, we will use Cloud NL to identify the entities mentioned in the reviews (think “parking”, “location”, “wifi”, etc.), and determine the sentiment (positive or negative) expressed with regard to these entities.

The Cloud NL method we’ll be using, [entity sentiment analysis](https://cloud.google.com/natural-language/docs/analyzing-entity-sentiment), currently supports English. Since the comment text in our data is in several languages, we’ll translate the text to English before sending it to Cloud NL. Google Sheets has two built-in functions that easily make this happen: [DETECTLANGUAGE](https://support.google.com/docs/answer/3093278) and [GOOGLETRANSLATE](https://support.google.com/docs/answer/3093331).

![](../_resources/2c1d535ce205c2c5f181517df4296c5d.png)

### Sending text data to Cloud Natural Language

Now, we are ready to write some Apps Script to manage the API calls and add the Cloud NL data to our sheet.

First, we’ll write a function called `retrieveEntitySentiment` that takes a line of text as a parameter and queries the `[analyzeEntitySentiment](https://cloud.google.com/natural-language/docs/analyzing-entity-sentiment)` method of Cloud NL. Calling this method requires a Google Cloud Platform account and project, [enabling the Google Natural Language API](https://support.google.com/cloud/answer/6158841), and [creating an API key](https://support.google.com/cloud/answer/6158862?hl=en&ref_topic=6262490). In the function, we will provide this API key, the request URL, and our request body for `analyzeEntitySentiment`. The request body includes our text along with its language and type, and a field called `[encodingType](https://cloud.google.com/natural-language/docs/reference/rest/v1/EncodingType)`. Once our request JSON is ready, the function will call the endpoint and parse the JSON response with the entities and related sentiment.

hdr_strong

	function retrieveEntitySentiment (line) {
	 var apiKey = "your key here";
	 var apiEndpoint = https://language.googleapis.com/v1/documents:analyzeEntitySentiment?key=' + apiKey;
	 // Create our json request, w/ text, language, type & encoding
	  var nlData = {
	   document: {
	     language: 'en-us',
	     type: 'PLAIN_TEXT',
	     content: line
	   },
	   encodingType: 'UTF8'  };
	 //  Package all of the options and the data together for the call
	 var nlOptions = {
	   method : 'post',
	   contentType: 'application/json',
	   payload : JSON.stringify(nlData)
	 };
	 //  And make the call
	 var response = UrlFetchApp.fetch(apiEndpoint, nlOptions);
	 return JSON.parse(response);
	};

([link to gist](https://gist.github.com/aliciawilliams/2f27bb592d16109c8c977dab5302af13))

When using API keys, [take care to keep them secure](https://support.google.com/cloud/answer/6310037?hl=en&ref_topic=6262490). You may also consider [alternative methods to authenticate](https://cloud.google.com/natural-language/docs/auth), including [using a service account](https://github.com/googlesamples/apps-script-oauth2).

Now we can incorporate this function into our primary function, let’s call it `markEntitySentiment`. This primary function will identify which reviews have not yet been sent to Cloud NL, call the `retrieveEntitySentiment` function, and record the response data in a format ready for further analysis. We will also set variables that identify the review sheet and index the columns we will need to reference.

hdr_strong

	function markEntitySentiment() {
	 // set variables for reviewData sheet
	 var ss = SpreadsheetApp.getActiveSpreadsheet();
	 var dataSheet = ss.getSheetByName('reviewData');
	 var rows = dataSheet.getDataRange();
	 var numRows = rows.getNumRows();
	 var values = rows.getValues();
	 var headerRow = values[0];

	 // checks to see if entitySentiment sheet is present; if not, creates new sheet and sets header row
	 var entitySheet = ss.getSheetByName('entitySentiment');
	 if (entitySheet == null) {
	  ss.insertSheet('entitySentiment');
	  var entitySheet = ss.getSheetByName('entitySentiment');
	  var esHeaderRange = entitySheet.getRange(1,1,1,6);
	  var esHeader = [['Review ID','Entity','Salience','Sentiment Score','Sentiment Magnitude','Number of mentions']];
	  esHeaderRange.setValues(esHeader);
	 };

	 // find the column index for comments, language_detected, comments_english
	 var commentsColumnIdx = headerRow.indexOf(COLUMN_NAME.COMMENTS);
	 var languageColumnIdx = headerRow.indexOf(COLUMN_NAME.LANGUAGE);
	 var translationColumnIdx = headerRow.indexOf(COLUMN_NAME.TRANSLATION);
	 var entityColumnIdx = headerRow.indexOf(COLUMN_NAME.ENTITY);
	 var idColumnIdx = headerRow.indexOf(COLUMN_NAME.ID);

([link to gist](https://gist.github.com/aliciawilliams/2f27bb592d16109c8c977dab5302af13))

In the next part of the function, we will process each row, calling Cloud NL for each review comment. We will call the API only for rows that contain a text comment, and also have not already been processed in a previous run. By building this check into our code, we can set the function to run on various [triggers](https://developers.google.com/apps-script/guides/triggers/), such as on form submit, on edit, or on a regular pre-defined time interval.

hdr_strong

	 ss.toast("Analyzing entities and sentiment...");
	 // Process each row
	 for (var i = 0; i < numRows; ++i) {
	   var value = values[i];
	   var commentEnCellVal = value[translationColumnIdx];
	   var entityCellVal = value[entityColumnIdx];
	   var reviewId = value[idColumnIdx];

	   // Call retrieveEntitySentiment function for each row that has comments and also an empty entity_sentiment cell
	   if(commentEnCellVal && !entityCellVal) {
	       var nlData = retrieveEntitySentiment(commentEnCellVal);
	       // Paste each entity and sentiment score into entitySentiment sheet
	       for (var j = 0; j < nlData.entities.length; ++j) {
	         var entityInResponse = nlData.entities[j];
	         var lastRowIdx = entitySheet.getLastRow() + 1;
	         var newValues = [[reviewId, entityInResponse.name, entityInResponse.salience, entityInResponse.sentiment.score, entityInResponse.sentiment.magnitude, entityInResponse.mentions.length]];
	         var pastingRange = entitySheet.getRange(lastRowIdx,1,1,6);
	         pastingRange.setValues(newValues);
	       }
	       // Paste "complete" into entity_sentiment column to denote completion of NL API call
	       dataSheet.getRange(i+1, entityColumnIdx+1).setValue("complete");
	    }
	  }
	};

([link to gist](https://gist.github.com/aliciawilliams/2f27bb592d16109c8c977dab5302af13))

Now that our Apps Script is complete, we are ready to run markEntitySentiment and watch the response data stream into the entitySentiment tab.

![](../_resources/755f8fb098cffebc1aef678de79a2132.png)

### Visualizing NL insights with Data Studio

Once the script finishes running, we’ll find we have over 5,000 rows of data in the entitySentiment sheet! Now to visualize the results. [Google Data Studio (beta)](https://www.google.com/analytics/data-studio/) is a reporting and visualization tool with built-in connections to several data sources, including Google Sheets. Data Studio makes it possible to share interactive dashboards while helping to protect the security of the raw data.

To get started, we’ll navigate to [datastudio.google.com](https://datastudio.google.com/), start a new report, and create a new data source. After choosing the Google Sheets connector, we’ll be able to add our entitySentiment and listings sheets as data sources for our report.

![sheets-nl-4.gif](../_resources/5176b76d7976a4ed323c1e1931b874be.gif)

Data Studio has several chart options to choose from. In our report, we’ll start with two simple tables showing the entities by average sentiment and number of mentions for both the most positive and negative entities.

![](../_resources/76bce4e40a0e1b5aea0939964ddde9dc.png)

Adding in rating data from the listings tab, we will use scorecard charts to show our listing’s ratings against the average ratings across all Boston properties. Data Studio also offers a geo map chart that shows us the location of the listing using latitude and longitude coordinates from the data.

Take a look at the final product, as an interactive web embed! With just a few clicks, Data Studio will give you the code snippet you need to [embed your report into a web page](https://support.google.com/datastudio/answer/7450249?hl=en), making it available to the public or to a certain set of users.

### Get started

Try submitting an example of your own text on the [Cloud NL product page](https://cloud.google.com/natural-language/) to instantly see the API response. Once you determine which insights are important to you, copy and paste [the code from this tutorial](https://gist.github.com/aliciawilliams/2f27bb592d16109c8c977dab5302af13) into your own sheet, and adjust it for your needs using the product documentation for [Cloud NL](https://cloud.google.com/natural-language/docs/) and [Apps Script](https://developers.google.com/apps-script/reference/spreadsheet/).

If you’re new to Apps Script and Javascript, Codecademy’s [Introduction to Javascript](https://www.codecademy.com/learn/introduction-to-javascript) course  provides a helpful foundation, and the [Google Apps Script intro codelab](https://codelabs.developers.google.com/codelabs/apps-script-intro) will teach you how to write and interact with Apps Script in a sheet.