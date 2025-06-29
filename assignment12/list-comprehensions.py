import pandas as pd

df = pd.read_csv("../csv/employees.csv")

# for i, row in df.iterrows():
#     print(f"{row.first_name} {row.last_name}")


full_name = [f"{row.first_name} {row.last_name}" for i, row in df.iterrows()]
print(full_name)


names_contain_e = [x for x in full_name if "e" in x]
print(names_contain_e)
