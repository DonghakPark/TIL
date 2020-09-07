def solution(logs):
    dig = []
    let = []

    for log in logs:
        if log.split()[1].isdigit():
            dig.append(log)
        else:
            let.append(log)

    let.sort(key = lambda x: (x.split()[1:], x.split()[0]))

    for element in dig:
        let.append(element)

    return let

if __name__=="__main__":
    logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    answer = ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
    if solution(logs) == answer:
        print("correct")
    else:
        print("Wrong")