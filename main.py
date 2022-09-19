import random
import math
def generate_random_array(number_of_elements):
    array = []
    for element in range(1, number_of_elements+1):
        array.append(element)
    random.shuffle(array)
    return array

def binary_search_algorithm (number_to_find, array):
    array.sort()
    top_index = len(array) - 1
    bottom_index = 0
    while bottom_index <= top_index:
        middle_element = math.floor((bottom_index+top_index)/2)
        if array[middle_element] < number_to_find:
            bottom_index = middle_element + 1
        elif array[middle_element] > number_to_find:
            top_index = middle_element - 1
        else:
            return middle_element
    return -1

if __name__ == '__main__':
    random_array = []
    number_of_elements = int(input("How many elements in the array? "))
    random_array = generate_random_array(number_of_elements)
    find_this_number = int(input("Which number would you like to find? "))

    index_of_number = binary_search_algorithm(find_this_number, random_array)

    print()
    if index_of_number == -1:
        print("The number {} has not been found".format(find_this_number))
    else:
        print("The number {} has been found at index {}".format(find_this_number,index_of_number))
