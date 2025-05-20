import requests
import sys
from bs4 import BeautifulSoup

def get_names_page(num):
    r = requests.get(f"https://www.behindthename.com/names/{num}")
    if (r.status_code != requests.codes.ok):
        sys.exit(-1)
    return r.text

if __name__ == "__main__":
    get_names_page(1)
