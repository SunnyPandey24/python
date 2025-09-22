# wap to create a dictionary words with vali=ues as therir eng
# Example of Dictionary as a mini word translator

# Dictionary where keys are Hindi words and values are English meanings
words = {
    "madad": "Help",      # "madad" → "Help"
    "kursi": "CHAIR",     # "kursi" → "CHAIR"
    "billi": "Cat"        # "billi" → "Cat"
}

# Taking user input
word = input("Enter the word u want meaning of : ")

# Printing the meaning of the entered word
print(words[word])  

# Example Run:
# Input : kursi
# Output: CHAIR

