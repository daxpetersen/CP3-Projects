def bubble_sort():
    def sort_list(items):
        length = len(items)
        comparisons = 0
        swaps = 0
        print(items)  
        for step in range(length):
            for index in range(length - step - 1):
                comparisons += 1
                if items[index] > items[index + 1]:
                    items[index], items[index + 1] = items[index + 1], items[index]
                    swaps += 1
            print(items)
        return items, comparisons, swaps
    
    count = int(input("Enter the data you need sorted: "))
    numbers = []
    
    for _ in range(count):
        number = int(input("Enter a number: "))
        numbers.append(number)
    
    sorted_numbers, comparisons, swaps = sort_list(numbers)
    print("Sorted list:", sorted_numbers)
    print("Algorithm: Bubble Sort")
    print("Comparisons:", comparisons)
    print("Swaps:", swaps)

def pigeon():
    def pigeonhole_sort(items):
        min_value = min(items)
        max_value = max(items)
        range_of_values = max_value - min_value + 1
        holes = [[] for _ in range(range_of_values)]
    
        for item in items:
            holes[item - min_value].append(item)
    
        sorted_list = []
        comparisons = 0
        swaps = 0
        for hole in holes:
            for item in hole:
                sorted_list.append(item)
                print(sorted_list)
        return sorted_list, comparisons, swaps
    
    count = int(input("Enter the data you need sorted: "))
    numbers = []
    
    for _ in range(count):
        number = int(input("Enter a number: "))
        numbers.append(number)
    
    print("Initial list:", numbers)
    sorted_numbers, comparisons, swaps = pigeonhole_sort(numbers)
    print("Sorted list:", sorted_numbers)
    print("Algorithm: Pigeonhole Sort")
    print("Comparisons:", comparisons)
    print("Swaps:", swaps)

def selection():
    def selection_sort(items):
        length = len(items)
        comparisons = 0
        swaps = 0
        for step in range(length):
            min_index = step
            for index in range(step + 1, length):
                comparisons += 1
                if items[index] < items[min_index]:
                    min_index = index
            items[step], items[min_index] = items[min_index], items[step]
            swaps += 1
            print(items)
        return items, comparisons, swaps
    
    count = int(input("Enter the data you need sorted: "))
    numbers = []
    
    for _ in range(count):
        number = int(input("Enter a number: "))
        numbers.append(number)
    
    print("Initial list:", numbers)
    sorted_numbers, comparisons, swaps = selection_sort(numbers)
    print("Sorted list:", sorted_numbers)
    print("Algorithm: Selection Sort")
    print("Comparisons:", comparisons)
    print("Swaps:", swaps)

def counting():
    def counting_sort(items):
        max_value = max(items)
        count = [0] * (max_value + 1)
        comparisons = 0
        swaps = 0
    
        for item in items:
            count[item] += 1
            print(count)
    
        sorted_list = []
        for value in range(len(count)):
            for _ in range(count[value]):
                sorted_list.append(value)
                print(sorted_list)
        
        return sorted_list, comparisons, swaps
    
    count = int(input("Enter the data you need sorted: "))
    numbers = []
    
    for _ in range(count):
        number = int(input("Enter a number: "))
        numbers.append(number)
    
    print("Initial list:", numbers)
    sorted_numbers, comparisons, swaps = counting_sort(numbers)
    print("Sorted list:", sorted_numbers)
    print("Algorithm: Counting Sort")
    print("Comparisons:", comparisons)
    print("Swaps:", swaps)

code = input("what sort? ")
if code == "pigeon":
    pigeon()
elif code == "bubble":
    bubble_sort()
elif code == "selection":
    selection()
elif code == "counting":
    counting()