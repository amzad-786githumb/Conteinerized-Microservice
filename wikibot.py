from mylib.bot import scrap
import click


@click.command()
@click.option("--name", help="Webpage we want to scrap.")
def cli(name):
    results = scrap(name)
    click.echo(click.style(f"{results}:", bg="blue", fg="white"))


if __name__ == "__main__":
    cli()
