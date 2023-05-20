# lowbirthweight.1
                                       Analysis of Factors of Low Birth Weight
The data on 189 births were collected at Bay state Medical Center,Springfield,Mass,during 1986.
The data set contains an indicator of low infant birth weight as a reponse and several risk factors associated with birth weight. 
The data set contains the following variables: 
 + low : indicator of birth weight either >=2.5kg(normal weight) or <2.5kg(underweight) 
 + age :mother’s age in years + lwt : Mother’s weight in pounds at last menstrual period 
 + race: Mother’s race(white, black or other) 
 + smoke: Smoking status during pregnancy(yes,no) 
 + ht :History of hypertension(yes,no) 
 + ui : Presence of uterine irritability(yes,no) 
 + ftv: Number of physician visits during 1st trimester(0-6) 
 + ptl : Number of previous premature labours(0-3) + bwt :Birth weight in grams
We will first tidy our dataset by: 
 + categorizing our ordinal and categorical variables into factors 
 + converting lwt and bwt into the same unit of measurement(kgs)

