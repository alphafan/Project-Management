import glob

files = glob.glob("./images/*")
files.sort()

file = open('slides/README.md','w') 
 
for name in files:
    file.write('<img src=".'+name+'"/>\n')

file.close() 
