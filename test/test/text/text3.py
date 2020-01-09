with open(".\dataset_3363_4.txt") as inf:
    m1 = 0
    m2 = 0
    m3 = 0
    n = 0
    for line in inf:
        line = line.strip().split(";")
        print((int(line[1]) + int(line[2]) + int(line[3])) / 3)
        n += 1
        m1 += int(line[1])
        m2 += int(line[2])
        m3 += int(line[3])
    print(m1 / n, m2 / n, m3 / n)


