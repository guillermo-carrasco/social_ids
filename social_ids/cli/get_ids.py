from __future__ import print_function

import sys

import click

from social_ids.networks import facebook, twitter, instagram

networks = {
    'facebook': facebook,
    'twitter': twitter,
    'instagram': instagram
}

@click.command()
@click.argument('network', type=click.Choice(networks.keys()))
@click.argument('handler', type=click.STRING)
def get_id(network, handler):
    network_id = networks[network].get_id(handler)
    if network_id is not None:
        print('ID for {network} handler "{handler}" is: {network_id}'.format(network=network,
                                                                             handler=handler,
                                                                             network_id=network_id))
    else:
        print('Couldn\'t fetch {network} ID for handler {handler}... is it the correct handler? Sorry!'.format(network=network,
                                                                                                               handler=handler))
        sys.exit(1)
