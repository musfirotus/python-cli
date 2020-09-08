import click
import requests

@click.group()
def cli():
    pass

no = "Nomor 8"

# Number 8

# Get External IP Address
@cli.command(name="ip_external")
def ip_external():
    res = requests.get('http://ip.42.pl/raw').text
    print(no)
    print(f"Your External IP Address : {res}")
    
if __name__ == "__main__":
    cli()