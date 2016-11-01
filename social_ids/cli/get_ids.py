import click

from social_ids.networks import facebook, twitter, instagram

networks = {
    'FACEBOOK': facebook,
    'TWITTER': twitter,
    'INSTAGRAM': instagram
}


@click.command()
@click.argument('network', click.Choice(networks.keys()))
@click.argument('handler', type=click.STRING)
def get_id(network, handler):
    print(network.upper(), handler)
    networks[network.upper()].get_id(handler)
