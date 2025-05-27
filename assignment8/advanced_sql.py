import sqlite3

with sqlite3.connect("../db/lesson.db") as conn:
    try:

        conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor()

        # Task 1
        cursor.execute(
            """
            SELECT orders.order_id, line_items.line_item_id, products.product_name FROM orders JOIN line_items ON orders.order_id = line_items.order_id 
            JOIN products ON products.product_id = line_items.product_id 
            WHERE orders.order_id IN (SELECT order_id FROM orders 
            ORDER BY order_id 
            LIMIT 5)
            """
        )
        result = cursor.fetchall()

        # for row in result:
        # print(row)

        # Task 2
        cursor.execute(
            """
            select o.order_id, SUM(p.price * li.quantity) AS total_price FROM orders o JOIN line_items li ON o.order_id = li.order_id 
            JOIN products p ON p.product_id = li.product_id GROUP BY o.order_id ORDER BY o.order_id LIMIT 5
            """
        )

        result = cursor.fetchall()

        # for row in result:
        #     print(row)

        # Task 3
        cursor.execute(
            "SELECT customer_id FROM customers where customer_name = 'Perez and Sons'"
        )
        result = cursor.fetchone()
        customer_id = result[0]
        print(customer_id)

        cursor.execute(
            "SELECT employee_id FROM employees where first_name = 'Miranda' AND last_name = 'Harris'"
        )
        result = cursor.fetchone()
        employee_id = result[0]
        print(employee_id)

        cursor.execute("SELECT product_id FROM products ORDER BY price LIMIT 5")
        products = cursor.fetchall()
        print(products)

        try:
            # Creating order record
            cursor.execute(
                "INSERT INTO orders (customer_id, employee_id) VALUES (?,?) RETURNING order_id",
                (customer_id, employee_id),
            )
            result = cursor.fetchone()
            order_id = result[0]
            print(order_id)

            # Creating line_item record
            for product in products:
                product_id = product[0]
                cursor.execute(
                    "INSERT INTO line_items (order_id, product_id, quantity) VALUES (?, ?, 10) RETURNING line_item_id",
                    (order_id, product_id),
                )
                result = cursor.fetchone()
                print(result)

        except Exception as e:
            conn.rollback()
            print("Error:", e)

        # Print out the Order row
        cursor.execute(
            """
            SELECT o.order_id, li.line_item_id, li.quantity, p.product_name
             FROM products p
             JOIN line_items li ON li.product_id = p.product_id
             JOIN orders o ON o.order_id = li.order_id
             WHERE o.order_id = ?;
            """,
            (order_id,),
        )

        result = cursor.fetchall()
        print(result)

        # Task 4
        cursor.execute(
            """
            SELECT e.first_name, e.last_name, COUNT(o.order_id) AS order_count
            FROM employees e
            JOIN orders o ON e.employee_id = o.employee_id
            GROUP BY e.employee_id, e.first_name, e.last_name
            HAVING order_count > 5;
            """
        )

        result = cursor.fetchall()
        print(result)

        conn.commit()

    except Exception as e:
        print("SQL Error: ", e)
