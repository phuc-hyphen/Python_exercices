from random import randint
from faker import Faker
import dic

fk = Faker()
dic_age = dict()
for i in range(12):
    dic_age[fk.name()] = randint(0, 100)

dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
# print(dic_age)
# dic.dic_sum_values(dic_age)
# dic.dic_max_int(dic_age)
# dic.is_value_exists(67,dic_age)
# dic.sort_dict_key(dic_age)
# dic.rev_sort_dict_values(dic_age)
# dic.dict_less_n(67, dic_age)


# list1 = list()
# list2 = list()
# for i in range(12):
#     list1.append(fk.name())
#     list2.append(randint(0, 100))
#
# print(list1)
# print(list2)

# dic.make_new_dict_from_2_list(list1,list2)
dic.merge_2_dict(dic2,dic3)

