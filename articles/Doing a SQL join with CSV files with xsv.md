Doing a SQL join with CSV files with xsv

# Doing a database join with CSV files

Posted on [31 December 2019](https://www.johndcook.com/blog/2019/12/31/sql-join-csv-files/) by [John](https://www.johndcook.com/blog/author/john/)

It’s easy to manipulate CSV files with basic command line tools until you need to do a join. When your data is spread over two different files, like two tables in a normalized database, joining the files is more difficult unless the two files have the same keys in the same order. Fortunately, the [xsv](https://github.com/BurntSushi/xsv) utility is just the tool for the job. Among other useful features, `xsv` supports database-like joins.

Suppose you want to look at weights broken down by sex, but weights are in one file and sex is in another. The weight file alone doesn’t tell you whether the weights belong to men or women.

Suppose a file `weight.csv` has the following rows:
ID,weight
123,200
789,155
999,160
and a file `person.csv` has the following:
ID,sex
123,M
456,F
789,F

Note that the two files have different `ID` values: 123 and 789 are in both files, 999 is only in `weight.csv` and 456 is only in `person.csv`. We want to join the two tables together, analogous to the `JOIN` command in SQL.

The command
xsv join ID person.csv ID weight.csv
does just this, producing
ID,sex,ID,weight
123,M,123,200
789,F,789,155
by joining the two tables on their `ID` columns.

The command includes `ID` twice, once for the field called `ID` in `person.csv` and once for the field called ID in `weight.csv`. The fields could have different names. For example, if the first column of `person.csv` were renamed `Key`, then the command

xsv join Key person.csv ID weight.csv
would produce
Key,sex,ID,weight
123,M,123,200
789,F,789,155

We’re not interested in the `ID` columns per se; we only want to use them to join the two files. We could suppress them in the output by asking `xsv` to select the second and fourth columns of the output

xsv join Key person.csv ID weight.csv | xsv select 2,4
which would return
sex,weight
M,200
F,155

We can do other kinds of joins by passing a modifier to join. For example, if we do a **left join**, we will include all rows in the left file, `person.csv`, even if there isn’t a match in the right file, `weight.csv`. The weight will be missing for such records, and so

$ xsv join --left Key person.csv ID weight.csv
produces
Key,sex,ID,weight
123,M,123,200
456,F,,
789,F,789,155

**Right joins** are analogous, including every record from the second file, and so

xsv join --right Key person.csv ID weight.csv
produces
Key,sex,ID,weight
123,M,123,200
789,F,789,155
,,999,160
You can also do a **full join**, with
xsv join --full Key person.csv ID weight.csv
producing
Key,sex,ID,weight
123,M,123,200
456,F,,
789,F,789,155
,,999,160

## Related posts

- [Munging CSV files with cut, sort, and awk](https://www.johndcook.com/blog/2019/08/30/cut-sort-awk/)
- [Exporting Excel files to CSV](https://www.johndcook.com/blog/2019/12/30/excel-to-csv/)
- [Wrangling wide files with cut](https://www.johndcook.com/blog/2019/08/28/cut/)

Categories : [Computing](https://www.johndcook.com/blog/category/computing/)

Bookmark the [permalink](https://www.johndcook.com/blog/2019/12/31/sql-join-csv-files/)