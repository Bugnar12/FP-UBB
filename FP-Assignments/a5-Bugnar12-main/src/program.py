from sys import maxsize
import random
import cmath

#
# Write the implementation for A5 in this file
#

#
# Write below this comment
# Functions to deal with complex numbers -- list representation
# -> There should be no print or input statements in this section
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#


def generate_complex():
    """
    z = a + bi
    ex. : z1 = 3 + 2i
    x, y are the real parts
    :return: the complex number using the real numbers x, y (generates real part and imaginary)
    """
    x = random.randint(-40, 40)
    y = random.randint(-40, 40)
    z = complex(x, y)
    return z

def absolute_value(z : complex):
    return abs(z)


# def convert_array(array : list):
#     new_array = []
#     for i in range(len(array) - 1):
#         x = abs(array[i])
#         new

# def generate_complex_dic():
#     x = random.randint(0, 50)
#     y = random.randint(0, 50)
#     z = {
#         'real' : x,
#         'imag' : y
#     }
#     return z


def longest_increasing_modulus(array : list):
    """
    Iterative version :
    Time complexity O(n^2)
    :param array:
    :return: The first position and the last one of the longest array
    """
    max_length = 1
    max_current = 1
    poz1 = 0
    poz2 = 0
    max_poz1 = 0
    max_poz2 = 0
    for i in range(len(array) - 2):
        poz1 = i
        for j in range(i+1, len(array)):
            if abs(array[j]) > abs(array[j-1]):
                max_current = max_current + 1
                poz2 = j
            elif abs(array[j]) < abs(array[j-1]):
                if max_current > max_length:
                    max_length = max_current
                    max_poz1 = poz1
                    max_poz2 = poz2
                max_current = 1
                poz1 = j
                poz2 = j

    return max_poz1, max_poz2

def longest_subarray_sum(array: list):
    """
    Dynamic programming version:
    Time complexity : O(n)

    :param array:
    :return: The first and the last position of the elements building the largest sum
    """

    max_so_far = -maxsize - 1
    max_ending_here = 0
    start = 0
    size = len(array)
    end = 0
    s = 0

    for i in range(0, size):

        max_ending_here += array[i].real

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i

        if max_ending_here < 0:
            max_ending_here = 0
            s = i + 1

    return start, end

def generate_list(list_complex : list):
    """
    Function appends to the list random complex generated numbers using the function generate_complex
    :return: a list contining 10 random complex numbers
    """
    for i in range (10):
        list_complex.append(generate_complex())
    return list_complex

def complex_conversion(x, y : int):
    """

    :param x:
    :param y:
    :return: Returns the complex representation of two numbers according to Python function
    """
    return complex(x, y)

# def complex_dict(z : complex):
#     """
#     dictionary representation of complex numbers
#     :return:
#     """
#     complex = {
#         "real" : z.real,
#         "imag" : z.imag
#     }

def to_str(z : complex):
    """

    :param z:
    :return: The string representation of the complex number z
    """
    return str(z.real) + "+" + "(" + str(z.imag) + ")"


#
# Write below this comment
# Functions to deal with complex numbers -- dict representation
# -> There should be no print or input statements in this section
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#

#
# Write below this comment
# Functions that deal with subarray/subsequence properties
# -> There should be no print or input statements in this section
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#

#
# Write below this comment
# UI section
# Write all functions that have input or print statements here
# Ideally, this section should not contain any calculations relevant to program functionalities
#

# def generate_dic():
#     for i in range(10):
#         print(generate_complex())

def checking_continuity():
    print("Add a number ? If yes enter 1, else enter 0.")
    button = int(input("->"))
    if button == 1:
        return True
    elif button == 0:
        return False
    else:
        print("Error : value is not valid")
        checking_continuity()

def read_complex(array_complex : list):
    array_complex = []
    while checking_continuity() == True :
        print("\n Enter the real part of the number. (INTEGERS ONLY)")
        nr_real = int(input(">"))

        print("\n Enter the imaginary part of the number. (INTEGERS ONLY)")
        nr_imag = int(input(">"))

        z = complex_conversion(nr_real, nr_imag)
        array_complex.append(z)
    print("This is the array you have created : \n")
    return array_complex

def ui_menu():
    """
    Generating or inputing a list of complex numbers
    :return:
    """
    print("Welcome to the 6-th assignment of the FP class!\n")
    print("Choose between the following options:\n")
    print("1.Generate a list of 10 complex numbers\n"
          "2.Add some complex numbers by yourself to the list\n"
          "3.Exit the program")
    while True:
        array = []
        option = int(input(">"))
        if option == 1:
            ui_1(array)
        elif option == 2:
            ui_2(array)
        elif option == 3:
            return
        else:
            print("Bad user Option. Try 1 or 2!")

def ui_1(array):
    print(generate_list(array), "\n")
    print("Congratulations! You generated a random array of complex numbers :).\n"
          "What do you want do get now?\n"
          "1.Length and elements of a longest subarray of numbers having increasing modulus.\n"
          "2.The length and elements of a longest increasing subsequence, when considering each number's real part\n"
          "3.Exit the program")
    option_1 = int(input(">"))
    if option_1 == 1:
        ui_modify_1(array)
    elif option_1 == 2:
        ui_modify_2(array)
    elif option_1 == 3:
        return
    else:
        print("Value is not accepted. Try again")
        ui_1(array)

def ui_2(array):
    print(read_complex(array))
    print("What do you want do get now?\n"
          "1.Length and elements of a longest subarray of numbers having increasing modulus.\n"
          "2.The length and elements of a longest increasing subsequence, when considering each number's real part\n"
          "3.Exit the program")
    option_2 = int(input(">"))
    if option_2 == 1:
        ui_modify_1(array)
    elif option_2 == 2:
        ui_modify_2(array)
    elif option_2 == 3:
        return
    else:
        print("Value is not accepted. Try again")
        ui_2(array)

def ui_modify_1(array : list):
    """
    Prints the size of the array and its elements
    :return:
    """

    max_poz1, max_poz2 = longest_increasing_modulus(array)

    for i in range(max_poz1, max_poz2 + 1):
        print(array[i])
    print(max_poz1, max_poz2)
    print("\n")
    print(ui_menu())

kd
def ui_modify_2(array : list):

    longest_subarray_sum(array)
    start, end = longest_subarray_sum(array)

    print("This is the array : \n")
    for i in range(start, end + 1):
        print(array[i])
    print("This is the length of the array : ")
    print(end - start + 1)
    ui_menu()

def start():
    ui_menu()

start()

