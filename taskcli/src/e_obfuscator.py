import click

@click.group()
def cli():
    pass

no = "Nomor 5"

# Number 5

# Generate Obfuscator
@cli.command(name="obfuscator")
@click.argument("value", type=click.STRING)
def obfuscator(value):
    print(no)
    text = list(value)
    print(''.join(list(map(lambda char: f"&#{ord(char)};",text))))
    
if __name__ == "__main__":
    cli()