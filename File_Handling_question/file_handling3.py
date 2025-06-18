# with out creat a file to red and used except method in file handling 

try:
    f = open("data2.text",'r')
    print(f.readlines())
except:
    print("file is not available... first creat file ")
else:
    f.close()
    print("file is close : ")