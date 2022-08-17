data = open("../data/twitter_training.csv", "r")

#Global variables:
allSentiments = {}

#input: a line containing traning data
#description: example: 2401,Borderlands,Positive,"im getting on borderlands and i will murder you all ,"
#return: a dictionary with two keys. {"entity": , "sentiment": }
def createDataEntry(unprocessedData):
    readableData = unprocessedData.split(",")
    entry = {"entity" : readableData[1], "sentiment" : readableData[2]}
    return entry

def updateSentimentScore(entity, sentiment):
    score = 0
    if (sentiment == "positive"):
        score = 1
    elif (sentiment == "negative"):
        score = -1
    else:
        print("could not read sentiment")

    allSentiments[entity]["score"] += score
    allSentiments[entity]["amountOfDataEntries"] += 1


#print(data.readline())

for line in data:
    dataEntry = createDataEntry(line)

    entity = dataEntry["entity"]
    sentiment = dataEntry["sentiment"]

    updateSentimentScore(entity, sentiment)

    currentScore = allSentiments[entity]["score"] / allSentiments[entity]["amountOfDataEntries"]

    print("Current score for ${entity} is {currentScore}")


    


