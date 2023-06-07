# A tool to crawl for all available HTML, CSS, JAVASCRIPT, INTERNAL, EXTERNAL and IMAGES links.
# importing requests library to send HTTP requests
import requests
#importing BeautifulSoup class from bs4 library which helps us parse and navigate html documents
from bs4 import BeautifulSoup
# Importinge urlparse and urljoin functions from the urllib.parse module, which helps parse and manipulate URLs.
from urllib.parse import urlparse, urljoin

#defining a function to fetch html links for given url
def getHtmlLinks(url):
    # sends http get requests to specified url and stores the response in the response variable
    response = requests.get(url)
    if response.status_code == 200: # checks if the status code is 200 indicating a successfull request
        soup = BeautifulSoup(response.content, 'html.parser') # creates a object for Beautifulsoup class with soup
        # object  by passing the HTML content of the response to the constructor. The 'html.parser' argument specifies the parser to use.
        baseUrl = urlparse(url).scheme + '://' + urlparse(url).netloc # Parses the url to extract the
        # scheme (e.g., http, https) and the network location (e.g., www.example.com).
        # This base_url will be used to resolve relative URLs.
        cssLinks, jsLinks, internalLinks, externalLinks, imageLinks = [], [], [], [], [] # Initializes empty lists to store CSS links,
        # JavaScript links, internal links, external links, and image links.

        for link in soup.find_all('link', {'rel': 'stylesheet'}): # Iterates over all <link> tags with rel="stylesheet" in the HTML content.
            cssLinks.append(urljoin(baseUrl, link['href'])) # Extracts the href attribute of each CSS link,
            # resolves it using urljoin() to get an absolute URL, and appends it to the css_links list.

        for script in soup.find_all('script', {'src': True}): # Iterates over all <script> tags with a src attribute in the HTML content.
            jsLinks.append(urljoin(baseUrl, script['src'])) # Extracts the src attribute of each JavaScript link,
            # resolves it using urljoin() to get an absolute URL, and appends it to the js_links list.

        for anchor in soup.find_all('a', href=True): #Iterates over all <a> tags with an href attribute in the HTML content.
            href = anchor['href'] # Extracts the value of the href attribute of each anchor tag.
            if href.startswith('#'):
                continue # Skips the iteration if the href value starts with #, as it represents an internal page anchor.
            elif href.startswith('/'):
                internalLinks.append(urljoin(baseUrl, href)) # Resolves the relative URL using urljoin() with
                # the base_url and appends it to the internal_links list if it starts with "/".
            else:
                externalLinks.append(href) # Appends the href value to the external_links
                # list if it does not start with "/" (considered an external link).

        for img in soup.find_all('img', {'src': True}): #  Iterates over all <img> tags with a src attribute in the HTML content.
            imageLinks.append(urljoin(baseUrl, img['src'])) #  Extracts the src attribute of each image,
            # resolves it using urljoin() to get an absolute URL, and appends it to the image_links list.
        return {"Css Links": cssLinks,
                "Js Links" : jsLinks,
                "Internal Links": internalLinks,
                "External Links" : externalLinks,
                "Image Links" : imageLinks}

    print(f"Error {response.status_code} {response.reason}")

if __name__ == '__main__':
    url = input("Enter the url to crawl: ")
    links = getHtmlLinks(url)
    print("Css Links")
    print('\n'.join(links['Css Links']))
    print("\nJs Links")
    print('\n'.join(links['Js Links']))
    print("\nInternal Links")
    print('\n'.join(links['Internal Links']))
    print("\nExternal Links")
    print('\n'.join(links['External Links']))
    print("\nImage Links")
    print('\n'.join(links['Image Links']))




