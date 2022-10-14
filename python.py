#Operator precedence

# Operators     	Meaning
# ()	            Parentheses
# **	            Exponent
# +x, -x, ~x	    Unary plus, Unary minus, Bitwise NOT
# *, /, //, %	    Multiplication, Division, Floor division, Modulus
# +, -	            Addition, Subtraction
# <<, >>	        Bitwise shift operators
# &	                Bitwise AND
# ^	                Bitwise XOR
# |	                Bitwise OR
# ==, !=, >, >=, <, <=, is, is not, in, not in	Comparisons, Identity, Membership operators
# not	            Logical NOT
# and	            Logical AND
# or	            Logical OR


from icecream import ic
# using * and ** to pass arguments to a function
# l = [1,23,56,3,45]
# ic(*l)
# l1 = [*l,0,88]
# ic(*l1)
# first,second,*remaining = l
# # ** in dictionary 
# date = {'year':2020,'month':1,'day':1}
# track = {'artist':'beckham','title':'symphony'}
# all_info={**date,**track}
# ic(all_info)
#----------------------------------------------------------------------------------------------------------
# split() : splits the string and return the list
s = "i am happy"
s = s.split(' ')
ic(s)

s1 = "22 33 44 55"
l = [int(x) for x in s1.split()]
ic(l)
#end and sep
s2 = "alam"
print(*s2,end="-")
print()
print(*s2,sep='-')
#----------------------------------------------------------------------------------------------------------
#format in python 
ic("{} is a test".format("this"))
# print(f'{0}')
ic("{gfg} is {0} science portal for {1}".format("computer","geeks",gfg="GeekForGeek"))

ic("{0:.2f}".format(27.33333))
ic("{0} of 15 is {1:b}".format("binary",15))
ic("{0} of 15 is {1:o}".format("octal",15))
ic("{0} of 15 is {1:X}".format("Hexa",15))
#padding substitution or generating spaces
ic("{0:10}test".format("this"))
#Use "<" to left-align the value:
txt = "We have {:<8} chickens."
ic(txt.format(49))
#Use ">" to right-align the value:
txt = "We have {:>8} chickens."
ic(txt.format(49))

ic("{:*^20s}".format("alam"))

def organize(a,b):
    for i in range(a,b):
        ic("{:6d}{:6d}{:6d}{:6d}".format(i,i**2,i**3,i**4))
organize(3, 7)

txt = "The universe is {:,} years old."
ic(txt.format(13800000000))
#-------------------------------------------------------------------------------------------------------------
#string in python
s = "nova is my alias name"
ic(s[0:4])#slicing the string
ic(s[4:-1])#-1 indicates the last character of the string
del s #this will delete the string s after execution of this particular line s is will not be available anymore
s1 = "this is test"
ic(s1)
s1 = "".join([s1,"aa"])  #.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
ic(s1)
#program to find the duplicates in the counter
from collections import Counter
s = "aabbbccccddddd"
wordCount = Counter(s)
for k,v in wordCount.items():
    if v>1:
        print(k)
#different  of method strings
import string
ic(string.ascii_letters)
ic(string.ascii_lowercase)
ic(string.ascii_uppercase)
text = "hey buddies how are you hope u good"
ic(text.endswith("good"))  #return true if the sstring ends with goood false otherwise
ic(text.startswith("hey"))  #same as above except it compares the start
dig = "1234"
ic(dig.isdigit()) #returns true if all the characters in the string is digit
alpha = "abacdfe"
ic(alpha.isalpha())#return true if all the characters are the alphabet in the string
#index and find functions difference is that if element not found than index raise error and find return -1
#tip:- always use index in try block and handle the exception
try:
   ic(dig.index('6'))
except:
   ic("not found")
ic(dig.find('3'))
sc = "AlamAnsari"
ic(sc.swapcase()) #converts all capital to small and small to capital
ic(sc.replace('a','0'))

