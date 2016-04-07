# -*- coding: utf-8 -*-

# Standard library imports.
import os
import sys

# Third party imports.
import irc3

# Project local imports.
import settings
import sio


def main(args):
    config = settings.CardinalSettings()
    config.load()

    print("{nick} connecting to {host}:{ssl}{port}...".format(
        nick=config.nick,
        host=config.host,
        ssl='+' if config.ssl else '',
        port=config.port
    ))

    bot = irc3.IrcBot.from_config(config.to_json())
    bot.run(forever=True)

    # print(sio.Cafeteria.from_name("parken"))
    # return os.EX_OK


if __name__ == "__main__":
    sys.exit(main(sys.argv))
