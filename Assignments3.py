from operator import itemgetter
#list_oftuples.sort(key=itemgetter(1,0))

def getbigrams(wordlist):
    bigramdict = {}
    for i in range(len(wordlist) -1):
        bigram = (wordlist[i], wordlist[i+1])
        if bigram not in bigramdict:
            bigramdict[bigram] = 1
        else:
            bigramdict[bigram] += 1
    return bigramdict

def createwordlist(fileobj):
    newlist = []
    for line in fileobj:
        for word in line.strip(",.!?\n").split():
            word2 = ''.join(filter(str.isalpha, word))
            newlist.append(word2.lower().strip('''!()-[]{};:'"\,<>./?@#$%^&*_~''').strip())
    return newlist

def sortdict(dicti):
    diclist = list(dicti.items())
    diclist.sort(key=itemgetter(0))
    diclist.sort(key=itemgetter(1),reverse=True)
    return list(diclist)

def main():
    filename = input("Enter name of file: ")
    try:
        file_obj = open(filename)
    except:
        return
    wordlist = createwordlist(file_obj)
    bigramdict = getbigrams(wordlist)
    sortedlist = sortdict(bigramdict)
    top10 = sortedlist[0:10]
    print(top10)

main()