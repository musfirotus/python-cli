import click

@click.group()
def cli():
    pass

no = "Nomor 9"

# Number 9

# Infinite Inputs
@cli.command(name="inputs")
def inputs():
    nums = []

    # Set new_name to something other than 'quit'.
    new_nums = ''

    # Start a loop that will run until the user enters 'quit'.
    while new_nums != 'quit':
        # Ask the user for a name.
        new_nums = input("Please tell me someone I should know, or enter 'quit': ")

        # Add the new name to our list.
        nums.append(new_nums)

    # Show that the name has been added to the list.
    print(nums)
    
if __name__ == "__main__":
    cli()