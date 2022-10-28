from mplsoccer import VerticalPitch

def drawDividedPitch(ax , grids = False):
    '''
    This function returns a vertical football pitch
    divided in specific locations.

    Arguments passed as parameters :
        ax    (obj)  : a matplotlib axes
        grids (bool) : should draw the grid lines or not
    '''

    # Draw a vertical pitch
    pitch = VerticalPitch (
                            pitch_type = "opta",
                            half       = True,
                            label      = False,
                            tick       = False,
                            goal_type  = 'box',
                            linewidth  = 3,
                            line_color = 'black'
                          )

    pitch.draw(ax = ax)

    # Draw the divisions
    if grids:
        y_lines = [100 - 10 * x for x in range(1,10)]
        x_lines = [100 - 20 * x for x in range(1,10)]

        for i in x_lines:
            ax.plot(
                        [i, i],
                        [0, 100], 
                        color  = "lightgray", 
                        ls     = "--",
                        lw     = 2,
                        zorder = -1
                   )
        for j in y_lines:
            ax.plot(
                        [100, 0],
                        [j, j],
                        color  = "lightgray", 
                        ls     = "--",
                        lw     = 2,
                        zorder = -1
                   )

    return ax