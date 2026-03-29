# DSP 557 Capstone Project:
#### Group Members
- Kyle Nadeau
- Hilary Henshaw
- Ashley Velasquez

## Project Goals
The aim of this project is to develop a data-driven predictive analytics solution that can accurately predict and identify customer churn and help businesses understand the key factors influencing the decisions of customers to leave. By analyzing historical customer data, the project seeks to identify patterns and uncover trends associated with churn behavior. Additionally the project aims to segment customers into different risk levels (low, medium, high) and provide actionable insights that businesses can use to support and implement targeted retention strategies. Ultimately, this project will demonstrate how data-driven approaches can enable organizations to support better decision-making to reduce customer loss, improve customer satisfaction, and make more informed business decisions using predictive analytics.


## Methodologies
### Data Source
- The Telco Customer Churn dataset will be used for this project, it includes customer demographics, service usage, and billing information. The Project will follow a structured data analytics approach, beginning with data collection and preprocessing. Data cleaning will involve handling missing values, converting data types and encoding categorical variables into numerical formats suitable for modeling.
    - - https://www.kaggle.com/datasets/blastchar/telco-customer-churn
### Exploratory Analysis
- Exploratory Data Analysis (EDA) will be conducted using Python to identify trends, correlations, and patterns within the data. Power Bi visualization will be used to further examine how factors such as contract type, tenure and monthly charges correlate with customer churn.
### Machine Learning
- Following EDA, multiple machine learning models will be developed and evaluated, including Logistic Regression, Random Forest, and Gradient Boosting. These models will be compared using performance metrics such as accuracy, precision, recall, F1-score, and ROC-AUC.
    - Based on the evaluation results, Gradient Boosting was identified as the best-performing model, achieving an accuracy of 80.41%. As a result, this model will be selected as the final model for predicting customer churn, due to its ability to capture complex patterns and interactions within the data.
### Dashboards/Visualizations
- Results will be presented through an interactive dashboard using tools such as Power BI and Tableau. This dashboard will allow users to explore churn trends, identify high-risk customers, and gain insights into key drivers of churn.

## Possible Outcomes
- The expected outcome of this project is the development of a predictive model capable of identifying customers who are at high risk if leaving a service. Additionally, the analysis is expected to reveal key factors that influence customer churn, such as contract type, service usage patterns, and billing characteristics. 
- The project may also provide a comparative evaluation of different machine learning models, highlighting the strengths and limitations of each approach in the context of churn prediction. Visualizations and summary statistics will further support the interpretation of results and provide a clear understanding of customer behavior. 

## Implications of the proposed project
The success of this project has the potential to enhance both business workflows and customer management, as well as the raw customer experience. From  a business perspective, customers with a high likelihood to churn will be identified early, showing exactly which predictors led to this high churn risk. Having access to this information is extremely valuable as plans can be put in place to keep these high churn risk customers through driving down/up predictors leading to the risk in the first place. Without this data, companies are left completely blind to which customers are expected to stay and which will be planning to go elsewhere. Through successfully implementing strategies to drive retention, companies will be able to reduce the loss of revenue due to customer churn. Financial metrics are for the most part the main indication of success for a company, and customer retention is a main focus in keeping these metrics consistent and driving upward. From a customer perspective, any company with a focus on customer retention will generally be enhancing the overall customer experience to do so. Customer satisfaction will be expected to increase due to initiatives to target high churn risk customers, allowing for happy customers with long-term loyalty. In addition, the success of this project will show how valuable machine learning techniques can be in identifying customer churn, and how any field of business with customers can implement these methods and models for themselves.

## Conclusion
Our project and team have the potential to re-define how companies implement customer retention strategies. Each team member’s background is what our project is built around, being machine learning and LLM techniques, retention analysis in a healthcare domain, data exploration and modeling in MATLAB, computer engineering and more “low-level” languages like C++ for optimization, along with a mastery of several other data science techniques learned throughout our master’s program. We hope to bring real world solutions that can be realistically implemented into any company's workflow to effortlessly identify customers with high churn risk, along with what exactly is driving the risk, and even suggestions to drive retention.