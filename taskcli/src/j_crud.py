import click

@click.group()
def cli():
    pass

no = "Nomor 10"

# Number 10

# CRUD CLI-Apps
@cli.command(name="crud")
def crud():
    print(no)
    
if __name__ == "__main__":
    cli()