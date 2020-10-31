#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def loadWords(filename):
    """
    Returns a list of words or integers
    """
    # inFile: file
    inFile = open(filename, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(int(line))
    print("  ", len(wordList), "items loaded.")
    return wordList

integer_list = loadWords("IntegerArray.txt")


def Sort_Count_Inversions(int_list):
    if len(int_list) == 1:
        inv = 0
        return int_list, inv
    elif len(int_list) == 2:
        if int_list[0] > int_list[1]:
            inv = 1
            int_list[0], int_list[1] = int_list[1], int_list[0]
            return int_list, inv
        else:
            inv = 0
            return int_list, inv
    else:
        split = int(len(int_list)/2)
        Left, x = Sort_Count_Inversions(int_list[0:split])
        Right, y = Sort_Count_Inversions(int_list[split:])
        
        def Merge_Count_Inversions(L,R):
            fl = []
            n = len(L) + len(R)
            i = 0
            j = 0
            inv = 0
            for k in range(n):
                if L[i] <= R[j]:
                    fl.append(L[i])
                    i += 1
                    if i == len(L):
                        for m in range(j, len(R)):
                            fl.append(R[m])
                        return fl, inv
                else:
                    fl.append(R[j])
                    j += 1
                    inv += (len(L)-i)
                    if j == len(R):
                        for m in range(i, len(L)):
                            fl.append(L[m])
                        return fl, inv
        
        Full, z = Merge_Count_Inversions(Left,Right)
        return Full, x+y+z
    
# Sort_Count_Inversions(integer_list)[1]