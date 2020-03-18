def majority_vote(list):
    list.sort()
    if len(list)==0:
        return "None"

    for x in range(len(list)):
        num=0
        for y in range(len(list)):
             if list[x]==list[y]:
                 num += 1
        if num>(len(list)/2):
            return list[x]

    return "None"

if __name__=="__main__":
    resenie=majority_vote(["A", "B", "B", "A", "B", "A"])
    print(resenie)