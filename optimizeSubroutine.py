import sim as sim

def optimize(EngineChoice, timeStepSeconds, timeLimitSeconds, solveFor, engineRange):
    trials = []
    for i in range(1, engineRange):
        trials.append(sim.calculateSim(EngineChoice, timeStepSeconds, timeLimitSeconds, 0, i))
    optimizeIndex = 0
    if solveFor == "maxHeight":
        solveForIndex = 1
    elif solveFor == "maxVelocity":
        solveForIndex = 2
    elif solveFor == "maxThrust":
        solveForIndex = 3
    elif solveFor == "maxAcceleration":
        solveForIndex = 4

    maxValue = 0
    for i in trials:
        tempVal = max(i[solveForIndex])
        if tempVal > maxValue:
            maxValue = tempVal
            optimizeIndex = trials.index(i)

    optimalHeight = trials[optimizeIndex][1]
    engineNumber = optimizeIndex
    optimalTime = trials[optimizeIndex][0]
    optimalVelocity = trials[optimizeIndex][2]
    optimalThrust = trials[optimizeIndex][3]
    optimalAcceleration = trials[optimizeIndex][4]
    optimalQ = trials[optimizeIndex][5]

    return engineNumber, optimalTime, optimalHeight, optimalVelocity, optimalThrust, optimalAcceleration, optimalQ