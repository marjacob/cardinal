var ChatController = function(client) {
	var observers = [ ];

	client.addListener("join", function(channel, nick, message) {
		for (var i = 0, j = observers.length; i < j; ++i) {
			var observer = observers[i];
			if (typeof observer.onJoin === "function") {
				observer.onJoin(
					client, 
					channel, 
					nick, 
					message);
			}
		}
	});

	client.addListener("message", function(from, to, text, message) {
		for (var i = 0, j = observers.length; i < j; ++i) {
			var observer = observers[i];
			if (typeof observer.onMessage === "function") {
				observer.onMessage(client, 
					from, 
					to, 
					text, 
					message);
			}
		}
	});

	this.attach = function(observer) {
		observers.push(observer);
	};

	this.detach = function(observer) {
		for (var i = 0, j = observers.length; i < j; ++i) {
			if (observers[i] === observer) {
				observers.splice(i, 1);
			}
		}
	};
}

module.exports = ChatController;
