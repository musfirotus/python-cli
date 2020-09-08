import click
import re

@click.group()
def cli():
    pass

no = "Nomor 4"

# Number 4

# Check for Palindrome
@cli.command(name="palindrome")
@click.argument("text", type=click.STRING)
def palindrome(text):
    print(no)
    print(f"String: {text}")
    replaced = re.sub(r'[^\w]', '', text)
    lowered = replaced.lower()
    print("Is Palindrome? Yes") if(lowered==lowered[::-1]) else print("Is Palindrome? No")
    
if __name__ == "__main__":
    cli()