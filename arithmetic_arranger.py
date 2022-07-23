#this is my proposed solution to problem 1 given by freecodecamp 
# for Scientific Computing with Python certification

data=list()
class splitt:
    def __init__(self,data,solve=False):
        self.data=data
        self.solve=solve
#---------------------------------Defining Errors---------------------------------#          
        if len(data)>5:
            print("Error: Too many problems.")                    
        elif len(data)<6:           
            for w in range(1):
                y=list()
                for i,k in enumerate(data):
                    y.append(data[i].split(" "))
                    try:
                        if type(int(y[i][0]))!= int or type(int(y[i][2]))!=int:
                            print("Error: Numbers must only contain digits")
                    except ValueError:
                        print("Error: Numbers must only contain digits")
                        w+=2
                        break
                        
                    if len(y[i][0])>4  or len(y[i][2])>4 :
                        print("Error: Numbers cannot be more than four digits.")
                        w+=2
                        break
                    
                    elif y[i][1]!= "+" and y[i][1]!= "-" :
                        print("Error: Operator must be '+' or '-'.")
                        w+=2
                        break
                                               
                if w==2:
                    break   
 #---------------------------Evaluating list length------------------------#
 # Each block evaluates size, performs split, generates lines for the result 
 # and prints according to the constraints of the given problem in file.pdf
 # --------------------------Block 1---------------------------------------#            
                if len(data)==1:
                    b0=data[0].split(" ")
                    if b0[1]== "+" :
                        res0=int(b0[0])+int(b0[2])
                    elif b0[1]== "-":
                        res0=int(b0[0])-int(b0[2])
                    d=max(len(b0[0]),len(b0[2]))
                    ilis0=""
                    t="-"
                    for s in range(d+2):
                        ilis0+=t
                    if self.solve==True:
                        print((f"{b0[0]}").rjust(len(ilis0)," "))
                        print(((f"{b0[1]}")),(f"{b0[2]}").rjust(len(ilis0)-2," "))
                        print(f"{ilis0}")
                        print((f"{res0}").rjust(len(ilis0)," "))

                    else :
                        print((f"{b0[0]}").rjust(len(ilis0)," "))
                        print(((f"{b0[1]}")),(f"{b0[2]}").rjust(len(ilis0)-2," "))
                        print(f"{ilis0}")

# --------------------------Block 2---------------------------------------#  

                elif len(data)==2:
                    b0=data[0].split(" ")
                    b1=data[1].split(" ")
                    if b0[1]== "+" :
                        res0=int(b0[0])+int(b0[2])
                    elif b0[1]== "-":
                        res0=int(b0[0])-int(b0[2])
                    if b1[1]== "+" :
                        res1=int(b1[0])+int(b1[2])
                    elif b1[1]== "-" :
                        res1=int(b1[0])-int(b1[2])
                    d=max(len(b0[0]),len(b0[2]))
                    e=max(len(b1[0]),len(b1[2]))
                    ilis0=""
                    ilis1=""
                    t="-"
                    for s in range(d+2):
                        ilis0+=t
                    for s in range(e+2):
                        ilis1+=t
                    if self.solve==True:
                        print((f"{b0[0]}").rjust(len(ilis0)," "),(f"{b1[0]}").rjust(len(ilis1)," "),sep="    ")
                        print(((f"{b0[1]}")),(f"{b0[2]}").rjust(len(ilis0)-2," "),((f"   {b1[1]}")),(f"{b1[2]}").rjust(len(ilis1)-2," "))
                        print((f"{ilis0}"),(f"{ilis1}"),sep="    ")
                        print((f"{res0}").rjust(len(ilis0)," "),(f"{res1}").rjust(len(ilis1)," "),sep="    ")
                        q=+1
                    else :
                        print((f"{b0[0]}").rjust(len(ilis0)," "),(f"{b1[0]}").rjust(len(ilis1)," "),sep="    ")
                        print(((f"{b0[1]}")),(f"{b0[2]}").rjust(len(ilis0)-2," "),((f"   {b1[1]}")),(f"{b1[2]}").rjust(len(ilis1)-2," "))
                        print((f"{ilis0}"),(f"{ilis1}"),sep="    ")

# --------------------------Block 3---------------------------------------#  

                elif len(data)==3:
                    b0=data[0].split(" ")
                    b1=data[1].split(" ")
                    b2=data[2].split(" ")
                    if b0[1]== "+" :
                        res0=int(b0[0])+int(b0[2])
                    elif b0[1]== "-":
                        res0=int(b0[0])-int(b0[2])
                    if b1[1]== "+" :
                        res1=int(b1[0])+int(b1[2])
                    elif b1[1]== "-" :
                        res1=int(b1[0])-int(b1[2])
                    if b2[1]== "+" :
                        res2=int(b2[0])+int(b2[2])
                    elif b2[1]== "-":
                        res2=int(b2[0])-int(b2[2])
                    d=max(len(b0[0]),len(b0[2]))
                    e=max(len(b1[0]),len(b1[2]))
                    f=max(len(b2[0]),len(b2[2]))
                    ilis0=""
                    ilis1=""
                    ilis2=""
                    t="-"
                    for s in range(d+2):
                        ilis0+=t
                    for s in range(e+2):
                        ilis1+=t
                    for s in range(f+2):
                        ilis2+=t
                    if self.solve==True:
                        print((f"{b0[0]}").rjust(len(ilis0)," "),(f"{b1[0]}").rjust(len(ilis1)," "),(f"{b2[0]}").rjust(len(ilis2)," "),sep="    ")
                        print(((f"{b0[1]}")),(f"{b0[2]}").rjust(len(ilis0)-2," "),((f"   {b1[1]}")),(f"{b1[2]}").rjust(len(ilis1)-2," "),((f"   {b2[1]}")),(f"{b2[2]}").rjust(len(ilis2)-2," "))
                        print((f"{ilis0}"),(f"{ilis1}"),(f"{ilis2}"),sep="    ")
                        print((f"{res0}").rjust(len(ilis0)," "),(f"{res1}").rjust(len(ilis1)," "),(f"{res2}").rjust(len(ilis2)," "),sep="    ")
                        q=+1
                    else :
                        print((f"{b0[0]}").rjust(len(ilis0)," "),(f"{b1[0]}").rjust(len(ilis1)," "),(f"{b2[0]}").rjust(len(ilis2)," "),sep="    ")
                        print(((f"{b0[1]}")),(f"{b0[2]}").rjust(len(ilis0)-2," "),((f"   {b1[1]}")),(f"{b1[2]}").rjust(len(ilis1)-2," "),((f"   {b2[1]}")),(f"{b2[2]}").rjust(len(ilis2)-2," "))
                        print((f"{ilis0}"),(f"{ilis1}"),(f"{ilis2}"),sep="    ")

# --------------------------Block 4---------------------------------------#
  
                elif len(data)==4:
                    b0=data[0].split(" ")
                    b1=data[1].split(" ")
                    b2=data[2].split(" ")
                    b3=data[3].split(" ")
                    if b0[1]== "+" :
                        res0=int(b0[0])+int(b0[2])
                    elif b0[1]== "-":
                        res0=int(b0[0])-int(b0[2])
                    if b1[1]== "+" :
                        res1=int(b1[0])+int(b1[2])
                    elif b1[1]== "-" :
                        res1=int(b1[0])-int(b1[2])
                    if b2[1]== "+" :
                        res2=int(b2[0])+int(b2[2])
                    elif b2[1]== "-":
                        res2=int(b2[0])-int(b2[2])
                    if b3[1]== "+" :
                        res3=int(b3[0])+int(b3[2])
                    elif b3[1]== "-":
                        res3=int(b3[0])-int(b3[2])
                    d=max(len(b0[0]),len(b0[2]))
                    e=max(len(b1[0]),len(b1[2]))
                    f=max(len(b2[0]),len(b2[2]))
                    g=max(len(b3[0]),len(b3[2]))
                    ilis0=""
                    ilis1=""
                    ilis2=""
                    ilis3=""
                    t="-"
                    for s in range(d+2):
                        ilis0+=t
                    for s in range(e+2):
                        ilis1+=t
                    for s in range(f+2):
                        ilis2+=t
                    for s in range(g+2):
                        ilis3+=t
                    if self.solve==True:
                        print((f"{b0[0]}").rjust(len(ilis0)," "),(f"{b1[0]}").rjust(len(ilis1)," "),(f"{b2[0]}").rjust(len(ilis2)," "),(f"{b3[0]}").rjust(len(ilis3)," "),sep="    ")
                        print(((f"{b0[1]}")),(f"{b0[2]}").rjust(len(ilis0)-2," "),((f"   {b1[1]}")),(f"{b1[2]}").rjust(len(ilis1)-2," "),((f"   {b2[1]}")),(f"{b2[2]}").rjust(len(ilis2)-2," "),((f"   {b3[1]}")),(f"{b3[2]}").rjust(len(ilis3)-2," "))
                        print((f"{ilis0}"),(f"{ilis1}"),(f"{ilis2}"),(f"{ilis3}"),sep="    ")
                        print((f"{res0}").rjust(len(ilis0)," "),(f"{res1}").rjust(len(ilis1)," "),(f"{res2}").rjust(len(ilis2)," "),(f"{res3}").rjust(len(ilis3)," "),sep="    ")

                    else :
                        print((f"{b0[0]}").rjust(len(ilis0)," "),(f"{b1[0]}").rjust(len(ilis1)," "),(f"{b2[0]}").rjust(len(ilis2)," "),(f"{b3[0]}").rjust(len(ilis3)," "),sep="    ")
                        print(((f"{b0[1]}")),(f"{b0[2]}").rjust(len(ilis0)-2," "),((f"   {b1[1]}")),(f"{b1[2]}").rjust(len(ilis1)-2," "),((f"   {b2[1]}")),(f"{b2[2]}").rjust(len(ilis2)-2," "),((f"   {b3[1]}")),(f"{b3[2]}").rjust(len(ilis3)-2," "))
                        print((f"{ilis0}"),(f"{ilis1}"),(f"{ilis2}"),(f"{ilis3}"),sep="    ")

# --------------------------Block 5---------------------------------------#  

                elif len(data)==5:
                    b0=data[0].split(" ")
                    b1=data[1].split(" ")
                    b2=data[2].split(" ")
                    b3=data[3].split(" ")
                    b4=data[4].split(" ")
                    if b0[1]== "+" :
                        res0=int(b0[0])+int(b0[2])
                    elif b0[1]== "-":
                        res0=int(b0[0])-int(b0[2])
                    if b1[1]== "+" :
                        res1=int(b1[0])+int(b1[2])
                    elif b1[1]== "-" :
                        res1=int(b1[0])-int(b1[2])
                    if b2[1]== "+" :
                        res2=int(b2[0])+int(b2[2])
                    elif b2[1]== "-":
                        res2=int(b2[0])-int(b2[2])
                    if b3[1]== "+" :
                        res3=int(b3[0])+int(b3[2])
                    elif b3[1]== "-":
                        res3=int(b3[0])-int(b3[2])
                    if b4[1]== "+" :
                        res4=int(b4[0])+int(b4[2])
                    elif b4[1]== "-":
                        res4=int(b4[0])-int(b4[2])
                    d=max(len(b0[0]),len(b0[2]))
                    e=max(len(b1[0]),len(b1[2]))
                    f=max(len(b2[0]),len(b2[2]))
                    g=max(len(b3[0]),len(b3[2]))
                    h=max(len(b4[0]),len(b4[2]))
                    ilis0=""
                    ilis1=""
                    ilis2=""
                    ilis3=""
                    ilis4=""
                    t="-"
                    for s in range(d+2):
                        ilis0+=t
                    for s in range(e+2):
                        ilis1+=t
                    for s in range(f+2):
                        ilis2+=t
                    for s in range(g+2):
                        ilis3+=t
                    for s in range(h+2):
                        ilis4+=t
                    if self.solve==True:
                        print((f"{b0[0]}").rjust(len(ilis0)," "),(f"{b1[0]}").rjust(len(ilis1)," "),(f"{b2[0]}").rjust(len(ilis2)," "),(f"{b3[0]}").rjust(len(ilis3)," "),(f"{b4[0]}").rjust(len(ilis4)," "),sep="    ")
                        print(((f"{b0[1]}")),(f"{b0[2]}").rjust(len(ilis0)-2," "),((f"   {b1[1]}")),(f"{b1[2]}").rjust(len(ilis1)-2," "),((f"   {b2[1]}")),(f"{b2[2]}").rjust(len(ilis2)-2," "),((f"   {b3[1]}")),(f"{b3[2]}").rjust(len(ilis3)-2," "),((f"   {b4[1]}")),(f"{b4[2]}").rjust(len(ilis4)-2," "))
                        print((f"{ilis0}"),(f"{ilis1}"),(f"{ilis2}"),(f"{ilis3}"),(f"{ilis4}"),sep="    ")
                        print((f"{res0}").rjust(len(ilis0)," "),(f"{res1}").rjust(len(ilis1)," "),(f"{res2}").rjust(len(ilis2)," "),(f"{res3}").rjust(len(ilis3)," "),(f"{res4}").rjust(len(ilis4)," "),sep="    ")

                    else :
                        print((f"{b0[0]}").rjust(len(ilis0)," "),(f"{b1[0]}").rjust(len(ilis1)," "),(f"{b2[0]}").rjust(len(ilis2)," "),(f"{b3[0]}").rjust(len(ilis3)," "),(f"{b4[0]}").rjust(len(ilis4)," "),sep="    ")
                        print(((f"{b0[1]}")),(f"{b0[2]}").rjust(len(ilis0)-2," "),((f"   {b1[1]}")),(f"{b1[2]}").rjust(len(ilis1)-2," "),((f"   {b2[1]}")),(f"{b2[2]}").rjust(len(ilis2)-2," "),((f"   {b3[1]}")),(f"{b3[2]}").rjust(len(ilis3)-2," "),((f"   {b4[1]}")),(f"{b4[2]}").rjust(len(ilis4)-2," "))
                        print((f"{ilis0}"),(f"{ilis1}"),(f"{ilis2}"),(f"{ilis3}"),(f"{ilis4}"),sep="    ")  
                    
            