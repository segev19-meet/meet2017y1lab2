Python 3.5.2 (default, Nov 17 2016, 17:05:23) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> 
>>> a=5
>>> b=10
>>> a=b
>>> b=a
>>> a
10
>>> b
10
>>> c=a
>>> c
10
>>> a=5
>>> a=5
>>> b=10
>>> c=a
>>> c
5
>>> a=b
>>> b=c
>>> a
10
>>> b
5
>>> four='4'
>>> print(four*3)
444
>>> five=4
>>> print(five)
4
>>> five=4
>>> print(five)
4
>>> print(five*3)
12
>>> '4'*3
'444'
>>> my_name='student'
>>> print("hi,"+myname')
      
SyntaxError: EOL while scanning string literal
>>> print("hi,"+my_name)
hi,student
>>> print("hi",+my_name)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    print("hi",+my_name)
TypeError: bad operand type for unary +: 'str'
>>> print("hi,"m
      
SyntaxError: invalid syntax
>>> 
>>> my_age=15
>>> print('i am '+my_age+'years old')
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    print('i am '+my_age+'years old')
TypeError: Can't convert 'int' object to str implicitly
>>> print('i am' +'my_age'+'years old')
i ammy_ageyears old
>>> 0str(my_age0
    )
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> str(my_age)
'15'
>>> my_age='15'
>>> print('i am '+my_age+'years old')
i am 15years old
>>> 

>>> 
>>> 
>>> my age='15'
SyntaxError: invalid syntax
>>> print('i am' +my age +'years old')
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> score=1
>>> total=score=(count*2)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    total=score=(count*2)
NameError: name 'count' is not defined
>>> print(total)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    print(total)
NameError: name 'total' is not defined
>>> score='1'
>>> total=score=(count*2)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    total=score=(count*2)
NameError: name 'count' is not defined
>>> score=1
>>> total=score=(count*2)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    total=score=(count*2)
NameError: name 'count' is not defined
>>> 1+'1'
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    1+'1'
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 1+1
2
>>> '1'+'1'
'11'
>>> 1+1.0
2.0
>>> score=1
>>> total=score+(count*2)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    total=score+(count*2)
NameError: name 'count' is not defined
>>> count=1
>>> print('total'='score'(count*2))
SyntaxError: keyword can't be an expression
>>> print(total)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    print(total)
NameError: name 'total' is not defined
>>> 
>>> 

>>> 
>>> 
