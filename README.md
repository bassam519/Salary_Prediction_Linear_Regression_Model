# Salary Prediction using Linear Regression

## 📌 Project Overview
This project predicts the **salary of an employee** based on their **years of experience** using a **Linear Regression model**.  
It is a beginner-friendly machine learning project but presented in a professional way for portfolio purposes.  

The model learns the relationship between years of experience and salary from historical data and can be used to estimate salaries for new candidates.

---

## 📊 Dataset
- **Source:** [Salary Dataset (Kaggle)](https://www.kaggle.com/datasets/abhishek14398/salary-dataset-simple-linear-regression)
- **Features:**
  - `YearsExperience` → Number of years the person has worked.
  - `Salary` → The salary in USD.
- **Rows:** 30

---

## 🛠️ Technologies Used
- **Python**
- **Pandas** → Data handling
- **NumPy** → Numerical operations
- **Matplotlib & Seaborn** → Data visualization
- **Scikit-learn** → Machine learning model & evaluation

---

## 📈 Workflow
1. **Data Loading & Exploration**  
   - Load dataset using Pandas.
   - View data summary & check missing values.

2. **Data Visualization**  
   - Scatter plot of Years of Experience vs. Salary.
   - Regression line to visualize model fit.

3. **Data Preprocessing**  
   - Split data into training and testing sets.

4. **Model Training**  
   - Train a `LinearRegression` model from Scikit-learn.

5. **Model Evaluation**  
   - Metrics used:
     - **MAE (Mean Absolute Error)**
     - **MSE (Mean Squared Error)**
     - **RMSE (Root Mean Squared Error)**
     - **R² Score**

6. **Prediction**  
   - Predict salaries for test set.
   - Predict salaries for new given experience values.

---

## 📊 Results
- **Regression Equation:**  
  `Salary = m * YearsExperience + b`  
  Where:
  - `m` = model coefficient (slope)
  - `b` = intercept

- **Performance Metrics (example)**:
  - RMSE: `2450.38`
  - R² Score: `0.97` → Model explains 97% of variance.

---

## 📷 Visualizations
### Scatter Plot (Actual Data)
![scatter]([images/scatter_plot.png](https://github.com/bassam519/Salary_Prediction_Linear_Regression_Model/blob/main/sctter_plot.png))

### Predicted vs Actual
![prediction]([images/prediction_plot.png](https://github.com/bassam519/Salary_Prediction_Linear_Regression_Model/blob/main/prediction_plot.png))

---

## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/salary-prediction.git
   cd salary-prediction
