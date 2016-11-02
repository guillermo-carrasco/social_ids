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
    _id = networks[network.upper()].get_id(handler)
    if _id is not None:
        print('ID for {} handler "{}" is: {}'.format(network, handler, _id))
    else:
        print('Couldn\'t fetch {} ID for handler {}... is it the correct handler? Sorry! ¯\_(ツ)_/¯'.format(network, handler))
