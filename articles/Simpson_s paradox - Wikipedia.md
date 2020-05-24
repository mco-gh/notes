Simpson's paradox - Wikipedia

# Simpson's paradox

From Wikipedia, the free encyclopedia

[![220px-Simpson's_paradox_continuous.svg.png](../_resources/7c415edd688077f982a27b36622510f2.png)](https://en.wikipedia.org/wiki/File:Simpson%27s_paradox_continuous.svg)

Simpson's paradox for quantitative data: a positive trend (, ) appears for two separate groups, whereas a negative trend () appears when the groups are combined.

**Simpson's paradox**, or the **Yule–Simpson effect**, is a phenomenon in [probability](https://en.wikipedia.org/wiki/Probability) and [statistics](https://en.wikipedia.org/wiki/Statistics), in which a trend appears in several different groups of data but disappears or reverses when these groups are combined. It is sometimes given the descriptive title **reversal paradox** or **amalgamation paradox**.[[1]](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_note-1)

This result is often encountered in social-science and medical-science statistics[[2]](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_note-2)[[3]](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_note-3)[[4]](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_note-VogelFranks2017-4) and is particularly problematic when frequency data is unduly given [causal](https://en.wikipedia.org/wiki/Causal) interpretations.[[5]](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_note-pearl-5) The paradoxical elements disappear when causal relations are brought into consideration.[[6]](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_note-6) It has been used to try and inform the non-specialist or public audience about the kind of misleading results mis-applied statistics can generate.[[7]](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_note-7)[[8]](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_note-8)  [Martin Gardner](https://en.wikipedia.org/wiki/Martin_Gardner) wrote a popular account of Simpson's paradox in his March 1976 [Mathematical Games column](https://en.wikipedia.org/wiki/Mathematical_Games_column) in *[Scientific American](https://en.wikipedia.org/wiki/Scientific_American)*.[[9]](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_note-9)

[Edward H. Simpson](https://en.wikipedia.org/wiki/Edward_H._Simpson) first described this phenomenon in a technical paper in 1951,[[10]](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_note-10) but the statisticians [Karl Pearson](https://en.wikipedia.org/wiki/Karl_Pearson) et al., in 1899,[[11]](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_note-11) and [Udny Yule](https://en.wikipedia.org/wiki/Udny_Yule), in 1903,[[12]](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_note-yule-12) had mentioned similar effects earlier. The name *Simpson's paradox* was introduced by Colin R. Blyth in 1972.[[13]](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_note-blyth-72-13)

## Description[]

[![220px-Simpson_paradox_balances.svg.png](../_resources/9f72c48cba3cd3d796ea60bd611f0029.png)](https://en.wikipedia.org/wiki/File:Simpson_paradox_balances.svg)

Illustration of Simpson's Paradox; the upper figure represents Lisa's contribution and the lower one Bart's. The left bars represent the first week, the right bars the second week; the triangles indicate the combined percentage of good contributions (weighted average). While each of Bart's bars show greater success than Lisa's, Lisa's combined rate is higher because she improved a greater ratio relative to the quantity edited.

Suppose two people, Lisa and Bart, each edit articles for two weeks. In the first week, Lisa fails to improve the only article she edited, and Bart improves 1 of the 4 articles he edited. In the second week, Lisa improves 3 of 4 articles she edited, while Bart improves the only article he edited.

| Week 1 | Week 2 | Total |
| --- | --- | --- |
| Lisa | 0/1 | 3/4 | **3/5** |
| Bart | **1/4** | **1/1** | 2/5 |

Both times Bart improved a higher percentage of articles than Lisa, but the actual number of articles each edited (the bottom number of their ratios, also known as the *[sample size](https://en.wikipedia.org/wiki/Sample_size)*) were not the same for both of them either week. When the totals for the two weeks are added together, Bart and Lisa's work can be judged from an equal sample size; i.e., the total number of articles edited by each. Looked at in this more accurate manner, Lisa's ratio is higher and, therefore, so is her percentage. Also when the two tests are combined using a weighted average, overall, Lisa has improved a much higher percentage than Bart because the quality modifier had a significantly higher percentage. Therefore, like other paradoxes, it only appears to be a paradox because of incorrect assumptions, incomplete or misguided information, or a lack of understanding a particular concept.

| Week 1 quantity | Week 2 quantity | Total quantity *and* weighted quality |
| --- | --- | --- |
| Lisa | 0%  | 75% | **60%** |
| Bart | **25%** | **100%** | 40% |

This imagined paradox is caused when the percentage is provided but not the ratio. In this example, if only the 25% in the first week for Bart was provided but not the ratio (1:4), it would distort the information and so cause the imagined paradox. Even though Bart's percentage is higher for the first and second week, when two weeks of articles is combined, overall Lisa had improved a greater proportion, 60% of the 5 total articles. Lisa's proportional total of articles improved exceeds Bart's total.

### Vector interpretation[]

[![220px-Simpson_paradox_vectors.svg.png](../_resources/dee817b8bfe197b5d7c7f31a3b4d952b.png)](https://en.wikipedia.org/wiki/File:Simpson_paradox_vectors.svg)

Vector interpretation of Simpson's paradox for the Lisa and Bart example

Simpson's paradox can also be illustrated using the 2-dimensional [vector space](https://en.wikipedia.org/wiki/Vector_space).[[14]](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_note-14) A success rate of               p  q            {\displaystyle \textstyle {\frac {p}{q}}}  [{\displaystyle \textstyle {\frac {p}{q}}}](../_resources/00ffaeafaeb49244eabc4255c3f380ec.bin) (i.e., *successes/attempts*) can be represented by a [vector](https://en.wikipedia.org/wiki/Vector_(geometry))              A  →      =  (  q  ,  p  )      {\displaystyle {\overrightarrow {A}}=(q,p)}  [{\displaystyle {\overrightarrow {A}}=(q,p)}](../_resources/f80f97e3321c19025ec4087ff61acf2c.bin), with a [slope](https://en.wikipedia.org/wiki/Slope) of               p  q            {\displaystyle \textstyle {\frac {p}{q}}}  [{\displaystyle \textstyle {\frac {p}{q}}}](../_resources/00ffaeafaeb49244eabc4255c3f380ec.bin). A larger slope, meaning a steeper vector direction, represents then a more successful week. If two rates                 p    1        q    1                {\displaystyle \textstyle {\frac {p_{1}}{q_{1}}}}  [{\displaystyle \textstyle {\frac {p_{1}}{q_{1}}}}](../_resources/4834e3b2448047f8befb202b9ef91825.bin) and                 p    2        q    2                {\displaystyle \textstyle {\frac {p_{2}}{q_{2}}}}  [{\displaystyle \textstyle {\frac {p_{2}}{q_{2}}}}](../_resources/97a6c408ccff251a273a99547f81ce23.bin) are combined, as in the examples given above, the result can be represented by the sum of the vectors         (    q    1      ,    p    1      )      {\displaystyle (q_{1},p_{1})}  [(q_{1},p_{1})](../_resources/a9181437a996c2779394edc5df11dd96.bin) and         (    q    2      ,    p    2      )      {\displaystyle (q_{2},p_{2})}  ![(q_{2},p_{2})](../_resources/f6db0d6bdd2f50173298473db7e4aaa8.bin), which according to the [parallelogram rule](https://en.wikipedia.org/wiki/Parallelogram_rule) is the vector         (    q    1      +    q    2      ,    p    1      +    p    2      )      {\displaystyle (q_{1}+q_{2},p_{1}+p_{2})}  [{\displaystyle (q_{1}+q_{2},p_{1}+p_{2})}](../_resources/ea9e38c1a7ab97b3eacf804bd0751e23.bin), with slope                   p    1      +    p    2            q    1      +    q    2                  {\displaystyle \textstyle {\frac {p_{1}+p_{2}}{q_{1}+q_{2}}}}  [{\displaystyle \textstyle {\frac {p_{1}+p_{2}}{q_{1}+q_{2}}}}](../_resources/4e13bbbbda2bdc045411ced3c93766a4.bin).

Simpson's paradox says that even if a vector               L    1      →          {\displaystyle {\overrightarrow {L_{1}}}}  [{\displaystyle {\overrightarrow {L_{1}}}}](../_resources/bc83741d4c4673c40a0fbf843eff9eac.bin) (in orange in figure) has a smaller slope than another vector               B    1      →          {\displaystyle {\overrightarrow {B_{1}}}}  [{\displaystyle {\overrightarrow {B_{1}}}}](../_resources/66fd763ed675595ac3498c0cdfa88579.bin) (in blue), and               L    2      →          {\displaystyle {\overrightarrow {L_{2}}}}  [{\displaystyle {\overrightarrow {L_{2}}}}](../_resources/2dac8f2b3dc18707d3737c82cf050214.bin) has a smaller slope than               B    2      →          {\displaystyle {\overrightarrow {B_{2}}}}  [{\displaystyle {\overrightarrow {B_{2}}}}](:/d9b5bfee9875bc6954c197334eff8e6e), the sum of the two vectors               L    1      →      +        L    2      →          {\displaystyle {\overrightarrow {L_{1}}}+{\overrightarrow {L_{2}}}}  [{\displaystyle {\overrightarrow {L_{1}}}+{\overrightarrow {L_{2}}}}](../_resources/a1192ea0eb3038cda12aacf32dc0224d.bin) can still have a larger slope than the sum of the two vectors               B    1      →      +        B    2      →          {\displaystyle {\overrightarrow {B_{1}}}+{\overrightarrow {B_{2}}}}  [{\displaystyle {\overrightarrow {B_{1}}}+{\overrightarrow {B_{2}}}}](../_resources/1ab6ba5cdca54af0ca5281d8cc67fcd9.bin), as shown in the example.

## Examples[]

### UC Berkeley gender bias[]

One of the best-known examples of Simpson's paradox is a study of gender bias among [graduate school](https://en.wikipedia.org/wiki/Graduate_school) admissions to [University of California, Berkeley](https://en.wikipedia.org/wiki/University_of_California,_Berkeley). The admission figures for the fall of 1973 showed that men applying were more likely than women to be admitted, and the difference was so large that it was unlikely to be due to chance.[[15]](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_note-freedman-15)[[16]](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_note-Bickel-16)

| Applicants | Admitted |
| --- | --- |
| Men | 8442 | **44%** |
| Women | 4321 | 35% |

But when examining the individual departments, it appeared that six out of 85 departments were significantly biased against men, whereas only four were significantly biased against women. In fact, the pooled and corrected data showed a "small but [statistically significant](https://en.wikipedia.org/wiki/Statistical_significance) bias in favor of women."[[16]](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_note-Bickel-16) The data from the six largest departments are listed below.

| Department | Men | Women |
| --- | --- | --- |
| Applicants | Admitted | Applicants | Admitted |
| A   | 825 | 62% | 108 | **82%** |
| B   | 560 | 63% |  25 | **68%** |
| C   | 325 | **37%** | 593 | 34% |
| D   | 417 | 33% | 375 | **35%** |
| E   | 191 | **28%** | 393 | 24% |
| F   | 373 |  6% | 341 |  **7%** |

The research paper by Bickel et al.[[16]](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_note-Bickel-16) concluded that women tended to apply to competitive departments with low rates of admission even among qualified applicants (such as in the English Department), whereas men tended to apply to less-competitive departments with high rates of admission among the qualified applicants (such as in [engineering](https://en.wikipedia.org/wiki/Engineering) and [chemistry](https://en.wikipedia.org/wiki/Chemistry)).

### Kidney stone treatment[]

This is a real-life example from a medical study[[17]](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_note-17) comparing the success rates of two treatments for [kidney stones](https://en.wikipedia.org/wiki/Kidney_stone).[[18]](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_note-18)

The table below shows the success rates and numbers of treatments for treatments involving both small and large kidney stones, where Treatment A includes all open surgical procedures and Treatment B is [percutaneous nephrolithotomy](https://en.wikipedia.org/wiki/Percutaneous_nephrolithotomy) (which involves only a small puncture). The numbers in parentheses indicate the number of success cases over the total size of the group.

| Treatment A | Treatment B |
| --- | --- |
| Small<br>stones | *Group 1*<br>**93% (81/87)** | *Group 2*<br>87% (234/270) |
| Large<br>stones | *Group 3*<br>**73% (192/263)** | *Group 4*<br>69% (55/80) |
| Both | 78% (273/350) | **83% (289/350)** |

The paradoxical conclusion is that treatment A is more effective when used on small stones, and also when used on large stones, yet treatment B is more effective when considering both sizes at the same time. In this example, the "lurking" variable (or **[confounding variable](https://en.wikipedia.org/wiki/Confounding)**) is the severity of the case (represented by the doctors' treatment decision trend of favoring B for less severe cases), which was not previously known to be important until its effects were included.

Which treatment is considered better is determined by an inequality between two ratios (successes/total). The reversal of the inequality between the ratios, which creates Simpson's paradox, happens because two effects occur together:

1. The sizes of the groups, which are combined when the lurking variable is ignored, are very different. Doctors tend to give the severe cases (large stones) the better treatment (A), and the milder cases (small stones) the inferior treatment (B). Therefore, the totals are dominated by groups 3 and 2, and not by the two much smaller groups 1 and 4.

2. The lurking variable has a large effect on the ratios; i.e., the success rate is more strongly influenced by the severity of the case than by the choice of treatment. Therefore, the group of patients with large stones using treatment A (group 3) does worse than the group with small stones (groups 1 and 2), even if the latter used the inferior treatment B (group 2).

Based on these effects, the paradoxical result is seen to arise by suppression of the causal effect of the severity of the case on successful treatment. The paradoxical result can be rephrased more accurately as follows: When the less effective treatment (B) is applied more frequently to less severe cases, it can appear to be a more effective treatment.

### Batting averages[]

A common example of Simpson's Paradox involves the [batting averages](https://en.wikipedia.org/wiki/Batting_average) of players in [professional baseball](https://en.wikipedia.org/wiki/Professional_baseball). It is possible for one player to have a higher batting average than another player each year for a number of years, but to have a lower batting average across all of those years. This phenomenon can occur when there are large differences in the number of at-bats between the years. (The same situation applies to calculating batting averages for the first half of the baseball season, and during the second half, and then combining all of the data for the season's batting average.)

A real-life example is provided by Ken Ross[[19]](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_note-19) and involves the batting average of two baseball players, [Derek Jeter](https://en.wikipedia.org/wiki/Derek_Jeter) and [David Justice](https://en.wikipedia.org/wiki/David_Justice), during the years 1995 and 1996:[[20]](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_note-20)

| 1995 | 1996 | Combined |
| --- | --- | --- |
| Derek Jeter |  12/48 | .250 | 183/582 | .314 | 195/630 | **.310** |
| David Justice | 104/411 | **.253** |  45/140 | **.321** | 149/551 | .270 |

In both 1995 and 1996, Justice had a higher batting average (in bold type) than Jeter did. However, when the two baseball seasons are combined, Jeter shows a higher batting average than Justice. According to Ross, this phenomenon would be observed about once per year among the possible pairs of interesting baseball players. In this particular case, the Simpson's Paradox can still be observed if the year 1997 is also taken into account:

| 1995 | 1996 | 1997 | Combined |
| --- | --- | --- | --- |
| Derek Jeter |  12/48 | .250 | 183/582 | .314 | 190/654 | .291 | 385/1284 | **.300** |
| David Justice | 104/411 | **.253** |  45/140 | **.321** | 163/495 | **.329** | 312/1046 | .298 |

The Jeter and Justice example of Simpson's paradox was referred to in the "Conspiracy Theory" episode of the television series *[Numb3rs](https://en.wikipedia.org/wiki/Numb3rs)*, though a chart shown omitted some of the data, and listed the 1996 averages as 1995.[*[citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation_needed)*]

### Correlation between variables[]

Simpson's paradox can also arise in [correlations](https://en.wikipedia.org/wiki/Correlation), in which two variables appear to have (say) a positive correlation towards one another, when in fact they have a negative correlation, the reversal having been brought about by a "lurking" confounder. Berman et al.[[21]](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_note-21) give an example from economics, where a dataset suggests overall demand is positively correlated with price (that is, higher prices lead to *more* demand), in contradiction of expectation. Analysis reveals time to be the confounding variable: plotting both price and demand against time reveals the expected negative correlation over various periods, which then reverses to become positive if the influence of time is ignored by simply plotting demand against price.

## Implications for decision making[]

The practical significance of Simpson's paradox surfaces in decision making situations where it poses the following dilemma: Which data should we consult in choosing an action, the aggregated or the partitioned? In the Kidney Stone example above, it is clear that if one is diagnosed with "Small Stones" or "Large Stones" the data for the respective subpopulation should be consulted and Treatment A would be preferred to Treatment B. But what if a patient is not diagnosed, and the size of the stone is not known; would it be appropriate to consult the aggregated data and administer Treatment B? This would stand contrary to common sense; a treatment that is preferred both under one condition and under its negation should also be preferred when the condition is unknown.

On the other hand, if the partitioned data is to be preferred a priori, what prevents one from partitioning the data into arbitrary sub-categories (say based on eye color or post-treatment pain) artificially constructed to yield wrong choices of treatments? Pearl[[5]](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_note-pearl-5) shows that, indeed, in many cases it is the aggregated, not the partitioned data that gives the correct choice of action. Worse yet, given the same table, one should sometimes follow the partitioned and sometimes the aggregated data, depending on the story behind the data, with each story dictating its own choice. Pearl[[5]](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_note-pearl-5) considers this to be the real paradox behind Simpson's reversal.

As to why and how a story, not data, should dictate choices, the answer is that it is the story which encodes the causal relationships among the variables. Once we explicate these relationships and represent them formally, we can test which partition gives the correct treatment preference. For example, if we represent causal relationships in a graph called "causal diagram" (see [Bayesian networks](https://en.wikipedia.org/wiki/Bayesian_networks)), we can test whether nodes that represent the proposed partition intercept spurious paths in the diagram. This test, called "back-door," reduces Simpson's paradox to an exercise in graph theory.[[22]](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_note-pearl-2013-r414-22)

## Psychology[]

Psychological interest in Simpson's paradox seeks to explain why people deem sign reversal to be impossible at first, offended by the idea that an action preferred both under one condition and under its negation should be rejected when the condition is unknown. The question is where people get this strong [intuition](https://en.wikipedia.org/wiki/Intuition) from, and how it is encoded in the [mind](https://en.wikipedia.org/wiki/Mind).

Simpson's paradox demonstrates that this intuition cannot be derived from either classical logic or [probability calculus](https://en.wikipedia.org/wiki/Probability_calculus) alone, and thus led [philosophers](https://en.wikipedia.org/wiki/Philosopher) to speculate that it is supported by an innate causal logic that guides people in reasoning about actions and their consequences[*[citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation_needed)*]. Savage's [sure-thing principle](https://en.wikipedia.org/wiki/Sure-thing_principle)[[13]](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_note-blyth-72-13) is an example of what such logic may entail. A qualified version of Savage's sure thing principle can indeed be derived from Pearl's *do*-calculus[[5]](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_note-pearl-5) and reads: "An action *A* that increases the probability of an event *B* in each subpopulation *Ci* of *C* must also increase the probability of *B* in the population as a whole, provided that the action does not change the distribution of the subpopulations." This suggests that knowledge about actions and consequences is stored in a form resembling Causal [Bayesian Networks](https://en.wikipedia.org/wiki/Bayesian_Networks).

## Probability[]

A paper by Pavlides and Perlman presents a proof, due to Hadjicostas, that in a random **2 × 2 × 2** table with uniform distribution, Simpson's paradox will occur with a [probability](https://en.wikipedia.org/wiki/Probability) of exactly 1/60.[[23]](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_note-23) A study by Kock suggests that the probability that Simpson’s paradox would occur at random in path models (i.e., models generated by [path analysis](https://en.wikipedia.org/wiki/Path_analysis_(statistics))) with two predictors and one criterion variable is approximately 12.8 percent; slightly higher than 1 occurrence per 8 path models.[[24]](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_note-24)

## See also[]

## References[]

1. **[Jump up ^](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_ref-1)**  [I. J. Good](https://en.wikipedia.org/wiki/I._J._Good), Y. Mittal (June 1987). "The Amalgamation and Geometry of Two-by-Two Contingency Tables". *[The Annals of Statistics](https://en.wikipedia.org/wiki/The_Annals_of_Statistics)*. **15** (2): 694–711. [doi](https://en.wikipedia.org/wiki/Digital_object_identifier):[10.1214/aos/1176350369](https://doi.org/10.1214%2Faos%2F1176350369). [ISSN](https://en.wikipedia.org/wiki/International_Standard_Serial_Number) [0090-5364](https://www.worldcat.org/issn/0090-5364). [JSTOR](https://en.wikipedia.org/wiki/JSTOR) [2241334](https://www.jstor.org/stable/2241334).

2. **[Jump up ^](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_ref-2)**  Clifford H. Wagner (February 1982). "Simpson's Paradox in Real Life". *[The American Statistician](https://en.wikipedia.org/wiki/The_American_Statistician)*. **36** (1): 46–48. [doi](https://en.wikipedia.org/wiki/Digital_object_identifier):[10.2307/2684093](https://doi.org/10.2307%2F2684093). [JSTOR](https://en.wikipedia.org/wiki/JSTOR) [2684093](https://www.jstor.org/stable/2684093).

3. **[Jump up ^](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_ref-3)** Holt, G. B. (2016). [Potential Simpson's paradox in multicenter study of intraperitoneal chemotherapy for ovarian cancer.](http://jco.ascopubs.org/content/34/9/1016.1.full) Journal of Clinical Oncology, 34(9), 1016-1016.

4. **[Jump up ^](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_ref-VogelFranks2017_4-0)**  Franks, Alexander; Airoldi, Edoardo; Slavov, Nikolai (2017). "Post-transcriptional regulation across human tissues". *PLOS Computational Biology*. **13** (5): e1005535. [doi](https://en.wikipedia.org/wiki/Digital_object_identifier):[10.1371/journal.pcbi.1005535](https://doi.org/10.1371%2Fjournal.pcbi.1005535). [ISSN](https://en.wikipedia.org/wiki/International_Standard_Serial_Number) [1553-7358](https://www.worldcat.org/issn/1553-7358).

5. ^ [Jump up to: ***a***](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_ref-pearl_5-0)  [***b***](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_ref-pearl_5-1)  [***c***](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_ref-pearl_5-2)  [***d***](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_ref-pearl_5-3)  [Judea Pearl](https://en.wikipedia.org/wiki/Judea_Pearl). *Causality: Models, Reasoning, and Inference*, Cambridge University Press (2000, 2nd edition 2009). [ISBN](https://en.wikipedia.org/wiki/International_Standard_Book_Number) [0-521-77362-8](https://en.wikipedia.org/wiki/Special:BookSources/0-521-77362-8).

6. **[Jump up ^](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_ref-6)** Kock, N., & Gaskins, L. (2016). [Simpson's paradox, moderation and the emergence of quadratic relationships in path models: An information systems illustration.](http://cits.tamiu.edu/kock/pubs/journals/2016JournalIJANS_ModJCveNetCorrp/Kock_Gaskins_2016_IJANS_SimpPdox.pdf) International Journal of Applied Nonlinear Science, 2(3), 200-234.

7. **[Jump up ^](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_ref-7)** Robert L. Wardrop (February 1995). "Simpson's Paradox and the Hot Hand in Basketball". *The American Statistician*, **49 (1)**: pp. 24–28.

8. **[Jump up ^](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_ref-8)** Alan Agresti (2002). "Categorical Data Analysis" (Second edition). [John Wiley and Sons](https://en.wikipedia.org/wiki/John_Wiley_and_Sons)  [ISBN](https://en.wikipedia.org/wiki/International_Standard_Book_Number) [0-471-36093-7](https://en.wikipedia.org/wiki/Special:BookSources/0-471-36093-7)

9. **[Jump up ^](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_ref-9)**  Gardener, Martin (March 1979). ["MATHEMATICAL GAMES: On the fabric of inductive logic, and some probability paradoxes"](http://flowcytometry.sysbio.med.harvard.edu/files/flowcytometryhms/files/herzenbergfacshistory.pdf#129) (PDF). *Scientific American*. **234**: 119. Retrieved 28 February 2017.

10. **[Jump up ^](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_ref-10)**  Simpson, Edward H. (1951). "The Interpretation of Interaction in Contingency Tables". *[Journal of the Royal Statistical Society](https://en.wikipedia.org/wiki/Journal_of_the_Royal_Statistical_Society), Series B*. **13**: 238–241.

11. **[Jump up ^](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_ref-11)**  [Pearson, Karl](https://en.wikipedia.org/wiki/Karl_Pearson); Lee, Alice; Bramley-Moore, Lesley (1899). "Genetic (reproductive) selection: Inheritance of fertility in man, and of fecundity in thoroughbred racehorses". *[Philosophical Transactions of the Royal Society A](https://en.wikipedia.org/wiki/Philosophical_Transactions_of_the_Royal_Society_A)*. **192**: 257–330. [doi](https://en.wikipedia.org/wiki/Digital_object_identifier):[10.1098/rsta.1899.0006](https://doi.org/10.1098%2Frsta.1899.0006).

12. **[Jump up ^](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_ref-yule_12-0)**  G. U. Yule (1903). "Notes on the Theory of Association of Attributes in Statistics". *[Biometrika](https://en.wikipedia.org/wiki/Biometrika)*. **2** (2): 121–134. [doi](https://en.wikipedia.org/wiki/Digital_object_identifier):[10.1093/biomet/2.2.121](https://doi.org/10.1093%2Fbiomet%2F2.2.121).

13. ^ [Jump up to: ***a***](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_ref-blyth-72_13-0)  [***b***](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_ref-blyth-72_13-1)  Colin R. Blyth (June 1972). "On Simpson's Paradox and the Sure-Thing Principle". *Journal of the American Statistical Association*. **67** (338): 364–366. [doi](https://en.wikipedia.org/wiki/Digital_object_identifier):[10.2307/2284382](https://doi.org/10.2307%2F2284382). [JSTOR](https://en.wikipedia.org/wiki/JSTOR) [2284382](https://www.jstor.org/stable/2284382).

14. **[Jump up ^](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_ref-14)**  Kocik Jerzy (2001). ["Proofs without Words: Simpson's Paradox"](http://www.math.siu.edu/kocik/papers/simpson2.pdf) (PDF). *[Mathematics Magazine](https://en.wikipedia.org/wiki/Mathematics_Magazine)*. **74** (5): 399. [doi](https://en.wikipedia.org/wiki/Digital_object_identifier):[10.2307/2691038](https://doi.org/10.2307%2F2691038).

15. **[Jump up ^](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_ref-freedman_15-0)**  [David Freedman](https://en.wikipedia.org/wiki/David_A._Freedman), Robert Pisani, and Roger Purves (2007), *Statistics* (4th edition), [W. W. Norton](https://en.wikipedia.org/wiki/W._W._Norton_%26_Company). [ISBN](https://en.wikipedia.org/wiki/International_Standard_Book_Number) [0-393-92972-8](https://en.wikipedia.org/wiki/Special:BookSources/0-393-92972-8).

16. ^ [Jump up to: ***a***](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_ref-Bickel_16-0)  [***b***](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_ref-Bickel_16-1)  [***c***](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_ref-Bickel_16-2)  [P.J. Bickel](https://en.wikipedia.org/wiki/Peter_J._Bickel), E.A. Hammel and J.W. O'Connell (1975). ["Sex Bias in Graduate Admissions: Data From Berkeley"](http://homepage.stat.uiowa.edu/~mbognar/1030/Bickel-Berkeley.pdf) (PDF). *[Science](https://en.wikipedia.org/wiki/Science_(journal))*. **187** (4175): 398–404. [doi](https://en.wikipedia.org/wiki/Digital_object_identifier):[10.1126/science.187.4175.398](https://doi.org/10.1126%2Fscience.187.4175.398). [PMID](https://en.wikipedia.org/wiki/PubMed_Identifier) [17835295](https://www.ncbi.nlm.nih.gov/pubmed/17835295).

17. **[Jump up ^](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_ref-17)**  C. R. Charig; D. R. Webb; S. R. Payne; J. E. Wickham (29 March 1986). ["Comparison of treatment of renal calculi by open surgery, percutaneous nephrolithotomy, and extracorporeal shockwave lithotripsy"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1339981). *[Br Med J (Clin Res Ed)](https://en.wikipedia.org/wiki/Br_Med_J_(Clin_Res_Ed))*. **292** (6524): 879–882. [doi](https://en.wikipedia.org/wiki/Digital_object_identifier):[10.1136/bmj.292.6524.879](https://doi.org/10.1136%2Fbmj.292.6524.879). [PMC](https://en.wikipedia.org/wiki/PubMed_Central) [1339981](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1339981) . [PMID](https://en.wikipedia.org/wiki/PubMed_Identifier) [3083922](https://www.ncbi.nlm.nih.gov/pubmed/3083922).

18. **[Jump up ^](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_ref-18)**  Steven A. Julious; Mark A. Mullee (3 December 1994). ["Confounding and Simpson's paradox"](http://bmj.bmjjournals.com/cgi/content/full/309/6967/1480). *[BMJ](https://en.wikipedia.org/wiki/BMJ)*. **309** (6967): 1480–1481. [doi](https://en.wikipedia.org/wiki/Digital_object_identifier):[10.1136/bmj.309.6967.1480](https://doi.org/10.1136%2Fbmj.309.6967.1480). [PMC](https://en.wikipedia.org/wiki/PubMed_Central) [2541623](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2541623) . [PMID](https://en.wikipedia.org/wiki/PubMed_Identifier) [7804052](https://www.ncbi.nlm.nih.gov/pubmed/7804052).

19. **[Jump up ^](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_ref-19)** Ken Ross. "*A Mathematician at the Ballpark: Odds and Probabilities for Baseball Fans (Paperback)*" Pi Press, 2004. [ISBN](https://en.wikipedia.org/wiki/International_Standard_Book_Number) [0-13-147990-3](https://en.wikipedia.org/wiki/Special:BookSources/0-13-147990-3). 12–13

20. **[Jump up ^](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_ref-20)** Statistics available from [Baseball-Reference.com](https://en.wikipedia.org/wiki/Baseball-Reference.com): [Data for Derek Jeter](http://www.baseball-reference.com/j/jeterde01.shtml); [Data for David Justice](http://www.baseball-reference.com/j/justida01.shtml).

21. **[Jump up ^](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_ref-21)** Berman, S. DalleMule, L. Greene, M., Lucker, J. (2012), "[Simpson’s Paradox: A Cautionary Tale in Advanced Analytics](http://www.statslife.org.uk/the-statistics-dictionary/2012-simpson-s-paradox-a-cautionary-tale-in-advanced-analytics)", *[Significance](https://en.wikipedia.org/wiki/Significance_(magazine))*.

22. **[Jump up ^](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_ref-pearl-2013-r414_22-0)**  Pearl, Judea (December 2013). ["Understanding Simpson's paradox"](http://ftp.cs.ucla.edu/pub/stat_ser/r414.pdf) (PDF). *UCLA Cognitive Systems Laboratory, Technical Report R-414*.

23. **[Jump up ^](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_ref-23)**  Marios G. Pavlides & Michael D. Perlman (August 2009). "How Likely is Simpson's Paradox?". *[The American Statistician](https://en.wikipedia.org/wiki/The_American_Statistician)*. **63** (3): 226–233. [doi](https://en.wikipedia.org/wiki/Digital_object_identifier):[10.1198/tast.2009.09007](https://doi.org/10.1198%2Ftast.2009.09007).

24. **[Jump up ^](https://en.wikipedia.org/wiki/Simpson%27s_paradox#cite_ref-24)** Kock, N. (2015). [How likely is Simpson’s paradox in path models?](http://cits.tamiu.edu/kock/pubs/journals/2015JournalIJeC/Kock_2015_IJeC_SimpPdox.pdf) International Journal of e-Collaboration, 11(1), 1–7.

## Bibliography[]

- [Leila Schneps](https://en.wikipedia.org/wiki/Leila_Schneps) and [Coralie Colmez](https://en.wikipedia.org/wiki/Coralie_Colmez), *Math on trial. How numbers get used and abused in the courtroom*, Basic Books, 2013. [ISBN](https://en.wikipedia.org/wiki/International_Standard_Book_Number) [978-0-465-03292-1](https://en.wikipedia.org/wiki/Special:BookSources/978-0-465-03292-1). (Sixth chapter: "Math error number 6: Simpson's paradox. The Berkeley sex bias case: discrimination detection").

## External links[]

- [Were Richer Voters More Likely to Vote Trump? (Simpson’s Paradox)](https://www.youtube.com/watch?v=s7x5P1yiYks&list=PL0FfKwFuQb2Trlr06KCyfdGZyE5Et-Pgj&index=1) — YouTube video explaining Simpson's Paradox.
- [How statistics can be misleading - Mark Liddell](http://ed.ted.com/lessons/how-statistics-can-be-misleading-mark-liddell)—TED-Ed video and lesson.
- [Stanford Encyclopedia of Philosophy](https://en.wikipedia.org/wiki/Stanford_Encyclopedia_of_Philosophy): "[Simpson's Paradox](http://plato.stanford.edu/entries/paradox-simpson/)" – by Gary Malinas.
- [Earliest known uses of some of the words of mathematics: S](http://jeff560.tripod.com/s.html)
    - For a brief history of the origins of the paradox see the entries "Simpson's Paradox" and "Spurious Correlation"
- [Pearl, Judea](https://en.wikipedia.org/wiki/Judea_Pearl), "["The Art and Science of Cause and Effect.](http://bayes.cs.ucla.edu/LECTURE/lecture_sec1.htm)" A slide show and tutorial lecture.
- [Pearl, Judea](https://en.wikipedia.org/wiki/Judea_Pearl), ["Simpson's Paradox: An Anatomy"](http://bayes.cs.ucla.edu/R264.pdf) ([PDF](https://en.wikipedia.org/wiki/PDF))
- [Simpson's Paradox Visualized](http://vudlab.com/simpsons/) - an interactive demonstration of Simpson's paradox.
- [Pearl, Judea](https://en.wikipedia.org/wiki/Judea_Pearl), ["The Sure-Thing Principle"](http://ftp.cs.ucla.edu/pub/stat_ser/r466.pdf) ([PDF](https://en.wikipedia.org/wiki/PDF))
- Short articles by Alexander Bogomolny at [cut-the-knot](https://en.wikipedia.org/wiki/Cut-the-knot):
- [The Wall Street Journal column "The Numbers Guy"](https://www.wsj.com/articles/SB125970744553071829) for December 2, 2009 dealt with recent instances of Simpson's paradox in the news. Notably a Simpson's paradox in the comparison of unemployment rates of the 2009 recession with the 1983 recession.
- [How to resolve Simpson's paradox?](http://stats.stackexchange.com/questions/78255/how-to-resolve-simpsons-paradox) question on statistics Q&A site CrossValidated
- [Reich, Henry](https://en.wikipedia.org/wiki/MinutePhysics). ["Simpson's Paradox"](https://www.youtube.com/watch?v=ebEkn-BiW5k) (video). *YouTube*. MinutePhysics. Retrieved 24 October 2017.