# -*- coding: utf-8 -*-
"""
Authors: Tim Hessels
         UNESCO-IHE 2017
Contact: t.hessels@unesco-ihe.org
Repository: https://github.com/wateraccounting/watools
Module: Collect/DEM
"""

#General modules
import os
import sys

# Water Accounting modules
from watools.Collect.DEM.DataAccess import DownloadData

def main(Dir, latlim, lonlim, resolution = '3s', Waitbar = 1):
    """
    Downloads HydroSHED flow direction data from http://www.hydrosheds.org/download/

    this data includes a Digital Elevation Model Flow Direction
    The spatial resolution is 90m (3s) or 450m (15s)

    The following keyword arguments are needed:
    Dir -- 'C:/file/to/path/'
    latlim -- [ymin, ymax]
    lonlim -- [xmin, xmax]
    resolution -- '3s' (default) or '15s'
    """

    # Create directory if not exists for the output
    output_folder = os.path.join(Dir, 'HydroSHED', 'DIR')
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Define the output map and create this if not exists  # Define the output map and create this if not exists
    nameEnd = os.path.join(Dir, 'HydroSHED', 'DIR', 'DIR_HydroShed_-_%s.tif' %resolution)
    parameter = "dir_%s" %resolution

    if not os.path.exists(nameEnd):

        # Create Waitbar
        if Waitbar == 1:
            print('\nDownload HydroSHED Drainage Direction map with a resolution of %s' %resolution)
            import watools.Functions.Start.WaitbarConsole as WaitbarConsole
            total_amount = 1
            amount = 0
            WaitbarConsole.printWaitBar(amount, total_amount, prefix = 'Progress:', suffix = 'Complete', length = 50)

        # Download and process the data
        DownloadData(output_folder, latlim, lonlim, parameter, resolution)

        if Waitbar == 1:
            amount = 1
            WaitbarConsole.printWaitBar(amount, total_amount, prefix = 'Progress:', suffix = 'Complete', length = 50)

    else:
        if Waitbar == 1:
            print("\nHydroSHED Drainage direction (%s) already exists in output folder" %resolution)

if __name__ == '__main__':
    main(sys.argv)
