import csv
import json
import xml.etree.ElementTree as ET
import mysql.connector

def retrieve_popular_books(csv_in, json_out):
    out_dict = {}
    with open(csv_in, newline='') as csv_file:
        csv_dict_reader = csv.DictReader(csv_file)

        for row in csv_dict_reader:
            if float(row["average_rating"]) > 4.5 and int(row["num_pages"]) > 50 and int(row["ratings_count"]) > 1000: 
                out_dict[row["bookID"]] = {"info": {"title": row["title"],
                                                    "authors": row["authors"],
                                                    "isbn": row["isbn"],
                                                    "isbn13": row["isbn13"],
                                                    "language_code": row["language_code"],
                                                    "num_pages": int(row["num_pages"]),
                                                    "publication_date": row["publication_date"],
                                                    "publisher": row["publisher"]},
                                           "rating": {"average_rating": float(row["average_rating"]),
                                                      "ratings_count": int(row["ratings_count"]),
                                                      "text_reviews_count": int(row["text_reviews_count"])}}
    data = json.dumps(out_dict, indent=4, sort_keys=True)
    with open(json_out, "w") as f:
        f.write(data)

def retrieve_boring_books(json_in, xml_out):
    xml_file = open(xml_out, "w")
    xml_file.write("<books>\n</books>")
    xml_file.close()
    tree = ET.parse(xml_out)
    root = tree.getroot()
    with open(json_in, "r") as f:
        data = json.load(f)
        for row in data:
            if float(row["average_rating"]) < 3.0 and int(row["num_pages"]) > 300 and int(row["ratings_count"]) > 100:
                # Creates a child node (new_node) under the root 
                # and sets the id and language attributes.
                info_node = ET.SubElement(root, 'book')                 
                info_node.attrib['id'] = row["bookID"]

                new_node = ET.SubElement(info_node, "info")

                # Adds the new movie’s title, director, year, and rating 
                # as child nodes and sets their values.
                title_node = ET.SubElement(new_node, 'title')            

                title_node.text = row["title"]

                authors_node = ET.SubElement(new_node, 'authors')
                authors_node.text = row["authors"]

                isbn_node = ET.SubElement(new_node, 'isbn')
                isbn_node.text = row["isbn"]

                isbn13_node = ET.SubElement(new_node, 'isbn13')
                isbn13_node.text = row["isbn13"]

                language_code_node = ET.SubElement(new_node, 'language_code')
                language_code_node.text = row["language_code"]

                num_pages_node = ET.SubElement(new_node, "num_pages")
                num_pages_node.text = row["num_pages"]

                publication_date_node = ET.SubElement(new_node, "publication_date")
                publication_date_node.text = row["publication_date"]

                publisher_node = ET.SubElement(new_node, "publisher")
                publisher_node.text = row["publisher"]

                rating_node = ET.SubElement(info_node, "rating")

                avg_rating_node = ET.SubElement(rating_node, "average_rating")
                avg_rating_node.text = row["average_rating"]

                ratings_count_node = ET.SubElement(rating_node, "ratings_count")
                ratings_count_node.text = row["ratings_count"]

                text_review_count_node = ET.SubElement(rating_node, "text_reviews_count")
                text_review_count_node.text = row["text_reviews_count"]

            # Arranges the indentation for cleaner XML.
            ET.indent(root, space='    ')                           
            ET.tostring(root, encoding='utf-8')

            # Saves it as a file named 'output.xml'
    tree.write(xml_out)

def retrieve_wildly_popular_books(xml_in, csv_out):
    # avg rating > 4.0, ratings count > 1,000,000
    tree = ET.parse(xml_in)
    books = tree.getroot()

    with open(csv_out, "a", newline="") as f:
        f.write("book_id,title,authors,average_rating,isbn,isbn13,language_code,num_pages,ratings_count,text_reviews_count,publication_date,publisher\n")
        writer = csv.writer(f,
                            delimiter=",",
                            quotechar='"',
                            quoting=csv.QUOTE_MINIMAL)
        for book in books.findall('book'):
            avg_rating = float(book.find("average_rating").text)
            rating_count = int(book.find("ratings_count").text)
            if avg_rating > 4.0 and rating_count > 1000000:
                book_id = book.find("bookID").text
                title = book.find("title").text
                authors = book.find("authors").text
                #average_rating above
                isbn = book.find("isbn").text
                isbn13 = book.find("isbn13").text
                language_code = book.find("language_code").text
                num_pages = book.find("num_pages").text
                #rating_count above
                text_reviews = book.find("text_reviews_count").text
                publication_date = book.find("publication_date").text
                publisher = book.find("publisher").text
                writer.writerow(
                    [book_id, title, authors, avg_rating, isbn, isbn13, language_code, num_pages, rating_count, text_reviews, publication_date, publisher]
                )

def retrieve_long_books(user, password, host, db, table, csv_out):
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password
    )
    cur = conn.cursor()
    select_query = f"SELECT * FROM {db}.{table}"
    cur.execute(select_query)
    rows = cur.fetchall()
    with open(csv_out, "a", newline="") as f:
        f.write("book_id,title,authors,average_rating,isbn,isbn13,language_code,num_pages,ratings_count,text_reviews_count,publication_date,publisher\n")
        writer = csv.writer(f,
                            delimiter=",",
                            quotechar='"',
                            quoting=csv.QUOTE_MINIMAL)
        for row in rows:
            if (row[7] > 2000):
                writer.writerow(
                    [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11]]
                )
    cur.close()
    conn.close()
