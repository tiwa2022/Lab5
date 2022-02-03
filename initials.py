#My initials
def printInitials(name):

    if(len(name) == 0):
        return

    word = name.split(" ")
    for word in word:
        print(word[0].upper(),  end = " ")

if __name__ == '__main__':
    name = "Tiwalade F Olobayo"
    printInitials(name)

