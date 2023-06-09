import dns.resolver
# This line imports the dns.resolver module from the dnspython library. It provides the functionality
# to perform DNS queries and retrieve DNS records.


def printRecords(records):
    #defining function to print records
    for record in records:
        #This line starts a for loop that iterates over each element in the records list.
        print(record)
        # This line prints the current record to the console.

def enumerateDnsRecords(domain):
    # defining a function to enumerate dns records
    aRecords = dns.resolver.resolve(domain, 'A')
    # This line uses the dns.resolver.resolve() function from the dns.resolver module to
    # perform a DNS query for the specified domain and record type 'A'. The 'A' record type
    # is used to retrieve the IPv4 address associated with the domain. The returned result is
    # assigned to the variable a_records.
    print('A records')
    printRecords(aRecords)
    # This line prints the string "A Records:" to the console, indicating that the following records are of type 'A'.
    # The next line print_records(a_records) calls the printRecords function (assuming it has been defined earlier in
    # the code) and passes a_records as the argument.This function is responsible for printing the DNS records.

    aaaaRecords = dns.resolver.resolve(domain, 'AAAA')
    # This line uses the dns.resolver.resolve() function to perform a DNS query for the specified domain and record
    # type 'AAAA'. The 'AAAA' record type is used to retrieve the IPv6 address associated with the domain. The returned
    # result is assigned to the variable aaaa_records.
    print('AAAA Records')
    printRecords(aaaaRecords)
    #This line prints the string "AAAA Records:" to the console, indicating that the following records are of type
    # 'AAAA', which represents IPv6 addresses.
    # The next line print_records(aaaa_records) calls the printRecords function (assuming it has been defined earlier in
    # the code) and passes aaaa_records as the argument. This function is responsible for printing the DNS records.

    # anyRecords = dns.resolver.resolve(domain, 'ANY')
    #This line uses the dns.resolver.resolve() function from the dns module to perform a DNS query for the specified domain
    # and record type 'ANY'. The 'ANY' record type is a wildcard that retrieves all available DNS records for the domain.
    # The returned result is assigned to the variable any_records.
    # print('ANY Records')
    # print(anyRecords)
    #This line prints the string "ANY Records:" to the console, indicating that the following records are of type 'ANY',
    # which retrieves all available DNS records for the domain.
    # The next line print_records(any_records) calls the print_records function (assuming it has been defined earlier in
    # the code) and passes any_records as the argument. This function is responsible for printing the DNS records.
    try:
        cNameRecords = dns.resolver.resolve(domain, 'CNAME')
    #This line uses the dns.resolver.resolve() function from the dns module to perform a DNS query for the specified domain
    # and record type 'CNAME'. The 'CNAME' record type is used to resolve canonical names, which are aliases for the actual
    # domain name. The returned result is assigned to the variable cNameRecords.
        print("CNAME Records:")
        printRecords(cNameRecords)
    except dns.resolver.NoAnswer:
        print("No answer")
    #This line prints the string "CNAME Records:" to the console, indicating that the following records are of type 'CNAME',
    # which represents canonical names.
    # The next line printRecords(cNameRecords) calls the printRecords function (assuming it has been defined earlier in the code)
    # and passes cNameRecords as the argument. This function is responsible for printing the DNS records.

    mxRecords = dns.resolver.resolve(domain, 'MX')
    # This line uses the dns.resolver.resolve() function to perform a DNS query for the specified domain and record type 'MX'.
    # The 'MX' record type is used to retrieve the mail exchange servers responsible for accepting incoming emails for the domain.
    # The result of the query is stored in the variable mx_records.
    print("MX Records:")
    printRecords(mxRecords)
    #This line prints the string "MX Records:" to the console, indicating that the following records are of type 'MX', which represents
    # mail exchange servers.
    # The next line print_records(mx_records) calls the print_records function (assuming it has been defined earlier in the code) and
    # passes mx_records as the argument. This function is responsible for printing the DNS records.
    nsRecords = dns.resolver.resolve(domain, 'NS')
    #This line uses the dns.resolver.resolve() function to perform a DNS query for the specified domain and record type 'NS'. The 'NS'
    # record type is used to retrieve the authoritative name servers for the domain. The result of the query is stored in the variable
    # ns_records.
    print("NS Records:")
    printRecords(nsRecords)
    #This line prints the string "NS Records:" to the console, indicating that the following records are of type 'NS', which represents
    # the authoritative name servers.
    # The next line printRecords(ns_records) calls the printRecords function (assuming it has been defined earlier in the code) and passes
    # ns_records as the argument. This function is responsible for printing the DNS records.

    soaRecords = dns.resolver.resolve(domain, 'SOA')
    #This line uses the dns.resolver.resolve() function to perform a DNS query for the specified domain and record type 'SOA'. The 'SOA'
    # record type (Start of Authority) provides information about the authoritative name server for the domain and other related details.
    # The result of the query is stored in the variable soa_records.
    print("SOA Records:")
    printRecords(soaRecords)
    #This line prints the string "SOA Records:" to the console, indicating that the following records are of type 'SOA', representing the
    # Start of Authority records.
    # The next line printRecords(soa_records) calls the printRecords function (assuming it has been defined earlier in the code) and passes
    # soa_records as the argument. This function is responsible for printing the DNS records.

    txtRecords = dns.resolver.resolve(domain, 'TXT')
    #This line uses the dns.resolver.resolve() function to perform a DNS query for the specified domain and record type 'TXT'. The 'TXT'
    # record type is used to store arbitrary text data associated with a domain. The result of the query is stored in the variable txt_records.
    print("TXT Records:")
    printRecords(txtRecords)
    #This line prints the string "TXT Records:" to the console, indicating that the following records are of type 'TXT', representing the TXT
    # records for the domain.
    # The next line printRecords(txt_records) calls the printRecords function (assuming it has been defined earlier in the code) and passes txt_records
    # as the argument. This function is responsible for printing the DNS records.

    dmarcRecords = dns.resolver.resolve('_dmarc.' + domain, 'TXT')
    # This line performs a DNS query for the _dmarc subdomain appended with the given domain and the record type 'TXT'. The _dmarc record is used to
    # specify the DMARC (Domain-based Message Authentication, Reporting, and Conformance) policy for the domain. The result of the query is stored in
    # the variable dmarc_records.
    print("DMARC Records:")
    printRecords(dmarcRecords)
    #This line prints the string "DMARC Records:" to the console, indicating that the following records are the DMARC records associated
    # with the domain.
    #The next line printRecords(dmarc_records) calls the printRecords function and passes dmarc_records as the argument
    # to print the DMARC records.


if __name__ == '__main__':
    domain = input("Enter the domain name: ")
    enumerateDnsRecords(domain)

