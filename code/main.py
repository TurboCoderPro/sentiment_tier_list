data = open("../data/twitter_training.csv", "r")

#Global variables:
allSentiments = {}
unread = 0

#input: a line containing traning data
#description: example: 2401,Borderlands,Positive,"im getting on borderlands and i will murder you all ,"
#return: a dictionary with two keys. {"entity": , "sentiment": }
def createDataEntry(unprocessedData):
    readableData = unprocessedData.split(",")
    entry = {"entity" : readableData[1], "sentiment" : readableData[2]}
    return entry

def updateSentimentScore(entity, sentiment):
    score = 0
    #upprättade fall för varje scenario, lättare att manipulera hantering då.
    if (sentiment == "Positive"):
        score = 1
    elif (sentiment == "Negative"):
        score = -1
    elif (sentiment == "Neutral"):
        pass
    ##probably irrelevant, or poorly formatted
    else:
        """ print(sentiment)
        global unread 
        unread += 1
        print("could not read sentiment. total unread: {}".format(unread))
        return """

    #if entity exists
    try:
        allSentiments[entity]["score"] += score
        allSentiments[entity]["amountOfDataEntries"] += 1
    
    #if entity does not exist, create and set first values.
    except:
        entityData = {"score": score,"amountOfDataEntries": 1}
        allSentiments[entity] = entityData

#print(data.readline())

for line in data:
    dataEntry = createDataEntry(line)

    entity = dataEntry["entity"]
    sentiment = dataEntry["sentiment"]

    updateSentimentScore(entity, sentiment)

    currentScore = allSentiments[entity]["score"] / allSentiments[entity]["amountOfDataEntries"]

    #print("Current score for {} is {}".format(entity, currentScore))

#print table when done

for entity, data in allSentiments.items():
    pass
    print("{} was rated {}, with {} sentiments analyzed".format(entity, data["score"], data["amountOfDataEntries"]))
    print("resulting in a score of: {}".format(data["score"]/data["amountOfDataEntries"]))


