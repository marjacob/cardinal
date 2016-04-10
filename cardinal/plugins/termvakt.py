# -*- coding: utf-8 -*-

import random

from irc3.plugins.command import command
import irc3


@irc3.plugin
class TermvaktPlugin(object):
    requires = [
        "irc3.plugins.command"
    ]

    def __init__(self, bot):
        self.bot = bot

    @command
    def enig(self, mask, target, args):
        """
        Gi uttrykk for at du er enig med noen.

            %%enig [<bruker>]
        """
        response = random.choice(RESPONSE_AGREE)
        if args["<bruker>"]:
            response = "{user}: {message}".format(
                user=args["<bruker>"],
                message=response)
        return response

RESPONSE_AGREE = [
    "Har tenkt mye på det samme selv.",
    "Joda, helt er enig der.",
    "Haha sant ass.",
    "Nemlig!",
    "Endelig en som sier det slik det er.",
    "Du ville gjort en god politiker.",
    "10/10 terningkast 6.",
    "Ville nok tatt det opp med drift, men ellers helt enig.",
    "Å tro noe annet er jo helt ute på viddene.",
    "Visste ikke alle det?"
];
