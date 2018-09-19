def question():
	q = input("What is your question?")
	while q[-1] != "?":
		q = input("I only accept questions. Ask again")

	return q
