import click

@click.group()
def cli():
    pass

no = ["Nomor 1", "Nomor 2", "Nomor 3", "Nomor 4", "Nomor 5", "Nomor 6", "Nomor 7", "Nomor 8", "Nomor 9", "Nomor 10"]

# Number 1

# Change text to lower case
@cli.command(name="lower_case")
@click.argument("value", type=click.STRING)
def lower_case(value):
    print(no[0])
    print("'Lower Text'")
    print(f"Original Value : {value}")
    res = value.lower()
    print(f"Lower Cased Value : {res}")

# Change text to upper case
@cli.command(name="upper_case")
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
    
if __name__ == "__main__":
    cli()