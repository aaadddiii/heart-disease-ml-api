## Heart Disease Detecting Machine Learning API

The API has a machine learning model that predicts whether a person had heart disease or not based on some medical assesments.<br/>
About 610,000 people die of heart disease in the United States every year–that’s 1 in every 4 deaths.<br/>
Heart disease is the leading cause of death for both men and women. More than half of the deaths due to heart disease in 2009 were in men.<br/>
Coronary heart disease (CHD) is the most common type of heart disease, killing over 370,000 people annually.<br/>
Every year about 735,000 Americans have a heart attack. Of these, 525,000 are a first heart attack and 210,000 happen in people who have already had a heart attack.<br/>
Heart disease is the leading cause of death for people of most ethnicities in the United States, including African Americans, Hispanics, and whites. For American Indians or Alaska Natives and Asians or Pacific Islanders, heart disease is second only to cancer.<br/>
The goal is to predict the binary class heart_disease_present, which represents whether or not a patient has heart disease:<br/>
0 represents no heart disease present <br/>
1 represents heart disease present <br/> 
<br/>
The model is trained using UCL heart disease dataset <br/>
the model is integrated with  django framework to make this a rest API <br/>
To use the API the send the json in the following format to https://heartmlapi.herokuapp.com/weight/ <br/>
```
{ 
   "age":,
  "sex":,
  "cp":,
  "trestbps":,
  "chol":,
  "fbs":,
  "restecg":,
  "thalach":,
  "exang":,
  "oldpeak":,
  "slope":,
   "ca":,
  "thal":
}
```
For example :
```
{ 
   "age":57,
  "sex":1,
  "cp":3,
  "trestbps":170,
  "chol":288,
  "fbs":0,
  "restecg":0,
  "thalach":159,
  "exang":0,
  "oldpeak":0.2,
  "slope":1,
   "ca":0,
  "thal":3
}
```
The kaggle ucl heart disease dataset is used for training the model , refer  https://www.kaggle.com/ronitf/heart-disease-uci for more information about the dataset used <br/>

The API is hosted in heroku<br/>
[@rawho](https://github.com/rawho) made a front end that uses this api, checkout https://rahult.in/heart-api-frontend/

For more information check ipython notebook used to train the model in the repository <br/>
