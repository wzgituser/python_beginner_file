# class TestClass:
#     test_var ='helo'
#     another_var = 1986
#     obj = []
#     def test_foo(props):
#         print(f'test_foo_with_f_func_and_param_{props}_insid_of_the_class')
#     def another_test_func(param2):
#         x = pow(param2,param2) 
#         print(f'idiotic_func_to_the_power_of_{x}')

# print(TestClass.test_var)
# test = TestClass
# print((test.another_var))
# test.test_foo('THIS_IS_PARAM')
# TestClass.another_test_func(int(3))
# print(type(TestClass.obj))

# # mege class:

# class Mage:
#     def __init__(self ,health ,mana):
#         self.health = health
#         self.mana = mana
#         print('the mage class was created')
#     def __len__(self):
#         return self.mana
#     def attack(self,target):
#         target.health -= 10

# class Monster:
#     health = 40
# mage = Mage(100,200)

# monster = Monster()

# print(monster.health)
# mage.attack(monster)
# print(monster.health)
class Human:
    def __init__(self,health):
        self.health = health

class Warior:
    def __init__(self,health):
        self.health = health
       
    def attack(self):
        print('attack')

class Barbarian:
    def __init__(self, health):
        self.health = health
    def attack(self):
        print('attack')
        return 

warior = Warior(50)
barbarian = Barbarian(100)
warior.attack()
barbarian.attack()


def test_func():
    print('it was imported')