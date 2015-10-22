'''
This python script downloads all the moview scripts on www.imsdb.com
'''
import os
from htmlparser import *
import time
import socket
import urllib

imsdbUrl = "http://www.imsdb.com/"
alphabetical = "alphabetical/"
script = "scripts/"
endingExt = ".html"

class Downloader:
    def __init__(self):
        self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.scriptList = []

    def setDownloadPath(self):
        root = ["data"]
        root.append(root[0] + "/test")
        root.append(root[0] + "/train")
        root.append(root[0] + "/val")
        root.append("temp")
        for path in root:
            if not os.path.exists(path):
                print "Creating " + path + " folder..."
                os.makedirs(path)

    def getScriptList(self):
        return self.scriptList

    def download(self):
        print "Checking if folder structure exists, else creating it..."
        self.setDownloadPath()
        self.checkDownload()

    '''
    checkDownload() will smartly check the temp folder to see if it needs to download all raw html files.
    It accomplishes this doing 2 things:
        1. Checking if the file exists
        2. Checking that the modification date of the file is < 7 days old
    '''
    def checkDownload(self):
        #First check that alphabetical files lists raw html is downloaded
        fileList = os.listdir("temp")
        secondsInDay = 86400
        nowDays = time.time() / secondsInDay
        for f in fileList:
            #if 7 or more days old redownload!
            if ((nowDays - os.path.getmtime("temp/" + f)) / secondsInDay) < 7:
                self.letters = self.letters.replace(f.strip('.txt').replace("alphabetical", ''), '')
        print "Need to download " + str(len(self.letters)) + " files"

        #download list of new movie scripts here.
        success = self.retreiveRawHtml([alphabetical + char for char in self.letters])
        if not success:
            print "Something went wrong with download, possibly network or sever related" \
            " try again later."
            return 0
        try:
            with open('temp/scriptlist.txt', 'w+') as fi:
                print "Checking which scripts you already have..."
                parser = HtmlParser(self.letters)
                self.scriptlist = parser.getScriptLinks()
                for line in fi:
                    if line in self.scriptlist:
                        print "Already have " + line + " don't need to download..."
                        links.remove(line)
                print "Downloading scripts now..."
                success = self.retreiveRawHtml(self.scriptlist)
                if success:
                    print "Successfully downloaded all new scripts"
                else:
                    print "Something went wrong with download, possibly network or sever related" \
                    " try again later."
                [fi.write(link + "\n") for link in self.scriptlist]
                print "All scripts have been parsed, now creating training sets..."
                pass
        except IOError as e:
            print "Unable to open file temp file scriptlist.txt" + str(e)

    '''
    Takes a list of urls to download the raw html of.
    returns 0 or 1 indicating sucessful download or not
    '''
    def retreiveRawHtml(self, urls):
        socket.setdefaulttimeout(5)
        print (len(urls) and 1)*"Downloading raw html to parse!"
        for url in urls:
            timeoutCount = 0
            quitTrying = False
            while timeoutCount < 5:
                try:
                    urllib.urlretrieve(imsdbUrl + url, "temp/" + url.replace('/', '').strip(".html") + ".txt")
                    print "Successfully downloaded " + imsdbUrl + url
                    break
                except KeyboardInterrupt:
                    print "Download stopped by user..."
                    return 0;
                except:
                    timeoutCount += 1
                    if timeoutCount <= 4:
                        print "Timed out, attempting download again..."
                    else:
                        print "Either network or server error, try again later..."
                        return 0
        return 1
