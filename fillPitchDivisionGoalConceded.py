import pandas                 as pd
import matplotlib.patheffects as effect

def fillPitchDivisionGoalConceded(nConcededGoal, axGoalMap, dfGoalCoord, clubColor):
    # Invert x and y coordinate to match vertical pitch

    dfGoalCoord.rename(
                        columns = {"x":"y", "y":"x"},
                        inplace = True
                      )

    # Create and sort data bins

    x_bins = [0 + 20 * x for x in range(0,6)]
    y_bins = [50 + 10 * x for x in range(0,6)]

    x_bins.sort()
    y_bins.sort()

    # Add bins to the data frame
    
    dfGoalCoord["bins_x"] = pd.cut(dfGoalCoord["x"], bins = x_bins)
    dfGoalCoord["bins_y"] = pd.cut(dfGoalCoord["y"], bins = y_bins)
    
    dfGoalCoord =  (
                        dfGoalCoord
                            .sort_values(by = ["bins_y", "bins_x"])
                            .reset_index(drop = True)
                    )

    dfGoalZones = pd.DataFrame(
                                dfGoalCoord[['bins_x', 'bins_y']].value_counts()
                              ).reset_index()

    dfGoalZones.columns = ['zoneX', 'zoneY', 'occurence']

    dfGoalZones = (
                    dfGoalZones.assign(
                                        occurenceShare = lambda x : x.occurence/nConcededGoal
                                      )
                  )

    dfGoalZones = (
                    dfGoalZones.assign(
                                        occurenceScale = lambda x : x.occurenceShare/x.occurenceShare.max()
                                      )
                  )

    # Fill the pitch div

    counter = 0
    for X, Y in zip(dfGoalZones["zoneX"], dfGoalZones["zoneY"]):
        # Fill zones with color gradient
        axGoalMap.fill_between(
                                x      = [X.left, X.right],
                                y1     = Y.left,
                                y2     = Y.right,
                                color  = clubColor,
                                alpha  = dfGoalZones["occurenceScale"].iloc[counter],
                                zorder = -1,
                                lw = 0
                              )
        # Add percentage values as text in zones
        if dfGoalZones['occurenceShare'].iloc[counter] > .02:
                text_ = axGoalMap.annotate(
                                            xy = (X.right - (X.right - X.left)/2, Y.right - (Y.right - Y.left)/2),
                                            text = f"{dfGoalZones['occurenceShare'].iloc[counter]:.0%}",
                                            ha = "center",
                                            va = "center",
                                            color = "white",
                                            size = 12,
                                            weight = "bold",
                                            zorder = 3
                                          )
                text_.set_path_effects(
                                        [
                                            effect.Stroke(
                                                        linewidth  = 1.5,
                                                        foreground = "black"
                                                         ),
                                            effect.Normal()
                                         ]
                                      )
        counter += 1