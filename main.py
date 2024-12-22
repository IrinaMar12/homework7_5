
my_list = [42,69,322,13,0,99,-5,9,8,7,-6,5]
my_list_number = 0
my_list.pop(4)          # - выводим из списка 0, не положительное и не отрицательное число.
while my_list_number < len(my_list):
    if my_list[my_list_number] < 0:
          break
    print(my_list[my_list_number])
    my_list_number += 1




