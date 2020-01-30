import os
import shutil

Source = r'I:\Music\File'               #Source directory to extract string
os.chdir(Source)
                                               #Directory folder not required for duplicate names on win7

def CapFirstLetter(name):                      #Function to capitalize first letter
  Capname= name[0].upper() + name[1:]
  return Capname


for f in os.listdir():                         #Main Program
   filename, filetype = os.path.splitext(f)
   StrFile=str(filename)
   Cap_name = CapFirstLetter(StrFile)
   CapFile ='{}{}'.format(Cap_name,filetype)
   print(CapFile)
   os.rename(f, CapFile)                       #Comment until you are sure this program behaves correctly!