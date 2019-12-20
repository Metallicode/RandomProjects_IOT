from pydub import AudioSegment
from pydub.playback import play
from threading import Thread
from random import randint

print_bool = False

def job(word):
      global print_bool
      counter = 0
      while print_bool == True:
            counter = counter+1
            if counter>40:
                  counter = 0
            w = (word + (" "*counter))*randint(0,len(word))
            print(w[:200])
##            new_str = ""
##            for i in range(10):
##                  new_str += f"  {word[randint(0,len(word)-1)]}  {word}"
##            print(new_str)
            


words = []

with open("words.txt", "r", encoding="utf-8") as file:
      for line in file.read().splitlines() :
            words.append(line)



for i in range(0,5):
      for j in range(1, 32):
            sound = AudioSegment.from_wav(f"out{j}.wav")
            print_bool = True
            t = Thread(target=job, args=(words[j-1],))
            t.start()
            play(sound)
            print_bool = False
            t.join()


