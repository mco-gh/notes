zygmuntz/goodbooks-10k

###    README.md

# [(L)](https://github.com/zygmuntz/goodbooks-10k?utm_campaign=Revue%20newsletter&utm_medium=Newsletter&utm_source=The%20Wild%20Week%20in%20AI#goodbooks-10k)goodbooks-10k

This dataset contains six million ratings for ten thousand most popular (with most ratings) books. There are also:

- books marked to read by the users
- book metadata (author, year, etc.)
- tags/shelves/genres

## [(L)](https://github.com/zygmuntz/goodbooks-10k?utm_campaign=Revue%20newsletter&utm_medium=Newsletter&utm_source=The%20Wild%20Week%20in%20AI#access)Access

Some of these files are quite large, so GitHub won't show their contents online. See [samples/](https://github.com/zygmuntz/goodbooks-10k/blob/master/samples) for smaller CSV snippets.

Open the [notebook](https://github.com/zygmuntz/goodbooks-10k/blob/master/quick_look.ipynb) for a quick look at the data.

Download individual zipped files from [releases](https://github.com/zygmuntz/goodbooks-10k/releases).

The dataset is accessible from [Spotlight](https://maciejkula.github.io/spotlight/datasets/goodbooks.html), recommender software based on PyTorch.

## [(L)](https://github.com/zygmuntz/goodbooks-10k?utm_campaign=Revue%20newsletter&utm_medium=Newsletter&utm_source=The%20Wild%20Week%20in%20AI#contents)Contents

**ratings.csv** contains ratings sorted by time. It is 69MB and looks like that:

	user_id,book_id,rating
	1,258,5
	2,4081,4
	2,260,5
	2,9296,5
	2,2318,3

Ratings go from one to five. Both book IDs and user IDs are contiguous. For books, they are 1-10000, for users, 1-53424.

**to_read.csv** provides IDs of the books marked "to read" by each user, as *user_id,book_id* pairs, sorted by time. There are close to a million pairs.

**books.csv** has metadata for each book (goodreads IDs, authors, title, average rating, etc.). The metadata have been extracted from goodreads XML files, available in ` books_xml `.

### [(L)](https://github.com/zygmuntz/goodbooks-10k?utm_campaign=Revue%20newsletter&utm_medium=Newsletter&utm_source=The%20Wild%20Week%20in%20AI#tags)Tags

**book_tags.csv** contains tags/shelves/genres assigned by users to books. Tags in this file are represented by their IDs. They are sorted by *goodreads_book_id* ascending and *count* descending.

In raw XML files, tags look like this:

	<popular_shelves>
		<shelf name="science-fiction" count="833"/>
		<shelf name="fantasy" count="543"/>
		<shelf name="sci-fi" count="542"/>
		...
		<shelf name="for-fun" count="8"/>
		<shelf name="all-time-favorites" count="8"/>
		<shelf name="science-fiction-and-fantasy" count="7"/>
	</popular_shelves>

Here, each tag/shelf is given an ID. **tags.csv** translates tag IDs to names.

### [(L)](https://github.com/zygmuntz/goodbooks-10k?utm_campaign=Revue%20newsletter&utm_medium=Newsletter&utm_source=The%20Wild%20Week%20in%20AI#goodreads-ids)goodreads IDs

Each book may have many editions. *goodreads_book_id* and *best_book_id* generally point to the most popular edition of a given book, while goodreads *work_id* refers to the book in the abstract sense.

You can use the goodreads book and work IDs to create URLs as follows:
https://www.goodreads.com/book/show/2767052
https://www.goodreads.com/work/editions/2792775

Note that *book_id* in **ratings.csv** and **to_read.csv** maps to *work_id*, not to *goodreads_book_id*, meaning that ratings for different editions are aggregated.