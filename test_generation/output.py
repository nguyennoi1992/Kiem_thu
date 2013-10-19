from itertools import *
from input import main
import math
import unittest

class TestSequense(unittest.TestCase):
     
    def setUp(self):
        pass
 
def readExisting():
    try:
        tmpF = open('input.py', 'r')
        arrayParameter = []
        aList = []
        check = 0
        while (True):
            line = tmpF.readline().strip()
            if (len(line) == 0): continue
            if not line: break
            
            split_line = line.replace('(', ' ').replace(')', ' ').replace(':', ' ').replace(',', ' ').split()
            length = len(split_line) - 2
            t = 0
            if split_line[0] == 'def' and split_line[1] == 'main':
                arrayParameter = [0] * length
                for parameter in split_line:
                    if parameter != 'def' and parameter != 'main':
                        arrayParameter[t] = parameter
                        t = t + 1

                check = -1
                continue
            if check == -1:
                check = 1
                continue

            split1_line = line.replace(':', ' ').replace('[', ' ').replace(']', ' ').replace(';', ' ').split()
            if(check >= 1 and check <= len(arrayParameter)):
                tempList = []
                for value in split1_line:
                    tempList.append(value)
                aList.append(tempList)
                check = check + 1
            if check == len(arrayParameter) + 1:
                break
        tmpF.close()
    except IOError:
        pass
    return aList

def sortList():
    List = readExisting()
    for i in List:
        for j in range(1, len(i), 2):
            for k in range(j, len(i), 2):
                if(i[j] > i[k]):
                    temp = i[j]
                    temp_ = i[j + 1]
                    i[j] = i[k]
                    i[j + 1] = i[k + 1]
                    i[k] = temp
                    i[k + 1] = temp_
    return List

def checkList():
    cList = sortList()
    check = 1
    for i in cList:
        for j in range(2, len(i) - 1, 2):
            if(i[j] >= i[j + 1]):
                check = -1
                break
        if(check == -1):
            break
    return check

def createEvalue():
    eList = sortList()
    check = checkList()
    valueList = []
    if check == 1:
        for i in eList:
            t = 0
            temp = []
            for j in i:
                if t % 2 != 0:
                    temp.append(j)
                t = t + 1
            valueList.append(temp)
    return valueList

def createTest():
    List = createEvalue()
    next_list = list(product(*List))
    return next_list

def test_generator(a, b):
    def test(self):
        self.assertEqual(a,b)
    return test

if __name__ == '__main__':

    param_list = createTest()
    check = checkList()
    
    if check == 1:
        for t in param_list:
            test_name = 'test_%s' % param_list.index(t)
            result = main(*t)
            test = test_generator(result, "")
            setattr(TestSequense, test_name, test)
    else:
        raise Exception("wrong input")
    unittest.main()
    
