__author__='Mohnish Mallya'
# Importing all necessary libraries
from bs4 import BeautifulSoup
from selenium import webdriver
import codecs

# Importing sentiment analysis code
import tweetSentiAnalysis

# Web scraping function
def imdbWebScraping():
    celebName = []
    celebKeyValue = {}
    counter = 0

    #URL to extract information
    BASE_URL = "http://m.imdb.com/feature/bornondate"
    
	#Content of the page is dynamic. Using selenium web driver to get celebrity info
    driver = webdriver.Firefox()
    driver.get(BASE_URL)

    html = driver.page_source

	# Using html5lib module to parse the html file
    soup = BeautifulSoup(html, "html5lib")
    mainInfo = soup.find("div", "lister-list")

    celebrityNameList = []

    # Getting all the specific celebrity details
    for i in mainInfo.findAll("div", "lister-item mode-detail"):

        celebKeyValue[counter] = {}
        # Celebrity Name
        celebrityName = i.find("h3").find("a").text
        celebrityNameList.append(celebrityName)
        celebKeyValue[counter]["celebrityName"] = celebrityName

        # Celebrity image link
        celebKeyValue[counter]["celebrityImg"] = i.img["src"]

        # Parsing Profession and the Best Movie
        profession = i.find("p", "text-muted text-small").text.strip().split(" ")[0]
        bestMovie = i.find("p").find("a").text

        # Profession
        celebKeyValue[counter]["profession"] = profession

        # Best Movie
        celebKeyValue[counter]["bestMovie"] = bestMovie

        counter += 1
    return celebName, celebKeyValue

#Magic
#Performing sentiment analysis and writing all the celebrity info to a file named 'Celebrity List'
if __name__ == '__main__':

    celebName, celebKeyValue = imdbWebScraping()
    celebrity = tweetSentiAnalysis.twitterSentimentAnalysis()
    outputFile = codecs.open("Celebrity List.txt", 'w', "utf-8")

    for i in range(10):

        celebrityName = celebKeyValue[i]["celebrityName"]
        celebrity.tweetSearch(celebrityName)

        celebKeyValue[i]["tSentiment"] = celebrity.tweetSentimentAnalysis()

        outputFile.write("Name of the celebrity: " + celebKeyValue[i]["celebrityName"] + "\n")
        print ("Name of the celebrity: " + celebKeyValue[i]["celebrityName"] + "\n")
        outputFile.write("Celebrity Image: " + celebKeyValue[i]["celebrityImg"] + "\n")
        print ("Celebrity Image: " + celebKeyValue[i]["celebrityImg"] + "\n")
        outputFile.write("Profession: " + celebKeyValue[i]["profession"] + "\n")
        print ("Profession: " + celebKeyValue[i]["profession"] + "\n")
        outputFile.write("Best Work: " + celebKeyValue[i]["bestMovie"] + "\n")
        print ("Best Work: " + celebKeyValue[i]["bestMovie"] + "\n")
        outputFile.write("Overall Sentiment on Twitter: " + celebKeyValue[i]["tSentiment"] + "\n")
        print ("Overall Sentiment on Twitter: " + celebKeyValue[i]["tSentiment"] + "\n")
        outputFile.write("*********************************************************************************")
        print ("*********************************************************************************")
        outputFile.write("\n\n")
        print ("\n\n")
    outputFile.close()
