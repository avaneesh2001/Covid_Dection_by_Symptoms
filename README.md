# Covid19 Prediction based on Symptoms
### Via Random Forest model

### About Covid 19
_From WHO website_

>Coronavirus disease (COVID-19) is an infectious disease caused by the SARS-CoV-2 virus.
>Most people infected with the virus will experience mild to moderate respiratory illness and recover without requiring special treatment. However, some will become seriously ill and require medical attention. Older people and those with underlying medical conditions like cardiovascular disease, diabetes, chronic respiratory disease, or cancer are more likely to develop serious illness. Anyone can get sick with COVID-19 and become seriously ill or die at any age.

### Dataset
The data for developing model was taken from [Here](https://github.com/nshomron/covidpred/blob/master/data/corona_tested_individuals_ver_006.english.csv.zip)

This dataset was cleaned and classificaion performed using python in a jupyter noterbook. The clead data set can be found in data folder and is saved as ***data.csv***. You can also find it by clicking [here](https://github.com/avaneesh2001/ML_project/blob/main/data/data.csv)

### Classification model
Classificaion was done using logistic regression and Random forest and the following confusion matrix was obtained.

![Confusion matrix](https://github.com/avaneesh2001/ML_project/blob/main/Confusion_mat.png)
 \
The Accuracy Precision and recall along with F1 score were better for the random forest model and so I went with it.

### Python Scripts
####   Random_forest.py
This python program creates the random forest model using the ***data.csv*** dataset and saves it as a joblib file.
#### Predictions.py
This python program accepts user information and uses it to predict covid 19 condition of the user using the created model.
