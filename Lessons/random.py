while True:
    finalScore = int(input("Final score: "))
    allscores = [73, 88, 92, 73.68, finalScore]
    if finalScore > 73:
        allscores[0] = allscores[0] + ((finalScore - allscores[0])/2)
    
    finalGrade = allscores[0] * 0.15 + allscores[1] * 0.2 + allscores[2] * 0.2 + allscores[3] * 0.15 + allscores[4] * 0.3
    print(finalGrade)