# Q1
def list_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

f1 = [5, 416, 54, 21, 6135, 15, 741]
result = list_sort(f1)
print(result)

# Q2
def file_type(extension_type, files):
    extension_dict = {}
    for pair in extension_type.split(';'):
        extension, file_type = pair.split(',')
        extension_dict[extension] = file_type

    result = {}
    for file in files:
        extension = file.split('.')[-1]
        if extension in extension_dict:
            result[file] = extension_dict[extension]
        else:
            result[file] = 'unknown'
    return result

extension_type = "xls,spreadsheet;xlsx,spreadsheet;jpg,image"
files = ["abc.jpg", "xyz.xls", "text.csv", "123"]
resultDict = file_type(extension_type, files)
print(resultDict)

# Q3
def sort_list_of_dicts(lst, key):
    return sorted(lst, key=lambda x: x[key])

fruits = [
    {"fruit": "orange", "color": "orange"},
    {"fruit": "apple", "color": "red"},
    {"fruit": "banana", "color": "yellow"},
    {"fruit": "blueberry", "color": "blue"}
]

sorted_By_fruits = sort_list_of_dicts(fruits, "fruit")
print(sorted_By_fruits)

sorted_By_colors = sort_list_of_dicts(fruits, "color")
print(sorted_By_colors)

# Q4
def switch_dict(dictionary):
    return {value: key for key, value in dictionary.items()}
dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",
    "key5": "value5"
}
result = switch_dict(dict)
print(result)

# Q5
def compare_lists(list1, list2):
    common_elements = list(set(list1) & set(list2))
    non_common_elements = list(set(list1) ^ set(list2))
    return common_elements, non_common_elements

mainstream = ["One Punch Man", "Attack On Titan", "One Piece", "Sword Art Online", "Bleach", "Dragon Ball Z", "One Piece"]
must_watch = ["Full Metal Alchemist", "Code Geass", "Death Note", "Stein's Gate", "The Devil is a Part Timer!", "One Piece", "Attack On Titan"]

common, non_common = compare_lists(mainstream, must_watch)
print("Common_elements:", common)
print("Non-common_elements:", non_common)

# Q6
def get_sublist(lst, start_idx, end_idx):
    sublist = lst[start_idx:end_idx+1]  # Extract the sublist between start_idx and end_idx (inclusive)
    return sublist[1::2]  # Return every second element of the sublist

lst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
start_idx = 2
end_idx = 9
result = get_sublist(lst, start_idx, end_idx)
print(result)

# Q7
from functools import reduce

def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n+1))
num = 5
result = factorial(num)
print(result)

# Q8
A0 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
A1 = range(0, 10) #A1 containing numbers from 0 to 9 
A2 = []
A3 = [1, 2, 3, 4, 5]
A4 = [1, 2, 3, 4, 5]
A5 = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
A6 = [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]]
A7 = 21
A8 = <map object at [memory_address]>
A9 = <filter object at [memory_address]>

# Q9
from datetime import datetime, timedelta

def check_date_difference(from_date, to_date, difference):
    # Convert string dates to datetime objects
    from_datetime = datetime.strptime(from_date, '%y-%m-%d')
    to_datetime = datetime.strptime(to_date, '%y-%m-%d')
    
    # Calculate the difference in days
    date_difference = abs((to_datetime - from_datetime).days)
    
    # Compare the difference with the provided value
    if date_difference < difference:
        return True
    else:
        return False
from_date = '21-01-01'
to_date = '21-01-10'
difference = 10

result = check_date_difference(from_date, to_date, difference)
print(result)

# Q10
from datetime import datetime, timedelta

def calculate_previous_date(date, n):
    # Convert string date to datetime object
    date_object = datetime.strptime(date, '%y-%m-%d')

    # Calculate the previous date by subtracting timedelta
    previous_date = date_object - timedelta(days=n)

    # Convert the previous date back to string format
    previous_date_string = previous_date.strftime('%y-%m-%d')

    return previous_date_string
date = '16-12-10'
n = 11

previous_date = calculate_previous_date(date, n)
print(previous_date)  # Output: 16-11-29

# Q11
def f(x, l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)
f(2)
f(3, [3, 2, 1])