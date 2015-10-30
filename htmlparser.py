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
