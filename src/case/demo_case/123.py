for i in ['', '0', '']:
    if i.isdigit():
        print(type(i))
    else:
        continue

a = [1, 2, 3]
b = [1, 2, 6, 9, 12]
print(set(a) & set(b))  # 交集 {1, 2}
print(set(a) | set(b))  # 并集 {1, 2, 3, 6, 9, 12}
print(set(a) ^ set(b))  # 异或，就是两个集合去掉交集的那部分 {3, 6, 9, 12}
print(set(a) - set(b))  # 差集，就是a去掉b中元素剩下的那部分 {3}


days = ['day 1', 'day 2', 'day 3', 'day 4', 'day 5', 'day 6', 'day 7']
golds = [10,30,15,20,25,30,35]
dicts = dict()
for i in range(7):
    dicts[days[i]] = golds[i]

print(dicts.keys())

