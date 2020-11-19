from datetime import datetime
from time import time
from functools import wraps
# def decor(fr):
#     def wrapper():
#         if 9<= datetime.now().hour < 21:
#             return fr()
#         else:
#             print('Keep silent, neighbours are sleeping!!!')
#     return wrapper

# @decor
# def whee_say():
#     return "WHEEEE"

# print(whee_say())



# 2)
# def timerss(fb):
#     def tmp(*args, **kwargs):
#         t = time()
#         res = fb(*args, **kwargs)
#         print("Time for taking this function: %f" % (time()-t))
#         return res

#     return tmp

# @timerss
# def func(x, y):
#     return x + y

# func(1, 2)


# 3)

# def repeat(n = 5):
#     def _repeat_(fn):
#         @wraps(fn)
#         def inner(*args, **kwargs):
#             for _ in range(n):
#                 fn(*args, **kwargs)
#         return inner
#     return _repeat_


# @repeat(n = 11)
# def func(name):
#     print(f"{name}")

# func('Python')

# 4)
# users = {
#     'Aktan': '12345', 
#     'Miraida': '345', 
#     'Sasha': '12', 
#     'Kylych': '134'
#     }

# def user_check(function):
#     def wrapper(username, password):
#         global users 
#         for key, value in users.items():
#             if key == username and value == password:
#                 print(f'Welcome, {username}!')
#                 break
#             elif key != username and value == password:
#                 raise Exception('Username is not defined!!!!')
#                 break
#             elif key == username and value != password:
#                 raise Exception('Password is not defined!!!!')
#                 break
#             elif key != username and value != password:
#                 raise Exception('Username and password are not defined!')
#                 continue
#                 # raise Exception('Username and password are not defined!!!!')   
#                 # break
#     return wrapper
# @user_check
# def login(username, password):
#     print(f'Wellcome, {username}')
# login('Aktan', '12345')

# 5)
# Создайте декоратор, который при применении к произвольной функции будет
# регистрировать вызов этой функции и его параметры. Пример кода может выглядеть
# следующим образом:

# def myDecorator(func):
#     def wrapper(a, b=1, *args, **kwargs):
#         print("Calling testFunc (", args, kwargs, ')')
#         print('argument a:', a)
#         print('argument b:', b)
#         print('argument args:', args)
#         print('argument kwargs:', kwargs)
        
        
#         print('Finished testFunc', func(a, b, *args, **kwargs))
#     return wrapper

# @myDecorator
# def testFunc(a, b=1, *args, **kwargs):
#     return a + b
    
# testFunc(2, 3, 4, 5, c=6, d=7)    
# print()
# testFunc(2, c=5, d=6) 
# print()
# testFunc(10)










