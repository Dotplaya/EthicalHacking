#importing the request library which provides convinent methods for making HTTP requests in python
import requests

#defining a function with a parameter called url. This finction will be used to retirve
# and display header information
def viewHeaderInfo(url):
    try:
        # using request.head method to send and HTTP head request to specified url.
        # This method retives only headers without response body
        res = requests.head(url)
        head = res.headers
        #this loop iterates over each header in the headers dictionary using the items()
        #method and prints each header and its coressponding value
        print("Header information")
        for header, value in head.items():
            print(f"{header}, {value}")
    # this block handles exceptions that catches any requests related Errors such network error or invalid url
    except requests.exceptions.RequestException as e:
        print(f"An error occurred as {e}")

if __name__ == '__main__':
    #calling the function with url parameter as input to display the header for given url
    url = input("Enter the URL: ")
    viewHeaderInfo(url)


