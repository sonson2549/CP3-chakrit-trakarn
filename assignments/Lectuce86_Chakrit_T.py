import csv

with open('86.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column  {", ".join(row)}')
            line_count += 1
        else:
            print(f'\tname are {row[0]} ,like {row[1]} movie, and like{row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')