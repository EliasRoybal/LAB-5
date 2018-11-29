import time
from LAB5 import *


def main():
    heap = Heap()
    start_time = int(round(time.time()*1000))
    heap.build_heap([17, 23, 40])

    print(heap.get_min_child())
    print(heap.get_min_child())
    print(heap.get_min_child())

    print("Running time for test 1: %s milliseconds " % (start_time - time.time()))

    print("")

    start_time = int(round(time.time()*1000))
    heap.build_heap([20, 0, 15, 2])

    print(heap.get_min_child())
    print(heap.get_min_child())
    print(heap.get_min_child())
    print(heap.get_min_child())

    print("Running time for test 2: %s milliseconds " % (start_time - time.time()))
    print("")

    start_time = int(round(time.time()*1000))
    heap.build_heap([12,91,2,51,3])

    print(heap.get_min_child())
    print(heap.get_min_child())
    print(heap.get_min_child())
    print(heap.get_min_child())
    print(heap.get_min_child())

    print("Running time for test 3: %s milliseconds " % (start_time - time.time()))

    print("")

    start_time = int(round(time.time()*1000))
    heap.build_heap([12000, 1522, 95566, 13350, 30030, 500])

    print(heap.get_min_child())
    print(heap.get_min_child())
    print(heap.get_min_child())
    print(heap.get_min_child())
    print(heap.get_min_child())
    print(heap.get_min_child())

    print("Running time for test 4: %s milliseconds " % (start_time - time.time()))


main()
