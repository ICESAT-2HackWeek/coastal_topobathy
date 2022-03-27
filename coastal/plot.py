# -*- coding: utf-8 -*-
"""
Plotting helpers.

"""
import matplotlib.pyplot as plt
import numpy as np

from oa import dataCollector


def plot_atl08(df, figsize=None):
    """
    Plot the ATL08 classifications.

    Refactored from DataDownload/SlideRule_example.ipynb by @eeholmes
    """
    if figsize is None:
        figsize = [8, 6]

    fig = plt.figure(figsize=figsize)

    colors = {0: ['gray', 'noise'],
              4: ['pink', 'unclassified'],
              2: ['green', 'canopy'],
              3: ['lime', 'canopy_top'],
              1: ['brown', 'ground']}

    d0 = np.min(df['segment_dist'])

    for class_val, color_name in colors.items():
        ii = df['atl08_class'] == class_val
        plt.plot(df['segment_dist'][ii] + df['distance'][ii] - d0,
                 df['height'][ii],
                 'o', markersize=1, color=color_name[0], label=color_name[1])

    plt.legend(loc=3, frameon=False, markerscale=5)
    # plt.gca().set_xlim([26000, 30000])
    # plt.gca().set_ylim([2950, 3150])

    plt.ylabel('height, m')
    plt.xlabel('$x_{ATC}$, m')

    return fig


def plot_yapc(df, vmin=100, vmax=255, figsize=None):
    """
    YAPC classifications.

    Refactored from DataDownload/SlideRule_example.ipynb by @eeholmes
    """
    if figsize is None:
        figsize = [10, 6]

    fig = plt.figure(figsize=figsize)

    d0 = np.min(df['segment_dist'])
    ii = np.argsort(df['yapc_score'])
    plt.scatter(df['segment_dist'][ii] + df['distance'][ii] - d0,
                df['height'][ii],
                2, c=df['yapc_score'][ii],
                vmin=vmin, vmax=vmax, cmap='plasma_r')
    plt.colorbar(label='YAPC score')
    # plt.gca().set_xlim([26000, 30000])
    # plt.gca().set_ylim([2950, 3150])

    plt.ylabel('height, m')
    plt.xlabel('$x_{ATC}$, m')

    return fig


def plot_from_oa_url(gtx, url=None, latlims=None, lonlims=None, rgt=None, date=None, title='ICESat-2 Data',
                     verbose=False):
    """Download and plot from OpenAltimetry.

    Refactored from DataDownload/OpenAltimetry_example.ipynb by @eeholmes

    Get data URL from the OpenAltimetry API
    * Go to [openaltimetry.org](https://openaltimetry.org/)
    * Select **BROWSE ICESAT-2 DATA**.
    * Select **ATL 08** on the left
    * Select a date
    * Click **SELECT A REGION** on the top left, and drew a rectangle
    * Right click on the rectangle and select **View Elevation profile**. This opens a pop up, and shows ATL06 and
        ATL08 elevations.
    * Scroll to the **bottom** and select **Get API URL**. Copy it.

    Note, we don't need EarthData credentials for this.

    Alternatively, we could use a date, track number, beam, and lat/lon bounding box as input to the `dataCollector`.

    Parameters
    ----------
    gtx : str
        Beam to look for. E.g., 'gt1r' or 'gt2r'.
    url : str, optional
        OpenAltimetry API URL. Required if the search parameters are not provided.
    latlims : list, optional
        Latitude limits for the boundary box.
    lonlims : list, optional
        Longitude limits for the boundary box.
    rgt : int, optional
        Track number
    date : str, optional
        Date to look for. Use 'YYYY-MM-DD'.
    title : str, optional
        Plot title.
    verbose : bool, default False
        Controls verbosity of the data collection process.

    Returns
    -------
    myplot : plt.Figure
        Handle for the resulting plot.
    mydata : pd.DataFrame
        Downloaded data.

    """
    # make sure we have all the parameters for at least one of the methods
    alt_params = [latlims, lonlims, rgt, date]
    assert (any([url is not None] + [all(v is not None for v in alt_params)]))

    if url is not None:
        mydata = dataCollector(oaurl=url, beam=gtx)
    else:
        mydata = dataCollector(date=date, latlims=latlims, lonlims=lonlims, track=rgt, beam=gtx, verbose=verbose)

    mydata.requestData(verbose=verbose)
    myplot = mydata.plotData(title=title)

    return myplot, mydata
