import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score


# Load data
salary = pd.read_csv('Salary_dataset.csv')

# Visualize the Relationship -> Experience vs Salary
plt.figure(1)
sns.scatterplot(x='YearsExperience',y='Salary',data=salary)
plt.title("Experience vs Salary")

# Prepare Data
X = salary[['YearsExperience']]
y = salary['Salary']
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

#Create a Model
salary_prediction_model = LinearRegression()

# Train a model
salary_prediction_model.fit(X_train,y_train)

# Predictions
predictions = salary_prediction_model.predict(X_test)

# Evaluate Model
mse = mean_squared_error(y_test,predictions)
rmse = np.sqrt(mse)
r2 = r2_score(y_test,predictions)

print('MSE:',mse)
print("RMSE:", rmse)
print("R² Score:", r2)

# Visualize Predictions
plt.figure(2)
plt.scatter(X_test,y_test,color='blue',label='Actual')
plt.plot(X_test, predictions, color='red', linewidth=2, label='Predicted')
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.legend()
plt.show()