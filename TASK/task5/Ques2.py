check_list = [1,'c',5,'k','9',4,245,'100']

int_or_str_check = lambda item : type(item)
result = list(map(int_or_str_check, check_list))
print(result)