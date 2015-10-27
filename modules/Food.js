var Client = require("node-rest-client").Client;

var DinnerClient = function() {
	var restClient = new Client();
	var apiUri = "http://api.desperate.solutions/dagens/";

	this.getRestaurants = function(callback) {
		restClient.get(apiUri, function(data, response){
			callback(data);
		});
	};

	this.getMenu = function(restaurant, callback) {
		var restaurants = this.getRestaurants(
			function(restaurants) {
				console.log("restaurant: " + restaurant);
				console.log(restaurants);
				var apiUriRestaurant = restaurants[restaurant];

				// Check if the restaurant exists.
				if (!apiUriRestaurant) {
					return;
				}

				console.log(apiUriRestaurant);
				restClient.get(apiUriRestaurant, function(data, response) {
					callback(data["cafeteria"]);
				});
			}
		);
	}
}

var Food = function(client) {
	var m_dinner_client = new DinnerClient();

	var onMessage = function(nick, to, text, message) {
		var command = text.substr(0, text.indexOf(' '));
		var argument = text.substr(text.indexOf(' ') + 1);

		console.log("command : " + command);
		console.log("argument: " + argument);

		if (!command) {
			command = argument;
			argument = "";
		}

		switch (command) {
		case "!mat":
			onListRestaurants(nick, to, text, message);
			break;
		case "!meny":
			onListMenu(nick, to, argument);
			break;
		}
	}

	var onListRestaurants = function(nick, to, text, message) {
		m_dinner_client.getRestaurants(function(restaurants) {
			console.log(restaurants)

			client.say(
				to, 
				nick + ": Skriv \"!meny <restaurant>\" " + 
				"for dagens meny.");

			// Send the restaurants list back.
			for (var restaurant in restaurants) {
				if (restaurants.hasOwnProperty(restaurant)) {
					client.say(to, " - " + restaurant);
				}
			}
		});
	};

	var printCategory = function(nick, to, dishes) {
		for (var i = 0, j = dishes.length; i < j; ++i) {
			client.say(to, (i + 1) + ". " + dishes[i]);
		}
	}

	var onListMenu = function(nick, to, restaurant) {
		m_dinner_client.getMenu(restaurant, function(cafeteria) {
			client.say(
				to, 
				nick + ": Ok, lister opp for " + restaurant
			);

			for (var i = 0, j = cafeteria.length, j; i < j; ++i) {

				client.say(to, "Meny: " + cafeteria[i].category);
				printCategory(nick, to, cafeteria[i].dishes);
			}
		});
	}

	client.addListener("message", onMessage);
}

module.exports = Food;
