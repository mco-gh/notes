Using BigQuery’s New ML.NGRAMS() Function To Construct 122 Years Of Book NGrams With One Line Of SQL – The GDELT Project

# [Using BigQuery's New ML.NGRAMS() Function To Construct 122 Years Of Book NGrams With One Line Of SQL](https://blog.gdeltproject.org/using-bigquerys-new-ml-ngrams-function-to-construct-122-years-of-book-ngrams-with-one-line-of-sql/)

 ** January 9, 2020

   [![ocaandgooglebooks.jpg](../_resources/78f27f87b37f3325eeb23b9f533dc18b.jpg)](https://blog.gdeltproject.org/using-bigquerys-new-ml-ngrams-function-to-construct-122-years-of-book-ngrams-with-one-line-of-sql/)

Back in 2016 we [showed](https://blog.gdeltproject.org/making-ngrams-bigquery-scale/) how you could [construct ngrams](https://blog.gdeltproject.org/making-ngrams-bigquery-scale/) from 122 years of public domain books (1800 to 1922) from the Internet Archive using BigQuery. While incredibly powerful for the time and requiring just a single SQL statement, the logic necessary to construct ngrams in the legacy SQL of the time meant the resulting queries were long and complex. With BigQuery's new [ML.NGRAMS()](https://cloud.google.com/bigquery-ml/docs/reference/standard-sql/bigqueryml-preprocessing-functions#mlngrams) feature, BigQuery can now convert word arrays into shingles automatically with a single command, eliminating all of the complexity of the original queries. What would it look like to apply this to 122 years of public domain books?

The public domain Internet Archive books collection in BigQuery predates BigQuery's support for modern partitioning and thus is stored as a set of per-year tables, with the tables for 1800-1922 containing a column "BookMeta_FullText" that stores the fulltext, while the 1923-2014 tables contain only metadata and thus lack this field.

Using BigQuery Standard SQL table wildcards we can count the total number of public domain books and total number of fulltext characters in their OCR:

> 

> select DATE, count, txtlen from (SELECT DATE, count(1) count, sum(length(BookMeta_FullText)) txtlen FROM `gdelt-bq.internetarchivebooks.18*` GROUP BY DATE)

> UNION ALL

> (SELECT DATE, count(1) count, sum(length(BookMeta_FullText)) txtlen FROM `gdelt-bq.internetarchivebooks.190*` GROUP BY DATE)

> UNION ALL

> (SELECT DATE, count(1) count, sum(length(BookMeta_FullText)) txtlen FROM `gdelt-bq.internetarchivebooks.191*` GROUP BY DATE)

> UNION ALL

> (SELECT DATE, count(1) count, sum(length(BookMeta_FullText)) txtlen FROM `gdelt-bq.internetarchivebooks.1920` GROUP BY DATE)

> UNION ALL

> (SELECT DATE, count(1) count, sum(length(BookMeta_FullText)) txtlen FROM `gdelt-bq.internetarchivebooks.1921` GROUP BY DATE)

> UNION ALL

> (SELECT DATE, count(1) count, sum(length(BookMeta_FullText)) txtlen FROM `gdelt-bq.internetarchivebooks.1922` GROUP BY DATE)

> order by DATE asc
> 
In all, there were 998,655 books totaling 445,349,814,757 bytes of text.

While we could leave the text in-place and query this combined set of tables directly, we're going to extract the publication date and fulltext column into a new temporary table to make our ngrams examples simpler to understand.

Compiling the fulltext into a new temporary table is simple:
> 

> select DATE, BookMeta_FullText from (SELECT DATE, BookMeta_FullText FROM `gdelt-bq.internetarchivebooks.18*`)

> UNION ALL
> (SELECT DATE, BookMeta_FullText FROM `gdelt-bq.internetarchivebooks.190*`)
> UNION ALL
> (SELECT DATE, BookMeta_FullText FROM `gdelt-bq.internetarchivebooks.191*`)
> UNION ALL
> (SELECT DATE, BookMeta_FullText FROM `gdelt-bq.internetarchivebooks.1920`)
> UNION ALL
> (SELECT DATE, BookMeta_FullText FROM `gdelt-bq.internetarchivebooks.1921`)
> UNION ALL
> (SELECT DATE, BookMeta_FullText FROM `gdelt-bq.internetarchivebooks.1922`)
> 

Compiling a single unigram table is trivial and doesn't even require the new ML.NGRAMS() function:

> 

> SELECT ngram, count(1) count FROM `[TEMPORARYTABLE]`, UNNEST(SPLIT(REGEXP_REPLACE(LOWER(BookMeta_FullText), r'(\pP)', r' \1 '), ' ')) as ngram group by ngram

> 

In a single line of SQL, this query lowercases the text in Unicode-aware fashion, splits it into spaces using Unicode-aware punctuation rules (this is a naive approach that can be impacted by OCR error but will still preserve the major ngram patterns at scale) and splits the final text into words based on spaces. Since a SPLIT() under Standard SQL yields an array, UNNEST() is used to flatten the results back into individual rows.

Taking just 1 minute 57 seconds, this query processes all 446 billion characters of text into 471,828,100 distinct words occurring 115,206,925,267 total times, working out to around 115,362 words per book. The large number of distinct words and large number of words per book suggests OCR error yielded a large number of distinct words with internal punctuation mistakenly taking the place of letters (such as the number one replacing the lowercase letter "L").

Simply by adding "group by DATE" to the query above we can generate a per-year unigram dataset:

> 

> SELECT DATE, ngram, count(1) count FROM `[TEMPORARYTABLE]`, UNNEST(SPLIT(REGEXP_REPLACE(LOWER(BookMeta_FullText), r'(\pP)', r' \1 '), ' ')) as ngram group by DATE, ngram

> 

This yields 1,116,548,353 distinct year-word pairings in 3 minutes 9 seconds of compute time. The relatively low record count increase from breaking down in 122 years reinforces the hypothesis that much of the distinct word volume are OCR errors that appear only in a single year.

While it is not necessary for unigrams, it is trivial to modify the above query to use the new ML.NGRAMS() function:

> 

> SELECT DATE, ngram, count(1) count FROM `[TEMPORARYTABLE]`, UNNEST(ML.NGRAMS(SPLIT(REGEXP_REPLACE(LOWER(BookMeta_FullText), r'(\pP)', r' \1 '), ' '), [1,1], ' ')) as ngram group by DATE, ngram

> 
This yields the same result as above.

The power of ML.NGRAMS() comes in when we want to move beyond individual words towards bigrams, trigrams, quadgrams, five-grams and the like. We have to change only a single argument in the query above to switch from unigrams to computing 1-grams, 2-grams, 3-grams, 4-grams and 5-grams combined all in a single query:

> 

> SELECT DATE, ngram, count(1) count FROM `[TEMPORARYTABLE]`, UNNEST(ML.NGRAMS(SPLIT(REGEXP_REPLACE(LOWER(BookMeta_FullText), r'(\pP)', r' \1 '), ' '), [1,5], ' ')) as ngram group by DATE, ngram

> 

That's literally all there is to it – just changing the "[LOWERBOUND, UPPERBOUND]" parameter of ML.NGRAMS() from "[1,1]" which generates only unigrams to "[1,5]" which generates 1-grams, 2-grams, 3-grams, 4-grams and 5-grams all at once.

This single line of SQL basically does the equivalent work of the original [Google Books NGrams dataset](http://storage.googleapis.com/books/ngrams/books/datasetsv2.html) (though with a slightly different mix of books and without the preprocessing steps of the former) in just 2 hours and 2 minutes, yielding a final dataset of 113,775,545,338 distinct date-ngram pairs totaling 576,045,801,155 total appearances.

Putting this all together, BigQuery's powerful new built-in ngramming capability means we were able to construct 114 billion distinct 1-grams, 2-grams, 3-grams, 4-grams and 5-grams by year from 122 years of public domain books totaling 446 billion characters of text in just 2 hours with just a single line of SQL!