# -*- coding: utf-8 -*-

# Standard library imports.
import os
import sys

# Third party imports.
import click
import irc3

# Project local imports.
import cardinal.settings
import cardinal.sio


# The version as used in setup.py.
__version__ = "1.0.0"


def main(args=None):
    return 0


@click.group()
@click.option("--debug", "-D", is_flag=True)
def cli(debug):
    pass


@cli.command()
@click.argument("persona", required=False)
@click.option("--host", "-H",
              default="chat.freenode.net",
              prompt="Host", 
              help="Set the hostname of the IRC service.")
@click.option("--port", "-p", 
              default=6697,
              prompt="Port", 
              type=click.IntRange(1, 65535),
              help="Set the port nubmer of the IRC service.")
@click.option("--ssl", "-s",
              default=True,
              prompt="SSL", 
              help="Enable SSL for the IRC service.", 
              is_flag=True)
@click.option("--nick", "-n", 
              default="cardinal",
              prompt="Nick", 
              help="Set the friendly name of the bot.")
@click.option("--name", "-N", 
              default="cardinal",
              prompt="Name", 
              help="Set the full name of the bot.")
@click.option("--channels", "-c", 
              default="##cardinal-default",
              prompt="Channels", 
              help="Set the IRC channels the bot should join.")
def new(persona, host, port, ssl, nick, name, channels):
    config = settings.CardinalSettings(persona=persona)
    config.autojoins = channels.split(',')
    config.host = host
    config.nick = nick
    config.port = port
    config.realname = name
    config.ssl = ssl
    config.save()


@cli.command()
@click.argument("persona", nargs=1, required=False)
def start(persona):
    config = settings.CardinalSettings(persona=persona)
    config.load()

    print("{nick} connecting to {host}:{ssl}{port}...".format(
        nick=config.nick,
        host=config.host,
        ssl='+' if config.ssl else '',
        port=config.port))

    bot = irc3.IrcBot.from_config(config.to_dict())

    try:
        bot.run(forever=True)
    except:
        return os.EX_SOFTWARE
    return os.EX_OK

if __name__ == '__main__':
    sys.exit(main())

