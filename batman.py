def findNumOfStepsRequired(ppl, step):
    total_steps = 0 
    for i in range(1, ppl+1):
        total_steps+= 10*i
    print(total_steps)

findNumOfStepsRequired(3, 10)