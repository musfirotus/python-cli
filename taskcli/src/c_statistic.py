import click
import statistics

@click.group()
def cli():
    pass

no = "Nomor 3"

# Number 3

# Mean
@cli.command(name="mean")
@click.argument("number", type=click.INT, nargs=-1)
def mean(number):
    res = statistics.mean(number)
    print(no)
    print("Mean Numbers :")
    print(res)
    
# Median
@cli.command(name="median")
@click.argument("number", type=click.INT, nargs=-1)
def median(number):
    res = statistics.mean(number)
    print(no)
    print("Median of all Numbers :")
    print(res)
    
# Mode
@cli.command(name="mode")
@click.argument("number", type=click.INT, nargs=-1)
def mode(number):
    res = statistics.mode(number)
    print(no)
    print("Mode of all Numbers :")
    print(res)
    
# FMode
@cli.command(name="fmean")
@click.argument("number", type=click.INT, nargs=-1)
def fmean(number):
    res = statistics.fmean(number)
    print(no)
    print("FMean Numbers :")
    print(res)
    
if __name__ == "__main__":
    cli()