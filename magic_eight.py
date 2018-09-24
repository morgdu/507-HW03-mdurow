def question():
	q = input("What is your question?")

	while q[-1] != "?":
		q = input("I only accept questions. Ask again")

	return q
	

answers = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.", "You may rely on it.", 
"As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again",
"Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", 
"My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]

import random

#Found this on stackoverflow (https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list)
#print(random.choice(answers))

status = ""

while status != "quit":
	question()
	print(random.choice(answers))
	status = input("Continue? Y for continue, 'quit' to end")

