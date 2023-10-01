import math
from time import perf_counter
import random

random_nums = []
NANI = 0
while NANI != 10000:
    random_nums.append(random.randint(0, 100000))
    NANI += 1

def is_sorted(lyst):
    for i in range(0, len(lyst) - 1):
        if lyst[i] > lyst[i + 1]:
            return False
    return True

def insertion_sort(lyst):
    nani = 0
    while is_sorted(lyst) is False:
        if lyst[nani] is lyst[nani - 1]:
            nani += 1
        if lyst[nani] > lyst[nani - 1]:
            nani += 1
        elif lyst[nani] < lyst[nani - 1]:
            sani = nani
            while lyst[sani-1] > lyst[sani]:
                indx_1 = lyst[sani]
                indx_2 = lyst[sani - 1]
                lyst[sani] = indx_2
                lyst[sani - 1] = indx_1
                if sani - 1 > 0:
                    sani -= 1
            nani += 1
        return lyst

def quicksort(lyst):
    unchanged_lyst_len = len(lyst)
    normal_lyst = []
    master_lyst = [lyst]
    pivot = lyst[-1]
    while unchanged_lyst_len != len(master_lyst):
        i = 0
        while i != len(master_lyst):
            if len(master_lyst[i]) > 1:
                pivot = master_lyst[i][-1]
                master_lyst[i].pop(-1)
                left_list = []
                right_list = []
                for value in master_lyst[i]:
                    if value <= pivot:
                        left_list.append(value)
                    elif value > pivot:
                        right_list.append(value)
                master_lyst.pop(i)
                master_lyst.insert(i, left_list)
                master_lyst.insert(i + 1, [pivot])
                master_lyst.insert(i + 2, right_list)
                while [] in master_lyst:
                    master_lyst.pop(master_lyst.index([]))
            if len(master_lyst[i]) == 1:
                i += 1
    for lists in master_lyst:
        normal_lyst.append(lists[0])
    return normal_lyst

def mergesort(lyst):
    new_list = []
    for items in lyst:
        new_list.append([items])
    while len(lyst) > 1:
        temp_list = []
        temp_lizt = []
        k = 0
        start = 0
        if len(new_list) % 2 != 0:
            start = len(new_list) - 2
            temp_lizt = new_list[0:len(new_list) - 2]
        for i in range(start, len(new_list), 2):
            k = 0
            j = 0
            temp_list = []
            while k < len(new_list[i + 1]) and j < len(new_list[i]):
                left = new_list[i]
                right = new_list[i + 1]
                if right[k] >= left[j]:
                    temp_list.append(left[j])
                    j += 1
                elif right[k] < left[j]:
                    temp_list.append(right[k])
                    k += 1
            while j != len(left):
                temp_list.append(left[j])
                j += 1
            while k != len(right):
                temp_list.append(right[k])
                k += 1
            temp_lizt.append(temp_list)
        new_list = temp_lizt
        lyst = new_list
    return lyst[0]

def selection_sort(lyst):
    while is_sorted(lyst) is False:
        for nani, something in enumerate(lyst):
            comparing_item = lyst[nani]
            item_to_start = lyst[nani]
            for i in range(nani + 1, len(lyst)):
                if lyst[i] < item_to_start:
                    item_to_start = lyst[i]
                    item_switch_index = i
                    lyst[nani] = item_to_start
                    lyst[item_switch_index] = comparing_item
    return lyst

def timed_function(func):
    start = perf_counter()
    func(random_nums)
    elapsed_time = perf_counter() - start
    return str(elapsed_time)

def linear_search(lyst, target):
    for item in lyst:
        if target == item:
            return True
    return False

def binary_search(lyst, target):
    low = 0
    high = len(lyst)
    while low < high:
        # calc mid
        mid = (low + high) // 2
        # is lyst(mid) == target
        if lyst[mid] == target:
            return True
        # if lyst[mid] > target
        if lyst[mid] > target:
            high = mid
        # if lyst[mid] < target
        if lyst[mid] < target:
            low = mid + 1
        return False

def jump_search(lyst, target):
    pos = 0
    jump = math.floor(math.sqrt(len(lyst)))
    for i in range(0, len(lyst) - 1, jump):
        if target > lyst[i]:
            pos = i
    for i in range(pos, len(lyst)):
        if target == lyst[i]:
            return True
    return False