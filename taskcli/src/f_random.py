import click
import random

@click.group()
def cli():
    pass

no = "Nomor 6"

# Number 6

# Random Alphanumeric
@cli.command(name="randoms")
@click.option("--length", default=10, type=click.INT)
@click.option("--letters", is_flag=True, default=False, type=click.BOOL)
@click.option("--numbers", is_flag=True, default=False, type=click.BOOL)
@click.option("--uppercase", is_flag=True, default=False, type=click.BOOL)
@click.option("--lowercase", is_flag=True, default=False, type=click.BOOL)
def randoms(length, letters, numbers, uppercase, lowercase):
    char = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    num = list("1234567890")
    # print(type(letters))
    output = ''
    for i in enumerate(char):
        charnum = list([char,num])
        select = random.randrange(0,2)
        if numbers == True:
            select = 1
        if letters == True:
            select = 0
        # print(charnum)
        output+=charnum[select][random.randrange(0, len(charnum[select]), 3)]
        
        if i == length:
            break

    if uppercase == True:
        output = output.upper()
    if lowercase == True:
        output = output.lower()
    # if number == False
    print(output)
    print(length)
    
if __name__ == "__main__":
    cli()
    
# app random
# # Output Nf2HZlmJ9TItezKL1EcVrstKjxzLaQj8

# app random --length=10
# # Output l1BgUotRmS

# app random --letters=false
# # Output 83628194739182748381981283721982

# app random --numbers=false
# # Output kdBOsSSFvqLCRvommVauHzmPdvSoYRIs

# app random --uppercase
# # Output 9JWSY6OOTNPJ6LZLUQE9JIXWPQTLC0K2

# app random --numbers=false --lowercase --length=20
# # Output ljmuoyopwxcvhycowqqi