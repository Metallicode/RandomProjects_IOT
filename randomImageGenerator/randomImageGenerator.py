import webbrowser 
from random import randint

###setup variables
things = []
thingsLen = 0

adj = []
adjLen = 0

stops = []
stopsLen = 0

###open all the files and translate to python lists
with open('things.csv', newline='') as f:
      data = f.read()
      things = data.split(',')
      thingsLen = len(things)-1
      
with open('adjective.csv', newline='') as f:
      data = f.read()
      adj = data.split(',')
      adjLen = len(adj)-1

with open('stops.csv', newline='') as f:
      data = f.read()
      stops = data.split(',')
      stopsLen = len(stops)-1


###random image descriptor will be:
###{ADJECTIVE}+{THING} {STOP} {ADJECTIVE}+{THING}

###set variables
ADJECTIVE_A = adj[randint(0, adjLen)]
ADJECTIVE_B = adj[randint(0, adjLen)]
THING_A = things[randint(0, thingsLen)]
THING_B = things[randint(0, thingsLen)]
STOP = stops[randint(0, stopsLen)]

###create search phrases
phraseToSearchImage = f"{ADJECTIVE_A} {THING_A} {STOP} {ADJECTIVE_B} {THING_B}"
phraseToSearchSound = f"{ADJECTIVE_A} {THING_B}"

###append phrase to file
print(phraseToSearchImage, file=open('searchPhrases.txt', 'a'))

###create urls
image_url = "https://www.youtube.com/results?search_query=" +(phraseToSearchSound)
##image_url = "https://www.google.com/search?tbm=isch&q=" +(phraseToSearchImage)
##sound_url = "https://freesound.org/search/?q=" +(phraseToSearchSound)

###cale pages
webbrowser.open_new(image_url)
webbrowser.open_new(sound_url)
