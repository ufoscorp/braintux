import re
import requests
class Youtube:
    def __init__(self):
        self.findYtLink=r'"\/watch\?v=.{11}" class="y"'
        self.findVideoName=r'"title=".+rel="spf-prefetch""'
    def removeDuplicate(self, duplicate):
        final_list = [] 
        for item in duplicate: 
            if item not in final_list: 
                final_list.append(item) 
        return final_list 
    def search(self, term):
        self.resultsSite = requests.get("https://www.youtube.com/results?search_query={}&sp=EgIQAQ%253D%253D".format(term))
        self.links=re.findall(r'watch\?v=.{11}', self.resultsSite.text)
        self.links = Youtube.removeDuplicate(self, self.links)
        self.dirtyVideoNames=re.findall('title=".+rel="spf', self.resultsSite.text)
        self.videoNames=[]
        for name in self.dirtyVideoNames:
            name = name.replace("title=\"", '')
            name = name.replace('" rel="spf', '')
            self.videoNames.append(name)
        resultsDict=dict(zip(self.videoNames, self.links))
        return resultsDict