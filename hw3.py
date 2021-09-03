import math
import csv
import tempfile
import os

def Question1():
    for i in range(1,101):
        if i % 3 == 0 and i % 5 ==0:
            print('FizzBuzz')
        elif i % 5 == 0:
            print('Buzz')
        elif i % 3 == 0:
            print('Fizz')
        else:
            print(i)

def Question2(radius):
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
def Question3(input):

    with open('book.csv', 'w', newline='') as output:
        writer = csv.writer(output)
        header = ['Title', 'Author', 'ISBN13', 'Pages']
        # write the header to file
        writer.writerow(header)

        # write each list in records to the csv file
        for row in input:
            writer.writerow(row)
    output.close() # close csv file

def Question4():
    dict = {}

    with open('book.csv', 'r', newline='') as source:
        reader = csv.reader(source)
        header = next(reader)
        for item in header:
            dict[item] = []
        
        for row in reader:
            for item in range(len(row)):
                dict[header[item]].append(row[item])
    source.close()

    print(dict)

def Question5(data):
    tmp = tempfile.NamedTemporaryFile(delete=False)
    header = ['Title', 'Author', 'ISBN13', 'Pages']
    
    dict = {}
    try:
        with open(tmp.name,'w', newline='') as destination:
            writer=csv.writer(destination)
            writer.writerow(header)
            for row in data:
                try:
                    writer.writerow(row)
                except Exception as e:
                    print ('Error in writing row:',e)

            
        with open(tmp.name,'r', newline='') as source:
            reader = csv.reader(source)
            header = next(reader)
            for item in header:
                dict[item] = []
            
            for row in reader:
                for item in range(len(row)):
                    dict[header[item]].append(row[item])
    finally:
        tmp.close()

    print(dict)


Question1()
print(Question2(4))
# Question3(records)
# Question4()
Question5(records)