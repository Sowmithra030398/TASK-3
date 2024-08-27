class Circle:
# 1. Creating a class using constructor
    def __init__(self, my_list):
        self.__pi = 3.141  # 2. declaring a private property
        self.my_list = my_list

    # 3.1. Creating two methods: Area
    def area(self):
        return [self.__pi * (r ** 2) for r in self.my_list]

    # 3.2. Creating two methods: Perimeter
    def perimeter(self):
        return [2 * self.__pi * r for r in self.my_list]

# Passing a list
my_data = Circle([10, 501, 22, 37, 100, 999, 87, 351])

# Calculate areas
area_result = my_data.area()
print("Areas:", area_result)

# Calculate perimeters
perimeter_result = my_data.perimeter()
print("Perimeters:", perimeter_result)