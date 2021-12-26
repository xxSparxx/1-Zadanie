prefix = input("Введите выражения в префиксной нотации: ")

# prefix = "/ + 3 10 * + 2 4 - 3 5"
# prefix = "+ + 10 20 30"
# prefix = "+ 2 * 2 - 2 1"
# prefix = "+ - 13 4 55"
# prefix = "- - 2 1"
prefixString = prefix.split()

operatorList = list()
numbersList = list()
resultList = list()

result = ''

def toInfix(param = ''):
    if param == 'merge':
        result = '(' + resultList[len(resultList) - 1] + ' ' + operatorList[0] + ' ' + resultList[len(resultList) - 2] + ')'
        resultList.clear()
        operatorList.pop(0)
        return resultList.append(result)
    elif param == 'last':
        result = resultList[0] + ' ' + operatorList[0] + ' ' + numbersList[0]
        operatorList.clear()
        numbersList.clear()
        resultList.clear()
        return resultList.append(result)
    elif param == 'sec':
        result = numbersList[0] + ' ' + operatorList[0] + ' ' + resultList[0]
        numbersList.clear()
        operatorList.clear()
        resultList.clear()
        return resultList.append(result)
    else :
        if len(numbersList) == 3:
            result = '(' + numbersList[0] + ' ' + operatorList[0] + ' ' + numbersList[1] + ')'
            numbersList.pop(0)
            numbersList.pop(0)
            resultList.clear()
            operatorList.pop(0)
            return resultList.append(result)
        elif len(numbersList) >= 2 and len(operatorList) >= 1:
            result = '(' + numbersList[len(numbersList) - 2] + ' ' + operatorList[0] + ' ' + numbersList[len(numbersList) - 1] + ')'
            numbersList.pop(len(numbersList) - 1)
            numbersList.pop(len(numbersList) - 1)
            operatorList.pop(0)
            return resultList.append(result)
        else:
            result = resultList[len(resultList) - 1] + ' ' + operatorList[0] + ' ' + resultList[len(resultList) - 2]
            resultList.clear()
            operatorList.pop(0)
            return resultList.append(result)


if len(prefixString) < 4:
    print("Вы ввели неверное выражение")
else:
    for value in reversed(prefixString):
        if value == '/' or value == '*' or value == '-' or value == '+':
            operatorList.insert(0,value)
            if len(resultList) >= 2 and len(operatorList) >= 1:
                toInfix('merge')
            elif len(resultList) == 1 and len(numbersList) == 1 and len(operatorList) == 1:
                toInfix('sec')
            elif len(numbersList) >= 2 and len(operatorList) >= 1:
                toInfix()
        elif value.isdigit():
            numbersList.insert(0, value)
            if len(numbersList) >= 2 and len(operatorList) >= 1 and prefixString[0].isdigit() != 1:
                toInfix()
        else:
            print('Вы ввели неверное выражение')

    if len(numbersList) != 0 and len(operatorList) != 0:
        toInfix('last')
    elif len(numbersList) == 0 and len(operatorList) != 0:
        result = operatorList[0] + ' ' + resultList[0]
        resultList.clear()
        operatorList.clear()
        resultList.append(result)

    correctResult = resultList[0].split()
    print(resultList[0])