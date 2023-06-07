#importing Whois module
import whois


#defining a function to perform a whois lookup

def whoisLookup(domain):
    try:
        w = whois.whois(domain)
        print(w)
    #adding exceptional for whois lookup error
    except:
        print(f"WHOIS lookup failed:")

#getting user input for domain name
if __name__ == '__main__':
    domain = input("Enter the domain name: ")
    #calling the whois Function
    whoisLookup(domain)

