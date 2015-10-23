var operators = require("../config/operators.js");
var UserController = require("../controllers/UserController.js");

var Authenticator = function(client) {
	var authenticate = function(hostmask, user) {
		for (var i = 0, j = user.hostmasks.length; i < j; ++i) {
			var re = new RegExp(user.hostmasks[i]);
			return (re.test(hostmask));
		}
	}

	var isOperator = function(channel, nick, message) {
		var hostmask = message.user + "@" + message.host;
		
		for (var i = 0, j = operators.length; i < j; ++i) {
			var user = operators[i];
			// Check whether the user has this channel.
			if (user.channels.indexOf(channel) > -1) {
				return authenticate(hostmask, user);
			}
		};
	};
	
	var onModeRemoved = function(channel, by, mode, argument, message) {
		if (0 != mode.localeCompare("o")) {
			return;
		}

		var nick = argument;
		if (isOperator(channel, nick, message)) {
			client.send("MODE", channel, "+o", nick);
		}
	}

	var onUserJoined = function(channel, nick, message) {
		if (isOperator(channel, nick, message)) {
			client.send("MODE", channel, "+o", nick);
		}
	}

	client.addListener("join", onUserJoined);
	client.addListener("-mode", onModeRemoved);
}

module.exports = Authenticator;
