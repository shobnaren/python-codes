csv_list =[]
with open("try.csv","r") as f:
    f1 = ((f.readline().strip('\n')).split(','))
    for line in f.readlines():
        temp=(line.strip('\n')).split(',')
        csv_dict = {f1[i]: temp[i] for i in range(len(temp))}
        csv_list.append(csv_dict)
    print(csv_list)
