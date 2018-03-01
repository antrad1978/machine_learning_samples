import re
import encodings

months = ('January','February','March','April','May','June',\
'July','August','September','October','November','  December')

print(months)

mystr="ddd"

cats = ['Tom', 'Snappy', 'Kitty', 'Jessie', 'Chester']
cats.append("pippo")
cats.count(4)

print(cats)

dict = {'Andrew Parson':8806336, \
'Emily Everett':6784346, 'Peter Power':7658344, \
'Lewis Lame':1122345}

dict["aaa"]="000"

print(dict.keys())
print(dict.values())
print(dict)

a = [5, 1, 4, 3]
print(sorted(a))  ## [1, 3, 4, 5]
print(a)  ## [5, 1, 4, 3]

str = 'an example word:cat!!'
match = re.search(r'word:\w\w\w', str)
# If-statement after search() tests if it succeeded
if match:
    print('found', match.group()) ## 'found word:cat'
else:
    print('did not find')

def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

print(factorial(5))

class MyClass:
    @staticmethod
    def my_method():
        return "aaa"
