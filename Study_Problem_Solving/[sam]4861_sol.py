def solution(expression):
    answer = 0
    s =''
    operating = [['*','+','-'],
                 ['-','*','+'],
                 ['-','+','*'],
                ['*','+','-'],
                ['*','-','+'],
                ['+','-','*'],
                ['+','*','-']]
    max = 0
    arr = []
    arr2 = []
    for i in range(len(expression)):
        if expression[i] in ['+','-','*']:
            arr.append(int(s))
            arr2.append(expression[i])
            s = ''
        elif i == len(expression)-1:
            s = s+expression[i]
            arr.append(int(s))
        else:
            s = s+expression[i]


    for element in operating:
        temp = arr
        temp2 = arr2
        for i in range(3):
            oper = 0
            while True:

                if temp2[oper] == element[i]:
                    if temp2[oper] == "*":
                        T = temp[oper] * temp[oper+1]
                    elif temp2[oper] == "-":
                        T = temp[oper] - temp[oper + 1]
                    elif temp2[oper] == "+":
                        T = temp[oper] + temp[oper + 1]
                    temp.pop(oper)
                    temp.pop(oper)
                    temp.insert(oper,T)
                    temp2.pop(oper)
                elif oper >= len(temp2)+1:
                    break;
                else:
                    oper += 1


        max = abs(temp)
        print(temp)
    return answer

if __name__ =="__main__":
    expression = "100-200*300-500+20"
    result = solution(expression)
    print(result)
