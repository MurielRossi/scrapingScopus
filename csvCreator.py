import csv


def create_row_check(row):
    file = []

    size = len(row)
    i = 0
    while i < size:
        a = "0"
        row2 = []

        row2.insert(0, row[i])
        row2.insert(1, a)
        file.insert(i, row2)
        i = i + 1

    print(file)
    return file


def csv_writer(row):
    f = open('/home/muriel/PycharmProjects/pythonProject1/file.csv', 'w')

    writer = csv.writer(f)

    file = create_row_check(row)

    writer.writerows(file)

    f.close()
