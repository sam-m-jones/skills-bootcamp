# defined string as sentence and removed spaces.
sentence = "we like to mix uppercase with lowercase"
sentence = sentence.replace(" "," ")

# stored characters in list, set index ratio and used map function to alternate cases.
chars = list(sentence)
chars[1::2] = map(str.upper, chars[1::2])

# joined and printed the result.
new_sentence = "".join(chars)
print(new_sentence)

# used split function to isolate words and modified the map function from line 15.
words = sentence.split()
words[1::2] = map(str.upper, words[1::2])

# joined and printed the result with spaces added between words
new_sentence = " ".join(words)
print(new_sentence)
