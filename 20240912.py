import re

def howMany(sentence):
    valid_word_pattern = re.compile(r"^[a-zA-Z-]+$")
    words = sentence.split()
    valid_word_count = 0
    
    for word in words:
        word = word.strip(",.?!")
        
        if valid_word_pattern.match(word):
            valid_word_count += 1
    
    return valid_word_count