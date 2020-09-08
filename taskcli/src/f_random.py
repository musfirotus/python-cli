import click

@click.group()
def cli():
    pass

no = "Nomor 6"

# Number 6

# Random Alphanumeric
@cli.command(name="randoms")
@click.option("--length")
def randoms(value=32):
    print(no)
    
if __name__ == "__main__":
    cli()