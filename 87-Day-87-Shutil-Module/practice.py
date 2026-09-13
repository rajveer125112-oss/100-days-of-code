import shutil
import os
shutil.copy("test.txt","Nice.txt")
shutil.copy2("test.txt","Amazing.txt")

#shutil.copytree(".tutorial","MyTutorial")
#shutil.rmtree("MyTutorial")
#shutil.move(".tutorial/Tutorial.md","Tutorial.md")
os.remove("Tutorial.md")