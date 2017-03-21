# -*- coding: utf-8 -*-  
# Filename : helloworld.py
# Author : Adair@http://www.kuqin.com/

number = 23
while True:
    s = raw_input(u'请输入number0：')
    print s,number
    if s == 'quit':
        break
    if int(s) == int(number):
	    print u'恭喜你, 猜对了.' # New block starts here
	    print u"(但是没有任何奖品！)" # New block ends here
    elif int(s) < int(number):
            print u'小于'
    else:
	    print u'大于'
    print 'Length of the string is', len(s)
print 'Done'


# if else
number = 23
guess = int(raw_input(u'请输入number1：'))

if guess == number:
    print u'恭喜你, 猜对了.' # New block starts here
    print u"(但是没有任何奖品！)" # New block ends here
elif guess < number:
    print u'小于' # Another block
    # You can do whatever you want in a block ...
else:
    print u'大于'
    # you must have guess > number to reach here

print u'结束'


# while
number = 23
running = True
flag = 0

while flag < 2:
#while running:
	guess = int(raw_input(u'请输入number2：'))
        if guess == 1000:
            break
	flag = flag + 1

	if guess == number:
	    print u'恭喜你, 猜对了.' # New block starts here
	    print u"(但是没有任何奖品！)" # New block ends here
	elif guess < number:
	    print u'小于' # Another block
	    # You can do whatever you want in a block ...
	else:
	    print u'大于'
	    # you must have guess > number to reach here
else:
    print u'循环结束.'


print u'结束'


# for
def sayLoop(start,end):
    for i in range(start,end):
        print i
        i = 666
        print 'Changed local x to',i
    else:
        print 'The for loop is over'

sayLoop(1,10)
