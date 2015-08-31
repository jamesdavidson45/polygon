# -------------------------------------------------------------------------
# This source is part of:
# P l e t h o r a Interview Coding Challenge
# -------------------------------------------------------------------------
# Name:        step4Tests.m
# Type:        Driver
# Defines:     Testing of polygon object tranformation.
# Author:      James Davidson
# Institution: N/A
# Created:     08/28/2015
# -------------------------------------------------------------------------


# utility modules
import math as mth

# project modules
import polygon as plg


def main():
    
    # specify test case vertex points
    pointChain = [[-10.2,-6],[0,0],[1,-3],[1,-7],[0,-4],[-10.2,-6]]
    
    # generate shape according to chain of points
    shape = plg.polygon(pointChain)
    print 'Original polygon properties (vetices, perimeter, and area):'
    print shape.vertices
    print shape.getPerimeter()
    print shape.getArea()
    print
    
    # rotate polygon about origin by 30 degrees counterclockwise
    transArray1 = [[mth.cos(mth.pi/6),mth.sin(mth.pi/6),0],[-mth.sin(mth.pi/6),mth.cos(mth.pi/6),0],[0,0,1]]
    newShape = shape.getNewTransformedPolygon(transArray1)
    print 'Transformation 1 properties (vetices, perimeter, and area):'
    print newShape.vertices
    print newShape.getPerimeter()
    print newShape.getArea()
    print
    
    # scale polygon about origin by one half
    transArray2 = [[0.5,0,0],[0,0.5,0],[0,0,1]]
    newShape = shape.getNewTransformedPolygon(transArray2)
    print 'Transformation 2 properties (vetices, perimeter, and area):'
    print newShape.vertices
    print newShape.getPerimeter()
    print newShape.getArea()
    print
    
    # translate polygon by [3,5]
    transArray3 = [[1,0,0],[0,1,0],[3,5,1]]
    newShape = shape.getNewTransformedPolygon(transArray3)
    print 'Transformation 3 properties (vetices, perimeter, and area):'
    print newShape.vertices
    print newShape.getPerimeter()
    print newShape.getArea()
    print
    
if __name__ == '__main__':
    main()