import os,time

filename = 'C:\\Formation\\Python\\Exercices\\classes.py'

st = os.stat(filename)


print(st.st_size)
# print(st.st_ctime)
print(time.ctime(os.path.getmtime(filename)))