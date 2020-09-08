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
    print(no)
    print("Add Numbers")
    print(sum(number))

# Subtract all numbers
@cli.command(name="subtract")
@click.argument("number", type=click.INT, nargs=-1)
def subtract(number):
    print(no)
    print("Subtract Numbers")
    res = functools.reduce(lambda x,y: x - y, number)
    print(res)
    
# Multiply all numbers
@cli.command(name="multiply")
@click.argument("number", type=click.INT, nargs=-1)
def multiply(number):
    print(no)
    print("Multiply Numbers :")
    res = functools.reduce(lambda x,y: x * y, number)
    print(res)
    
# Divide all numbers
@cli.command(name="divide")
@click.argument("number", type=click.INT, nargs=-1)
def divide(number):
    print(no)
    print("Divide Numbers :")
    res = functools.reduce(lambda x,y: x / y, number)
    print(res)
    
if __name__ == "__main__":
    cli()