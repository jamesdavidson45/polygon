# -------------------------------------------------------------------------
# This source is part of:
# P l e t h o r a Interview Coding Challenge
# -------------------------------------------------------------------------
# Name:        step3Tests.m
# Type:        Driver
# Defines:     Testing of polygon object area calculaton.
# Author:      James Davidson
# Institution: N/A
# Created:     08/28/2015
# -------------------------------------------------------------------------


# utility modules
# -- none --

# project modules
import polygon as plg


def main():
    
    # specify test case vertex points
    pointChain_1 = [[0,0],[1,0],[1,1],[0,1],[0,0]]
    pointChain_2 = [[-10.2,-6],[0,0],[1,-3],[1,-7],[0,-4],[-10.2,-6]]
    pointChain_3 = [[13.5,41.5],[42.5,56.5],[39.5,69.5],[42.5,84.5],[13.5,100],[6.0,70.5],[13.5,41.5]]
    
    # generate shape according to chain of points, display area
    shape = plg.polygon(pointChain_1)
    print 'Polygon 1 area:'
    print shape.getArea()
    print
    
    shape = plg.polygon(pointChain_2)
    print 'Polygon 2 area:'
    print shape.getArea()
    print
    
    shape = plg.polygon(pointChain_3)
    print 'Polygon 3 area:'
    print shape.getArea()
    print
    
if __name__ == '__main__':
    main()
