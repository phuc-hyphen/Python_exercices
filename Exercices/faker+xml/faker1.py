from faker import Faker

f_aker = Faker("fr_FR")

# # ---------------- identity data -----------
print(f'name : {f_aker.name()}')
print(f'firstname : {f_aker.first_name()}')
print(f_aker.date_of_birth())
# # ---------------- location data -----------
# print(" 5 randoms location in France")
# Faker.seed(0)
# for _ in range(5):
#     print(f_aker.address())


