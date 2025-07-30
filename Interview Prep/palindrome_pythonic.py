#palindrome is a string that has the same value after you reverse it
#we can take advantage of our old reverse string method in the bruteforce way

#Clean the string of unwanted characters and make sure to lower the case
#Reverse the clean string
#Compare cleaned string against the reversed string
#use Pythonic Reverse

def is_palindrome(string):
    clean_str = ""
    for c in string:
        if c.isalnum():
            clean_str += c.lower()
    return clean_str == clean_str[::-1]
