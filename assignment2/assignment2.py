import csv
import traceback
import os
import custom_module
from datetime import datetime


# Task 2
# This function reads "../csv/employees.csv" and creates a dictionary.
# The dictionary has two keys:
#   "fields": the header row (list of column names)
#   "rows": the rest of the file (list of rows as lists)
# If any error occurs (like file not found), it prints details and exits.
def read_employees():
    try:
        employees_dict = {}
        list_of_employees = []

        with open("../csv/employees.csv", "r") as file:

            reader = csv.reader(file)
            header = next(reader)

            for emp in reader:
                list_of_employees.append(emp)

            employees_dict = {"fields": header, "rows": list_of_employees}
            return employees_dict

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(
                f"File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}"
            )
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")


employees = read_employees()
# print(employees)


# Task 3
# This function looks in the employees['fields'] dictionary to find the index of the column header.
def column_index(string):
    index = employees["fields"].index(string)
    return index


employee_id_column = column_index("employee_id")


# Task 4
# This function accepts a row number and returns the first name from that row.
def first_name(row_number):
    index = column_index("first_name")
    row = employees["rows"][row_number]
    first_name = row[index]

    # print(name)
    return first_name


# print(first_name(0))


# Task 5
# This function takes an employee_id (integer) and returns all rows matching that id.
# It defines an inner function (employee_match) that checks if a row's employee_id (converted to int) equals the given employee_id.
def employee_find(employee_id):

    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    matches = list(filter(employee_match, employees["rows"]))

    return matches


# print(employee_find(1))


# Task 6
# This function does the same as Task 5 but uses a lambda function to filter the rows.
def employee_find_2(employee_id):
    matches = list(
        filter(
            lambda x: int(x[employee_id_column]) == employee_id,
            employees["rows"],
        )
    )
    return matches


# employee_find_2(10)


# Task 7
# This function sorts the employees["rows"] list in place using the last_name.
# It uses the lambda to tell sort() which column (last_name) to sort by.
def sort_by_last_name():
    employees["rows"].sort(key=lambda x: x[column_index("last_name")])
    return employees["rows"]


# sort_by_last_name()


# Task 8
# This function converts a row (list) into a dictionary.
# The keys are the header names from employees["fields"] (skipping employee_id) and the values are the corresponding data.
def employee_dict(row_list):
    single_employee = {
        "first_name": row_list[1],
        "last_name": row_list[2],
        "phone": row_list[3],
    }

    return single_employee


# print(employee_dict(employees['rows'][0]))


# Task 9
# This function creates a dictionary where each key is an employee_id and each value is the employee's dictionary.
# It uses the employee_dict function for each row.
def all_employees_dict():

    all_employees = {}
    employee_id_column = column_index("employee_id")

    for row in employees["rows"]:
        all_employees[row[employee_id_column]] = employee_dict(row)

        # Can also use update method
        # single_employee = {row[employee_id_column]: employee_dict(row)}
        # all_employees.update(single_employee)

    return all_employees


# print(all_employees_dict())


# Task 10
# This function returns the value of the environment variable "THISVALUE".
# Environment variables can change the program's behavior without modifying the code.
def get_this_value():
    return os.getenv("THISVALUE")


# print(get_this_value())


# Task 11
# This function sets a new secret in our custom module.
# It calls custom_module.set_secret() with a new secret, which changes the value of custom_module.secret.
def set_that_secret(new_secret):
    return custom_module.set_secret(new_secret)


set_that_secret("batman")
# print(custom_module.secret)


# Task 12
# This function reads two CSV files.
# It returns two dictionaries (one for each file) with:
#   "fields": the header row
#   "rows": a list of tuples (each tuple is a row, making it hashable)
def read_minutes():
    minutes1_dict = {}
    minutes2_dict = {}

    try:
        # Reads the csv, loops through the list of lists, and changes each row from a list to a tuple.
        # Appends it to an empty list. Then creates a dict with "fields" and "rows".
        def read_and_append_list(filepath, mode):
            with open(filepath, mode) as file:
                list_of_people = []
                reader = csv.reader(file)
                header = next(reader)
                for row in reader:

                    list_of_people.append(tuple(row))

            minutes_dict = {"fields": header, "rows": list_of_people}

            return minutes_dict

        minutes1_dict = read_and_append_list("../csv/minutes1.csv", "r")
        minutes2_dict = read_and_append_list("../csv/minutes2.csv", "r")

        return minutes1_dict, minutes2_dict

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(
                f"File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}"
            )
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")


minutes1, minutes2 = read_minutes()
# print(minutes1)
# print("------------------------")
# print(minutes2)


# Task 13
# This function converts the "rows" from both minutes1 and minutes2 into sets,
# then performs a union to combine them into one set.
def create_minutes_set():
    rows1 = set(minutes1["rows"])
    rows2 = set(minutes2["rows"])
    new_set = rows1.union(rows2)
    return new_set


minutes_set = create_minutes_set()
# print(minutes_set)


# Task 14
# This function converts the minutes_set (which is a set that contains tuples with a date string)
# into a list of tuples where the date string is converted to a datetime object.
def create_minutes_list():

    new_list = list(
        map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), list(minutes_set))
    )
    # print(type(new_list[0]))

    return new_list


minutes_list = create_minutes_list()
# print("BEFORE SORTING", minutes_list)


# Task 15
# This function sorts minutes_list by date (ascending).
# It then converts each datetime object back to a string,
# writes the header (from minutes1) and sorted rows to "./minutes.csv",
# and returns the sorted, converted list.
def write_sorted_list():
    minutes_list.sort(key=lambda x: x[1])
    # print("AFTER SORTING", minutes_list)

    new_list = list(
        map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), minutes_list)
    )
    print(new_list)

    try:
        with open("./minutes.csv", "w") as file:
            writer = csv.writer(file)
            writer.writerow(minutes1["fields"])

            writer.writerows(new_list)

        return new_list
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(
                f"File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}"
            )
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")


write_sorted_list()
