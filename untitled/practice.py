__author__ = 'Noventa'
import re

try:
    fh = open('test.txt')
except IOError as e:
    print("can't open dis file: ", e)
else:
    print("maybe yes?")
    for line in fh:
        print(line.strip())






aString = 'Come and show me another city with lifted head singing so proud to be alive and coarse and strong and cunning...proud to be Hog Butcher, Tool Maker, Stacker of Wheat, Player with Railroads and Freight Handler to the Nation.'
def howManyAnds(sentString):
    count = 0
    ''' Still need to go back to RE, and figure out it's methods
    a_new = 'and'
    pattern = re.compile(a_new, re.IGNORECASE)
    for line in sentString:
        if re.search(pattern, line):
            count += 1
            print(count)
    count = 0
    '''
    while sentString.find("and") != -1:
        count = count + 1
        sentString = sentString[sentString.find("and") + 1:]
        print (count)

howManyAnds(aString)

'''bit wise operators and a formating def '''
def b(n): print('{:08b}'.format(n))
b(5)
x, y = 0x55, 0xaa
b(x)
b(y)
b(x | y)
b(x ^ y)
b(x & y)
b(x ^ 0)
b(x ^ 0xfff)
b(x << 4)
b(x >> 4)
b(~x)


''' one checks for value equality, the other to see if it is the same object'''
print(x is y)
print(x is not y)
print(x == y)
print(x != y)

''' you can use the is operator to see if things are the same type '''
choices = dict(
    one = 'first',
    two = 'second',
    three = 'third',
    four = 'fourth'
)
v =  'first'
print(choices.get(v, 'other'))
a, b = 1, 0
vee = 'this is true' if a < b else 'this is not true'
print(vee)



danton = "De l'audace, encore de l'audace, toujours de l'audace."

print(danton.find('audace', 25))
print(danton.find('audace', 26))

recruit_1 = 70000
recruit_2 = 70000
recruit_you = 80000


''' Each placed recruit gives the agent (recruiter) about 20-30% of profit'''
profit_1 = recruit_1 * 0.20 + recruit_2 * 0.20
profit_2 = recruit_you * 0.30
if profit_1 > profit_2:
    print(profit_1)
    print(profit_2)
else:
    print(profit_2)


''' play with dictionaries '''
d = dict(
    one = 1, two = 2, three = 3, four = 4, five = 'five'
)
for k in sorted(d.keys()):
    print(k, d[k])

print(d)

