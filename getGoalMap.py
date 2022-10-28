import matplotlib.pyplot as plt

def getGoalMap():
    figGoalMap = plt.figure(
                                figsize = (4,4),
                                dpi = 800
                           )
    axGoalMap  = plt.subplot(111)
    
    return figGoalMap, axGoalMap