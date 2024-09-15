def minimalOperations(words):
    results = []
    
    for word in words:
        count = 0
        i = 0
        
        while i < len(word) - 1:
            if word[i] == word[i + 1]:
                count += 1
                i += 2
                i += 1
        
        results.append(count)
    
    return results