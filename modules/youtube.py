import os, re, sys, subprocess
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
        YouTube(link).streams.first().download('videos')


    def search(self, term):
        resultsSite = requests.get("https://www.youtube.com/results?search_query={}&sp=EgIQAQ%253D%253D".format(term))
        self.links=re.findall(r'watch\?v=.{11}', resultsSite.text)
        self.links = self.removeDuplicate(self.links)
        dirtyVideoNames=re.findall('title=".+rel="spf', resultsSite.text)
        self.videoNames=[]

        for name in dirtyVideoNames:
            name = name.replace("title=\"", '')
            name = name.replace('" rel="spf', '')
            if  'describe' in name:
                name = name[:-41]

            self.videoNames.append(name)
        self.resultsDict=dict(zip(self.videoNames, self.links))

def sendText(content):
    subprocess.Popen("python3 {}/braintux-core.py sendtext {}".format(os.getcwd(), str(content)), shell=True)

def sendFile(content):
    subprocess.Popen("python3 {}/braintux-core.py sendfile {}".format(os.getcwd(), str(content)), shell=True)

Youtube = Youtube()

if sys.argv[1] == "search":

    term = str(sys.argv[2])
    Youtube.search(term)
    sendText("Results:")

    results = '\n'.join(map(str, Youtube.videoNames))

    sendText(results)
    sendText("To download a video: youtube download {} <number>".format(term))

elif sys.argv[1] == 'download':


    term = str(sys.argv[2])
    choice = sys.argv[3]
    Youtube.search(term)

    results = '\n'.join(map(str, Youtube.videoNames))

    link='www.youtube.com/'+list(Youtube.resultsDict.values())[choice]
    sendText('Downloading the video: '+link)
    Youtube.download(link)

    files = os.listdir('videos')

    for index in range(len(files)):
        files[index] = 'videos/' + files[index]

    files.sort(key=os.path.getmtime)
    ourvideo = files[-1]

    sendFile(ourvideo)