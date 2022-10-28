import matplotlib.pyplot as plt

from mplsoccer import PyPizza, FontManager

def makeComparisonRadar(clubColors, playerName, playerValues, leagueValues):

    fontNormal = FontManager('https://github.com/google/fonts/blob/main/ofl/barlowcondensed/BarlowCondensed-Medium.ttf?raw=true')
    
    # parameter and value list
    params = [
                "Defending Duel Success Rate\n(vs PL Defenders)",
                "Air Duel Success Rate\n(vs PL Players)",
                "Interceptions\n(vs PL Defenders)",
                "Red Cards Per Game\n(vs PL Players)"
             ]
    
    
    # Min and Max range for parameters
    min_range = [0, 0, 0, 0]
    max_range = [50, 90.6, 10.4, 0.08]
    
    params_offset = [
                        True,
                        True,
                        True,
                        False,
                    ]
    

    # instantiate PyPizza class
    baker = PyPizza(
                        params              = params,
                        min_range           = min_range,   
                        max_range           = max_range,
                        straight_line_color = "white",
                        straight_line_lw    = 2,
                        last_circle_color   = "black",
                        last_circle_lw      = 5,
                        background_color    = "white"
                   )
    
    # plot pizza
    fig, ax = baker.make_pizza(
                                playerValues,
                                compare_values    = leagueValues,
                                figsize           = (10, 10),
                                color_blank_space = ["#C5C5C5"] * len(params),
                                blank_alpha       = 0.7,          
                                param_location    = 110,
                                # Values to be used when plotting slices
                                kwargs_slices     = dict(
                                                            facecolor = clubColors[0],
                                                            edgecolor = "white",
                                                            zorder    = 2,
                                                            linewidth = 2
                                                        ),
                                # Values to be used when plotting comparison slices
                                kwargs_compare    = dict(
                                                            facecolor = "black",
                                                            alpha     = 0.4,
                                                            edgecolor = "white",
                                                            zorder    = 2,
                                                            linewidth = 2,
                                                        ),
                                # Values to be used when adding parameter
                                kwargs_params     = dict(
                                                            color          = "black",
                                                            fontsize       = 24,
                                                            fontproperties = fontNormal.prop,
                                                            va             = "center"
                                                        ),
                                # Values to be used when adding parameter-values
                                kwargs_values     = dict(
                                                            color          = "white",
                                                            fontsize       = 16,
                                                            fontproperties = fontNormal.prop,
                                                            zorder         = 4,
                                                            bbox           = dict(
                                                                                    edgecolor = "white",
                                                                                    facecolor = clubColors[1],
                                                                                    boxstyle  = "circle,pad = 0.4",
                                                                                    lw        = 2
                                                                                 )
                                                        ),
                                # Values to be used when adding comparison-values
                                kwargs_compare_values = dict(
                                                                color          = "white",
                                                                fontsize       = 16,
                                                                fontproperties = fontNormal.prop,
                                                                zorder         = 3,
                                                                bbox = dict(
                                                                                edgecolor = "white",
                                                                                facecolor = "black",
                                                                                boxstyle  = "circle,pad=0.4",
                                                                                lw        = 2
                                                                            )
                                                            )                         
                              )

    baker.adjust_texts(params_offset, offset = -0.25)
    
    plt.show()