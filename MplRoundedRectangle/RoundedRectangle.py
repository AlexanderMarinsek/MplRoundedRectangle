
import matplotlib.path as mpath
import matplotlib.patches as patches
import warnings


def RoundedRectangle( xy=(0.5, 0.5), width=1, height=1, round=[True]*4, corner_function=lambda w,h: h*0.2, **kwargs ):
    """
    Draw rounded rectangle patch using Matplotlib.

    An upgrade to Matplotlib's rectangle patch.
    Contrary to FancyBboxPatch, RoundedRectangle doesn't inflate the rectangle.

    :param xy: Center coordinates of the rounded rectangle
    :type xy: float, float
    :param width: Rectangle width
    :type width: float
    :param height: Rectangle height
    :type height: float
    :param round: Corner rounding indicator (counter clockwise, start at bottom right)
    :type round: list of 4 boolean elements
    :param corner_function: Rounding function (ratio of width, height, both, or constant)
    :type corner_function: function
    :param **kwargs: Arguments for matplotlib patch (color, linewidth, etc.)
    :type **kwargs: kwargs

    :return: Rounded rectangle
    :rtype: matplotlib.patches.PathPatch
    """

    if len(round) != 4:
        raise ValueError ('Round param length not equal to 4: %d' % len(round))

    corner_offset = corner_function(width, height)

    if corner_offset > width*0.5 or corner_offset > height*0.5:
        warnings.warn('Rounding exceedes width/height constraints: %.3f' % corner_offset, UserWarning)

    # Start
    if round[-1] == True:
        verts = [( xy[0] - width / 2 + corner_offset, xy[1] - height / 2 )]
    else:
        verts = [( xy[0] - width/2, xy[1] - height/2 )]

    # Start movement instructions
    codes = [ mpath.Path.MOVETO ]

    # Compose
    if round[0] == True:
        verts += [
            ( xy[0] + width / 2 - corner_offset, xy[1] - height / 2 ),
            ( xy[0] + width / 2, xy[1] - height / 2 ),
            ( xy[0] + width / 2, xy[1] - height / 2 + corner_offset )
        ]
        codes += [ mpath.Path.LINETO, mpath.Path.CURVE3, mpath.Path.CURVE3 ]
    else:
        verts += [
            ( xy[0] + width / 2, xy[1] - height / 2 )
        ]
        codes += [ mpath.Path.LINETO ]

    if round[1] == True:
        verts += [
            ( xy[0] + width / 2, xy[1] + height / 2 - corner_offset ),
            ( xy[0] + width / 2, xy[1] + height / 2 ),
            ( xy[0] + width / 2 - corner_offset , xy[1] + height / 2 )
        ]
        codes += [ mpath.Path.LINETO, mpath.Path.CURVE3, mpath.Path.CURVE3 ]
    else:
        verts += [
            ( xy[0] + width / 2, xy[1] + height / 2 )
        ]
        codes += [ mpath.Path.LINETO ]

    if round[2] == True:
        verts += [
            ( xy[0] - width / 2 + corner_offset, xy[1] + height / 2 ),
            ( xy[0] - width / 2, xy[1] + height / 2 ),
            ( xy[0] - width / 2, xy[1] + height / 2 - corner_offset )
        ]
        codes += [ mpath.Path.LINETO, mpath.Path.CURVE3, mpath.Path.CURVE3 ]
    else:
        verts += [
            ( xy[0] - width / 2, xy[1] + height / 2 )
        ]
        codes += [ mpath.Path.LINETO ]

    if round[3] == True:
        verts += [
            ( xy[0] - width / 2, xy[1] - height / 2 + corner_offset ),
            ( xy[0] - width / 2, xy[1] - height / 2 ),
            ( xy[0] - width / 2 + corner_offset, xy[1] - height / 2 )
        ]
        codes += [ mpath.Path.LINETO, mpath.Path.CURVE3, mpath.Path.CURVE3 ]
    else:
        verts += [
            ( xy[0] - width / 2, xy[1] - height / 2 )
        ]
        codes += [ mpath.Path.LINETO ]

    paths = mpath.Path(verts, codes)
    patch = patches.PathPatch(paths, **kwargs)

    return patch


if __name__ == '__main__':

    from matplotlib import pyplot as plt

    patch = RoundedRectangle(
        xy = [1., 2.], width = 1, height = 1, round = [True, False, True, False], facecolor='C3', lw=2)

    fig, ax = plt.subplots(1, 1)

    ax.add_patch(patch)

    ax.set_xlim(0, 5)
    ax.set_ylim(0, 5)

    plt.show()
