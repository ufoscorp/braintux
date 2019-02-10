import re
import requests
from pytube import YouTube

class Youtube:

    def __init__(self):
        self.option = 0

    def removeDuplicate(self, duplicate):

        final_list = [] 
        for item in duplicate: 
            if item not in final_list: 
                final_list.append(item) 
        return final_list 

    def download(self, link):
        YouTube(link).streams.first().download()


    def search(self, term):
        resultsSite = requests.get("https://www.youtube.com/results?search_query={}&sp=EgIQAQ%253D%253D".format(term))
        self.links=re.findall(r'watch\?v=.{11}', resultsSite.text)
        self.links = self.removeDuplicate(self.links)
        dirtyVideoNames=re.findall('title=".+rel="spf', resultsSite.text)
        self.videoNames=[]
        for name in dirtyVideoNames:
            name = name.replace("title=\"", '')
            name = name.replace('" rel="spf', '')
            self.videoNames.append(name)
        self.resultsDict=dict(zip(self.videoNames, self.links))
        
    def download(self, link):
        pass
