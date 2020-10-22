def openfile(filename):
    ''' This function accepts a filename and tries to open it, returns error if it can't '''
    try:
        obj = open(filename)
        return obj
    except FileNotFoundError:
        print("Documents not found.")
        return


def createwordlist(fileobj):
    ''' This function creates a list of strings where each string is a document '''
    doclist = []
    substring = ""
    for line in fileobj:
        if line == "<NEW DOCUMENT>\n":
            doclist.append(substring)
            substring = ""
        else:
            substring += line
    doclist.append(substring)
    return doclist


def searchdocs(docudict,searchkey):
    ''' This function searches the document for a specific search key '''
    foundin = []
    keylist = searchkey.split(" ")
    if len(keylist) > 1:
        for key in keylist:
            if key in docudict:
                foundin.append(docudict[key])
            else:
                return
        founddocs = list(set.intersection(*foundin))
        foundints = [int(i) for i in founddocs]
        foundints.sort()
        return foundints
    else:
        try:
            founddocs = list(docudict[searchkey])
            foundints = [int(i) for i in founddocs]
            foundints.sort()
            return foundints
        except KeyError:
            return


def printdoc(doculist,docnumber):
    ''' This function prints the document selected by the user '''
    try:
       str(doculist[int(docnumber)])
    except IndexError:
        print("No match.")
        return
    except ValueError:
        print("Please input a number.")
        return
    print("Document #{}".format(docnumber))
    print(doculist[int(docnumber)])


def generatedictionary(wordlist):
    ''' This function generates a dictionary of each word with its value as a set of its occurences '''
    worddict = {}
    for i in range(len(wordlist)):
        for word in wordlist[i].lower().split():
            if word.strip(",.!? ") not in worddict:
                worddict[word.strip(",.!? ")] = set(str(i))
            else:
                worddict[word.strip(",.!? ")].add(str(i))
    return worddict


def menu(documentlist,worddict):
    ''' This function prints the menu and handles user input '''
    choice = "1"
    while choice == "1" or choice == "2":
        print()
        print("What would you like to do?")
        print("1. Search Documents")
        print("2. Print Document")
        print("3. Quit Program")
        choice = input("> ")
        if choice == "1":
            searchkey = input("Enter search words: ").lower()
            foundinlist = searchdocs(worddict,searchkey)
            if foundinlist == None or foundinlist == []:
                print("No match.")
            else:
                print("Documents that fit search:",*foundinlist)
        elif choice == "2":
            documenttoprint =input("Enter document number: ")
            printdoc(documentlist,documenttoprint)
    return


def main():
    ''' This is the main function of the program '''
    filename = input("Document collection: ")
    fileobj = openfile(filename)
    if fileobj == None:
        return
    documentlist = createwordlist(fileobj)
    worddict = generatedictionary(documentlist)
    menu(documentlist,worddict)
    print("Exiting program.")
main()