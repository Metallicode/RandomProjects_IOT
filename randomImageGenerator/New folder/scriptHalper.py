import csv

with open("xest.txt") as f:
      data = f.read()
      listOfWords = data.split('\n')
      ls = []
      ls.append(listOfWords)
      with open("xest.csv", 'w') as nf:
            writer = csv.writer(nf)
            writer.writerows(ls)





##with open('stopwords.csv', newline='') as f:
##      reader = csv.reader(f)
##      newLst = []
##      for row in reader:
##            for i in row:
##                  newLst.append(i.strip())
##      print(newLst)
##      listOfLists = []
##      listOfLists.append(newLst)
##      with open("stops.csv", 'w') as nf:
##            writer = csv.writer(nf)
##            writer.writerows(listOfLists)






###https://www.naxos.com/education/glossary.asp
##import re
##pattern = re.compile(r"<bdi>.+?</bdi>")
##
##
##with open("instrument2ToClean.txt", "r") as f:
##      data = f.read()
##
##      newList = []
##      
##      #preform search in text
##      matches = pattern.findall(data)
##      for i in range(len(matches)):
##            if i%2 == 0:
##                  print(matches[i][5:-6].strip())
##                  newList.append(matches[i][5:-6].strip())
##      with open("instrument.csv", 'w') as nf:
##            writer = csv.writer(nf)
##            lis = []
##            lis.append(newList)
##            writer.writerows(lis)


###https://www.imit.org.uk/pages/a-to-z-of-musical-instrument.html
##import re
##pattern = re.compile(r"<td>.+?</td>")
##innerPattern = re.compile(r"<a.+?</a>")
##innerPattern2 = re.compile(r"\(.+?\)")
##with open("instrumentsToClean.txt", "r") as f:
##      data = f.read()
##
##      newList = []
##      
##      #preform search in text
##      matches = pattern.findall(data)
##      for i in range(len(matches)):
##            st = matches[i][4:-5].strip()
##            if st != "&nbsp;" and not innerPattern.match(st) and not innerPattern2.match(st):
##                  lw = innerPattern2.split(st)
##                  newList.append(lw[0].strip())
##                  
####      for i in newList:
####            print(i)
##
##
##      with open("instrument2.csv", 'w') as nf:
##            writer = csv.writer(nf)
##            lis = []
##            lis.append(newList)
##            writer.writerows(lis)


list1 = []
list2 = []


with open('instrument.csv', newline='') as f:
      reader = csv.reader(f)
      for row in reader:
            for i in row:
                  list1.append(i.strip())

      
with open('instrument2.csv', newline='') as f:
      reader = csv.reader(f)
      for row in reader:
            for i in row:
                  list2.append(i.strip())


se = set(list1 + list2)
newList= list(se)
newList.sort()

##for i in newList:
##      print(i)
##
##with open("xest.txt", "w") as ww:
##      for i in newList:
##            ww.write(i+"\n")










