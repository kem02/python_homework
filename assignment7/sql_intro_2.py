import pandas as pd
import sqlite3

with sqlite3.connect("../db/lesson.db") as conn:
    sql_statement = """SELECT line_items.line_item_id, line_items.quantity, products.product_id, products.product_name, products.price
    FROM line_items JOIN products ON line_items.product_id = products.product_id;"""
    df = pd.read_sql_query(sql_statement, conn)
    print(df.head(5))

    df["total"] = df["quantity"] * df["price"]

    print(df.head(5))

    grouped_df = (
        df.groupby("product_id")
        .agg({"line_item_id": "count", "total": "sum", "product_name": "first"})
        .reset_index()
    )
    print(grouped_df.head(5))

    sorted_df = grouped_df.sort_values(by="product_name")
    print(sorted_df.head(5))

    sorted_df.to_csv("./order_summary.csv", index=False)
