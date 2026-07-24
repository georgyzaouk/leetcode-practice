
def groupAnagrams(strs):
    anagrams = {}

    for word in strs:
        sorted_word = "".join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]

    return list(anagrams.values())


if __name__ == "__main__":

    # test case 1
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(groupAnagrams(strs))  # Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    # test case 2
    strs = [""]
    print(groupAnagrams(strs))  # Output: [['']]

    # test case 3
    strs = ["a"]
    print(groupAnagrams(strs))  # Output: [['a']]

