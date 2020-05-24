join challenges

#  Joins!

Clicking "Run query" will run the query with SQLite.

#  ★★★ challenges ★★★

#  How many cats does each owner have?

Make a query that outputs, for each owner in the cat_owners table:

- the owner name

- how many cats they have

- the total number of activities their cats have done

Sort by number of activities descending.

# tables

`cats`

| owner | name |
| --- | --- |
| 1   | mr darcy |
| 1   | lady catherine |
| 2   | bella |
| 4   | simba |
| 4   | luna |
| 4   | max |

`cat_owners`

| owner | name |
| --- | --- |
| 1   | mandy |
| 2   | mary |
| 3   | marshal |

`cat_activities`

| name | activity | time |
| --- | --- | --- |
| bella | eat | 1   |
| bella | sleep | 2   |
| bella | purr | 3   |
| lady catherine | sleep | 4   |
| simba | sleep | 5   |
| max | eat | 6   |
| luna | eat | 7   |
| luna | purr | 8   |
| luna | sleep | 9   |
| mr darcy | sleep | 10  |

Results you want

| name | num_cats | num_activities |
| --- | --- | --- |
| mary | 1   | 3   |
| mandy | 2   | 2   |
| marshal | 0   | 0   |

#  Which activity do cats like the best?

Make a query that outputs, for every activity, how many cats have done that activity

Sort the activities alphabetically.

# tables

`cats`

| owner | name |
| --- | --- |
| 1   | mr darcy |
| 1   | lady catherine |
| 2   | bella |
| 4   | simba |
| 4   | luna |
| 4   | max |

`cat_activities`

| name | activity | time |
| --- | --- | --- |
| bella | eat | 1   |
| bella | sleep | 2   |
| bella | purr | 3   |
| lady catherine | sleep | 4   |
| simba | sleep | 5   |
| max | eat | 6   |
| luna | eat | 7   |
| luna | purr | 8   |
| luna | sleep | 9   |
| mr darcy | sleep | 10  |

Results you want

| activity | num_cats |
| --- | --- |
| eat | 3   |
| purr | 2   |
| sleep | 5   |

#  Find cats with no owners

For every cat with no owners, find the number of times they did the 'sleep' activity.

Order the cats alphabetically by name.

# tables

`cats`

| owner | name |
| --- | --- |
| 1   | mr darcy |
| 1   | lady catherine |
| 2   | bella |
| 4   | simba |
| 4   | luna |
| 4   | max |

`cat_activities`

| name | activity | time |
| --- | --- | --- |
| bella | eat | 1   |
| bella | sleep | 2   |
| bella | purr | 3   |
| lady catherine | sleep | 4   |
| simba | sleep | 5   |
| max | eat | 6   |
| luna | eat | 7   |
| luna | purr | 8   |
| luna | sleep | 9   |
| mr darcy | sleep | 10  |

`cat_owners`

| owner | name |
| --- | --- |
| 1   | mandy |
| 2   | mary |
| 3   | marshal |

Results you want

| name | times_slept |
| --- | --- |
| luna | 1   |
| max | 0   |
| simba | 1   |