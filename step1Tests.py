# -------------------------------------------------------------------------
# This source is part of:
# P l e t h o r a Interview Coding Challenge
# -------------------------------------------------------------------------
# Name:        step1Tests.m
# Type:        Driver
# Defines:     Testing of polygon object formation against degeneracy.
# Author:      James Davidson
# Institution: N/A
# Created:     08/28/2015
# -------------------------------------------------------------------------


# utility modules
# -- none --

# project modules
import polygon as plg


def main():
    
    # specify test case vertex points - should be valid
    pointChain_1 = [[0,0],[1,0],[1,1],[0,1],[0,0]]
    pointChain_2 = [[-10.2,-6],[0,0],[1,-3],[1,-7],[0,-4],[-10.2,-6]]
    
    # specify test case vertex points - should not be valid
    pointChain_3 = [[0,0],[1,0],[0,0]]
    pointChain_4 = [[0,0],[1,0],[1,1],[0.5,1],[0.5,0],[0,0]]
    pointChain_5 = [[0,0],[1,0],[1,1],[0,0],[-1,0],[0,-1],[0,0]]
    pointChain_6 = [[-1,0],[1,0],[0,1],[0,-1],[-1,0]]
    
    # generate shape according to chain of points of nested iterables
    # change passed in points chain to pointChain_1, pointChain_2, and so on...
    shape = plg.polygon(pointChain_1)
    print 'Vertices for successfully created polygon:'
    print shape.vertices
    print
    
if __name__ == '__main__':
    main()
