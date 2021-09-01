def groupAnagrams(words):
    anagrams = dict()

    for i in range(len(words)):
        sortedWords = "".join(sorted(words[i]))
        

        # If sorted word in anagram append to it 
        if sortedWords in anagrams:
           anagrams[sortedWords].append(words[i])
          
        else:
            anagrams[sortedWords] = [words[i]]
    return list(anagrams.values())
        

words = ["yo","act","flop","tac","foo","cat","oy","olfp"]
print(groupAnagrams(words))