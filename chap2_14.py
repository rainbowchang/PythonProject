# import csv
#
# with open("mytest.csv", 'a') as r:
#     writer = csv.writer(r)
#     writer.writerow([41, 42, 43])
#     writer.writerow([51, 52, 53])
#     writer.writerow([51, 52, 53])
# print("写入完毕！")
#
# exit()

import time


def test():
    start = time.time()
    print(start)
    time.sleep(4.1)
    end = time.time()
    print(end)
    during = end - start
    print(during)


test()

