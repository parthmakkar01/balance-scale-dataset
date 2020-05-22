# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 15:30:14 2019

@author: hp
"""

import numpy as np

#import numpy as np
def balance_fun(r,l):
        r1=-1
        l1=-1
        v=0
        v1=0
        if(r>l):
            k=r-l
            l1=k
        else:
            k=l-r
            r1=k
        if(r1!=-1):
            if(r1%2==0):
                 r1=r1/2
        else:
            v=1
            r1=r1-1
            r1=r1/2
            
        if(l1!=-1):
            if(l1%2==0):
                l1=l1/2
        else:
            v1=1
            l1=l1-1
            l1=l1/2
     #   print('r1:',r1)
        x=np.genfromtxt('pro.csv',delimiter=',')
        for i in range(625):
            temp=x[i][0] * x[i][1] 
            temp1=x[i][2] * x[i][3]
            if(v==1):
                if(temp1<temp):
                    x[i][0]=x[i][2]
                    x[i][1]=x[i][3]
            if(v1==1):
                if(temp<temp1):
                    x[i][0]=x[i][2]
                    x[i][1]=x[i][3]
            
            if(l1>0):
                if(temp<temp1):
                    x[i][0]=x[i][2]+1
                    #print('x[i][0] :',x[i][0])
                    x[i][1]=x[i][3]+2
                    l1=l1-1
            elif(r1>0):
                if(temp1<temp):
                    print('yes r1:',r1)
                    x[i][2]=x[i][0]+1
                    x[i][3]=x[i][1]+2
                    r1=r1-1
            else:
                break
        target_value = 0;   #neutral
        lrate= 0.6
        b=0;
        l=0;
        r=0;
        kk=0
        for i in range(625):
            temp=x[i][0] * x[i][1] 
            temp1=x[i][2] * x[i][3]
        
            if(temp==temp1):
                b=b+1
            #print('scale is balanced : ')
            elif(temp<temp1):
                r=r+1
            #print('scale is on the right ')
            else:
                l=l+1
           # print('scale is on the left')
       
        
        print('scale is balanced :', b)
        print('scale is on left :', l)
        print('scale is on right :', r)



        total=b+l+r

        bal=(b*100)/total
        rig=(r*100)/total
        lef=(l*100)/total


        print('balanced percentage ',bal)
        print('right tip percentage ',rig)
        print('left tip percentage ',lef)

        if(r==l):
            v=0
            if(v==target_value):
                print('scale is balanced')
            else:
                kk=1
                print('scale is not balanced')
        else:
            balance_fun(r,l)
            


    
    
def start():    
    x=np.genfromtxt('pro.csv',delimiter=',')
#x = np.array([[ 1, 1, 0, 0],[0, 0, 0, 1],[1, 0, 0, 0],[0, 0, 1, 1]])
    
#w =np.array([[0.2 ,0.8], [0.6, 0.4], [0.5, 0.7], [0.9, 0.3]])
    w =np.array([[1 ,1], [1, 1], [1, 1], [1, 1]])
#t=np.array([0,0,1,1])
    target_value = 0;   #neutral
    lrate= 0.6
    b=0;
    l=0;
    r=0;
    kk=0
    e=1
    D=[0,0]
    print('learning rate of this epoch is',lrate)
    while(e<=1):
        print('Epoch is',e);
    
        for i in range(625):
            temp=x[i][0] * x[i][1] * w[1][1]
            temp1=x[i][2] * x[i][3] * w[1][1]
        
            if(temp==temp1):
                b=b+1
            #print('scale is balanced : ')
            elif(temp<temp1):
                r=r+1
            #print('scale is on the right ')
            else:
                l=l+1
           # print('scale is on the left')
        e=e+1
        
    print('scale is balanced :', b)
    print('scale is on left :', l)
    print('scale is on right :', r)



    total=b+l+r

    bal=(b*100)/total
    rig=(r*100)/total
    lef=(l*100)/total


    print('balanced percentage ',bal)
    print('right tip percentage ',rig)
    print('left tip percentage ',lef)

    if(r==l):
        v=0
        if(v==target_value):
            print('scale is balanced')
    else:
        kk=1
        print('scale is not balanced')



    if(kk==1):
        print('if you want to make scale balance then press 0 :')
        num=input()
        if(num=='0'):
            print('yes')
            balance_fun(r,l)
        else:
            print('')
start()       
    
    





