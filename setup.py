from distutils.core import setup
import py2exe
import sys
if len(sys.argv) == 1:
    sys.argv.append("py2exe")
setup( options = {"py2exe": {"includes": ["tkinter"]}},
       console=["webcrawler.py"])


#Hello guyz this video is gonna show u how to create an exe using py2exe for tkinter program
#i will just explain few points u have to change in this source code

#1.change webcrawler to your program name
#thats all guyz now  to run this save this program with a name i have setup.py and keep it in the same place as ur program
#now open command prompt
#now go to the location where ur program  is i have it inside python34 so i will change my directory to that
#now write your python location
#after that ur setup file name
#i don't know why its showing error in mine but it should nt be the case inn urs
#so if u get error than put your main program and setup inside folder where ur python is
#so after doing that

#now it is done so go check inside your python folder where u placed your setup file and check for folder named dist

#inside that u will find your program exe

#so thats all for this video thank u guyz
#if u want me to make any other kind of helping video please mention in the comment below and i will do it for u

#Programming has huge community so there is nothing that you can't learn never hesitate to ask any1 every1 will help u
#thanks enjoy programming
