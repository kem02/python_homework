import sqlite3


def add_publisher(cursor, publisher_name):
    try:
        cursor.execute(
            "INSERT INTO publishers (publisher_name) VALUES (?)", (publisher_name,)
        )
    except sqlite3.IntegrityError:
        print(f"{publisher_name} is already in the database.")


def add_magazine(cursor, publisher_name, magazine_name):
    cursor.execute(
        "SELECT * FROM publishers WHERE publisher_name = ?", (publisher_name,)
    )
    result = cursor.fetchall()
    print(result)
    if len(result) > 0:
        publisher_id = result[0][0]
    else:
        print(f"There is no publisher by the name of {publisher_name}")
        return

    try:
        cursor.execute(
            "INSERT INTO magazines (publisher_id, magazine_name) VALUES (?, ?)",
            (publisher_id, magazine_name),
        )
    except sqlite3.IntegrityError:
        print(f"{magazine_name} is already in the database")


def add_subscribers(cursor, subscriber_name, subscriber_address):
    # you might have several subscribers with the same name --
    # but when creating a subscriber you should check that you
    # don't already have an entry where BOTH the name and the address are the same
    # as for the one you are trying to create.

    cursor.execute(
        "SELECT * FROM subscribers WHERE subscriber_name= ? AND subscriber_address = ?",
        (subscriber_name, subscriber_address),
    )
    result = cursor.fetchall()
    print(result)

    if len(result) > 0:
        print(
            f"The subscriber {subscriber_name} with address {subscriber_address} already exists."
        )
        return

    cursor.execute(
        "INSERT INTO subscribers (subscriber_name, subscriber_address) VALUES (?,?)",
        (subscriber_name, subscriber_address),
    )

    # if (
    #     subscriber_name == existing_subscriber_name
    #     and subscriber_address == existing_subscriber_address
    # ):
    #     print(
    #         f"The subscriber {subscriber_name} with address {subscriber_address} already exists."
    #     )
    #     return
    # else:
    #     cursor.execute(
    #         "INSERT INTO subscribers (subscriber_name, subscriber_address) VALUES (?,?)",
    #         (subscriber_name, subscriber_address),
    #     )


def add_subscription(
    cursor, subscriber_name, subscriber_address, magazine_name, expiration_date
):
    cursor.execute(
        "SELECT * FROM subscribers WHERE subscriber_name= ? AND subscriber_address = ?",
        (subscriber_name, subscriber_address),
    )
    result = cursor.fetchall()
    print(result)

    if len(result) > 0:
        subscriber_id = result[0][0]
    else:
        print(
            f"There is no subscriber by the name of {subscriber_name} and address of {subscriber_address}"
        )
        return

    cursor.execute("SELECT * FROM magazines WHERE magazine_name = ?", (magazine_name,))
    result = cursor.fetchall()
    print(result)
    if len(result) > 0:
        magazine_id = result[0][0]
    else:
        print(f"There is no magazine by the name of {magazine_name}")
        return

    cursor.execute(
        "SELECT * FROM subscriptions WHERE subscriber_id = ? AND magazine_id = ?",
        (subscriber_id, magazine_id),
    )
    result = cursor.fetchall()
    print(result)
    if len(result) > 0:
        print(
            f"Subscription already exist with Subscriber: {subscriber_name} and Magazine: {magazine_name}"
        )
        return

    cursor.execute(
        "INSERT INTO subscriptions (expiration_date, subscriber_id, magazine_id) VALUES (?,?,?)",
        (expiration_date, subscriber_id, magazine_id),
    )


with sqlite3.connect("../db/magazines.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS publishers(
    publisher_id INTEGER PRIMARY KEY,
    publisher_name TEXT NOT NULL UNIQUE
    )"""
    )

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS magazines(
    magazine_id INTEGER PRIMARY KEY,
    magazine_name TEXT NOT NULL UNIQUE,
    publisher_id INTEGER,
    FOREIGN KEY (publisher_id) REFERENCES publishers(publisher_id)

    )
    """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS subscribers(
        subscriber_id INTEGER PRIMARY KEY,
        subscriber_name TEXT NOT NULL,
        subscriber_address TEXT NOT NULL

        )
    """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS subscriptions(
        subscription_id INTEGER PRIMARY KEY,
        expiration_date TEXT NOT NULL,  
        magazine_id INTEGER,
        subscriber_id INTEGER,
        FOREIGN KEY (magazine_id) REFERENCES magazines (magazine_id),
        FOREIGN KEY (subscriber_id) REFERENCES subscribers (subscriber_id)

        )
    """
    )

    add_publisher(cursor, "Condé Nast")
    add_publisher(cursor, "Hearst Communications")
    add_publisher(cursor, "Meredith Corporation")
    add_publisher(cursor, "Future plc")

    add_magazine(cursor, "Condé Nast", "Vogue")
    add_magazine(cursor, "Hearst Communications", "Cosmopolitan")
    add_magazine(cursor, "Meredith Corporation", "Better Homes & Gardens")
    add_magazine(cursor, "Hearst Communications", "Popular Mechanics")
    add_magazine(cursor, "Meredith Corporation", "People")
    add_magazine(cursor, "Future plc", "TechRadar")

    add_subscribers(cursor, "Alice Johnson", "123 Maple St")
    add_subscribers(cursor, "Bob Smith", "456 Oak Ave")
    add_subscribers(cursor, "Charlie Davis", "789 Pine Rd")

    add_subscription(cursor, "Alice Johnson", "123 Maple St", "Vogue", "2025-12-31")
    add_subscription(cursor, "Bob Smith", "456 Oak Ave", "Cosmopolitan", "2025-10-15")
    add_subscription(
        cursor, "Charlie Davis", "789 Pine Rd", "Better Homes & Gardens", "2026-01-01"
    )

    # Task 4
    cursor.execute("SELECT * FROM subscribers")
    result = cursor.fetchall()
    print(result)

    cursor.execute("SELECT * FROM magazines GROUP BY magazine_name")
    result = cursor.fetchall()
    print(result)

    cursor.execute(
        "SELECT * FROM publishers JOIN magazines ON publishers.publisher_id = magazines.publisher_id WHERE publishers.publisher_name = 'Hearst Communications'"
    )
    result = cursor.fetchall()
    print(result)

    conn.commit()
