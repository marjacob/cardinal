# -*- coding: utf-8 -*-

from irc3.plugins.command import command
import irc3

import cardinal.sio as sio


@irc3.plugin
class SioPlugin(object):
    requires = [
        "irc3.plugins.command"
    ]

    def __init__(self, bot):
        self.bot = bot

    @command
    def sio(self, mask, target, args):
        """
        List opp alle spisestedene som driftes av SiO, eller eventuelt de
        stedene som har noe spesielt.

            %%sio [<rett>]
        """
        if args["<rett>"]:
            hits = sio.Cafeteria.search(args["<rett>"])
            if hits:
                return ", ".join(cafeteria[0].name for cafeteria in hits)
            else:
                return "ingen som serverer det i dag （ﾉ´д｀）"
        else:
            cafeterias = ", ".join(sorted(sio.Cafeteria.all().keys()))
            if cafeterias:
                return "{0}".format(cafeterias)
            else:
                return "virker som tjenesten er nede (╯°□°）╯︵ ┻━┻"

    @command
    def dagens(self, mask, target, args):
        """
        List opp alle rettene som serveres et gitt sted i dag.

            %%dagens [<sted>]
        """
        place = args["<sted>"] if args["<sted>"] else "ifi"
        cafeteria = sio.Cafeteria.from_name(place)
        if cafeteria:
            if cafeteria.dishes:
                return "{cafeteria}: {dishes}".format(
                    cafeteria=cafeteria.name,
                    dishes=numbered_dishes(cafeteria.dishes))
            else:
                return "{cafeteria} har ikke publisert noe :(".format(
                    cafeteria=cafeteria.name)
        else:
            return "kjenner ikke til det stedet :(".format(mask)


def numbered_dishes(dishes):
    if len(dishes) == 1:
        return dishes[0]
    result = ""
    for i in range(0, len(dishes)):
        result += "{0}) {1} ".format(i + 1, dishes[i])
    return result.strip()
