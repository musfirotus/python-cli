'''taskcli'''
import click
import functools
import statistics
import re
import socket
import requests

@click.group()
def cli():
    pass

no = ["Nomor 1", "Nomor 2", "Nomor 3", "Nomor 4", "Nomor 5", "Nomor 6", "Nomor 7", "Nomor 8", "Nomor 9", "Nomor 10"]

# Number 1

# Change text to lower case
@cli.command(name="lowercase")
@click.argument("value", type=click.STRING)
def lower_case(value):
    print(no[0])
    print("'Lower Text'")
    print(f"Original Value : {value}")
    res = value.lower()
    print(f"Lower Cased Value : {res}")

# Change text to upper case
@cli.command(name="uppercase")
@click.argument("value", type=click.STRING)
def upper_case(value):
    print(no[0])
    print("'Upper Text'")
    print(f"Original Value : {value}")
    res = value.upper()
    print(f"Upper Cased Value : {res}")

# Capitalized text
@cli.command(name="capitalize")
@click.argument("value", type=click.STRING)
def capitalize(value):
    print(no[0])
    print("'Capitalize Text'")
    print(f"Original Value : {value}")
    res = value.title()
    print(f"Capitalize Cased Value : {res}")
    
# Number 2

# Add all nunmbers
@cli.command(name="adds")
@click.argument("number", type=click.INT, nargs=-1)
def add_number(number):
    print(no[1])
    print("Add Numbers")
    print(sum(number))

# Subtract all numbers
@cli.command(name="subtract")
@click.argument("number", type=click.INT, nargs=-1)
def sub_number(number):
    print(no[1])
    print("Subtract Numbers")
    res = functools.reduce(lambda x,y: x - y, number)
    print(res)
    
# Multiply all numbers
@cli.command(name="multiply")
@click.argument("number", type=click.INT, nargs=-1)
def multiply(number):
    print(no[1])
    print("Multiply Numbers :")
    res = functools.reduce(lambda x,y: x * y, number)
    print(res)
    
# Divide all numbers
@cli.command(name="divide")
@click.argument("number", type=click.INT, nargs=-1)
def divide(number):
    print(no[1])
    print("Divide Numbers :")
    res = functools.reduce(lambda x,y: x / y, number)
    print(res)

# Number 3

# Mean
@cli.command(name="mean")
@click.argument("number", type=click.INT, nargs=-1)
def mean_number(number):
    res = statistics.mean(number)
    print(no[2])
    print("Mean Numbers :")
    print(res)
    
# Median
@cli.command(name="median")
@click.argument("number", type=click.INT, nargs=-1)
def median_number(number):
    res = statistics.mean(number)
    print(no[2])
    print("Median of all Numbers :")
    print(res)
    
# Mode
@cli.command(name="mode")
@click.argument("number", type=click.INT, nargs=-1)
def mode_number(number):
    res = statistics.mode(number)
    print(no[2])
    print("Mode of all Numbers :")
    print(res)
    
# FMode
@cli.command(name="fmean")
@click.argument("number", type=click.INT, nargs=-1)
def fmean_number(number):
    res = statistics.fmean(number)
    print(no[2])
    print("FMean Numbers :")
    print(res)

# Number 4

# Check for Palindrome
@cli.command(name="palindrome")
@click.argument("text", type=click.STRING)
def palindrome(text):
    print(no[3])
    print(f"String: {text}")
    replaced = re.sub(r'[^\w]', '', text)
    lowered = replaced.lower()
    print("Is Palindrome? Yes") if(lowered==lowered[::-1]) else print("Is Palindrome? No")

# Number 5
# Generate Obfuscator
@cli.command(name="obfuscator")
@click.argument("value", type=click.STRING)
def get_obfus(value):
    print(no[4])
    text = list(value)
    print(''.join(list(map(lambda char: f"&#{ord(char)};",text))))

# Number 6
# Random Alphanumeric
@cli.command(name="randoms")
@click.option("--length")
def get_random(value=32):
    print(no[5])

# Number 7
# referensi : https://www.tutorialspoint.com/python-program-to-find-the-ip-address-of-the-client
# Get Private IP Address
@cli.command(name="ip")
def get_ip():
    print(no[6])
    ## getting the hostname by socket.gethostname() method
    hostname = socket.gethostname()
    ## getting the IP address using socket.gethostbyname() method
    ip_address = socket.gethostbyname(hostname)
    ## printing the hostname and ip_address
    print(f"IP Address: {ip_address}")

# Number 8
# Get External IP Address
@cli.command(name="ip-external")
def get_external():
    print(no[7])
    print(requests.get('http://ip.42.pl/raw').text)

# Number 9
# Infinite Inputs
@cli.command(name="inputs")
def get_input():
    print(no[8])

# Number 10
# CRUD CLI-Apps
@cli.command(name="crud")
def get_crud():
    print(no[9])
    
if __name__ == "__main__":
    cli()