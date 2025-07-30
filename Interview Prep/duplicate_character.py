#Function takes a string
#Return True if there is a duplicate character
#Return False if there is none

#Idea
#Create a container for the sorted string
def is_duplicate(str):

    container = set()
    for c in str:
        if c.isalnum():
            if c.lower() in container:
                return True
            else:
                container.add(c.lower())
    return False