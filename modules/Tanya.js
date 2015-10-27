var random = function(min, max) {
	return Math.floor(Math.random() * (max - min + 1) + min);
}

var Tanya = function(client) {
	var tanya = "tanyabt";
	var question_responses = [
		"Nei dette ble vanskelig.",
		"Tja, hvorfor ikke?",
		"Usikker, men virker jo litt sånn.",
		"Bare send en mail drift.",
		"Høres ut som noe en termvakt må svare på.",
		"Vel, det er jo mange mulige svar på det.",
		"Tror nesten martbo må svare på det.",
		"Prøvd å lese manualen?",
		"Aner virkelig ikke.",
		"Haha, godt spørsmål."
	];
	var statement_responses = [
		"Har tenkt mye på det samme selv.",
		"Joda, er enig der.",
		"Haha.",
		"Nemlig!",
		"Endelig en som sier det slik det er.",
		"Du ville gjort en god politiker.",
		"Blitt noe kaffe i dag?",
		"Men det gir jo ingen mening.",
		"Hvordan mener du?",
		"Nå må vi ikke overdrive her da."
	];

	var reply = function(nick, to, response) {
		client.say(to, nick + ": " + response);
	}

	var onQuestion = function(nick, to, text, message) {
		var i = random(0, question_responses.length - 1);
		var response = question_responses[i];
		reply(nick, to, response);
	}

	var onStatement = function(nick, to, text, message) {
		var i = random(0, statement_responses.length - 1);
		var response = statement_responses[i];
		reply(nick, to, response);
	}

	var onRandomEvent = function(nick, to, text, message) {
		if (-1 < text.indexOf("?")) {
			onQuestion(nick, to, text, message);
		} else {
			onStatement(nick, to, text, message);
		}
	}

	var onTanya = function(nick, to, text, message) {
		var rnd = random(1, 100);

		/* 5% change of triggering. */
		if (24 < rnd && 31 > rnd) {
			onRandomEvent(nick, to, text, message);
		}
	}

	var onMessage = function(nick, to, text, message) {
		if (nick.substring(0, tanya.length) === tanya) {
			onTanya(nick, to, text, message);
		}
	}

	client.addListener("message", onMessage);
}

module.exports = Tanya;
