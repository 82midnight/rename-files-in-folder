import os
import shutil

Source = r'I:\Music\File'                 #Source directory to scan and remove characters
DEST = r'I:\Music\DUPLICATE'         #Destination directory if there are duplicates of files after rename

os.chdir(Source)
#print(os.getcwd())

def CheckInt1(name):                              #Function checks if second digit triggers Numbers
  Numbers=["(",")","_"," ","+","-",".","[",",","#"]   #list of Characters/symbols to remove
  for i in Numbers:
    if i == name[0]:
      return "true"

def Delete_first_CHR(trig1,name):                 #Function deletes first digit/char if conditions are met
 if trig1=="true":
    return name[1:]
 else:
    return name

#Main Program
for f in os.listdir():
   filename, filetype = os.path.splitext(f)       #print (filename , filetype)
   StrFile=str(filename)
   Check1 = CheckInt1(StrFile)
   CheckFile ='{}{}'.format(StrFile[1:],filetype)
   if os.path.exists(CheckFile):                     #If there are duplicates file moved to DEST Directory
       shutil.move(Source+r'\\'+StrFile+filetype,DEST)
   else:
     F_name = Delete_first_CHR(Check1,StrFile)
     NewFile ='{}{}'.format(F_name,filetype)
     print(NewFile)
     os.rename(f, NewFile)                         #comment until you are sure this program behaves correctly!