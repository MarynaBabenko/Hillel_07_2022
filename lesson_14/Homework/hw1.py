from random import randint
from threading import Thread
import statistics
from time import sleep


def get_random_list():
    """
    add the list with random numbers
    """
    random_list = [randint(1, 10) for i in range(10000)]
    print(f"random list is:{random_list}")
    sleep(2)
    return random_list


def sum_list_elem(x):
    """
    finds the sum of the elements of the list
    """
    sum_elem = sum(x)
    print(f"The sum is: {sum_elem}")
    return sum_elem


def list_average(x):
    """
    finds the arithmetic mean of the elements of the list
    """
    average = statistics.mean(x)
    print(f"The average is: {average}")
    return average


unified = get_random_list()
"""
the argument that creates a unified list
"""

def main():
    """
    creates and starts threads
    """
    t1 = Thread(target=get_random_list, args=(unified,))
    t2 = Thread(target=sum_list_elem, args=(unified,))
    t3 = Thread(target=list_average, args=(unified,))

    t1.start()
    t1.join()
    t2.start()
    t3.start()


if __name__ == "__main__":
    main()
