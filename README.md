# Chinese_University_Entrance_Ranking_GD
This is a repo to predict the university admission ranking in different year

## The main questions in this project
- Can we predict the approximate admission lowest ranking of different universities?
- If we can, what parameters is related to it?
 - The admission quatities?
 - The previous admission lowest ranking?
 - The university ranking of those years?
 - The media impact of those years?
 - The ecomonic of the city?
 - The house price of the city?
 - The participate students number?
 - Should I use ranking or marks or percentage to represent the enroll information

All the above variables may be able to influence the choice of each student, so that may influence the ranking. In this project, R will be used in cleaning and merging the data, doing the data pre-process like PCA and using some machinery algorithm to do the prediction. The following variables will used in analysing the data, more variables will be added:

- The university ranking
- The admission quantities
- Previous lowest admission ranking
- The GDP of the city
- The media impact
- The distance

## The previous research on this topic
Not many articles are relating to this topic while the baidu education has a application to help you choosing the application university via the big data, which I think will do the prediction insid

## Analysis chart
Several figure will be present the basic situation of the University Entrance Exam in Guangdong

- The admission population of different province variate with years
 - Enrolled Student of universities in Guangdong

![GD enrroled Number](https://github.com/duxuhao/Chinese_University_Entrance_Ranking_GD/blob/master/Analsys_Figure/GD enrroled Number.png )

 - Enrolled Student of universities Guangdong

![Province Enrolled Number without GD](https://github.com/duxuhao/Chinese_University_Entrance_Ranking_GD/blob/master/Analsys_Figure/Province Enrolled Number without GD.png )

- The GDP per person in each province variate with years

![GDP_PER_PERSON](https://github.com/duxuhao/Chinese_University_Entrance_Ranking_GD/blob/master/Analsys_Figure/GDP_PER_PERSON.png )
- The students' population variate with years in Guangdong

![GDStudentNumber](https://github.com/duxuhao/Chinese_University_Entrance_Ranking_GD/blob/master/Analsys_Figure/GDStudentNumber.png )
- The lowest admission ranking of different universities variate with years
 - Science
(https://github.com/duxuhao/Chinese_University_Entrance_Ranking_GD/blob/master/Analsys_Figure/ScienceUniversityLowestRank.png )
 - Liberal Art
(https://github.com/duxuhao/Chinese_University_Entrance_Ranking_GD/blob/master/Analsys_Figure/ArtLeberalUniversityLowestRank.png )

A more clear figure of different ranking range is include in this repo as well.

- The 1A Universities quantities of each Province
```
        Year
Province 2010 2011 2012 2013 2014 2015
  上海     14   17   21   20   24   23
  内蒙古    2    2    3    1    2    2
  北京     50   52   52   50   49   56
  吉林      6    6    8    6    6    7
  四川      8    8   10    9   11   15
  天津      6    7    5    5    5    5
  安徽      5    5    7    7    7    6
  山东      8    9   10    9    8    9
  山西      1    1    2    1    1    3
  广东     22   22   25   24   31   33
  广西      2    3    3    3    3    3
  新疆      0    0    2    1    1    2
  江苏     22   22   26   26   27   28
  江西      2    2    4    2    4    7
  河北      9    9   11    8    8    9
  河南      2    2    3    2    2    4
  浙江      3    3    3    3    5    6
  海南      2    2    2    2    2    2
  湖北     14   14   15   14   15   15
  湖南      9    9   14    9   13   18
  甘肃      2    2    2    2    2    2
  福建      5    6    7    6    8   10
  贵州      2    2    2    2    2    2
  辽宁     11   11   15   12   12   15
  重庆      6    6    7    6    8   10
  陕西     17   16   20   17   17   17
  黑龙江    9    8   14   10   11   13
```
 - 2010 universities consistance in all provinces

![ProvinceUniversities2014](https://github.com/duxuhao/Chinese_University_Entrance_Ranking_GD/blob/master/Analsys_Figure/ProvinceUniversities2010.png )

 - 2014 universities consistance in all provinces

![ProvinceUniversities2014](https://github.com/duxuhao/Chinese_University_Entrance_Ranking_GD/blob/master/Analsys_Figure/ProvinceUniversities2014.png )

 - universities consistance in all provinces variate with years

![ProvinceUniversitiesWithYears](https://github.com/duxuhao/Chinese_University_Entrance_Ranking_GD/blob/master/Analsys_Figure/ProvinceUniversitiesWithYears.png )

##Prediction method
- In the prediction section, R and python are used together and the following method is used in this prediction
 - Random Forest
 - Decision Tree
 - Adaboost

##Result

The prediction tree do the best job, here is the result:

Features include:
UniversityNo,Average_Ranking,Last_Ranking,Distance,GDP_Per_Person,Ranking_Scores,Media_Impact,Year,Topic,Plan_Number,Plan_Number_Total

- Decision Tree: 99.7%
 - The error within 10.0%: 82.3%
 - The error within 5.0%: 68.1%
 - The mean error: 15.3%
- Top university adjust
 - The error within 10.0%: 83.5%
 - The error within 5.0%: 67.8%
 - The mean error: 6.1%

![Prediction](https://github.com/duxuhao/Chinese_University_Entrance_Ranking_GD/blob/master/Analsys_Figure/Prediction.png )

