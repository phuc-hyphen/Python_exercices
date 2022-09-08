from collections import OrderedDict


def dic_sum_values(dict):
    sum = 0
    for val in dict.values():
        # print(type(val))
        if type(val) == int:
            sum += val
    print("Dictionary    sum : ", sum)


def dic_max_int(dict):
    max = 0
    for val in dict.values():
        if type(val) == int and val > max:
            max = val
    print("max int valu in dictionary is :", max)


def is_value_exists(ele, dict):
    if ele in dict.values():
        print(ele, "exist in dictionary")
    else:
        print(ele, "not exist in dictionary")


def sort_dict_key(dict):
    dict = sorted(dict.items())
    # for key in dict.keys():
    #     print(key)
    # dict1 = {1: 1, 2: 9, 3: 4}
    # sorted_values = sorted(dict1.values())  # Sort the values
    # sorted_dict = {}
    #
    # for i in sorted_values:
    #     for k in dict1.keys():
    #         if dict1[k] == i:
    #             sorted_dict[k] = dict1[k]
    #             break
    #
    # print(sorted_dict)
    print(dict)


def rev_sort_dict_values(diction):
    tmp_dict = sorted(diction.values(), reverse=True)
    # for key in dict.keys():
    #     print(key)
    print(tmp_dict)


def concatene(dict1, dict2, dict3):
    diction = dict()
    diction.update(dict1)
    diction.update(dict3)
    diction.update(dict2)
    print(diction)


def dict_less_n(n, diction):
    dict2 = dict()
    for key, val in diction.items():
        if n > val:
            dict2[key] = val
    print(dict2)

def make_new_dict_from_2_list(list1,list2):
    new_dict = dict()
    for ele1,ele2 in zip(list1,list2):
        new_dict[ele1] = ele2

    print(new_dict)

def merge_2_dict(dict1,dict2):
    tmp_dict = dict()
    tmp_dict.update(dict1)
    tmp_dict.update(dict2)
    sorted_dict = dict(sorted(tmp_dict.items()))
    print(sorted_dict)



