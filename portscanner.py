import socket
# This line imports the socket module, which provides low-level networking interfaces for creating sockets and
# performing network operations.

def scanPort(host, port):
    # defining a function to scan for open ports.
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            #This line creates a new TCP socket using socket.socket() with the socket.AF_INET
            # parameter indicating IPv4 and socket.SOCK_STREAM parameter indicating TCP protocol. The with statement
            # ensures proper handling of the socket by automatically closing it when the block is exited.
            sock.settimeout(1)
            #This line sets a timeout of 2 seconds on the socket, which means that if a connection attempt takes longer
            # than 2 seconds, it will time out.
            result = sock.connect_ex((host, port))
            #This line attempts to establish a connection to the specified host and port using sock.connect_ex().
            # The connect_ex() method returns an error code. If the connection is successful, it returns 0, indicating
            # that the port is open. Otherwise, it returns an error code.
            if result == 0:
                return True
            return False
        #This line checks the value of result. If it is 0, indicating a successful connection, the function returns
        # True to indicate that the port is open. Otherwise, it returns False to indicate that the port is closed.
    except socket.error as e:
        print(f"Some Error occured {e}")
        #This block is executed if there is an exception raised during the connection attempt. It catches any socket.error
        # exception and returns Error message to indicate that the port is closed.

def getServiceVersion(host, port):
    # defining a function to scan for services versions of open ports.
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # This line creates a new TCP socket using socket.socket() with the socket.AF_INET
        # parameter indicating IPv4 and socket.SOCK_STREAM parameter indicating TCP protocol. The with statement
        # ensures proper handling of the socket by automatically closing it when the block is exited.
            sock.settimeout(1)
        # This line sets a timeout of 2 seconds on the socket, which means that if a connection attempt takes longer
        # than 2 seconds, it will time out.
            sock.connect((host, port))
        #    This line attempts to establish a connection to the specified host and port using sock.connect(). If the
        #    connection is successful, the code continues to the next line. If the connection fails or an error occurs,
        #    it will raise a socket error exception.
            banner = sock.recv(1024).decode().strip()
        # This line receives data from the socket using sock.recv(). It receives up to 1024 bytes of data and decodes
        # it as a string using the decode() method. The strip() method removes any leading or trailing whitespace from
        # the received data. The received data is assigned to the variable banner, which typically represents a service
        # version or identification string.
            return banner
        # This line returns the banner, which represents the service version or identification string, to the caller
        # of the function.
    except socket.error:
        return None
    #  This block is executed if there is an exception raised during the connection attempt or data receiving.
    #  It catches any socket.error exception and returns None to indicate that the service version could not
    #  be obtained or an error occurred.

targetHost = input("Enter the Target host: ")
startPort = int(input("Enter the Start port: "))
endPort = int(input("Enter the End Port: "))
#These lines prompt the user to enter the target host, start port, and end port. The input is captured using
# the input() function, and the start and end ports are converted to integers using int().

for port in range(startPort, endPort + 1):
    #his line starts a loop that iterates through each port in the range from start_port to end_port + 1.
    # The loop will iterate over all the ports within the specified range.
    if scanPort(targetHost, port):
        #This line calls the scan_port() function, passing in the target_host and the current port.
        # It checks if the port is open by attempting to establish a connection to the host and port.
        serviceVersion = getServiceVersion(targetHost, port)
        # If the port is open, this line calls the get_service_version() function, passing in the
        # target_host and the current port. It retrieves the service version or identification string
        # for the open port.
        if serviceVersion:
            print(f"Port {port} is open - service version: {serviceVersion}")
        print(f"Port {port} is open - service version unavailable")
    print(f"port {port} is closed")








