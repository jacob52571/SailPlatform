import csv
import json
import xml.etree.ElementTree as ET

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
    tree = ET.parse(xml_out)
    root = tree.getroot()
    with open(json_in, "r") as f:
        data = json.load(f)
        for row in data.keys():
            # Creates a child node (new_node) under the root 
            # and sets the id and language attributes.
            new_node = ET.SubElement(root, 'movie')                 
            new_node.attrib['id'] = '5'
            new_node.attrib['language'] = 'English' 

            # Adds the new movie’s title, director, year, and rating 
            # as child nodes and sets their values.
            title_node = ET.SubElement(new_node, 'title')            

            title_node.text = 'The Good, the Bad and the Ugly'

            director_node = ET.SubElement(new_node, 'director')
            director_node.text = 'Sergio Leone'

            year_node = ET.SubElement(new_node, 'year')
            year_node.text = '1966'

            rating_node = ET.SubElement(new_node, 'rating')
            rating_node.text = '8.8'

            # Arranges the indentation for cleaner XML.
            ET.indent(root, space='    ')                           
            ET.tostring(root, encoding='utf-8')

            # Saves it as a file named 'output.xml'
            tree.write('output.xml')
    pass