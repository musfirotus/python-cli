import click
# 1
from src.a_transform import lower_case, upper_case, capitalize
# 2
from src.b_arithmetic import adds, subtract, multiply, divide
# 3
from src.c_statistic import mean, median, mode, fmean
# 4
from src.d_palindrome import palindrome
# 5
from src.e_obfuscator import obfuscator
# 6
# from src.f_random
# 7
from src.g_ip import ip
# 8
from src.h_exip import ip_external
# 9
# from src.i_inputs
# 10
# from src.j_crud

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

# Number 7
cli.add_command(ip)

# Number 8
cli.add_command(ip_external)

# Number 9

# Number 10

if __name__ == '__main__':
    cli()