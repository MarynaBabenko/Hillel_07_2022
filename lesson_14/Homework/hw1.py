from random import randint
from threading import Thread
import statistics


def get_random_list():
    """
    Generates the list with random numbers
    """
    random_list = [randint(1, 10) for i in range(10000)]
    print(random_list)
    return random_list


def sum_list_elem(x):
    """
    Find the sum of elements in the list
    """
    sum_elem = sum(x)
    print(sum_elem )
    return sum_elem


def list_average(x):
    """
    Find average of of given numbers in the list
    """
    average = statistics.mean(x)
    print(average)
    return average


unified = get_random_list()

# The argument that creates a unified list


def main():
    """
    Creating and starting threads
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
