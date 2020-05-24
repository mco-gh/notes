Pandas 75 exercises with solutions | Kaggle

This Notebook has been released under the [Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0) open source license.

Did you find this Notebook useful?
Show your appreciation with an upvote

154

[![1687-gr.jpg](../_resources/80b31e2aaa7908ed9329f528549469ee.jpg)](https://www.kaggle.com/nellaivijay)Vijay Ram

[![300759-kg.jpg](../_resources/602f22b522d81b08a6db937861ecf8e4.jpg)](https://www.kaggle.com/sumendar)karupakalas

[![315126-gp.jpg](../_resources/b02babee3441d2c7b566a7b429065662.jpg)](https://www.kaggle.com/sharangbhat)Sharang Bhat

[![default-thumb.png](../_resources/f1cee4ded9d19bb202587e7bfaab843f.png)](https://www.kaggle.com/cemrifkiaydin)Cem Rıfkı Aydın

[![default-thumb.png](../_resources/f1cee4ded9d19bb202587e7bfaab843f.png)](https://www.kaggle.com/tnovit)Thomas Novitsky

[![510701-fb.jpg](../_resources/508efcb8abb0232c1a2157e831b630ba.jpg)](https://www.kaggle.com/simonbergsten)SimonLondoñoBergsten

[![514588-gp.jpg](../_resources/fe4d12344effb0d795c4381998c8bcaf.jpg)](https://www.kaggle.com/wanwanliu)Wan Wan Liu

[![517258-kg.jpeg](../_resources/d840e7051201301eaedf52b0ccfbbf41.jpg)](https://www.kaggle.com/zzaibis)Qurratulain Saleem

[![default-thumb.png](../_resources/f1cee4ded9d19bb202587e7bfaab843f.png)](https://www.kaggle.com/vikingh)vikingh

[![566462-gp.jpg](../_resources/a4b9b971514dfdc4769cee00cb4d2ba7.jpg)](https://www.kaggle.com/sunneysood)SunneySood

[![575436-kg.png](../_resources/5ba3e464bdb32a22453610d0f30a9aec.png)](https://www.kaggle.com/thewhitetulip)thewhitetulip

[![700074-kg.jpg](../_resources/76e9f5a163883329f3969f065536b3d3.jpg)](https://www.kaggle.com/deweshdeosingh)DeweshDeoSingh(DEV)

[![782553-fb.jpg](../_resources/6389257f889db313502d8144d04abb35.jpg)](https://www.kaggle.com/tdl123)DenisTitlov

[![807182-kg.jpg](../_resources/5b74a1950bd14259561aeb1e3417257f.jpg)](https://www.kaggle.com/bombatkarvivek)Vivek Bombatkar

[![811628-kg.jpg](../_resources/55a6d8d54c086f5166ff0d90dc5233db.jpg)](https://www.kaggle.com/paluure)Toprak Ozturk

Data
Data Sources


Boston House Prices


housing.csv
1 columns


Cars93


Cars93.csv
28 columns
![dataset-thumbnail.png](../_resources/4a5da61db7c739bca62b9cba1a6296a1.jpg)
[Boston House Prices](https://www.kaggle.com/vikrishnan/boston-house-prices)
Regression predictive modeling machine learning problem from end-to-end Python
Last Updated: 3 years ago (Version 1)
About this Dataset

### Context

To Explore more on Regression Algorithm

### Content

Each record in the database describes a Boston suburb or town. The data was drawn from the Boston Standard Metropolitan Statistical Area (SMSA) in 1970. The attributes are deﬁned as follows (taken from the UCI Machine Learning Repository1): CRIM: per capita crime rate by town 2. ZN: proportion of residential land zoned for lots over 25,000 sq.ft. 3. INDUS: proportion of non-retail business acres per town 4. CHAS: Charles River dummy variable (= 1 if tract bounds river; 0 otherwise) 5. NOX: nitric oxides concentration (parts per 10 million) 1https://archive.ics.uci.edu/ml/datasets/Housing 123 20.2. Load the Dataset 124 6. RM: average number of rooms per dwelling 7. AGE: proportion of owner-occupied units built prior to 1940 8. DIS: weighted distances to ﬁve Boston employment centers 9. RAD: index of accessibility to radial highways 10. TAX: full-value property-tax rate per $10,000 11. PTRATIO: pupil-teacher ratio by town 12. B: 1000(Bk−0.63)2 where Bk is the proportion of blacks by town 13. LSTAT: % lower status of the population 14. MEDV: Median value of owner-occupied homes in $1000s We can see that the input attributes have a mixture of units.

### Acknowledgements

Thanks to Dr.Jason
Output Files
[New Dataset]()
[New Notebook]()
[Download All](https://www.kaggle.com/kernels/svzip/27899299)

Output Files


housing_preprocessed.csv

About this file

This file was created from a Kernel, it does not have a description.


housing_preprocessed.csv

[](https://www.kaggleusercontent.com/kf/27899299/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..Bk4Wytgrtr6arHtsfL3Jgg.98HMHb8A_cmJEewvjkjslrt3DlMnZUPFpMNXKXqCepz5DOJ2UQKHVvbU7Me4BpkKZ_wg_GbKmHah_x_WrVWghieGYC2m3ilVh0pIEEIm_Ga83pkNv_BEZ9htBrUHg9wAg8LIpEUuaTWDNv2uIAlSILuaRVwhTo7MchW8UtRlC0g.Xp4JkyM1AHX49M2MFrRTag/housing_preprocessed.csv)Download

Maximize

|     |
| --- |
|     |
| 1   |     | CRIM | ZN  | INDUS | CHAS | NOX | RM  | AGE | DIS | RAD | TAX | PTRATIO | B   | LSTAT | MEDV |
| 2   | 0   | 0.00632 | 18.00 | 2.310 | 0   | 0.5380 | 6.5750 | 65.20 | 4.0900 | 1   | 296.0 | 15.30 | 396.90 | 4.98 | 24.00 |
| 3   | 1   | 0.02731 | 0.00 | 7.070 | 0   | 0.4690 | 6.4210 | 78.90 | 4.9671 | 2   | 242.0 | 17.80 | 396.90 | 9.14 | 21.60 |
| 4   | 2   | 0.02729 | 0.00 | 7.070 | 0   | 0.4690 | 7.1850 | 61.10 | 4.9671 | 2   | 242.0 | 17.80 | 392.83 | 4.03 | 34.70 |
| 5   | 3   | 0.03237 | 0.00 | 2.180 | 0   | 0.4580 | 6.9980 | 45.80 | 6.0622 | 3   | 222.0 | 18.70 | 394.63 | 2.94 | 33.40 |
| 6   | 4   | 0.06905 | 0.00 | 2.180 | 0   | 0.4580 | 7.1470 | 54.20 | 6.0622 | 3   | 222.0 | 18.70 | 396.90 | 5.33 | 36.20 |
| 7   | 5   | 0.02985 | 0.00 | 2.180 | 0   | 0.4580 | 6.4300 | 58.70 | 6.0622 | 3   | 222.0 | 18.70 | 394.12 | 5.21 | 28.70 |
| 8   | 6   | 0.08829 | 12.50 | 7.870 | 0   | 0.5240 | 6.0120 | 66.60 | 5.5605 | 5   | 311.0 | 15.20 | 395.60 | 12.43 | 22.90 |
| 9   | 7   | 0.14455 | 12.50 | 7.870 | 0   | 0.5240 | 6.1720 | 96.10 | 5.9505 | 5   | 311.0 | 15.20 | 396.90 | 19.15 | 27.10 |
| 10  | 8   | 0.21124 | 12.50 | 7.870 | 0   | 0.5240 | 5.6310 | 100.00 | 6.0821 | 5   | 311.0 | 15.20 | 386.63 | 29.93 | 16.50 |
| 11  | 9   | 0.17004 | 12.50 | 7.870 | 0   | 0.5240 | 6.0040 | 85.90 | 6.5921 | 5   | 311.0 | 15.20 | 386.71 | 17.10 | 18.90 |
| 12  | 10  | 0.22489 | 12.50 | 7.870 | 0   | 0.5240 | 6.3770 | 94.30 | 6.3467 | 5   | 311.0 | 15.20 | 392.52 | 20.45 | 15.00 |
| 13  | 11  | 0.11747 | 12.50 | 7.870 | 0   | 0.5240 | 6.0090 | 82.90 | 6.2267 | 5   | 311.0 | 15.20 | 396.90 | 13.27 | 18.90 |
| 14  | 12  | 0.09378 | 12.50 | 7.870 | 0   | 0.5240 | 5.8890 | 39.00 | 5.4509 | 5   | 311.0 | 15.20 | 390.50 | 15.71 | 21.70 |
| 15  | 13  | 0.62976 | 0.00 | 8.140 | 0   | 0.5380 | 5.9490 | 61.80 | 4.7075 | 4   | 307.0 | 21.00 | 396.90 | 8.26 | 20.40 |
| 16  | 14  | 0.63796 | 0.00 | 8.140 | 0   | 0.5380 | 6.0960 | 84.50 | 4.4619 | 4   | 307.0 | 21.00 | 380.02 | 10.26 | 18.20 |
| 17  | 15  | 0.62739 | 0.00 | 8.140 | 0   | 0.5380 | 5.8340 | 56.50 | 4.4986 | 4   | 307.0 | 21.00 | 395.62 | 8.47 | 19.90 |
| 18  | 16  | 1.05393 | 0.00 | 8.140 | 0   | 0.5380 | 5.9350 | 29.30 | 4.4986 | 4   | 307.0 | 21.00 | 386.85 | 6.58 | 23.10 |
| 19  | 17  | 0.78420 | 0.00 | 8.140 | 0   | 0.5380 | 5.9900 | 81.70 | 4.2579 | 4   | 307.0 | 21.00 | 386.75 | 14.67 | 17.50 |
| 20  | 18  | 0.80271 | 0.00 | 8.140 | 0   | 0.5380 | 5.4560 | 36.60 | 3.7965 | 4   | 307.0 | 21.00 | 288.99 | 11.69 | 20.20 |
| 21  | 19  | 0.72580 | 0.00 | 8.140 | 0   | 0.5380 | 5.7270 | 69.50 | 3.7965 | 4   | 307.0 | 21.00 | 390.95 | 11.28 | 18.20 |
| 22  | 20  | 1.25179 | 0.00 | 8.140 | 0   | 0.5380 | 5.5700 | 98.10 | 3.7979 | 4   | 307.0 | 21.00 | 376.57 | 21.02 | 13.60 |
| 23  | 21  | 0.85204 | 0.00 | 8.140 | 0   | 0.5380 | 5.9650 | 89.20 | 4.0123 | 4   | 307.0 | 21.00 | 392.53 | 13.83 | 19.60 |
| 24  | 22  | 1.23247 | 0.00 | 8.140 | 0   | 0.5380 | 6.1420 | 91.70 | 3.9769 | 4   | 307.0 | 21.00 | 396.90 | 18.72 | 15.20 |
| 25  | 23  | 0.98843 | 0.00 | 8.140 | 0   | 0.5380 | 5.8130 | 100.00 | 4.0952 | 4   | 307.0 | 21.00 | 394.54 | 19.88 | 14.50 |
| 26  | 24  | 0.75026 | 0.00 | 8.140 | 0   | 0.5380 | 5.9240 | 94.10 | 4.3996 | 4   | 307.0 | 21.00 | 394.33 | 16.30 | 15.60 |
| 27  | 25  | 0.84054 | 0.00 | 8.140 | 0   | 0.5380 | 5.5990 | 85.70 | 4.4546 | 4   | 307.0 | 21.00 | 303.42 | 16.51 | 13.90 |
| 28  | 26  | 0.67191 | 0.00 | 8.140 | 0   | 0.5380 | 5.8130 | 90.30 | 4.6820 | 4   | 307.0 | 21.00 | 376.88 | 14.81 | 16.60 |
| 29  | 27  | 0.95577 | 0.00 | 8.140 | 0   | 0.5380 | 6.0470 | 88.80 | 4.4534 | 4   | 307.0 | 21.00 | 306.38 | 17.28 | 14.80 |
| 30  | 28  | 0.77299 | 0.00 | 8.140 | 0   | 0.5380 | 6.4950 | 94.40 | 4.4547 | 4   | 307.0 | 21.00 | 387.94 | 12.80 | 18.40 |
| 31  | 29  | 1.00245 | 0.00 | 8.140 | 0   | 0.5380 | 6.6740 | 87.30 | 4.2390 | 4   | 307.0 | 21.00 | 380.23 | 11.98 | 21.00 |
| 32  | 30  | 1.13081 | 0.00 | 8.140 | 0   | 0.5380 | 5.7130 | 94.10 | 4.2330 | 4   | 307.0 | 21.00 | 360.17 | 22.60 | 12.70 |
| 33  | 31  | 1.35472 | 0.00 | 8.140 | 0   | 0.5380 | 6.0720 | 100.00 | 4.1750 | 4   | 307.0 | 21.00 | 376.73 | 13.04 | 14.50 |
| 34  | 32  | 1.38799 | 0.00 | 8.140 | 0   | 0.5380 | 5.9500 | 82.00 | 3.9900 | 4   | 307.0 | 21.00 | 232.60 | 27.71 | 13.20 |
| 35  | 33  | 1.15172 | 0.00 | 8.140 | 0   | 0.5380 | 5.7010 | 95.00 | 3.7872 | 4   | 307.0 | 21.00 | 358.77 | 18.35 | 13.10 |
| 36  | 34  | 1.61282 | 0.00 | 8.140 | 0   | 0.5380 | 6.0960 | 96.90 | 3.7598 | 4   | 307.0 | 21.00 | 248.31 | 20.34 | 13.50 |
| 37  | 35  | 0.06417 | 0.00 | 5.960 | 0   | 0.4990 | 5.9330 | 68.20 | 3.3603 | 5   | 279.0 | 19.20 | 396.90 | 9.68 | 18.90 |
| 38  | 36  | 0.09744 | 0.00 | 5.960 | 0   | 0.4990 | 5.8410 | 61.40 | 3.3779 | 5   | 279.0 | 19.20 | 377.56 | 11.41 | 20.00 |
| 39  | 37  | 0.08014 | 0.00 | 5.960 | 0   | 0.4990 | 5.8500 | 41.50 | 3.9342 | 5   | 279.0 | 19.20 | 396.90 | 8.77 | 21.00 |
| 40  | 38  | 0.17505 | 0.00 | 5.960 | 0   | 0.4990 | 5.9660 | 30.20 | 3.8473 | 5   | 279.0 | 19.20 | 393.43 | 10.13 | 24.70 |
| 41  | 39  | 0.02763 | 75.00 | 2.950 | 0   | 0.4280 | 6.5950 | 21.80 | 5.4011 | 3   | 252.0 | 18.30 | 395.63 | 4.32 | 30.80 |
| 42  | 40  | 0.03359 | 75.00 | 2.950 | 0   | 0.4280 | 7.0240 | 15.80 | 5.4011 | 3   | 252.0 | 18.30 | 395.62 | 1.98 | 34.90 |
| 43  | 41  | 0.12744 | 0.00 | 6.910 | 0   | 0.4480 | 6.7700 | 2.90 | 5.7209 | 3   | 233.0 | 17.90 | 385.41 | 4.84 | 26.60 |
| 44  | 42  | 0.14150 | 0.00 | 6.910 | 0   | 0.4480 | 6.1690 | 6.60 | 5.7209 | 3   | 233.0 | 17.90 | 383.37 | 5.81 | 25.30 |
| 45  | 43  | 0.15936 | 0.00 | 6.910 | 0   | 0.4480 | 6.2110 | 6.50 | 5.7209 | 3   | 233.0 | 17.90 | 394.46 | 7.44 | 24.70 |
| 46  | 44  | 0.12269 | 0.00 | 6.910 | 0   | 0.4480 | 6.0690 | 40.00 | 5.7209 | 3   | 233.0 | 17.90 | 389.39 | 9.55 | 21.20 |
| 47  | 45  | 0.17142 | 0.00 | 6.910 | 0   | 0.4480 | 5.6820 | 33.80 | 5.1004 | 3   | 233.0 | 17.90 | 396.90 | 10.21 | 19.30 |
| 48  | 46  | 0.18836 | 0.00 | 6.910 | 0   | 0.4480 | 5.7860 | 33.30 | 5.1004 | 3   | 233.0 | 17.90 | 396.90 | 14.15 | 20.00 |
| 49  | 47  | 0.22927 | 0.00 | 6.910 | 0   | 0.4480 | 6.0300 | 85.50 | 5.6894 | 3   | 233.0 | 17.90 | 392.74 | 18.80 | 16.60 |
| 50  | 48  | 0.25387 | 0.00 | 6.910 | 0   | 0.4480 | 5.3990 | 95.30 | 5.8700 | 3   | 233.0 | 17.90 | 396.90 | 30.81 | 14.40 |
| 51  | 49  | 0.21977 | 0.00 | 6.910 | 0   | 0.4480 | 5.6020 | 62.00 | 6.0877 | 3   | 233.0 | 17.90 | 396.90 | 16.20 | 19.40 |
| 52  | 50  | 0.08873 | 21.00 | 5.640 | 0   | 0.4390 | 5.9630 | 45.70 | 6.8147 | 4   | 243.0 | 16.80 | 395.56 | 13.45 | 19.70 |
| 53  | 51  | 0.04337 | 21.00 | 5.640 | 0   | 0.4390 | 6.1150 | 63.00 | 6.8147 | 4   | 243.0 | 16.80 | 393.97 | 9.43 | 20.50 |
| 54  | 52  | 0.05360 | 21.00 | 5.640 | 0   | 0.4390 | 6.5110 | 21.10 | 6.8147 | 4   | 243.0 | 16.80 | 396.90 | 5.28 | 25.00 |
| 55  | 53  | 0.04981 | 21.00 | 5.640 | 0   | 0.4390 | 5.9980 | 21.40 | 6.8147 | 4   | 243.0 | 16.80 | 396.90 | 8.43 | 23.40 |
| 56  | 54  | 0.01360 | 75.00 | 4.000 | 0   | 0.4100 | 5.8880 | 47.60 | 7.3197 | 3   | 469.0 | 21.10 | 396.90 | 14.80 | 18.90 |
| 57  | 55  | 0.01311 | 90.00 | 1.220 | 0   | 0.4030 | 7.2490 | 21.90 | 8.6966 | 5   | 226.0 | 17.90 | 395.93 | 4.81 | 35.40 |
| 58  | 56  | 0.02055 | 85.00 | 0.740 | 0   | 0.4100 | 6.3830 | 35.70 | 9.1876 | 2   | 313.0 | 17.30 | 396.90 | 5.77 | 24.70 |
| 59  | 57  | 0.01432 | 100.00 | 1.320 | 0   | 0.4110 | 6.8160 | 40.50 | 8.3248 | 5   | 256.0 | 15.10 | 392.90 | 3.95 | 31.60 |
| 60  | 58  | 0.15445 | 25.00 | 5.130 | 0   | 0.4530 | 6.1450 | 29.20 | 7.8148 | 8   | 284.0 | 19.70 | 390.68 | 6.86 | 23.30 |
| 61  | 59  | 0.10328 | 25.00 | 5.130 | 0   | 0.4530 | 5.9270 | 47.20 | 6.9320 | 8   | 284.0 | 19.70 | 396.90 | 9.22 | 19.60 |
| 62  | 60  | 0.14932 | 25.00 | 5.130 | 0   | 0.4530 | 5.7410 | 66.20 | 7.2254 | 8   | 284.0 | 19.70 | 395.11 | 13.15 | 18.70 |
| 63  | 61  | 0.17171 | 25.00 | 5.130 | 0   | 0.4530 | 5.9660 | 93.40 | 6.8185 | 8   | 284.0 | 19.70 | 378.08 | 14.44 | 16.00 |
| 64  | 62  | 0.11027 | 25.00 | 5.130 | 0   | 0.4530 | 6.4560 | 67.80 | 7.2255 | 8   | 284.0 | 19.70 | 396.90 | 6.73 | 22.20 |
| 65  | 63  | 0.12650 | 25.00 | 5.130 | 0   | 0.4530 | 6.7620 | 43.40 | 7.9809 | 8   | 284.0 | 19.70 | 395.58 | 9.50 | 25.00 |
| 66  | 64  | 0.01951 | 17.50 | 1.380 | 0   | 0.4161 | 7.1040 | 59.50 | 9.2229 | 3   | 216.0 | 18.60 | 393.24 | 8.05 | 33.00 |
| 67  | 65  | 0.03584 | 80.00 | 3.370 | 0   | 0.3980 | 6.2900 | 17.80 | 6.6115 | 4   | 337.0 | 16.10 | 396.90 | 4.67 | 23.50 |
| 68  | 66  | 0.04379 | 80.00 | 3.370 | 0   | 0.3980 | 5.7870 | 31.10 | 6.6115 | 4   | 337.0 | 16.10 | 396.90 | 10.24 | 19.40 |
| 69  | 67  | 0.05789 | 12.50 | 6.070 | 0   | 0.4090 | 5.8780 | 21.40 | 6.4980 | 4   | 345.0 | 18.90 | 396.21 | 8.10 | 22.00 |
| 70  | 68  | 0.13554 | 12.50 | 6.070 | 0   | 0.4090 | 5.5940 | 36.80 | 6.4980 | 4   | 345.0 | 18.90 | 396.90 | 13.09 | 17.40 |
| 71  | 69  | 0.12816 | 12.50 | 6.070 | 0   | 0.4090 | 5.8850 | 33.00 | 6.4980 | 4   | 345.0 | 18.90 | 396.90 | 8.79 | 20.90 |
| 72  | 70  | 0.08826 | 0.00 | 10.810 | 0   | 0.4130 | 6.4170 | 6.60 | 5.2873 | 4   | 305.0 | 19.20 | 383.73 | 6.72 | 24.20 |
| 73  | 71  | 0.15876 | 0.00 | 10.810 | 0   | 0.4130 | 5.9610 | 17.50 | 5.2873 | 4   | 305.0 | 19.20 | 376.94 | 9.88 | 21.70 |
| 74  | 72  | 0.09164 | 0.00 | 10.810 | 0   | 0.4130 | 6.0650 | 7.80 | 5.2873 | 4   | 305.0 | 19.20 | 390.91 | 5.52 | 22.80 |
| 75  | 73  | 0.19539 | 0.00 | 10.810 | 0   | 0.4130 | 6.2450 | 6.20 | 5.2873 | 4   | 305.0 | 19.20 | 377.17 | 7.54 | 23.40 |
| 76  | 74  | 0.07896 | 0.00 | 12.830 | 0   | 0.4370 | 6.2730 | 6.00 | 4.2515 | 5   | 398.0 | 18.70 | 394.92 | 6.78 | 24.10 |
| 77  | 75  | 0.09512 | 0.00 | 12.830 | 0   | 0.4370 | 6.2860 | 45.00 | 4.5026 | 5   | 398.0 | 18.70 | 383.23 | 8.94 | 21.40 |
| 78  | 76  | 0.10153 | 0.00 | 12.830 | 0   | 0.4370 | 6.2790 | 74.50 | 4.0522 | 5   | 398.0 | 18.70 | 373.66 | 11.97 | 20.00 |
| 79  | 77  | 0.08707 | 0.00 | 12.830 | 0   | 0.4370 | 6.1400 | 45.80 | 4.0905 | 5   | 398.0 | 18.70 | 386.96 | 10.27 | 20.80 |
| 80  | 78  | 0.05646 | 0.00 | 12.830 | 0   | 0.4370 | 6.2320 | 53.70 | 5.0141 | 5   | 398.0 | 18.70 | 386.40 | 12.34 | 21.20 |
| 81  | 79  | 0.08387 | 0.00 | 12.830 | 0   | 0.4370 | 5.8740 | 36.60 | 4.5026 | 5   | 398.0 | 18.70 | 396.06 | 9.10 | 20.30 |
| 82  | 80  | 0.04113 | 25.00 | 4.860 | 0   | 0.4260 | 6.7270 | 33.50 | 5.4007 | 4   | 281.0 | 19.00 | 396.90 | 5.29 | 28.00 |
| 83  | 81  | 0.04462 | 25.00 | 4.860 | 0   | 0.4260 | 6.6190 | 70.40 | 5.4007 | 4   | 281.0 | 19.00 | 395.63 | 7.22 | 23.90 |
| 84  | 82  | 0.03659 | 25.00 | 4.860 | 0   | 0.4260 | 6.3020 | 32.20 | 5.4007 | 4   | 281.0 | 19.00 | 396.90 | 6.72 | 24.80 |
| 85  | 83  | 0.03551 | 25.00 | 4.860 | 0   | 0.4260 | 6.1670 | 46.70 | 5.4007 | 4   | 281.0 | 19.00 | 390.64 | 7.51 | 22.90 |
| 86  | 84  | 0.05059 | 0.00 | 4.490 | 0   | 0.4490 | 6.3890 | 48.00 | 4.7794 | 3   | 247.0 | 18.50 | 396.90 | 9.62 | 23.90 |
| 87  | 85  | 0.05735 | 0.00 | 4.490 | 0   | 0.4490 | 6.6300 | 56.10 | 4.4377 | 3   | 247.0 | 18.50 | 392.30 | 6.53 | 26.60 |
| 88  | 86  | 0.05188 | 0.00 | 4.490 | 0   | 0.4490 | 6.0150 | 45.10 | 4.4272 | 3   | 247.0 | 18.50 | 395.99 | 12.86 | 22.50 |
| 89  | 87  | 0.07151 | 0.00 | 4.490 | 0   | 0.4490 | 6.1210 | 56.80 | 3.7476 | 3   | 247.0 | 18.50 | 395.15 | 8.44 | 22.20 |
| 90  | 88  | 0.05660 | 0.00 | 3.410 | 0   | 0.4890 | 7.0070 | 86.30 | 3.4217 | 2   | 270.0 | 17.80 | 396.90 | 5.50 | 23.60 |
| 91  | 89  | 0.05302 | 0.00 | 3.410 | 0   | 0.4890 | 7.0790 | 63.10 | 3.4145 | 2   | 270.0 | 17.80 | 396.06 | 5.70 | 28.70 |
| 92  | 90  | 0.04684 | 0.00 | 3.410 | 0   | 0.4890 | 6.4170 | 66.10 | 3.0923 | 2   | 270.0 | 17.80 | 392.18 | 8.81 | 22.60 |
| 93  | 91  | 0.03932 | 0.00 | 3.410 | 0   | 0.4890 | 6.4050 | 73.90 | 3.0921 | 2   | 270.0 | 17.80 | 393.55 | 8.20 | 22.00 |
| 94  | 92  | 0.04203 | 28.00 | 15.040 | 0   | 0.4640 | 6.4420 | 53.60 | 3.6659 | 4   | 270.0 | 18.20 | 395.01 | 8.16 | 22.90 |
| 95  | 93  | 0.02875 | 28.00 | 15.040 | 0   | 0.4640 | 6.2110 | 28.90 | 3.6659 | 4   | 270.0 | 18.20 | 396.33 | 6.21 | 25.00 |
| 96  | 94  | 0.04294 | 28.00 | 15.040 | 0   | 0.4640 | 6.2490 | 77.30 | 3.6150 | 4   | 270.0 | 18.20 | 396.90 | 10.59 | 20.60 |
| 97  | 95  | 0.12204 | 0.00 | 2.890 | 0   | 0.4450 | 6.6250 | 57.80 | 3.4952 | 2   | 276.0 | 18.00 | 357.98 | 6.65 | 28.40 |
| 98  | 96  | 0.11504 | 0.00 | 2.890 | 0   | 0.4450 | 6.1630 | 69.60 | 3.4952 | 2   | 276.0 | 18.00 | 391.83 | 11.34 | 21.40 |
| 99  | 97  | 0.12083 | 0.00 | 2.890 | 0   | 0.4450 | 8.0690 | 76.00 | 3.4952 | 2   | 276.0 | 18.00 | 396.90 | 4.21 | 38.70 |
| 100 | 98  | 0.08187 | 0.00 | 2.890 | 0   | 0.4450 | 7.8200 | 36.90 | 3.4952 | 2   | 276.0 | 18.00 | 393.53 | 3.57 | 43.80 |

Comments (54)
All Comments

Sort by
Hotness

[![956411-gp.jpg](../_resources/927f264323ee8024265919c87bb6b68a.jpg)![](../_resources/1dea3f3e2f901f1fa5df95e19bf8a5ab.png)](https://www.kaggle.com/marcacohen)

[![3493900-kg.png](../_resources/cedf4bec9ff6f778d2d2b5b6bd4baf86.jpg)![](../_resources/673c9d64cac97f2d74fcc8c2d449c61f.png)](https://www.kaggle.com/adichamoli)![](../_resources/68e0f633614d66f0f824c61f7a7d246c.png)

 [Aditya Chamoli](https://www.kaggle.com/adichamoli)•Posted on Version 17 of 18•8 days ago•[Options]()•[Reply]()


1

Great stuff. thanks for sharing.

[![3694581-kg.jpg](../_resources/16d0fc6634df49213fc52bbbb604b4db.jpg)![](../_resources/a37126250cdceeaaae6192162adcca87.png)](https://www.kaggle.com/python10pm)![](../_resources/68e0f633614d66f0f824c61f7a7d246c.png)

 [python10pm](https://www.kaggle.com/python10pm)Kernel Author•Posted on Version 17 of 18•8 days ago•[Options]()•[Reply]()


1

I am glad you enjoyed it [@adichamoli](https://www.kaggle.com/adichamoli) .

[![4389902-kg.jpg](../_resources/2111725364a4cab3c44be9c12d99c863.jpg)](https://www.kaggle.com/plaxicoburress)![](../_resources/68e0f633614d66f0f824c61f7a7d246c.png)

 [Plaxico Burress](https://www.kaggle.com/plaxicoburress)•Posted on Version 16 of 18•9 days ago•[Options]()•[Reply]()


2

Thanks!

[![3694581-kg.jpg](../_resources/16d0fc6634df49213fc52bbbb604b4db.jpg)](https://www.kaggle.com/python10pm)

 [python10pm](https://www.kaggle.com/python10pm)Kernel Author•Posted on Version 16 of 18•9 days ago•[Options]()•[Reply]()


0

You're welcome [@plaxicoburress](https://www.kaggle.com/plaxicoburress) . Consider upvoting if you haven't done it already. Thanks in advance.

[![3663272-kg.JPG](../_resources/fff1fbdd4685299b704c107fa0e53fad.jpg)](https://www.kaggle.com/dnsigshv)![](../_resources/68e0f633614d66f0f824c61f7a7d246c.png)

 [Dennis Igshv](https://www.kaggle.com/dnsigshv)•Posted on Version 16 of 18•10 days ago•[Options]()•[Reply]()


1

thx for this material !

[![3694581-kg.jpg](../_resources/16d0fc6634df49213fc52bbbb604b4db.jpg)](https://www.kaggle.com/python10pm)

 [python10pm](https://www.kaggle.com/python10pm)Kernel Author•Posted on Version 16 of 18•9 days ago•[Options]()•[Reply]()


0

You're welcome [@dnsigshv](https://www.kaggle.com/dnsigshv) . Consider upvoting if you haven't done it already. Thanks in advance.

[![default-thumb.png](../_resources/f1cee4ded9d19bb202587e7bfaab843f.png)](https://www.kaggle.com/johnjvr)![](../_resources/68e0f633614d66f0f824c61f7a7d246c.png)

 [johnjvr](https://www.kaggle.com/johnjvr)•Posted on Version 15 of 18•11 days ago•[Options]()•[Reply]()


1

Thanks for sharing

[![4196658-kg.png](../_resources/00a303cb6f7469dbc4ea76b645d3f843.png)](https://www.kaggle.com/paulolopez001)![](../_resources/68e0f633614d66f0f824c61f7a7d246c.png)

 [pdnlr](https://www.kaggle.com/paulolopez001)•Posted on Version 15 of 18•11 days ago•[Options]()•[Reply]()


1

Great stuff..yeah, thanks for sharing. Much appreciated!

[![4120018-kg.jpg](../_resources/e845d70860d5bf1df16f93ad11c714ba.jpg)](https://www.kaggle.com/syedmubarak)![](../_resources/68e0f633614d66f0f824c61f7a7d246c.png)

 [Syed Mubarak](https://www.kaggle.com/syedmubarak)•Posted on Version 14 of 18•12 days ago•[Options]()•[Reply]()


1

thanks for sharing really useful

[![3694581-kg.jpg](../_resources/16d0fc6634df49213fc52bbbb604b4db.jpg)](https://www.kaggle.com/python10pm)

 [python10pm](https://www.kaggle.com/python10pm)Kernel Author•Posted on Version 14 of 18•12 days ago•[Options]()•[Reply]()


0

Please also check the numpy tutorial:

https://www.kaggle.com/python10pm/learn-numpy-the-hard-way-70-exercises-solutions

And the pandas tricks:
https://www.kaggle.com/python10pm/pandas-100-tricks
This will give you a solid foundation to do data analysis in Python.
Good luck [@syedmubarak](https://www.kaggle.com/syedmubarak)

[![4170033-kg.jpg](../_resources/b84c4c9daefa4f1de441807fb260d0c0.jpg)](https://www.kaggle.com/muhammetikbal)

 [Muhammet İkbal Elek](https://www.kaggle.com/muhammetikbal)•Posted on Version 14 of 18•15 days ago•[Options]()•[Reply]()


5

Usefull notebook ,Thanks for sharing !

[![358693-gp.jpg](../_resources/5591bf135a01fe77c5ab698f905aa46a.jpg)](https://www.kaggle.com/dzeksen)![](../_resources/68e0f633614d66f0f824c61f7a7d246c.png)

 [Ntandoyenkosi M Ndlovu](https://www.kaggle.com/dzeksen)•Posted on Version 14 of 18•14 days ago•[Options]()•[Reply]()


1

Thanks for sharing. Useful stuff.

[![4170033-kg.jpg](../_resources/b84c4c9daefa4f1de441807fb260d0c0.jpg)](https://www.kaggle.com/muhammetikbal)![](../_resources/01f8a1145fed1c5fa0d92cb8f70542cc.png)

 [Muhammet İkbal Elek](https://www.kaggle.com/muhammetikbal)•Posted on Version 14 of 18•18 days ago•[Options]()•[Reply]()


8

Good Job ! Thanks for sharing

[![3694581-kg.jpg](../_resources/16d0fc6634df49213fc52bbbb604b4db.jpg)](https://www.kaggle.com/python10pm)

 [python10pm](https://www.kaggle.com/python10pm)Kernel Author•Posted on Version 14 of 18•18 days ago•[Options]()•[Reply]()


0

Thank you [@muhammetikbal](https://www.kaggle.com/muhammetikbal) . Please upvote if you haven't already :)

[![2346157-kg.jpg](../_resources/c4afd9b9e60858b99a6ecea37aa1e4a9.jpg)](https://www.kaggle.com/arc4num)![](../_resources/68e0f633614d66f0f824c61f7a7d246c.png)

 [Enter your display name](https://www.kaggle.com/arc4num)•Posted on Version 14 of 18•15 days ago•[Options]()•[Reply]()


1

Thanks!

[![2918899-kg.jpg](../_resources/baf1cf2905c07b98f9be26fc44341859.jpg)](https://www.kaggle.com/saharseidi)![](../_resources/68e0f633614d66f0f824c61f7a7d246c.png)

 [Sahar Seidi Khorramabadi](https://www.kaggle.com/saharseidi)•Posted on Version 14 of 18•18 days ago•[Options]()•[Reply]()


1

Thanks for sharing this!

[![3694581-kg.jpg](../_resources/16d0fc6634df49213fc52bbbb604b4db.jpg)](https://www.kaggle.com/python10pm)![](../_resources/68e0f633614d66f0f824c61f7a7d246c.png)

 [python10pm](https://www.kaggle.com/python10pm)Kernel Author•Posted on Version 14 of 18•18 days ago•[Options]()•[Reply]()


1

Youre welcome [@saharseidi](https://www.kaggle.com/saharseidi) . Don't forget to upvote if you found it useful.

[![4131081-kg.JPG](../_resources/60a87961a43aa4ce7a7a265f1dbe3f63.jpg)](https://www.kaggle.com/danielcastagna)![](../_resources/68e0f633614d66f0f824c61f7a7d246c.png)

 [Daniel Castagna](https://www.kaggle.com/danielcastagna)•Posted on Version 14 of 18•18 days ago•[Options]()•[Reply]()


1

Very nice! tks!

[![3694581-kg.jpg](../_resources/16d0fc6634df49213fc52bbbb604b4db.jpg)](https://www.kaggle.com/python10pm)

 [python10pm](https://www.kaggle.com/python10pm)Kernel Author•Posted on Version 14 of 18•18 days ago•[Options]()•[Reply]()


0

Thanks Daniel and please upvote :)

[![807182-kg.jpg](../_resources/5b74a1950bd14259561aeb1e3417257f.jpg)](https://www.kaggle.com/bombatkarvivek)![](../_resources/68e0f633614d66f0f824c61f7a7d246c.png)

 [Vivek Bombatkar](https://www.kaggle.com/bombatkarvivek)•Posted on Version 14 of 18•19 days ago•[Options]()•[Reply]()


1

Upvote done.
Like the idea of such kernals, for our personal learning as well.

[![3694581-kg.jpg](../_resources/16d0fc6634df49213fc52bbbb604b4db.jpg)](https://www.kaggle.com/python10pm)

 [python10pm](https://www.kaggle.com/python10pm)Kernel Author•Posted on Version 14 of 18•19 days ago•[Options]()•[Reply]()


0

Thank you [@bombatkarvivek](https://www.kaggle.com/bombatkarvivek) .

The main idea was to have this kind of kernels for fast reference. I have 2 about pandas and numpy will be released on Monday.

Nico

[![default-thumb.png](../_resources/f1cee4ded9d19bb202587e7bfaab843f.png)](https://www.kaggle.com/mhertz)![](../_resources/68e0f633614d66f0f824c61f7a7d246c.png)

 [Michael Zheng](https://www.kaggle.com/mhertz)•Posted on Version 13 of 18•20 days ago•[Options]()•[Reply]()


1

Thanks for sharing!

[![3694581-kg.jpg](../_resources/16d0fc6634df49213fc52bbbb604b4db.jpg)](https://www.kaggle.com/python10pm)

 [python10pm](https://www.kaggle.com/python10pm)Kernel Author•Posted on Version 13 of 18•20 days ago•[Options]()•[Reply]()


0

Thank you [@mhertz](https://www.kaggle.com/mhertz) , would you mind upvoting the kernel? This would help me a lot and will spread the message.

[![2182277-kg.jpg](../_resources/65471d2f41998f1482019e36ae441e7a.jpg)](https://www.kaggle.com/sumitm004)![](../_resources/68e0f633614d66f0f824c61f7a7d246c.png)

 [Sumit Mishra](https://www.kaggle.com/sumitm004)•Posted on Version 13 of 18•20 days ago•[Options]()•[Reply]()


1

Thanks for sharing.

[![3694581-kg.jpg](../_resources/16d0fc6634df49213fc52bbbb604b4db.jpg)](https://www.kaggle.com/python10pm)

 [python10pm](https://www.kaggle.com/python10pm)Kernel Author•Posted on Version 13 of 18•20 days ago•[Options]()•[Reply]()


0

Hello [@sumitm004](https://www.kaggle.com/sumitm004) . Thank you. Can you please upvote the kernel. This will help me a lot.

[![3486296-kg.png](../_resources/9e115159dbe3caf31b9057c31609b00a.png)](https://www.kaggle.com/dasmehdixtr)![](../_resources/68e0f633614d66f0f824c61f7a7d246c.png)

 [dasmehdixtr](https://www.kaggle.com/dasmehdixtr)•Posted on Version 12 of 18•21 days ago•[Options]()•[Reply]()


1

Very nice notebook, thanks for share!

[![3694581-kg.jpg](../_resources/16d0fc6634df49213fc52bbbb604b4db.jpg)](https://www.kaggle.com/python10pm)

 [python10pm](https://www.kaggle.com/python10pm)Kernel Author•Posted on Version 13 of 18•20 days ago•[Options]()•[Reply]()


0

Thank you. I am happy you found it useful.

[![3012786-kg.JPG](../_resources/20d36a99ca67af09b144ef3840e3c549.jpg)](https://www.kaggle.com/mpwolke)![](../_resources/68e0f633614d66f0f824c61f7a7d246c.png)

 [Marília Prata](https://www.kaggle.com/mpwolke)•Posted on Version 12 of 18•21 days ago•[Options]()•[Reply]()


1

Another amazing work from you. Now, we're waiting to read the Numpy Notebook.

[![3694581-kg.jpg](../_resources/16d0fc6634df49213fc52bbbb604b4db.jpg)](https://www.kaggle.com/python10pm)

 [python10pm](https://www.kaggle.com/python10pm)Kernel Author•Posted on Version 13 of 18•20 days ago•[Options]()•[Reply]()


0

Thank you [@mpwolke](https://www.kaggle.com/mpwolke) . It takes some time to create one since I am doing it in my free time. Hopefully I will have it on next Monday.

[![2960676-kg.png](../_resources/7ee7ac1fb5338e74ed47a452fa3edc48.png)](https://www.kaggle.com/felvizzz)![](../_resources/68e0f633614d66f0f824c61f7a7d246c.png)

 [FeLvi](https://www.kaggle.com/felvizzz)•Posted on Version 11 of 18•21 days ago•[Options]()•[Reply]()


1

Thank you for sharing

[![3694581-kg.jpg](../_resources/16d0fc6634df49213fc52bbbb604b4db.jpg)](https://www.kaggle.com/python10pm)

 [python10pm](https://www.kaggle.com/python10pm)Kernel Author•Posted on Version 11 of 18•21 days ago•[Options]()•[Reply]()


0

Thank you [@felvizzz](https://www.kaggle.com/felvizzz) . I am working on a similar one about numpy. I will post a comment when it's done.

Cheers

[![1807168-kg.jpg](../_resources/0fe7f4ac6524b5be6d08d4b108f1d25f.jpg)](https://www.kaggle.com/vishnurapps)![](../_resources/68e0f633614d66f0f824c61f7a7d246c.png)

 [Vishnu R](https://www.kaggle.com/vishnurapps)•Posted on Version 10 of 18•22 days ago•[Options]()•[Reply]()


1

Thanks [@python10pm](https://www.kaggle.com/python10pm) for creating this wonderful excercise. I learned a lot from reading and executing this kernel. Thanks for sharing this with the commuity.

[![3694581-kg.jpg](../_resources/16d0fc6634df49213fc52bbbb604b4db.jpg)](https://www.kaggle.com/python10pm)

 [python10pm](https://www.kaggle.com/python10pm)Kernel Author•Posted on Version 11 of 18•21 days ago•[Options]()•[Reply]()


0

Hello [@vishnurapps](https://www.kaggle.com/vishnurapps) ,
Thank you my friend for your words.
You can also check this one about pandas tricks.
https://www.kaggle.com/python10pm/pandas-100-tricks
And Numpy is coming soon.

[![1200915-kg.png](../_resources/400109a4b53e3d588a76ede097cc56f5.png)](https://www.kaggle.com/bulentsiyah)![](../_resources/68e0f633614d66f0f824c61f7a7d246c.png)

 [Bulent Siyah](https://www.kaggle.com/bulentsiyah)•Posted on Version 6 of 18•a month ago•[Options]()•[Reply]()


7

it is really very useful. Thanks a lot for the effort

[![3694581-kg.jpg](../_resources/16d0fc6634df49213fc52bbbb604b4db.jpg)](https://www.kaggle.com/python10pm)![](../_resources/68e0f633614d66f0f824c61f7a7d246c.png)

 [python10pm](https://www.kaggle.com/python10pm)Kernel Author•Posted on Version 6 of 18•a month ago•[Options]()•[Reply]()


1

Thank you [@bulentsiyah](https://www.kaggle.com/bulentsiyah) . I hope you learned a lot.

[![2735179-kg.jpg](../_resources/047a03a574e44f303e446d2b099e354f.jpg)](https://www.kaggle.com/alenavorushilova)![](../_resources/68e0f633614d66f0f824c61f7a7d246c.png)

 [voru588](https://www.kaggle.com/alenavorushilova)•Posted on Version 10 of 18•22 days ago•[Options]()•[Reply]()


2

This is the most compleat guide for Pandas! Saved it and keep it as a reference

[![3694581-kg.jpg](../_resources/16d0fc6634df49213fc52bbbb604b4db.jpg)](https://www.kaggle.com/python10pm)![](../_resources/68e0f633614d66f0f824c61f7a7d246c.png)

 [python10pm](https://www.kaggle.com/python10pm)Kernel Author•Posted on Version 10 of 18•22 days ago•[Options]()•[Reply]()


1

Thank you.
You also have this compilation of tricks from dataschool.io
https://www.kaggle.com/python10pm/pandas-100-tricks
Happy learning [@alenavorushilova](https://www.kaggle.com/alenavorushilova)

[![2048920-kg.jpeg](../_resources/bdb324dc6e4b96c4e0b1935d7fc2789c.jpg)](https://www.kaggle.com/saeedtqp)![](../_resources/68e0f633614d66f0f824c61f7a7d246c.png)

 [Saeed Taghipour](https://www.kaggle.com/saeedtqp)•Posted on Version 9 of 18•24 days ago•[Options]()•[Reply]()


1

very useful , Thank you for Share

[![3694581-kg.jpg](../_resources/16d0fc6634df49213fc52bbbb604b4db.jpg)](https://www.kaggle.com/python10pm)![](../_resources/68e0f633614d66f0f824c61f7a7d246c.png)

 [python10pm](https://www.kaggle.com/python10pm)Kernel Author•Posted on Version 9 of 18•23 days ago•[Options]()•[Reply]()


1

Your welcome [@saeedtqp](https://www.kaggle.com/saeedtqp)

[![4311912-kg.jpg](../_resources/b84f83b65a7212d7e9d59d28653d910f.jpg)](https://www.kaggle.com/vinayakmishra)![](../_resources/68e0f633614d66f0f824c61f7a7d246c.png)

 [Vinayak Mishra](https://www.kaggle.com/vinayakmishra)•Posted on Version 8 of 18•a month ago•[Options]()•[Reply]()


1

how can we download this kernal.?

[![3694581-kg.jpg](../_resources/16d0fc6634df49213fc52bbbb604b4db.jpg)](https://www.kaggle.com/python10pm)

 [python10pm](https://www.kaggle.com/python10pm)Kernel Author•Posted on Version 9 of 18•23 days ago•[Options]()•[Reply]()


0

Hello, you must fork the kernel, and then open it in your machine,
When you open the kernel, you must click File section and download.
Sorry for the delay.

![inbox/3694581/e4cbd5e71e7728b33e0aff93b469119b/download.PNG](../_resources/db772f4a3ea00025df6a894b1ad4b4ed.png)

PS: Spoiler alert, Numpy Kernel is coming soon.

[![2566546-kg.png](../_resources/6d0775ee0aedb94d4dc96b1ee47f16ee.png)](https://www.kaggle.com/mashlyn)![](../_resources/68e0f633614d66f0f824c61f7a7d246c.png)

 [Mashlyn](https://www.kaggle.com/mashlyn)•Posted on Version 8 of 18•a month ago•[Options]()•[Reply]()


1

This kernel is also very useful! Thanks for sharing!!

[![3694581-kg.jpg](../_resources/16d0fc6634df49213fc52bbbb604b4db.jpg)](https://www.kaggle.com/python10pm)

 [python10pm](https://www.kaggle.com/python10pm)Kernel Author•Posted on Version 8 of 18•a month ago•[Options]()•[Reply]()


0

Thank you [@mashlyn](https://www.kaggle.com/mashlyn) ! I am very greatful for your support.

[![default-thumb.png](../_resources/f1cee4ded9d19bb202587e7bfaab843f.png)](https://www.kaggle.com/ezlovelace)

 [Elijah Lovelace](https://www.kaggle.com/ezlovelace)•Posted on Latest Version•14 hours ago•[Options]()•[Reply]()


0

Very helpful, thanks for sharing!

[![2202312-gp.jpg](../_resources/cf394afaf106f70c2c639f7f459294a6.jpg)](https://www.kaggle.com/prayankkul)

 [Prayank](https://www.kaggle.com/prayankkul)•Posted on Latest Version•2 days ago•[Options]()•[Reply]()


0

Great work !! Helps a lot

[![default-thumb.png](../_resources/f1cee4ded9d19bb202587e7bfaab843f.png)](https://www.kaggle.com/prabhjeets)

 [Coding Singh](https://www.kaggle.com/prabhjeets)•Posted on Latest Version•3 days ago•[Options]()•[Reply]()


0

Thank you

[![default-thumb.png](../_resources/f1cee4ded9d19bb202587e7bfaab843f.png)](https://www.kaggle.com/siddarthbulusu)

 [Siddarth Bulusu](https://www.kaggle.com/siddarthbulusu)•Posted on Latest Version•4 days ago•[Options]()•[Reply]()


0

nice

[![4412678-kg.jpg](../_resources/1cc7af5ed21495864743961ad9839518.jpg)](https://www.kaggle.com/hgarg9)

 [Harshit Garg](https://www.kaggle.com/hgarg9)•Posted on Latest Version•5 days ago•[Options]()•[Reply]()


0

Thank you.

[![default-thumb.png](../_resources/f1cee4ded9d19bb202587e7bfaab843f.png)](https://www.kaggle.com/mirzamawaz)

 [Mirza Mawaz](https://www.kaggle.com/mirzamawaz)•Posted on Version 17 of 18•6 days ago•[Options]()•[Reply]()


0

nice share. thank you

[![3694581-kg.jpg](../_resources/16d0fc6634df49213fc52bbbb604b4db.jpg)](https://www.kaggle.com/python10pm)

 [python10pm](https://www.kaggle.com/python10pm)Kernel Author•Posted on Version 15 of 18•11 days ago•[Options]()•[Reply]()


0

Thank you all folks for your support. I am really happy you found all the pandas and numpy series useful.

[![default-thumb.png](../_resources/f1cee4ded9d19bb202587e7bfaab843f.png)](https://www.kaggle.com/prudhvinagula)

 [Prudhvi NVM](https://www.kaggle.com/prudhvinagula)•Posted on Version 14 of 18•16 days ago•[Options]()•[Reply]()


0

Thanks for sharing [@python10pm](https://www.kaggle.com/python10pm)

[![2684086-gp.jpg](../_resources/e34d970d9078344bb3500e8d449b9013.png)](https://www.kaggle.com/dima8bit)

 [Dima8bit](https://www.kaggle.com/dima8bit)•Posted on Version 13 of 18•20 days ago•[Options]()•[Reply]()


0

thanks for sharing! I find it very useful as a beginner Py analyst!

[![default-thumb.png](../_resources/f1cee4ded9d19bb202587e7bfaab843f.png)](https://www.kaggle.com/mauliktailor)

 [Maulik Tailor](https://www.kaggle.com/mauliktailor)•Posted on Version 9 of 18•22 days ago•[Options]()•[Reply]()


0

Thank you for sharing

[![2853724-gr.jpg](../_resources/e0d87e3a7553745c762a11735d8f6ecb.jpg)](https://www.kaggle.com/moraviann)

 [Kubilay Gazioglu](https://www.kaggle.com/moraviann)•Posted on Version 9 of 18•23 days ago•[Options]()•[Reply]()


0

Seems good, thanks a lot

Showing 50 of 54 comments. [Show More]()
Similar Kernels
[(L)](https://www.kaggle.com/pavansanagapati/)
![](../_resources/25bc01c4dcdc78b2af6cc31e61437304.png)

[(L)](https://www.kaggle.com/python10pm/)
![](../_resources/25bc01c4dcdc78b2af6cc31e61437304.png)

[(L)](https://www.kaggle.com/kabure/)
![thumb76_76.png](../_resources/574bc7fe9c0ea4ebabe102f63002f130.png)

[(L)](https://www.kaggle.com/vinothan/)
![thumb76_76.png](../_resources/e44feeb1795dad0c1643383028127d93.jpg)

[(L)](https://www.kaggle.com/kpacocha/)
![thumb76_76.png](../_resources/e44feeb1795dad0c1643383028127d93.jpg)