# Task 1
import pandas as pd

# Create a dictionary with names, ages, and cities
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"],
}

# Convert the dictionary into a DataFrame and save it as task1_data_frame
task1_data_frame = pd.DataFrame(data)
# print(task1_data_frame)


# Make a copy of the DataFrame and add a new column 'Salary' with values
task1_with_salary = task1_data_frame.copy()
task1_with_salary["Salary"] = [70000, 80000, 90000]
# print(task1_with_salary)

# Make another copy to modify the existing Age column by adding 1 to each person's age count.
task1_older = task1_with_salary.copy()
task1_older["Age"] = task1_older["Age"].add(1)
# Can also use the + operator:
# task1_older["Age"] = task1_older["Age"] + 1
# print(task1_older)


# Save the updated DataFrame to a CSV file named 'employees.csv' without saving the row index
task1_older.to_csv("employees.csv", index=False)


# Task 2
# Load the CSV file created in Task 1 into a new DataFrame
task2_employees = pd.read_csv("employees.csv")
# print(task2_employees)

# Create a new DataFrame with additional employee data
more_employees_data = pd.DataFrame(
    {
        "Name": ["Eve", "Frank"],
        "Age": [28, 40],
        "City": ["Miami", "Seattle"],
        "Salary": [60000, 95000],
    }
)

# Save this new data as a JSON file
more_employees_data.to_json("additional_employees.json")

# Load the JSON file into a DataFrame and print
json_employees = pd.read_json("additional_employees.json")
# print(json_employees)

# Combine the CSV and JSON DataFrames into one and print the combined DataFrame
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
# print(more_employees)


# Task 3
# Get the first three rows of the combined DataFrame and print them
first_three = more_employees.head(3)
# print(first_three)

# Get the last two rows of the combined DataFrame and print them
last_two = more_employees.tail(2)
# print(last_two)

# Get the shape (number of rows and columns) of the combined DataFrame and print it
employee_shape = more_employees.shape
# print(employee_shape)

# Print a concise summary of the DataFrame to see data types and non-null counts
# print(more_employees.info())


# Task 4
# Load the dirty data from a CSV file into a DataFrame
dirty_data = pd.read_csv("dirty_data.csv")
# print(dirty_data)

# Create a copy of the dirty data to work on cleaning it
clean_data = dirty_data.copy()

# Remove any duplicate rows from the DataFrame
clean_data = clean_data.drop_duplicates()
# print(clean_data)

# Convert the Age and Salary column to numeric values, turning non-numeric values (unknown,n/a) into NaN
clean_data["Age"] = pd.to_numeric(clean_data["Age"], errors="coerce")
# print(clean_data)
clean_data["Salary"] = pd.to_numeric(clean_data["Salary"], errors="coerce")
# print(clean_data)

# Calculate the mean of Age and the median of Salary
mean_age = clean_data["Age"].mean()
median_salary = clean_data["Salary"].median()
# Fill in missing Age values with the mean and missing Salary values with the median
clean_data["Age"] = clean_data["Age"].fillna(mean_age)
clean_data["Salary"] = clean_data["Salary"].fillna(median_salary)
# print(clean_data)

# Convert the Hire Date column to datetime format
clean_data["Hire Date"] = pd.to_datetime(
    clean_data["Hire Date"], errors="coerce", format="mixed"
)
# print(clean_data)

# Remove extra spaces from the Name and Department columns and turn them to uppercase
clean_data["Name"] = clean_data["Name"].str.strip()
clean_data["Department"] = clean_data["Name"].str.strip()
clean_data["Name"] = clean_data["Name"].str.upper()
clean_data["Department"] = clean_data["Name"].str.upper()
# print(clean_data)
