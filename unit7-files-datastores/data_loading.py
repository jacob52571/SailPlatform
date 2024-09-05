import mysql.connector
import csv

def setup_sql_table(user, password, host, new_db, new_table):
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password
    )

    del_statement = f'DROP DATABASE IF EXISTS {new_db};'
    create_statement = f'CREATE DATABASE {new_db};'
    create_table = f'''
        CREATE TABLE {new_db}.{new_table} (
            id VARCHAR(255) PRIMARY KEY,
            title VARCHAR(1024),
            authors VARCHAR(1024),
            average_rating FLOAT(9, 2),
            isbn VARCHAR(255),
            isbn13 VARCHAR(255),
            language_code VARCHAR(255),
            num_pages INT,
            ratings_count INT,
            text_reviews_count INT,
            publication_date VARCHAR(255),
            publisher VARCHAR(255)
        );
    '''
    cur = conn.cursor()
    cur.execute(del_statement)
    cur.execute(create_statement)
    cur.execute(create_table)
    print(describe_table(conn, new_db, new_table))
    cur.close()
    conn.commit()


def load_to_sql(user, password, host, db, table, csv_in):
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password
    )
    with open(csv_in, newline='') as csv_file:
        csv_dict_reader = csv.DictReader(csv_file)
        for row in csv_dict_reader:
            cur = conn.cursor()
            insert_statement = f'''
                INSERT INTO {db}.{table}
                VALUES ({row["bookID"]}, {row["title"]}, {row["authors"]}, {row["average_rating"]}, {row["isbn"]}, {row["isbn13"]}, {row["language_code"]}, {row["num_pages"]}, {row["ratings_count"]}, {row["text_reviews_count"]}, {row["publication_date"]}, {row["publisher"]})'''
            cur.execute(insert_statement)
            cur.close()
            conn.commit()

def describe_table(connection, db_name: str, table_name: str):
    """
    Executes the DESCRIBE command on the specified table and prints the schema.

    Parameters:
    connection: MySQL connection object.
    table_name (str): The name of the table to describe.

    Returns:
    List of tuples containing the table schema.
    """
    try:
        cursor = connection.cursor()
        describe_query = f"DESCRIBE {db_name}.{table_name}"
        cursor.execute(describe_query)
        schema = cursor.fetchall()

        # Column headers for better readability
        headers = [i[0] for i in cursor.description]
        print(f"\nSchema of table '{table_name}':")
        print("-" * 60)
        print("{:<20} {:<20} {:<10} {:<10} {:<15} {:<10}".format(*headers))
        print("-" * 60)

        for column in schema:
            # Convert bytes to string if necessary
            #column = tuple(item.decode() if isinstance(item, bytes) else item for item in column)
            column = tuple("NULL" if value is None else value for value in column)
            print("{:<20} {:<20} {:<10} {:<10} {:<15} {:<10}".format(*column))

        return schema

    except Exception as e:
        print(f"Error describing table: {e}")
        return []

    finally:
        cursor.close()



if __name__ == "__main__":
    setup_sql_table('dbuser', 'dbroot', 'localhost', 'books', 'goodreads')