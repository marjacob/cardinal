"use strict";

var https = require('https');
var irc = require("irc");
var restify = require('restify');
var util = require("util")
var config = require("./config/config.js").config;
var Authenticator = require("./modules/Authenticator.js");
var EventEmitter = require('events').EventEmitter;
var Food = require("./modules/Food.js");
var Tanya = require("./modules/Tanya.js");

var main = function() {
	var bot = new irc.Client(config.server.address, config.nickname, {
		autoRejoin: true,
		channels: config.server.channels,
		port: config.server.port,
		realName: config.realname,
		userName: config.username
	});

	var auth = new Authenticator(bot);
	var food = new Food(bot);
	var tanya = new Tanya(bot);
}

if (require.main === module) {
	main();
}
