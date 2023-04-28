def pascal(list,n):
    if n > 1:
        answer = []
        answer.append(1)
        for i in range(len(list)-1):
            answer.append(list[i]+list[i+1])
        answer.append(1)
        n -= 1
        return pascal(answer,n)
    if n == 1:
        return list

start_list=[1]
a=pascal(start_list, 8)
print("real_result",a)
