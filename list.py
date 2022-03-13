def sum_list(list):
    som = 0
    for element in list:
        som += element
    print("som : ", som)


def less_13(list):
    for ele in list:
        if ele < 13:
            print(ele)


def max_list(list):
    print("max = ", max(list))


def min_list(list):
    print("max = ", min(list))


def remplace_0_par_5(list):
    for ele in list:
        if ele == 0:
            ele = 5


def find_char(list):
    for i in range(len(list)):
        if type(list[i]) == 'str':
            print(i)


def list_reverse(list):
    for i in range(len(list), 0, -1):
        print(list[i])


def list_sort_increase(list):
    list.sort()


def list_sort_decrease(list):
    list.sort(reverse=True)


def list_compare(list1, list2):
    for ele in list1:
        if ele in list2:
            print(ele)
