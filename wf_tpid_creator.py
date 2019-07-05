import csv

monthly_scorecards = open("/Users/knuchegbu/Desktop/FS TAM/Wells Fargo/Book2.csv", "r")
wfcf = open("/Users/knuchegbu/Desktop/FS TAM/Wells Fargo/wfcf.csv", "r")
results = open("/Users/knuchegbu/Desktop/FS TAM/Wells Fargo/results.csv", "w")

csv_m = csv.reader(monthly_scorecards)
csv_w = csv.reader(wfcf)
with results:
    writer = csv.writer(results)

    # for m in csv_m:
    #     if m[0] != 'Wells Fargo Capital Finance':
    #         print(m)
    #         writer.writerow(m)

    #     else:
    #         for w in csv_w:
    #             if w[1] == m[1]:
    #                 z = [w[0],m[1],m[2],m[3],m[4]]
    #                 print(z)
    #                 writer.writerow(z)

new_list=[m[0] for m in csv_m if m[0] != 'Wells Fargo Capital Finance' else for w in csv_w ]
print(new_list)
writer.writerow(new_list)
