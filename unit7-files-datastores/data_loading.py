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
    cur.close()
    conn.commit()
"""

def setup_sql_table(user, password, host, new_db, new_table):
    connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        #database=new_db,
        charset='latin1',
        use_unicode=False
    )

    with connection.cursor() as cur:
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
        cur.execute(del_statement)
        cur.execute(create_statement)
        cur.execute(create_table)
"""
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
            # Properly escape and insert data using parameterized queries
            insert_statement = f'''
                INSERT INTO {db}.{table}
                (id, title, authors, average_rating, isbn, isbn13, language_code, num_pages, ratings_count, text_reviews_count, publication_date, publisher)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            '''

            # Escape commas in the title and use parameterized query to avoid issues
            t = row["title"].replace(",", r'\,')

            # Define the values to insert (make sure string values are passed as strings)
            values = (
                row["bookID"],
                t,  # Escaped title
                row["authors"],
                row["average_rating"],
                row["isbn"],
                row["isbn13"],
                row["language_code"],
                row["num_pages"],
                row["ratings_count"],
                row["text_reviews_count"],
                row["publication_date"],
                row["publisher"]
            )

            # Execute the query with the parameterized values
            cur.execute(insert_statement, values)

            # Commit the transaction
            conn.commit()
