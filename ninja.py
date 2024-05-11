# print("type some text")
# text_two = input("text no: ")
# text = 10
# a = int(text_two) + int(text)

# print( a)
# print('val'.upper())
# print("VAl".lower())
# print('val'.replace('l','lue'))
# print(abs(-1))
# print(max(10,5))
# print(len('text'))

#calc

# a_value = int(input('type size of the shortest triangle arm:'))
# b_val = int(input('size of the mid arm: '))
# sthng = (a_value ** 2 + pow(b_val,2) ** 2) ** (1/2)
# print("the size of the triangle: ", sthng )

# print(round(sthng , 2))


# containers

# a_tuple = (1,2,3,"str")
# a_list = [1,2,3, 'list']
# set_cont = {1,2,3,3}
# a_list.append(1)
# a_dictionary = {"it is known as a obj in js": 123, 'acb': 123 ,"lista" : ['a',1,2]}
# print(set_cont)
# # print('it was tuple:',set(a_tuple))
# # print('it was set:' ,list(set_cont))
# # print('it was set',tuple(set_cont))
# print(a_dictionary)
# a_dictionary['new'] = "new value"
# print("list" ,a_list[2:3] ,"dictionary", a_dictionary["it is known as a obj in js"],"set:",)
# print(a_dictionary)

# conditions
# lenght_w = "12345"
# if 4 == 'w' and 3 == 3:
#      print("correcteeeeeeeeee")
# elif 2 == 1 :
#     print("correct")
# elif len(lenght_w) <= 5 :
#     print("itis")
# else: print('no')

#while loop:

# cont = 0
# while cont <= 7:
#     print(cont)
#     cont += 2
#     if cont == 2:
#         print('cout is 2')

#for loop
# some = [1,2,3,4,5,5]
# for x in some:
#     1+1

# list_l = {3:1,2:1,4:1}
# count = 0
# for x in list_l:
#     count += 1 
#     print(count,x)
# for x in list_l.keys():
#     print(x)
# for x in list_l.values():
#     print(x,'b')
# for k,v in list_l.items():
#     print(k, 'a')

# 0 == falsy 1 and rest of vals=truthy
# if 0 : 
#     print('false')
# if 2 :
#     print('true')

# list_a = (1,2,3,4,5,6)
# xxxx = 0
# for x in list_a:
#     if x == 2:
#         print(x,'v=2')
#     if x != 2:
#         print(x,'!=2')
# while xxxx <= 6:
#     print(list_a[-2])
#     xxxx += 1

#functions
# counter = ''
# param = int(input("loop amount: "))
# def print_5(param , amount):
#     counter = 0
#     while counter <= amount:
#         print(counter , param)
#         counter +=1
#     print('done')
#     return amount , counter

# def calc_foo(a_value , b_val):
#     # a_value = int(input('type size of the shortest triangle arm:'))
#     # b_val = int(input('size of the mid arm: '))
#     sthng = (a_value ** 2 + pow(b_val,2) ** 2) ** (1/2)
#     #print("the size of the triangle: ", sthng )
#     return round(sthng,2)

# #call

# print('print')
# test = print_5('test_io',param)
# print('this is returned value:',test)

# print('returned triangle calc result:', calc_foo(2,3))

############################################################
# exesise

# string_arg = input('first argument:')
# sec_arg = int(input('sec_arg_no:'))

# a = input("str:")

# b = input("int:")

# def shouter_foo(param_1 , param_2):
#         if param_2 <= 15:
#             for i in range(param_2):
#                   print(i,param_1)
#         else:
#             print('u are to loud')
#         return 'done'
# x = shouter_foo(a,int(b))
# print(x)

# strings concat
# # f string
# name = "anna"
# age = 36
# user_info = 'bob is 36 years old'
# bad_approach = name + ' is ' + str(user_info)
# good_approach =  f'{name} is {age} and {user_info}'
# print(bad_approach)
# print(f'f string use: {good_approach}')

# print('exercise TWO')
# check_age = int(input('type age to be checked: '))

# adult = 'adult'
# kid = 'kid'

# if check_age < 18:
#     print(f'the user is {kid}')
# else:
#     print(f'the user is {adult}')

# ---one--line--if--statment-----

# check = 'Adult' if check_age > 18 else 'child'

# print(check)

# iteration trough list-array with for loop

# list_a = [1,2,3,4,56,4,7]

# for i in range(0,11,1):
#     list_a.append(i)
# print(list_a)

#  list comprachension

# list_comprahension = [f'{j}{i}'for i in range(1,11,1) for j in ('a','b','c')]

# print('comprahension', list_comprahension)

# BATLESHI GAME

# battleship_board = [f'{letter}{num}'for letter in ('A','B','C','D','E') for num in range(1,6) if f'{letter}{num}' != 'C3']
# print(battleship_board)

#  import/export from another file (classes.py)
# from classes import Barbarian

# barbarian = Barbarian(100)
# print(barbarian)
# barbarian.attack(100)
import math
import random
from classes import test_func as test
print(math)
print(random.randint(1,10))
test()

def test_for_git_commit():
    print('i will comit this')