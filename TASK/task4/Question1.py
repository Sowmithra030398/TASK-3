#1. Creating a class using constructor
class Circle:
    def __init__(self, my_list):
        self.my_list = my_list

my_data = Circle([10, 501, 22, 37, 100, 999, 87, 351])   
for i in range (1):
    print(my_data.my_list)