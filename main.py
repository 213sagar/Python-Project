# function defination for most_grequent
def most_frequent(stringinput):
    if(stringinput  != ""):
        temp=list(stringinput)
        dic={}

        for i in temp:
            if(i in dic):
                dic[i]=dic[i]+1
            else:
                dic[i]=1
        return dic

if(__name__ == "__main__"):
    dic=most_frequent("Mississippi")
    if (dic is not None):
        temp= sorted(dic.items(),key=lambda x : (x[1],x[0]))
        for i in temp[::-1]:
            print(i[0] +"  -  "+str(i[1]))
    else:
        print("Invalid Input")
