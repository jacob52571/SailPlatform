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
            id VARCHAR(255) NOT NULL PRIMARY KEY,
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
if __name__ == "__main__":
    setup_sql_table('dbuser', 'dbroot', 'localhost', 'books', 'goodreads')