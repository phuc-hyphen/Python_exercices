import file_read as operation


# f = open("text.txt", "r+")
# operation.affiche_fiel(f)
# f.write("DAns ta gueule")


def overwrite_file(file, text):
    f = open(file, "w+")
    f.write(text)
    f.close()


def add_line(file, text):
    f = open(file, 'a')
    f.writelines(text)
    f.close()


def show_and_delete(File_name):
    f = open(File_name, "r+")
    print(f.read())
    f.truncate(0)  # delete the contents
    f.close()


def copie_and_save(file1, file2):
    f1 = open(file1, "r")
    f2 = open(file2, "w")
    f2.write(f1.read())
    f1.close()
    f2.close()


def merge_file(files, result_file):
    file_resul = open(result_file, "w")
    for file in files:
        f = open(file, "r")
        file_resul.write(f.read())
        f.close()
    file_resul.close()


def show_line_by_line(file):
    f = open(file, "r")

    while True:
        line = f.readline()
        if not line:
            break
        print(line)


def count_line(File):
    file = open(File, "r")

    line_count = 0

    for line in file:

        if line != "\n":
            line_count += 1

    file.close()
    print(line_count)


def count_word(File):
    f = open(File, "r")
    texts = f.read()
    list_word = texts.split()
    print(len(list_word))


def count_matched_word(file, find_word):
    f = open(file, "r")
    texts = f.read()
    list_word = texts.split()
    count = 0
    for word in list_word:
        if word == find_word:
            count += 1
    print(count)


files = {"text.txt", "text2.txt", "text3.txt"}
file1 = "text.txt"
file2 = "text2.txt"
text = "DAns ta gueule"
# add_line(file, text)
# show_and_delete(file)
# copie_and_save(file1, file2)
# merge_file(files, "merged.txt")
# show_line_by_line("merged.txt")
# count_line("merged.txt")
# count_word("merged.txt")
count_matched_word("merged.txt", "Lorem")
