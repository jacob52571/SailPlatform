import mysql.connector

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
        )
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
    cur = conn.cursor()
    insert_statement = f'''
        INSERT INTO {db}.{table} ()'''

if __name__ == "__main__":
    setup_sql_table('dbuser', 'dbroot', 'localhost', 'books', 'goodreads')