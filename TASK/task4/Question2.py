class Circle:

    def __init__(self,__pi, my_list):
        self.__pi = 3.141  # 2. declaring a private property
circle = Circle(3.141,[12,23,34])
output = circle.get_pi
print(output)