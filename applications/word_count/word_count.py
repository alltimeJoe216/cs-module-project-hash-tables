def word_count(s):
    dictionary = {}
    phrase = ""

    chars_to_ignore = '":;,.-+=/\\|[]{}()*^&'
    # find our characters
    for char in s:
        if char not in chars_to_ignore:
            phrase += char
    words = phrase.lower().split()

    # count each word
    for word in words:        
        if word not in dictionary:            
            dictionary[word] = 1
        else:
            dictionary[word] += 1

    return dictionary





if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))