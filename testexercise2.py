#ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
def animal_crackers(text):
	word = text.split()
	return word[0][0] == word[1][0]

text = ('Levelheaded Llama')
#text = ('Crazy cat')

text = animal_crackers(text)
print(text)