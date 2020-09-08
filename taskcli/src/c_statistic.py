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
    print(no)
    res = statistics.mean(number)
    print(f"Mean Numbers : {res}")
    
# Median
@cli.command(name="median")
@click.argument("number", type=click.INT, nargs=-1)
def median(number):
    print(no)
    res = statistics.mean(number)
    print(f"Median of all Numbers : {res}")
    
# Mode
@cli.command(name="mode")
@click.argument("number", type=click.INT, nargs=-1)
def mode(number):
    print(no)
    res = statistics.mode(number)
    print(f"Mode of all Numbers : {res}")
    
# FMode
@cli.command(name="fmean")
@click.argument("number", type=click.INT, nargs=-1)
def fmean(number):
    print(no)
    res = statistics.fmean(number)
    print(f"FMean Numbers : {res}")
    
if __name__ == "__main__":
    cli()