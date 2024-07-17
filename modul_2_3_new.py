my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
numbers = []
i = 0
while i < len(my_list):
    number = my_list[i]
    if number >= 0:
        numbers.append(number)
    else:
        print("число отрицательное", number)
        numbers.remove(0)
        break
    i = i + 1
print(numbers)