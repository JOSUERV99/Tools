import wikipedia, os

def searchSomething(query, sentencesPerResult=5):

    def getDataFromResult(key):
        return wikipedia.summary(key, redirect=True)

    def showOptions(results):
        for i, res in enumerate(results):
            print(i+1, ': ', res)

    def selectTopic(results):
        selection = 0
        while (selection not in range(1,len(results)+1) ):
            try:
                showOptions(results)
                selection = int(input('Selection: '))
            except ValueError:
                pass
            finally:
                os.system('cls')
        return selection

    results = wikipedia.search(query)
    if (len(results) > 0):
        selection = selectTopic(results)
        key = results[selection-1]
        data = getDataFromResult(key)
        print(f'{key} :\n {data} \n\nFrom: https://en.wikipedia.org/wiki/{key.replace(" ", "_")}')
    else:
        print("No results founded")

try:
    searchSomething(input('Wikipedia Search: '))
except KeyboardInterrupt as e:
    os.system('cls')
    exit()