# Capstone Project:
#### Group Members
- Hilary Henshaw
- Kyle Nadeau
- Ashley Velasquez

# Customer Churn Prediction and Analysis

## Overview

This project focuses on predicting customer churn using machine learning and identifying the key factors that contribute to customer attrition. The goal is to help businesses better understand churn behavior and make data-driven decisions to improve customer retention.

The workflow includes data preprocessing, model training, evaluation, and translating results into actionable business insights. The final outputs can be used for dashboards, reporting, and decision-making.

---

## Dataset

The dataset used is the Telco Customer Churn dataset, which includes customer demographics, account information, and service usage.

After cleaning:

* Total records: 7,032
* Features: 20
* Target variable: Churn (0 = Stay, 1 = Leave) 

Key preprocessing steps:

* Converted TotalCharges and MonthlyCharges to numeric
* Handled missing values by removing incomplete rows
* Encoded categorical variables using one-hot encoding
* Standardized numerical features

---

## Methodology

### Models Implemented

* Logistic Regression
* Random Forest
* Extra Trees
* Gradient Boosting
* K-Nearest Neighbors

### Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1 Score
* ROC AUC

Stratified 5-fold cross-validation was used to ensure balanced evaluation across churn classes.

---

## Model Performance

| Model               | Accuracy | Precision | Recall | F1 Score | ROC AUC |   |
| ------------------- | -------- | --------- | ------ | -------- | ------- | - |
| Logistic Regression | 0.75     | 0.52      | 0.80   | 0.63     | 0.85    |   |
| Gradient Boosting   | 0.80     | 0.66      | 0.52   | 0.58     | 0.85    |   |
| KNN                 | 0.77     | 0.57      | 0.54   | 0.56     | 0.80    |   |
| Random Forest       | 0.79     | 0.64      | 0.49   | 0.55     | 0.83    |   |
| Extra Trees         | 0.77     | 0.59      | 0.47   | 0.52     | 0.79    |   |

### Final Model Selection

Logistic Regression was selected as the final model due to its strong balance between recall and F1 score.

---

## Key Insights

### 1. Customer Retention Patterns

* Customers with **low tenure** are the most likely to churn
* Early-stage customer experience plays a critical role in retention

### 2. Pricing Impact

* Higher **monthly charges** are associated with increased churn risk
* Pricing sensitivity is a major driver of customer decisions

### 3. Service Influence

* Certain **internet service types** contribute more to churn
* Indicates potential issues in service quality or value perception

### 4. Customer Value Indicators

* Total charges and payment methods also influence churn behavior
* These features help identify long-term engagement patterns

---

## Feature Importance

Top drivers of churn:

1. Tenure
2. Monthly Charges
3. Internet Service
4. Total Charges
5. Payment Method 

Tenure is the most important factor, indicating that customer lifecycle stage is the strongest predictor of churn.

---

## Model Behavior

* High recall (~80%) means the model successfully identifies most customers who will churn
* Lower precision (~49%) means some non-churn customers are flagged as churn

This tradeoff is intentional, as missing a churn customer is more costly than incorrectly flagging one.

---

## Customer Risk Segmentation

Customers were grouped based on predicted churn probability:

* High Risk: ≥ 0.70
* Medium Risk: 0.40 – 0.69
* Low Risk: < 0.40 

This segmentation allows businesses to prioritize intervention strategies.

---

## Business Applications

### Targeted Retention

* Focus on high-risk customers with personalized outreach
* Implement loyalty programs and incentives

### Pricing Optimization

* Reevaluate pricing for customers with high monthly charges
* Introduce flexible plans or bundles

### Customer Experience Improvement

* Improve onboarding for new customers
* Address service-related issues tied to churn

### Decision Support

* Integrate predictions into Power BI dashboards
* Enable real-time monitoring of churn risk

---
## How to Run Project (MacOS)
### Setup Postgres SQL Database
* Requires local version of project database
- Install and run in terminal:
```
brew install postgresql
brew services start postgresql
```
- Open PostgresSQL and create new database:
```
psql -d postgres
CREATE DATABASE customer_retention;
```
### Setup config.yaml File
- Config file to hold credentials for your database
```yaml
host: localhost
port: 5432
database: customer_retention
user: username
password: password
```
- Add file to directory in project root called "config"
### Compile C++ Library
- Run in project root directory:
```
g++ -shared -fPIC -std=c++17 -o src/cpp_engine/libchurn_risk.dylib src/cpp_engine/churn_risk.cpp
```
### Run Pipeline
- Run in project root directory:
```
make pipeline
```
- This will run every portion of the project with one command
### Result
- View PowerBi dashboard in respective directory

---

## Conclusion

This project demonstrates how machine learning can be used not only to predict churn but also to uncover the underlying drivers of customer behavior. By combining predictive modeling with business insights, organizations can take proactive steps to reduce churn and improve long-term customer retention.
