# copy a data old file to other new file using exception

try:
    with open("data.text") as f2:
        with open("data2.text",'w') as f3:
            for i in f2:
                f3.write(i)
except:
    print("file not copy first creat a file : ")
else:
    f2.close()
    print("file is close : ")
