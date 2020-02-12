i = open("purchases.txt", "r")
o = open("01.txt", "w")

for line in i:
    datalist = line.strip().split("    ")
    date, time,store, item, cost, paymentType = datalist
    o.write(paymentType + "\t" + "1" + "\n")

i.close()
o.close()