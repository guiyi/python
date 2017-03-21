# -*- coding: utf-8 -*-  
# Filename: using_file.py
# Author : Adair@http://www.kuqin.com/
poem = u'''\
编程很开心
当你工作完成了
如果你仍然想找点乐子
用python！

Programming is fun
When the work is done
if you wanna make your work also fun:
        use Python!
'''

f = file('poem.txt', 'w') # open for 'w'riting
f.write(poem) # write text to file
f.write(poem) # write text to file
f.close() # close the file

f = file('poem.txt','r')
# if no mode is specified, 'r'ead mode is assumed by default
while True:
    line = f.readline()
    if len(line) == 0: # Zero length indicates EOF
        break
    print line,
    # Notice comma to avoid automatic newline added by Python
f.close() # close the file
