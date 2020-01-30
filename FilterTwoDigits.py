import os
import shutil

Source = r'I:\music'                 #Source directory to scan and remove characters
DEST = r'I:\music\DUPLICATE'         #Destination directory if there are duplicates of files after rename

os.chdir(Source)
print(os.getcwd())
Numbers=["0","1","2","3","4","5","6","7","8","9","(",")","_"," ","+","-",".","[",",","%"] #Numbers or characters to filter

def CheckInt1(name):      #checks if first digit triggers Numbers
    global Numbers
    for i in Numbers:
      if i == name[0]:
        Trig1="true"
        return Trig1

def CheckInt2(name):       #checks if second digit triggers Numbers
    global Numbers
    for i in Numbers:
      if i == name[1]:
        Trig2="true"
        return Trig2

def Delete_firsttwo_NUM(trig1,trig2,name): #deletes first two digits if conditions are met
 if trig1=="true" and trig2=="true":
    NewFile = name[2:]
    return NewFile
 else:
    return name


for f in os.listdir():
   filename, filetype = os.path.splitext(f)   #print (filename , filetype)
   StrFile=str(filename)                      #print(StrFile)
   Check1 = CheckInt1(StrFile)
   Check2 = CheckInt2(StrFile)
   CheckFile ='{}{}'.format(StrFile[2:],filetype)
   if os.path.exists(CheckFile):                     #If there are duplicates file moved to DEST Directory
       shutil.move(Source+r'\\'+StrFile+filetype,DEST)
   else:
     F_name = Delete_firsttwo_NUM(Check1,Check2,StrFile)
     NewFile ='{}{}'.format(F_name,filetype)
     print(NewFile)
     os.rename(f, NewFile) #comment until you are sure this program behaves correctly!