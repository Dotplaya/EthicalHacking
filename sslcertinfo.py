# importing ssl module for working with certificates
# and socket library to create a connection
import ssl
import socket

# defining a function to retirve ssl certificate with host name parameter
def retriveSslCertificateInfo(hostName):
    # creating a secure SSl context
    try:
        #establishing a secure conection to the provided hostname
        context = ssl.create_default_context()
        with socket.create_connection((hostName, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=hostName) as secureSock:
                #retirve ssl certificate
                cert = secureSock.getpeercert()
        # displaying the cerificate information using itmes()
        # method itereating over each field and value
        print("ssl certificate Information")
        for field, value in cert.items():
            print(f"{field}, {value}")
    # this exception catches potential ssl errors and scoket errors
    except ssl.SSLError as e:
        print(f"An error occured {e}")
    except socket.gaierror as e:
        print(f"An error occured {e}")

if __name__ == '__main__':
    hostName = input("Enter Domain Name: ")
    retriveSslCertificateInfo(hostName)







