Quip

CONCATENTATE(STR(bin_label*5), '-', STR(`bin_label*5+5)) bucket, [[NEWLINE]]    COUNT(DISTINCT session_id) count `

 GROUP BY
    bin_label
 Yellow HighlightORDER BY
    `bin_label ASC `End of Yellow Highlight

#2: CROSS JOIN (multi-part)
Part 1:

**Context:** Say we have a table `state_streams` where each row is a state and the total number of hours of streaming from a video hosting service:

| state | total_streams |

|-------|---------------|

| NC    |  34569         |
| SC    |  33999         |
| CA    |  98324         |
| MA    |  19345         |
|  ..    |  ..            |

(In reality these kinds of aggregate tables would normally have a date column, but we’ll exclude that component in this problem)

**Task:** Write a query to get the pairs of states with total streaming amounts within 1000 of each other. For the snippet above, we would want to see something like:

| state_a | state_b |

|---------|---------|

| NC      | SC      |
| SC      | NC      |

* * *

***Solution:***
SELECT
    a.state as state_a,
    b.state as state_b
 FROM
    state_streams a
 CROSS JOIN
    state_streams b
 WHERE
    ABS(a.total_streams - b.total_streams)  <  1000
    AND
    a.state <> b.state
FYI, `CROSS JOIN` s can also be written without explicitly specifying a join:
SELECT
    a.state as state_a,
    b.state as state_b
 FROM
    state_streams a, state_streams b
 WHERE
    ABS(a.total_streams - b.total_streams)  <  1000
    AND
    a.state <> b.state

Part 2:

**Note:** This question is considered more of a bonus problem than an actual SQL pattern. Feel free to skip it!

**Task:** How could you modify the SQL from the solution to Part 1 of this question so that duplicates are removed? For example, if we used the sample table from Part 1, the pair `NC` and `SC` should only appear in one row instead of two.

* * *

***Solution: ***
SELECT
    a.state as state_a,
    b.state as state_b
 FROM
    state_streams a, state_streams b
 WHERE
    ABS(a.total_streams - b.total_streams)  <  1000
    AND
    a.state > b.state

#3: Advancing Counting

**Acknowledgement:** This question is adapted from [﻿this Stack Overflow question﻿](https://stackoverflow.com/questions/54488894/using-case-to-properly-count-items-with-if-else-logic-in-sql) by me (zthomas.nc)

**Note:** this question is probably more complex than the kind you would encounter in an interview. Consider it a challenge problem, or feel free to skip it!

**Context: **Say I have a table `table` in the following form, where a `user` can be mapped to multiple values of `class`:

| user |  class  |

|------|-------|

|  1    | a     |
|  1    | b     |
|  1    | b     |
|  2    | b     |
|  3    | a     |

**Task:** Assume there are only two possible values for `class`. Write a query to count the number of users in each class such that any user who has label `a` and `b` gets sorted into `b`, any user with just `a` gets sorted into `a` and any user with just `b` gets into `b`.

For `table` that would result in the following table:

|  class  | count |

|-------|-------|

| a     |  1     |

 | b     |  2     |

* * *

***Solution: ***
WITH usr_b_sum AS
(
    SELECT
        user,
        SUM(CASE WHEN class = 'b' THEN 1 ELSE 0 END) num_b
    FROM
        table
    GROUP BY
        user
),

usr_class_label AS
(
    SELECT
        user,
        CASE WHEN num_b > 0 THEN 'b' ELSE 'a' END class
    FROM
        usr_b_sum
)

SELECT
    class,
    COUNT(DISTINCT user) count
FROM
    usr_class_label
GROUP BY
    class
ORDER BY
    class ASC

Alternate solution: Using `SELECT`s in the `SELECT` statement and `UNION`:
SELECT
    "a"  class,
    COUNT(DISTINCT user_id)  -
        (SELECT COUNT(DISTINCT user_id) FROM table WHERE class  =  'b') count
UNION
SELECT
    "b"  class,
    (SELECT COUNT(DISTINCT user_id) FROM table WHERE class  =  'b') count