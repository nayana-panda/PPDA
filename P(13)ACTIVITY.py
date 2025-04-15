import pandas as pd

employee_details = pd.DataFrame({
    'Employee_ID': [101, 102, 103, 104, 105],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Department': ['HR', 'Finance', 'IT', 'Marketing', 'Sales'],
})
employee_salaries = pd.DataFrame({
    'Employee_ID': [101, 102, 103, 104, 105],
    'Salary': [50000, 70000, 80000, 55000, 60000]
})
sales_region_1 = pd.DataFrame({
    'Date': pd.date_range(start='2024-01-01', periods=5, freq='D'),
    'Region': ['North', 'North', 'North', 'North', 'North'],
    'Sales': [250, 300, 200, 400, 350]
})
sales_region_2 = pd.DataFrame({
    'Date': pd.date_range(start='2024-01-01', periods=5, freq='D'),
    'Region': ['South', 'South', 'South', 'South', 'South'],
    'Sales': [300, 320, 280, 360, 310]
})

grouped_sales_region_1 = sales_region_1.groupby('Region')['Sales'].median()
print("Median Sales for Region 1:")
print(grouped_sales_region_1)

merged_employees = pd.merge(employee_details, employee_salaries, on='Employee_ID', how='outer')
print("\nMerged Employee Details and Salaries (Outer Join):")
print(merged_employees)

employee_details.set_index('Employee_ID', inplace=True)
employee_salaries.set_index('Employee_ID', inplace=True)
joined_employees = employee_details.join(employee_salaries)
print("\nJoined Employee Details and Salaries:")
print(joined_employees)

concatenated_sales = pd.concat([sales_region_1, sales_region_2], axis=1)
print("\nConcatenated Sales Data (Horizontally):")
print(concatenated_sales)
