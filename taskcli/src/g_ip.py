import click
import socket

@click.group()
def cli():
    pass

no = "Nomor 7"

# Number 7

# referensi : https://www.tutorialspoint.com/python-program-to-find-the-ip-address-of-the-client
# Get Private IP Address
@cli.command(name="ip")
def get_ip():
    print(no[6])
    hostname = socket.gethostname() # getting the hostname by socket.gethostname() method
    ip_address = socket.gethostbyname(hostname) # getting the IP address using socket.gethostbyname() method
    print(f"IP Address: {ip_address}") # printing the ip_address
    
if __name__ == "__main__":
    cli()