import webbrowser
from random import randint

###setup variables
instruments = []
instrumentsLen = 0

music = []
musicLen = 0

adj = []
adjLen = 0

stops = []
stopsLen = 0

###open all the files and translate to python lists
with open('instruments.csv', newline='') as f:
      data = f.read()
      instruments = data.split(',')
      instrumentsLen = len(instruments)-1

with open('music.csv', newline='') as f:
      data = f.read()
      music = data.split(',')
      musicLen = len(music)-1
      
with open('adjective.csv', newline='') as f:
      data = f.read()
      adj = data.split(',')
      adjLen = len(adj)-1

with open('stops.csv', newline='') as f:
      data = f.read()
      stops = data.split(',')
      stopsLen = len(stops)-1


###random image descriptor will be:
###{ADJECTIVE}+{INST} {STOP} {ADJECTIVE}+{MUSIC}

###set variables
ADJECTIVE_A = adj[randint(0, adjLen)]
ADJECTIVE_B = adj[randint(0, adjLen)]
INST = instruments[randint(0, instrumentsLen)]
INST2 = instruments[randint(0, instrumentsLen)]
MUSIC = music[randint(0, musicLen)]
MUSIC2 = music[randint(0, musicLen)]
STOP = stops[randint(0, stopsLen)]

###create search phrases
phraseToSearchSound = f"{ADJECTIVE_A} {INST} {MUSIC}    and    {ADJECTIVE_B} {INST2} {MUSIC2}"
phraseToSearchSoundShort =  f"{ADJECTIVE_A} {INST} {MUSIC}"
phraseToSearchSoundShort2 =  f"{ADJECTIVE_B} {INST2} {MUSIC2}"

###append phrase to file
print(phraseToSearchSound, file=open('searchPhrases.txt', 'a'))
print(phraseToSearchSoundShort)
print(phraseToSearchSoundShort2)


###create urls
youtube_url = "https://www.youtube.com/results?search_query=" +(phraseToSearchSoundShort)
sound_url = "https://freesound.org/search/?q=" +(phraseToSearchSoundShort)
video_url = "https://www.google.com/search?tbm=vid&q=" +(phraseToSearchSoundShort)



###cale pages
webbrowser.open_new(youtube_url)
webbrowser.open_new(video_url)
##webbrowser.open_new(sound_url)
