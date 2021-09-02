import math
import csv
import tempfile
import os

def FizzBuzz():
    for i in range(1,101):
        if i % 3 == 0 and i % 5 ==0:
            print('FizzBuzz')
        elif i % 5 == 0:
            print('Buzz')
        elif i % 3 == 0:
            print('Fizz')
        else:
            print(i)

def VolumeFormula(radius):
    return float(math.pow(radius, 3)*math.pi*4/3)

records = [
    ['1984','George Orwell', '978-0451524935','268'],
    ['Animal Farm', 'George Orwell','978-0060929879', '144'],
    ['Brave New World', 'Aldous Huxley', '978-0060929879', '288'],
    ['Fahrenheit 451', 'RayBradbury', '978-0345342966', '208'],
    ['Jane Eyre', 'Charlotte Bronte','978-1593083236', '532'],
    ['Wuthering heights', 'Emily Bronte', '978-0141439556', '416']
]

# https://docs.python.org/3/library/csv.html#csv.writer
def WriteCSV(input):
    with tempfile.NamedTemporaryFile() as temp_csv:

        
        writer = csv.writer(temp_csv)
        writer.writerow(header)
        
        for row in input:
            writer.writerow(row)
    temp_csv.close()


    with open('book.csv', 'w', newline='') as output:
        writer = csv.writer(output)
        header = ['Title', 'Author', 'ISBN13', 'Pages']
        # write the header to file
        writer.writerow(header)

        # write each list in records to the csv file
        for row in input:
            writer.writerow(row)
    output.close() # close csv file

    dict = {}

    # with open('book.csv', 'r', newline='') as source:
        # reader = csv.reader(source)
        # header = next(reader)
        # for item in header:
        #     dict[item] = []
        
        # for row in reader:
        #     for item in range(len(row)):
        #         dict[header[item]].append(row[item])
    # source.close()

    # return dict

def Question5(data):
    tmp = tempfile.NamedTemporaryFile(delete=False)
    header = ['Title', 'Author', 'ISBN13', 'Pages']
    
    dict = {}
    try:
        with open(tmp,'w', newline='') as destination:
            writer=csv.writer(destination)
            writer.writerow(header)
            for row in data:
                try:
                    writer.writerow(row)
                except Exception as e:
                    print ('Error in writing row:',e)

            
        with open(tmp,'r', newline='') as source:
            reader = csv.reader(source)
            # header = next(reader)
            # for item in header:
            #     dict[item] = []
        
            for rows in reader:
                for column, value in rows.items():
                    dict.setdefault(column, []).append(value)
    finally:
        # os.unlink(tmp)
        tmp.close()

    print(dict)


# FizzBuzz()
# print(VolumeFormula(4))
# WriteCSV(records)
Question5(records)