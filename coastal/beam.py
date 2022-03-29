# -*- coding: utf-8 -*-
"""
Tools for beam manipulation.

"""
from sliderule import icesat2


def reduce_dataframe(gdf, rgt=None, gt=None, track=None, pair=None, cycle=None, beam='', crs=4326):
    """
    Reduce GeoDataFrame to plot a single beam.
    This function is goint to subset the geodataframe. Since we had a span of
    dates, there are multiple dates (and beams). This function will also set the
    CRS (map projection).

    Refactored from DataDownload/SlideRule_example.ipynb by @eeholmes
    """
    # convert coordinate reference system
    D3 = gdf.to_crs(crs)
    # reduce to reference ground track
    if rgt is not None:
        D3 = D3[D3["rgt"] == rgt]
    # reduce to ground track (gt[123][lr]), track ([123]), or pair (l=0, r=1)
    gtlookup = {icesat2.GT1L: 1, icesat2.GT1R: 1, icesat2.GT2L: 2, icesat2.GT2R: 2, icesat2.GT3L: 3, icesat2.GT3R: 3}
    pairlookup = {icesat2.GT1L: 0, icesat2.GT1R: 1, icesat2.GT2L: 0, icesat2.GT2R: 1, icesat2.GT3L: 0, icesat2.GT3R: 1}
    if gt is not None:
        D3 = D3[(D3["track"] == gtlookup[gt]) & (D3["pair"] == pairlookup[gt])]
    if track is not None:
        D3 = D3[D3["track"] == track]
    if pair is not None:
        D3 = D3[D3["pair"] == pair]
    # reduce to weak or strong beams
    # tested on cycle 11, where the strong beam in the pair matches the spacecraft orientation.
    # Need to check on other cycles
    if beam == 'strong':
        D3 = D3[D3['sc_orient'] == D3['pair']]
    elif beam == 'weak':
        D3 = D3[D3['sc_orient'] != D3['pair']]
    # reduce to cycle
    if cycle is not None:
        D3 = D3[D3["cycle"] == cycle]
    # otherwise, return both beams
    return D3
