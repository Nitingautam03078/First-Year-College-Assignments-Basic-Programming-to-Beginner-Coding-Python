# delete a any file 
import os       # improt a 'os' modelosse
if os.path.exists("data.text"):        # used a contition 
    os.remove("data.text")             # used remove function in os liabre 
    print("file is deleted....")        # print statement after do some work
else:
    print("file is not avaliable : ")      
