def sort_list(items):
    length = len(items)
    for step in range(length):
        for index in range(length - step - 1):
            if items[index] > items[index + 1]:
                items[index], items[index + 1] = items[index + 1], items[index]
    return items

count = int(input("How many numbers do you want to sort? "))
numbers = []

for _ in range(count):
    number = float(input("Enter a number: "))
    numbers.append(number)

sorted_numbers = sort_list(numbers)
print("Sorted list:", sorted_numbers)
