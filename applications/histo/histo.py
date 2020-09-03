# Your code here

""" 
The first thing we want to do is get rid of all the puncuation marks.
Then we will open the file
Read the file then split the text using split()
Append the word to the a word_count dictionary
Clsoe the file


"""

def no_punc(s):
    r = ""
    chars_to_ignore = '"?:;,.-+=/\\|[]{}()*^&'
    for char in s:
        if char not in chars_to_ignore:
            r += char
    return r

word_counts = {}

fp = open('robin.txt', 'r')

text = fp.read()

for word in text.split():
    no_punc(word)
    # Add count
    if word in word_counts:
        word_counts[word] += "#"
    else:
        word_counts[word] = "#"
fp.close()

print(word_counts)
