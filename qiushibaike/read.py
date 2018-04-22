import csv

filename = input('输入csv文件名')
reader = csv.reader(open(filename, 'rt'))
for row in reader:
    i = input('按enter输出一条段子...')
    print('{0}赞，{3}评论>>>>>>>>>>>>>>>>>>>>>>作者：{1}\n{2}\n'.format(row[0], row[2], row[1], row[3]))



# import csv

# filename = '00.csv'
# # filename = input('输入csv文件名')
# writer = csv.writer(open(filename, 'wt'))
# for row in item:
#     writer.writerow(row)