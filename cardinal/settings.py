# -*- coding: utf-8 -*-

import json
import os


class CardinalSettings(object):
    def __init__(self, project="cardinal"):
        self.__project = project
        self.__user_home = os.path.expanduser('~')
        self.nick = "cardinal"
        self.realname = "cardinal"
        self.host = "chat.freenode.net"
        self.port = 6697
        self.ssl = True
        self.autojoins = ["##cardinal-default"]
        self.plugins = [
            "irc3.plugins.log",
            "plugins.sio_plugin"
        ]

    @property
    def project(self):
        return self.__project

    @property
    def user_home(self):
        return self.__user_home

    @property
    def config_home(self):
        return os.path.join(self.user_home, ".{0}".format(self.project))

    @property
    def config_file(self):
        return os.path.join(self.config_home, "config.json")

    def to_json(self):
        return {
            "nick": self.nick,
            "realname": self.realname,
            "host": self.host,
            "port": self.port,
            "ssl": self.ssl,
            "autojoins": self.autojoins,
            "includes": self.plugins
        }

    def from_json(self, data):
        if "nick" in data:
            self.nick = data["nick"]
        if "realname" in data:
            self.realname = data["realname"]
        if "host" in data:
            self.host = data["host"]
        if "port" in data:
            self.port = data["port"]
        if "ssl" in data:
            self.ssl = data["ssl"]
        if "autojoins" in data:
            self.autojoins = data["autojoins"]
        if "includes" in data:
            self.plugins = data["includes"]

    def load(self):
        try:
            with open(self.config_file,
                      mode="r",
                      encoding="UTF-8") as config_file:
                self.from_json(json.load(config_file))
        except FileNotFoundError:
            return

    def save(self):
        os.makedirs(self.config_home, mode=0o770, exist_ok=True)
        with open(self.config_file,
                  mode="w",
                  encoding="UTF-8") as config_file:
            return json.dump(self.to_json(), config_file, indent="\t")
