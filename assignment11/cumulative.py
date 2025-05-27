import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.data as pldata

with sqlite3.connect("../db/lesson.db") as conn:
    sql_statement = """SELECT o.order_id, SUM(price * quantity) AS total_price
    FROM orders o
    JOIN line_items l ON o.order_id = l.order_id
    JOIN products p ON l.product_id = p.product_id
    GROUP BY o.order_id
    ORDER BY o.order_id;"""

    df = pd.read_sql_query(sql_statement, conn)

    df["cumulative"] = df["total_price"].cumsum()
    print(df)


df.plot(
    x="order_id",
    y="cumulative",
    kind="line",
    xlabel="order_id",
    ylabel="cumulative revenue",
)
plt.show()


df = pldata.wind(return_type="pandas")

print(df.head(10))
print(df.tail(10))

# Clean the 'strength' column, remove non-digits and convert to float
df["strength"] = df["strength"].str.replace(r"\D+", "", regex=True).astype(float)
print(df)


# Create scatter plot
fig = px.scatter(
    df,
    x="strength",
    y="frequency",
    color="direction",
    title="Wind Strength vs Frequency by Direction",
    labels={"strength": "Strength (m/s)", "frequency": "Frequency (%)"},
)

fig.write_html("wind.html", auto_open=True)
