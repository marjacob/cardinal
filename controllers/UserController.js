var operators = require("../config/operators.js");

var UserController = function() {
	this.findByHostmask = function (hostmask) {
		for (var i = 0, j = operators.length; i < j; ++i) {
			var user = operators[i];
			
			for (var i = 0, j = user.hostmasks.length; i < j; ++i) {
				var re = new RegExp(user.hostmasks[i]);
				return (re.test(hostmask)
					? user
					: null);
			}
		};

		return false;
	};
}

module.exports = UserController;
