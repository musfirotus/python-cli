import click
from src.a import lower_case

@click.group()
def cli():
    pass

# Number 1
cli.add_command(lower_case)
# cli.add_command(upper_case)
# cli.add_command(capitalize)

if __name__ == '__main__':
    cli()