# -*- coding: utf-8 -*-
"""LVADSUSR201_Yuvan Barathi_Anomaly.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Fuf-M3vWWLwxmT_Kpu4LhA0jujys0QD-
"""

import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, LabelEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import IsolationForest

df = pd.read_csv('/content/anomaly_train.csv')
df

df.isnull().sum()

df.duplicated().sum()

# Identify numerical columns by data type
numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns

# Create a box plot for each numerical column
for column in numerical_columns:
    plt.figure(figsize=(10, 6))  # Set the figure size for better readability
    sns.boxplot(x=df[column])
    plt.title(f'Box Plot of {column}')
    plt.xlabel(column)
    plt.show()

# Plot the correlation matrix as a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(numeric_only=True), annot=True, fmt=".2f", cmap='coolwarm')
plt.title('Heatmap of Correlation Matrix')
plt.show()

df.columns

df.dtypes

model_outlier = IsolationForest(contamination=0.1, random_state=42)
outliers = model_outlier.fit_predict(df.drop(columns = ['TransactionID', 'Amount', 'Time', 'Type', 'Location']))
df['is_an_outlier'] = outliers

features = ['Amount', 'Time']
X = df[features]
y = df['is_an_outlier']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = IsolationForest(n_estimators=100, contamination=0.1, max_samples=10000, random_state=42)
model.fit(X_train)

# Predict the anomalies in the data
y_pred = model.predict(X_train)
df["anomaly_score"] = model.decision_function(X)

anomalies = df.loc[df["anomaly_score"] < 0]

plt.scatter(df["Amount"], df["anomaly_score"], label="Not an Anomaly")
plt.scatter(anomalies["Amount"], anomalies["anomaly_score"], color="r", label="Anomaly")
plt.xlabel("Amount")
plt.ylabel("Anomaly Score")
plt.title("Scatter plot for Amount and Anomaly Score")
plt.legend(loc='lower right')
plt.show()