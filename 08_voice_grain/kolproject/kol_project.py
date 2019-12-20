import wave
import random

bufferSizes = [904,955,307, 883,632,280,900,800,900,230,300]
stretch = 20

for i in range(1,32):
      newFile = wave.open(f"out{i}.wav", "wb")
      newFile.setnchannels(2)
      newFile.setsampwidth(2)
      newFile.setframerate(29000)
      newFile.setcomptype('NONE',"not compressed")

      with wave.open(f"data/{i}.wav", "rb") as file:
            data = file.readframes(1)
            rnd_buff_size = bufferSizes[random.randint(0, len(bufferSizes)-1)]*2
            for j in range(0, file.getnframes(), rnd_buff_size):
                  segment = file.readframes(rnd_buff_size)
                  for k in range(0,random.randint(0, stretch)):
                        data += segment

      newFile.setnframes(len(data))
      newFile.writeframes(data)
      newFile.close()



