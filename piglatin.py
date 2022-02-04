def main():
    list= ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p','q','r','s','t','u','v','w','x','y','z']
    sentence = input("Enter a sentence: ")
    sentence= sentence.split()
    for m in range (len(sentence)):
        i = sentence[m]
        if t(i) in list:
            sentence[m]= i[2: ] + i[ :2] + "ay"
        elif i.isalpha() == False:
            sentence[m]= i
        else:
            sentence[m]= i[1: ]+ i[0]+ "ay"
    return ''.join(sentence)


def t(str):
    return str[0] + str[1]

if __name__ == "__main__":
    x = main()
    print(x)