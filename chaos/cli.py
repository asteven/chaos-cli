import os
import sys
import configparser
import collections
import logging

import pkg_resources

import click
from click_plugins import with_plugins


@with_plugins(pkg_resources.iter_entry_points('chaos.cli.commands'))
@click.group()
@click.option('--verbose', '-v', 'log_level', flag_value='info', help='set log level to info', envvar='CHAOS_LOG_LEVEL')
@click.option('--debug', '-d', 'log_level', flag_value='debug', help='set log level to debug', envvar='CHAOS_LOG_LEVEL')
@click.option('--config', 'alternative_config', type=click.Path(readable=True, resolve_path=True),
    help='Path to a alternative config file.')
@click.pass_context
def main(ctx, log_level, alternative_config):
    """Bring order to your chaos.
    """
    setattr(ctx, 'obj', {})

    # configure logger and store it in the context
    logging.basicConfig(level=logging.ERROR, format='%(levelname)s: %(message)s', stream=sys.stderr)
    log = logging.getLogger('chaos')
    if log_level:
        log.setLevel(getattr(logging, log_level.upper()))
    ctx.obj['log'] = log

    # read config files if any
    config_file_exists = False
    if alternative_config:
        config_files = [alternative_config]
        # click already checked this for us
        config_file_exists = True
    else:
        config_files = [
            '/etc/%s/config.ini' % ctx.info_name,
            '/usr/local/etc/%s/config.ini' % ctx.info_name,
            os.path.join(click.get_app_dir(ctx.info_name), 'config.ini')
        ]
        for config_file in config_files:
            if os.path.isfile(config_file):
                config_file_exists = True
                log.debug('loading configuration from: %s', config_file)

    config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
    if config_file_exists:
        config.read(config_files)
    else:
        # TODO: error out no config file was found
        # hardcode defaults for now
        log.debug('No configuration file found, falling back to defaults.')
        _config = collections.OrderedDict()
        _config['consul'] = {'url': 'http://localhost:8500'}
        config.read_dict(_config)
    ctx.obj['config'] = config


    log.debug('chaos main ctx.args: {0}'.format(ctx.args))
    log.debug('chaos main ctx.params: {0}'.format(ctx.params))
    log.debug('chaos main ctx.obj: {0}'.format(ctx.obj))


if __name__ == '__main__':
    main()
