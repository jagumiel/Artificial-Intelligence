# Diabetes diag

This algorithm detects if a person may have diabetes using some input data. I followed [this video tutorial](https://www.youtube.com/watch?v=FWOZmmIUqHg) to replicate the steps.

The aim was to comprobate if the results had coherence after obfuscating the input data, in order to anonymize even more the patient. Health data should be personal!

Given a dataset containing parameters which are related to the diabetes disease, the porpoise was to replicate the model to predict if a patient may suffer from that illness or not.
[Here is the dataset to download!](https://www.kaggle.com/kumargh/pimaindiansdiabetescsv)


The more susceptible information on the dataset was the age of the patients, and this data was not the most relevant to diagnose diabetes. The method used to obfuscate this information was setting the age on ranges ([11-20], [21-30], ... , [71-80]). As this value in not comprehensible for the dataset, the mid-value of the range was used instead (16, 26, ... , 76).

The results obtained were very similar in both cases, and this can be seen on the Jupyter resume after training and testing the model with both datasets:



|  | **Model based on Raw Dataset** | **Model based on Anonymized dataset** |
| ------ | ------ | ------ |
| **Accuracy** | 0.7602459 | 0.7602459 |
| **Accuracy Baseline** | 0.6577869 | 0.6577869 |
| **Auc** | 0.7961647 | 0.8005204 |
| **Auc Precision Recall** | 0.6653 | 0.6717732 |
| **Average Loss** | 0.52358043 | 0.51717496 |
| **Label/mean** | 0.34221312 | 0.34221312 |
| **Loss** | 0.5233023 | 0.51687473 |
| **Precision** | 0.72321427 | 0.7314815 |
| **Prediction/mean** | 0.3392083 | 0.3290721 |
| **Recall** | 0.48502994 | 0.4730539 |
| **Global step** | 1000 | 1000 |
