import click


@click.group(name='hello')
@click.pass_context
def main(ctx):
    """I'll say something
    """


@main.command()
@click.pass_context
def world(ctx):
    """I'll say hello world
    """
    click.echo('hello world')


@main.command()
@click.pass_context
def moon(ctx):
    """I'll say hello moon
    """
    click.echo('hello moon')


@main.command()
@click.argument('name', nargs=1)
@click.pass_context
def name(ctx, name):
    """I'll say hello to you
    """
    click.echo('hello '+ name)
