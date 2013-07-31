# iTunes Export Formatter
# Keeps only the columns of the iTunes export that you want to keep

import csv

def pickColumns(column_names):
    for i in range(len(column_names)):
        print str(i) + "\t| " + column_names[i]
    print "\nPlease enter the numbers of the columns you want to keep, separated by spaces."
    user_str = str(raw_input())
    indices_to_keep = [int(x) for x in user_str.split()]
    return indices_to_keep

filename = str(raw_input("Please enter the filename: "))
with open(filename, "rU") as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    header = reader.next()
    indices = pickColumns(header)
    print str(indices)
    with open("output.txt", "w") as output_file:
        for row in reader:
            row_list = []
            for i in indices:
                row_list.append(row[i])
            output_file.write("\t\t".join(row_list))
            output_file.write("\n")