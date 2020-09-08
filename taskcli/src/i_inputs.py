import click

@click.group()
def cli():
    pass

no = "Nomor 9"

# Number 9

# Infinite Inputs
@cli.command(name="inputs")
def inputs():
    print(no)
    
if __name__ == "__main__":
    cli()