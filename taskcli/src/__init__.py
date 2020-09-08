import click
from src.a_transform import lower_case, upper_case, capitalize # 1
from src.b_arithmetic import adds, subtract, multiply, divide # 2
from src.c_statistic import mean, median, mode, fmean # 3
from src.d_palindrome import palindrome # 4
from src.e_obfuscator import obfuscator # 5
from src.f_random import randoms # 6
from src.g_ip import ip # 7
from src.h_exip import ip_external # 8
from src.i_inputs import inputs # 9
from src.j_crud import crud # 10

@click.group()
def cli():
    pass

# Number 1
cli.add_command(lower_case)
cli.add_command(upper_case)
cli.add_command(capitalize)

# Number 2
cli.add_command(adds)
cli.add_command(subtract)
cli.add_command(multiply)
cli.add_command(divide)

# Number 3
cli.add_command(mean)
cli.add_command(median)
cli.add_command(mode)
cli.add_command(fmean)

# Number 4
cli.add_command(palindrome)

# Number 5
cli.add_command(obfuscator)

# Number 6
cli.add_command(randoms)

# Number 7
cli.add_command(ip)

# Number 8
cli.add_command(ip_external)

# Number 9
cli.add_command(inputs)

# Number 10
cli.add_command(crud)

if __name__ == '__main__':
    cli()