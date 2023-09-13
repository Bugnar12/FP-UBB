import random
def to_str(z : complex):
    """

    :param z:
    :return: The string representation of the complex number z
    """


def generate_list(list_complex : list):
    """
    Function appends to the list random complex generated numbers using the function generate_complex
    :return: a list contining 10 random complex numbers
    """
    for i in range (10):
        list_complex.append(generate_complex())
    return list_complex

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

array = []
generate_list(array)
for i in range(len(array) - 1):
    print(to_str(array[i]))