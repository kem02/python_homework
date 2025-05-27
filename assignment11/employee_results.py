import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

with sqlite3.connect("../db/lesson.db") as conn:
    sql_statement = """SELECT last_name, SUM(price * quantity) AS revenue FROM employees e 
    JOIN orders o ON e.employee_id = o.employee_id 
    JOIN line_items l ON o.order_id = l.order_id 
    JOIN products p ON l.product_id = p.product_id 
    GROUP BY e.employee_id;"""

    employee_results = pd.read_sql_query(sql_statement, conn)
    print(employee_results)


employee_results.plot(
    x="last_name",
    y="revenue",
    kind="bar",
    color="skyblue",
    title="Revenue by Employee",
    xlabel="Employee Last Name",
    ylabel="Revenue",
)
plt.show()
