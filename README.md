# Stroke Prediction ML Project

## Overview

This machine learning project is designed to predict the likelihood of an individual experiencing a stroke based on several health and demographic attributes. The dataset used in this project contains the following features:

- `gender`: Gender of the individual (Male, Female, Other)
- `age`: Age of the individual in years
- `hypertension`: 0 if the individual doesn't have hypertension, 1 if the individual has hypertension
- `heart_disease`: 0 if the individual doesn't have any heart disease, 1 if the individual has a heart disease
- `ever_married`: "Yes" if the individual is married, "No" otherwise
- `work_type`: Type of work the individual is engaged in (Private, Self-employed, Govt_job, Children, Never_worked)
- `Residence_type`: Type of residence (Urban, Rural)
- `avg_glucose_level`: Average glucose level in the individual's blood
- `bmi`: Body Mass Index (BMI) of the individual
- `smoking_status`: Smoking status of the individual (formerly smoked, never smoked, smokes, unknown)
- `stroke`: Target variable - 1 if the individual had a stroke, 0 otherwise

## Importance

Predicting strokes accurately can be crucial in proactive healthcare. Identifying individuals at higher risk of strokes based on their health profile could lead to early interventions, lifestyle modifications, and targeted medical treatments, potentially reducing the incidence and severity of strokes and their associated complications.

This project aims to contribute to the field of healthcare by leveraging machine learning techniques to create predictive models that can assist in stroke risk assessment and preventive care strategies.

## Data Source

The dataset used in this project was obtained from <https://www.kaggle.com/>.

## Files

- `stroke_data.csv`: The dataset in CSV format containing the aforementioned attributes.

## Methodology

1. **Data Preprocessing**: The dataset undergoes preprocessing steps such as handling missing values, encoding categorical variables, and scaling numerical features.
2. **Exploratory Data Analysis (EDA)**: Statistical analysis and visualization techniques are applied to gain insights into the distribution and relationships between variables.
3. **Feature Engineering**: Creation of new features and transformation of existing ones to enhance the predictive power of the model.
4. **Model Building**: Utilization of various machine learning algorithms (e.g., Logistic Regression, Random Forest, XGBoost) to build predictive models.
5. **Model Evaluation**: Assessing model performance using relevant metrics like accuracy, precision, recall, and F1-score.
6. **Hyperparameter Tuning**: Optimizing model parameters to improve predictive accuracy.
7. **Deployment**: To be updated after deployment

## Usage

- Clone the repository: `git clone [repository URL]`
- Install the necessary libraries: `pip install -r requirements.txt`
- Run the Jupyter Notebook or Python script to execute the project.

## Requirements

The project requires the following libraries:

- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost

## License

This project is licensed under the MIT License.
