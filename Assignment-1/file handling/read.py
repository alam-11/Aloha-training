fp = open("demofile.txt", "r")

print(fp.read())  # it will read all the data in the file
fp.seek(0)  # this will make the file pointer to pointer back to the start of the file
print(fp.read(3))  # this will read athe

fp.seek(0)
while True:
    temp = fp.readline()
    # print(fp.tell())
    if temp == '':
        break
    print(temp)
fp.close()
