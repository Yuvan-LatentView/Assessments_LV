# -*- coding: utf-8 -*-
"""IA2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1enYGOOXYGnMKCj3LfiAnE1BhhB4tkvgT
"""

#1

import numpy as np
import pandas as pd

arr = np.array([1,2,3,4,5])
print(arr.min())
print(arr.max())
print(arr.sum())
print(arr.mean())
print(arr.std())

#2

health_data = np.array([[160, 70, 30],   # height, weight, age for individual 1
                        [165, 65, 35],   # height, weight, age for individual 2
                        [170, 75, 40]])  # height, weight, age for individual 3

def normalise(data):
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)
    normalized_data = (data - mean) / std
    return normalized_data

normalized_data = normalise(health_data)
print(normalized_data)

#3

scores = np.array([[30, 70, 80, 75, 90],
                    [40, 70, 80, 100, -1],
                     [25, 100, -1, 95, 68]])
averages = []
for marks in scores:
  exempt = marks[2:]
  average = np.mean(exempt[exempt != -1])
  averages.append(average)
print("Average marks of students in last three subjects: ", averages)

#4

readings = np.linspace(15, 25, 24)
print(readings)

#5

daily_closing_prices = np.array([100, 102, 98, 105, 107, 110, 108, 112, 115, 118, 120])
window_size = 5

df = pd.DataFrame(daily_closing_prices)
df['Moving avg'] = df.rolling(window=window_size).mean()
print(df)

#6

arr = np.arange(4).reshape(2, 2)
print(arr)
mean_v = [0,0]
cov = [[1, 0.5], [0.5, 2]]

#7

properties_matrix = np.array([[1, 2, 3],
                              [4, 5, 6],
                              [7, 8, 9]])

ans = np.linalg.det(properties_matrix)
print(ans)

#8

q8 = np.array([[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]])
boolean = q8 > 5
print(q8[boolean])

#9

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
        'Age': [25, 30, 35, 40, 45, 50, 55],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Miami', 'Boston'],
        'Department': ['HR', 'IT', 'Finance', 'Marketing', 'Sales', 'IT', 'HR']}

df = pd.DataFrame(data)
df = df[(df['Age'] < 45) & (df['Department'] != 'HR')]
df = df[['Name', 'City']]
print(df)

#10

data = {'Department': ['Electronics', 'Electronics', 'Clothing', 'Clothing', 'Home Goods'],
        'Salesperson': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Sales': [70000, 50000, 30000, 40000, 60000]}

df = pd.DataFrame(data)
avg_sp = df.groupby(['Department', 'Salesperson'])['Sales'].mean().reset_index()
print(avg_sp,"\n")
avg_dept = avg_sp.groupby('Department')['Sales'].mean().reset_index()
ranked_depts = avg_dept.sort_values(by='Sales', ascending=False)
print(ranked_depts)

#11

data = {
    'Product': ['Apples', 'Bananas', 'Cherries', 'Dates', 'Elderberries', 'Flour', 'Grapes'],
    'Category': ['Fruit', 'Fruit', 'Fruit', 'Fruit', 'Fruit', 'Bakery', 'Fruit'],
    'Price': [1.20, 0.50, 3.00, 2.50, 4.00, 1.50, 2.00],
    'Promotion': [True, False, True, True, False, True, False]
}
df = pd.DataFrame(data)
ans = df[(df['Category'] == 'Fruit') & (df['Promotion'] == False) & (df['Price'] > df[df['Category'] == 'Fruit']['Price'].mean())]

print(ans)

#12

employee_data = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'David'],
    'Department': ['HR', 'IT', 'Finance', 'IT'],
    'Manager': ['John', 'Rachel', 'Emily', 'Rachel']
}

# Dataset of employee project assignments
project_data = {
    'Employee': ['Alice', 'Charlie', 'Eve'],
    'Project': ['P1', 'P3', 'P2']
}

p_data = pd.DataFrame(project_data)
e_data = pd.DataFrame(employee_data)
ans = e_data.merge(p_data, on='Employee' ,how='outer')
ans.fillna('Unassigned', inplace=True)
ans = ans[(ans['Department'] != 'Unassigned') & (ans['Manager'] != 'Unassigned')]
print(ans)

#13

def performance(val):
  if val < 50:
    return "Poor performer"
  elif val < 80:
    return "Average Performer"
  else:
    return "Good Performer"

df = pd.read_csv('/content/Q13_sports_team_stats.csv')
df['Win Ratio'] = (df['Wins']/df['GamesPlayed']) * 100
df['Performance Metrics'] = df['Win Ratio'].apply(performance)
print(df)

#14

df = pd.read_csv('/content/Q14_customer_purchases.csv')
bef_join = df['PurchaseAmount'][df['LoyaltyProgramSignUp'] > df['Date']].mean()
bef_join
aft_join = df['PurchaseAmount'][df['LoyaltyProgramSignUp'] < df['Date']].mean()
aft_join
print(bef_join, aft_join)

#15

def feedback(val):
  if val < 85:
    return "More Practice needed"
  else:
    return "Good overall average"
df = pd.read_csv('/content/Q15_student_grades.csv')
ans_mean = df.groupby('Subject')['Grade'].mean().reset_index()
ans_std = df.groupby('Subject')['Grade'].std().reset_index()
ans_var = df.groupby('Subject')['Grade'].var().reset_index()
ans_mean['Inputs'] = ans_mean['Grade'].apply(feedback)
print(ans_mean,"\n")
print(ans_std)
print(ans_var)