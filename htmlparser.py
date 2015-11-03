from BeautifulSoup import BeautifulSoup
import os

class HtmlParser:
    def __init__(self, letters):
        self.urlList = []
        self.letters = letters

    '''
    Check if script list is cached, else scrape for it
    '''
    def getScriptLinks(self):
        if self.urlList:
            return self.urlList
        else:
            print "Scraping for script links..."
            self.scrapeForScriptLinks()
            return self.urlList

    def scrapeForScriptLinks(self):
        alphaFileList = ["alphabetical" + char + ".txt" for char in self.letters]
        for alpha in alphaFileList:
            with open("data/raw/temp/" + alpha, 'r') as f:
                soup = BeautifulSoup(f.read())
                print "Getting all script urls in " + alpha
                for a in soup.findAll('a', href=True):
                    if "Movie Script" in a['href']:
                        #Remove first '/' for formatting reasons
                        temp = a['href'][1:].replace("Movie Scripts", "scripts")
                        temp = temp.replace(" Script", "")
                        temp = temp.replace(":", "")

                        self.urlList.append(temp)
    '''
    This function takes in the script data and parses it into target/source pairs
    '''
    def scrapeForSourceTargetPairs(self, scriptDirectory, dataDirectory):
        fileList = os.listdir(scriptDirectory)
        for f in fileList:
            with open(scriptDirectory + f, 'r') as doc:
                tempSoup = BeautifulSoup(doc.read()).findAll('pre')[0]
                soup = BeautifulSoup(tempSoup.getText())
                for tag in soup.findAll(True):
                    if tag == 'b':
                        tag.replaceWith('\n')
                with open(dataDirectory + f, 'w') as pre:
                    pre.write(soup.getText().encode('ascii', 'ignore'))
