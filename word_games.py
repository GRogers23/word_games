
def main():
	#with open(filename, (open for reading 'r', #writing 'w' or reading and writing 'rw'))
	word = input("What's your word? Enter it here: ")
	print("Scrabble score: " + (str)(scrabble_value(word)));
	#everything past here the file is closed
	# scrabble_value("potato")

	#three options:
	# 1) write a program to compute the "scrabble score" or a word (assuming no tile modifiers).
		#I'll provide tile values for each tile
	# 2) Write a program to determine if a given "scrabble rack" of seven letters can be formed into a valid srabble word using the provided scrabble_dictionary.txt
	# valid_word("cearr") --> return a list of words from the dictionary that you can make with these letters; if no words ossible, return emoty list

	# 3) A small game: "GHOST"
	# a loop with text input (use input() function we talked about)

	#4) "GHOST BOT" same as above but one player, and then the computer makes guesses that make life hard for the player

	#def scrabble_value(word):
			# do some work
			# return the value


def scrabble_value(word):
	
	score = 0

	scrabble_dict = {
		"a": 1,
		"b": 3,
		"c": 3,
		"d": 2,
		"e": 1,
		"f": 4,
		"g": 2,
		"h": 4,
		"i": 1,
		"j": 8,
		"k": 5,
		"l": 1,
		"m": 3,
		"n": 1,
		"o": 1,
		"p": 3,
		"q": 10,
		"r": 1,
		"s": 1,
		"t": 1,
		"u": 1,
		"v": 4,
		"w": 4,
		"x": 8,
		"y": 4,
		"z": 10
	}	

	for i in word:
		score = score + scrabble_dict[i]

	return score

if __name__ == '__main__':
	main()

