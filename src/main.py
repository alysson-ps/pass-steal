import click

def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('Version: 0.1.0')
    ctx.exit()

@click.command('list')
def main():
    """list password of categories"""
    pass

@click.command('new')
def new():
    """save new password"""
    pass

@click.command('delete')
def delete():
    """delete a password if exists"""
    pass

@click.group()
@click.option('-v', '--version', is_flag=True, help='Show version and exit.', callback=print_version)
def group(version):
    """ Password Manager """
    pass

group.add_command(main)
group.add_command(new)
group.add_command(delete)

if __name__ == '__main__':
    group()