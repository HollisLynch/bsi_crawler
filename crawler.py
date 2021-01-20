import urllib.request
from bs4 import BeautifulSoup
import threading

def find_links():
    hobbies = ["rashomon", "hokey", "kurosawa", "david+lynch", "twin+peaks"]

    for i in hobbies:
        query = i + " article"
        query = query.replace(' ', '+')

        url = f"https://google.com/search?q={query}"

        # Perform the request
        request = urllib.request.Request(url)

        # Set a normal User Agent header, otherwise Google will block the request.
        request.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')
        raw_response = urllib.request.urlopen(request).read()

        # Read the repsonse as a utf-8 string
        html = raw_response.decode("utf-8")
        soup = BeautifulSoup(html, 'html.parser')

        # Find all the search result divs
        divs = soup.find_all('a')
        for div in divs:
            # Search for a h3 tag
            results = div.select("h3")

            if (len(results) >= 1):
                h3 = results[0]
                print(h3.get_text())
                print(div.get('href'))

if __name__ == "__main__":
    t = threading.Thread(target=find_links)
    t.start()
    t.join()
