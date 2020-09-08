import click
import functools

@click.group()
def cli():
    pass

no = "Nomor 2"

# Number 2

# Add all nunmbers
@cli.command(name="adds")
@click.argument("number", type=click.INT, nargs=-1)
def adds(number):
    res = sum(number)
    print(no)
    print(f"Add Result : {res}")

# Subtract all numbers
@cli.command(name="subtract")
@click.argument("number", type=click.INT, nargs=-1)
def subtract(number):
    print(no)
    res = functools.reduce(lambda x,y: x - y, number)
    print(f"Subtract Result : {res}")
    
# Multiply all numbers
@cli.command(name="multiply")
@click.argument("number", type=click.INT, nargs=-1)
def multiply(number):
    print(no)
    res = functools.reduce(lambda x,y: x * y, number)
    print(f"Multiply Result : {res}")
    
# Divide all numbers
@cli.command(name="divide")
@click.argument("number", type=click.INT, nargs=-1)
def divide(number):
    print(no)
    res = functools.reduce(lambda x,y: x / y, number)
    print(f"Divide Result : {res}")
    
if __name__ == "__main__":
    cli()