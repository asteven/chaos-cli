import os
import sys
import configparser
import collections
import logging


import click
from click_plugins import with_plugins

try:
   from reentry import manager as entry_pt_manager
except:
   import pkg_resources as entry_pt_manager


def get_config_files(ctx, file_name):
    possible_config_files = [
        '/etc/%s/%s' % (ctx.info_name, file_name),
        '/usr/local/etc/%s/%s' % (ctx.info_name, file_name),
        os.path.join(click.get_app_dir(ctx.info_name), file_name),
    ]
    config_files = []
    for config_file in possible_config_files:
        if os.path.isfile(config_file):
            config_files.append(config_file)
    return config_files


@with_plugins(reentry.manager.iter_entry_points('chaos.cli.commands'))
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

    # Configure logging.
    logging_config_files = get_config_files(ctx, 'logging.ini')
    if logging_config_files:
        logging_config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
        logging_config.read(logging_config_files)
        logging.config.fileConfig(logging_config)
    else:
        logging.basicConfig(level=logging.ERROR, format='%(levelname)s: %(message)s', stream=sys.stderr)
    log = logging.getLogger('chaos')
    ctx.obj['log_level'] = log_level
    if log_level:
        log.setLevel(getattr(logging, log_level.upper()))
    ctx.obj['log'] = log


    # Configure application.
    config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
    config_files = get_config_files(ctx, 'config.ini')
    if config_files:
        log.debug('loading configuration from: %s', ', '.join(config_files))
        config.read(config_files)
    else:
        log.warn('No configuration file found.')
        #raise exceptions.Error('No configuration file found.')
    ctx.obj['config'] = config


    log.debug('chaos main ctx.args: {0}'.format(ctx.args))
    log.debug('chaos main ctx.params: {0}'.format(ctx.params))
    log.debug('chaos main ctx.obj: {0}'.format(ctx.obj))


if __name__ == '__main__':
    main()
