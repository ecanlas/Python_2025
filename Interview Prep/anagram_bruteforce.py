#Anagrams are words that share the same exact amount of each character in a string
#An example is bat = tab, bata = atab

def is_anagram(str1, str2):
    countString1, countString2 = {}, {}

    if len(str1) != len(str2):
        return False

    for i in range(len(str1)):
        countString1[str1[i]] = 1 + countString1.get(str1[i],0)
        countString2[str2[i]] = 1 + countString2.get(str2[i],0)

    return countString1 == countString2

#call is_anagram
is_anagram("bata","taba")

