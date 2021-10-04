# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 14:15:29 2021

@author: BektasBaysal
"""
def sortList(array):
    """ listedeki elemanları büyükten küçüğe sıralama methodu"""
    print("sort içinde")
    for i in range(len(array)):
        
        IlkDeger = i
        
        for j in range(i+1, len(array)):
            if array[j] < array[IlkDeger]:
                IlkDeger = j
        array[i], array[IlkDeger] = array[IlkDeger], array[i]
        
    return array




def CypherKey(numbers, key):
    """ Şifre oluşturma"""
    NumberList = []

    """string haldeki sayıları bir listeye dönüştürme"""
    for i in numbers:
        NumberList.append(i)
    key = [int(x) for x in str(key)]
    """listedi sayıları integer hale dönüştürme"""
    for i in range(len(NumberList)):
        NumberList[i] = int(NumberList[i])
        
    NewList = sortList(NumberList.copy())
    # print(NewList) 
    """şifredeki ilk sayının, sayı listesindeki indeksini sayının sonuna ekleme """
    for i in range(len(NewList)):
        if NewList[i] == key[0]:
            NewList.append(i)
            break
        
    # print("org:"+ str(NumberList))
    # print("Result:"+ str(NewList) )   
    """şifreyi string formatına çevirme işlemi""" 
    StrList = ''.join([str(i) for i in NewList]) 
    print(StrList)
    StrListV2 = '"' + StrList +'"'
    
    print(StrListV2)
    return NewList,key

firstNumbers = str(input("key: "))
Key = input("number: ")

Result, key = CypherKey(firstNumbers, Key)
       
