# Importing the requests library, which allows us to send HTTP requests.
import requests
# Importing the re module, which provides support for regular expressions.
import re
# Importing the BeautifulSoup class from the bs4 module, which is used for parsing and navigating HTML documents.
from bs4 import BeautifulSoup
#Importing the urljoin and urlparse functions from the urllib.parse module, which help parse and manipulate URLs.
from urllib.parse import urljoin, urlparse
#Importing the datetime class and timedelta class from the
# datetime module, which are used for working with dates and times.
from datetime import datetime, timedelta
import json

def fetchUrl(url):
    # Function to fetch the content of a URL
    try:
        response = requests.get(url, timeout=5)#This line sends an HTTP GET request to the specified url using the requests.get function.
        # The timeout=5 parameter sets a timeout of 5 seconds for the request.
        response.raise_for_status() #This line checks the response status code and raises an exception if it
        # indicates an error (e.g., 4xx or 5xx status codes). It ensures that we handle any errors
        # during the request.
        return response.text #If the request is successful, this line returns the response content as a string.
        # It represents the HTML or text content of the web page.
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from the URl {e}") #If an exception is raised during the try block,
        # this except block catches the exception and assigns it to the variable e and prints the Error.
        return None #This line returns None to indicate that an error occurred during the request.


def extractLinksFromHtml(htmlContent, baseUrl):
    # Function to extract links from HTML content
    soup = BeautifulSoup(htmlContent, 'html.parser')
    #This line creates a BeautifulSoup object called soup by parsing the html_content using
    # the 'html.parser' parser. This object allows us to navigate and search the HTML structure easily.
    links = []
    #This line initializes an empty list called links to store the extracted links.
    for link in soup.find_all('a', href=True):
        # This line iterates over all <a> tags (anchor tags) in the HTML content that have an href attribute.
        # It uses the find_all method of the soup object to find all matching elements
        href = link['href']
        #This line extracts the value of the href attribute from each <a> tag and assigns it to the href variable.
        absoluteUrl = urljoin(baseUrl, href)
        # This line resolves the relative URL (href) to an absolute URL by using the urljoin function from the
        # urllib.parse module. It combines the base_url and href to create an absolute URL, handling any relative
        # path appropriately.
        links.append(absoluteUrl)
        #This line appends the absolute URL to the links list.
    return links
    #This line returns the links list, containing all the extracted links from the HTML content.

def ExtractLinksFromJS(jsContent, baseUrl):
    # Function to extract links from JavaScript content
    pattern = r'(?:href=|src=|url\(|link\s*\(\s*)[\'"]?([^\'">\)\s]+)'
    #This line defines a regular expression pattern using the re module. The pattern is designed to match
    # common JavaScript statements that specify links or URLs, such as href, src, url(), or link().
    # It captures the actual URL or link value using a group.
    links = re.findall(pattern, jsContent)
    #This line uses the re.findall() function to find all matches of the regular expression pattern in the
    # jscontent. It returns a list of all the captured link values found in the JavaScript content.
    absoluteLinks = [urljoin(baseUrl, link) for link in links]
    # This line creates a new list called absolute_links using a list comprehension. It iterates over each link
    # in the links list and uses the urljoin() function from the urllib.parse module to resolve the relative URL
    # (link) to an absolute URL based on the base_url. The absolute URLs are stored in the absolute_links list.
    return absoluteLinks
    #This line returns the absoluteLinks list, containing all the resolved absolute URLs extracted from the
    # JavaScript content.

def crawlWaybackMachineLinks(url, days):
    # Function to crawl Wayback Machine links for the last 1 year
    baseUrl = 'http://web.archive.org'
    wayBackUrl = f'{baseUrl}/wayback/available?url={url}'
    response = fetchUrl(wayBackUrl)
    #These lines define the base URL for the Wayback Machine and construct a specific URL for checking the availability
    # of archived snapshots for the provided url. The fetch_url function is used to fetch the content of the wayback_url
    # and store the response in the response variable.
    if response:
        data = json.loads(response)
        if 'archived_snapshots' in data:
            snapshots = data['archived_snapshots']
            if 'closest' in snapshots:
                closestSnapshots = snapshots['closest']
                timeStamp = closestSnapshots['timestamp']
                #These lines check if the response is not None (indicating a successful request) and extract relevant
                # data from the response JSON. It checks if the JSON contains the key 'archived_snapshots' and retrieves
                # the value associated with it. It then checks if the 'closest' key exists within the snapshots and retrieves
                # the corresponding snapshot's timestamp.
                timeStamp = datetime.strptime(timeStamp, '%Y%m%d%H%M%S')
                wayBackDate = datetime.strftime(timeStamp, '%Y%m%d%H%M%S')
                startDate = datetime.strptime(wayBackDate, '%Y%m%d%H%M%S') - timedelta(days=days)
                startTimeStamp = startDate.strftime('%Y%m%d%H%M%S')
                wayBackLinkUrls = f'{baseUrl}/cdx/search/cdx?url={url}&from={startTimeStamp}&to={timeStamp}&output=json'
                response = fetchUrl(wayBackLinkUrls)
                #These lines parse the retrieved timestamp into a datetime object and calculate the start date by subtracting
                # the provided days from the snapshot's date. The start date is then formatted into a timestamp string.
                # The wayback_links_url is constructed using the base URL and the formatted timestamps, specifying the
                # URL to fetch the links from Wayback Machine. The fetch_url function is used again to fetch the content
                # of the wayback_links_url and store the response in the response variable.
                if response:
                    links = response.split('\n')[1:]
                    waybackLinks = [urljoin(baseUrl, link.split('.')[2]) for link in links if len(link.split('.')) >= 3]
                    return waybackLinks
                #These lines check if the response is not None (indicating a successful request) and process the response
                # content. The response is split by newline character ('\n') and skipping the first line (header).
                # Each line represents a link in the response, and the third column contains the actual link URL.
                # The links are processed using a list comprehension to join the base URL with each link URL. The
                # resulting list of Wayback Machine links is returned.

    return []
    #If any of the conditions mentioned above are not satisfied or if there is an error during the process,
    # an empty list [] is returned.

def crawl(url):
    # Function to perform crawling for a given URL
    baseUrl = urlparse(url).scheme + '://' + urlparse(url).netloc
    #This line uses the urlparse function from the urllib.parse module to parse the provided url. It extracts the scheme
    # (e.g., http, https) and the network location (e.g., www.example.com) from the URL and concatenates them to form
    # the base_url.
    robotsUrl = urljoin(baseUrl, 'robots.txt')
    robotsContent = fetchUrl(robotsUrl)
    #These lines construct the URL for the robots.txt file by joining the base_url with /robots.txt. The fetch_url function
    # is used to fetch the content of the robots_url, and the response is stored in the robots_content variable.
    if robotsContent:
        print(f"robots.txt for {baseUrl}")
        print(robotsContent)
        #These lines check if the robots_content is not None (indicating a successful request) and print the content of the
        # robots.txt file along with the base_url.
    siteMapUrl = urljoin(baseUrl, 'sitemap.xml')
    siteMapContent = fetchUrl(siteMapUrl)
    # These lines construct the URL for the sitemap.xml file by joining the base_url with /sitemap.xml. The fetch_url function
    # is used to fetch the content of the sitemap_url, and the response is stored in the sitemap_content variable
    if siteMapContent:
        print(f"sitemap.xml for {baseUrl}")
        print(siteMapContent)
    #These lines check if the sitemap_content is not None (indicating a successful request) and print the content of the
    # sitemap.xml file along with the base_url
    htmlContent = fetchUrl(url)
    #This line uses the fetch_url function to fetch the HTML content of the provided url and stores it in the html_content
    # variable.
    if htmlContent:
         htmlLinks = extractLinksFromHtml(htmlContent, baseUrl)
         print(f"html links for {baseUrl}")
         for link in htmlLinks:
             print(link)
    #These lines check if the html_content is not None (indicating a successful request) and extract the links from the HTML
    # content using the extract_links_from_html function. It then prints the extracted links from the HTML content along
    # with the url
    jsLinks = ExtractLinksFromJS(htmlContent, baseUrl)
    print(f"linksfrom javascript {baseUrl}")
    for jsLink in jsLinks:
        jsContent = fetchUrl(jsLink)
        if jsContent:
            jsLinks = extractLinksFromHtml(jsContent, jsLink)
            for link in jsLinks:
                print(link)
    #These lines extract the JavaScript links from the HTML content using the extract_links_from_js function. It then
    # prints the extracted JavaScript links along with the url. For each JavaScript link, it fetches the content using
    # the fetch_url function and, if successful, extracts the links from the JavaScript content using the
    # extract_links_from_js function. It then prints the extracted links.
    wayBackLinks = crawlWaybackMachineLinks(baseUrl, 365)
    print(f"wayback machiene links for {baseUrl}")
    for link in wayBackLinks:
        print(link)

if __name__ == '__main__':
    url = input("Enter the Url: ")
    crawl(url)















