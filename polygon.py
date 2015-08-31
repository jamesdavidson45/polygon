# -------------------------------------------------------------------------
# This source is part of:
# Plethora Interview Coding Challenge
# -------------------------------------------------------------------------
# Name:        polygon.m
# Type:        Class definition
# Defines:     Point, segment, and polygon classes.
# Author:      James Davidson
# Institution: N/A
# Created:     08/28/2015
# -------------------------------------------------------------------------


# utility modules
import numpy as npy

# project modules
# -- none --


class point:
    'Defines a 2D point.'


    def __init__(self,pointSpecs):
        'Initializes a point object based on passed array.'
        
        self.x = pointSpecs[0]
        self.y = pointSpecs[1]
        

class segment:
    'Defines 2D line segment.'


    def __init__(self,startPoint,endPoint):
        'Initializes a segment object based on passed end points.'
        
        # store point locations
        self.p1 = point(startPoint)
        self.p2 = point(endPoint)


class polygon:
    'Defines a 2D polygon with associated support actions.'


    def __init__(self,vertices):
        'Initializes a polygon object based on passed vertex list/array.'
        
        # check for too few vertices
        if len(vertices) < 4:
            raise Exception('Polygon must have at least 3 vertices!')
        
        # check for open chain (zero tolerances!)
        xNoMatch = vertices[0][0] != vertices[-1][0]
        yNoMatch = vertices[0][1] != vertices[-1][1]
        if xNoMatch or yNoMatch:
            raise Exception('Polygon must be closed!')
        
        # store list of segments in polygon
        self.segments = [];
        for i in range(len(vertices) - 1):
            self.segments.append(segment(vertices[i],vertices[i + 1]))
        self.verticesCount = len(vertices)
        self.segmentCount = len(self.segments)
        
        # test polygon for degenerate properties
        self.degenerantTest();
        
        # store array of vertices for easy info printing and transformations
        self.vertices = npy.array(vertices)
                   
    
    def degenerantTest(self):
        'Returns if polygon is not degenerate, raises exception otherwise.'
        
        # check if polygon contains adjacent segments which are colinear
        for i in range(self.segmentCount):
            p1 = self.segments[i].p1
            p2 = self.segments[i].p2
            if i < self.segmentCount - 1:
                p3 = self.segments[i + 1].p2
            else:
                p3 = self.segments[0].p2
            area = p1.x*(p2.y - p3.y) + p2.x*(p3.y - p1.y) + p3.x*(p1.y - p2.y)
            if area == 0:
                raise Exception('Adjacent polygon edges must not be colinear!')
        
        
        # check if polygon contains non-adjacent self intersecting segments
        for i in range(self.segmentCount):
            for j in range(self.segmentCount):
                if abs(j - i) <= 1 or abs(j - i) == self.segmentCount - 1:
                    continue
                if self.segmentsDoIntersect(i,j):
                    raise Exception('Polygon edges must not interesct!')
                
                
    def segmentsDoIntersect(self,idx1,idx2):
        'Returns true if segments corresponding to indexed segments collide.'
        
        # perform orientation test
        s1 = self.segments[idx1]
        s2 = self.segments[idx2]
        s1Con = self.isccw(s1.p1,s1.p2,s2.p1) != self.isccw(s1.p1,s1.p2,s2.p2)
        s2Con = self.isccw(s2.p1,s2.p2,s1.p1) != self.isccw(s2.p1,s2.p2,s1.p2)
        return s1Con and s2Con
    
    
    def isccw(self,p1,p2,p3):
        'Returns true if passed points form a counter clockwise turn.'
        
        # return cross product based conditional
        return (p2.x - p1.x) * (p3.y - p1.y) > (p2.y - p1.y) * (p3.x - p1.x)
    
    
    def getPerimeter(self):
        'Returns distance along the polygon perimeter.'
        
        # cycle through segments, sum each length
        perimeter = 0.0
        for i in range(self.segmentCount):
            xDelta = self.segments[i].p2.x - self.segments[i].p1.x
            yDelta = self.segments[i].p2.y - self.segments[i].p1.y
            perimeter = perimeter + (xDelta**2 + yDelta**2)**0.5
        return perimeter
    
    
    def getArea(self):
        'Returns area within interior of the polygon.'
        
        # cycle through segments, sum areas formed from segment to zero-plane
        area = 0.0;
        for i in range(self.segmentCount):
            p1 = self.segments[i].p1;
            p2 = self.segments[i].p2;
            area = area + (p1.x + p2.x)*(p1.y - p2.y)
        return abs(0.5*area)
    
    
    def getNewTransformedPolygon(self,homTransArray):
        'Applies homogenous transformation matrix to polygon, returns new.'
        
        # multiply array of vertices by transformation array
        homTransArray = npy.array(homTransArray)
        augOnes = npy.ones((self.verticesCount,1))
        homVertices = npy.concatenate((self.vertices,augOnes),axis=1)
        newHomVertices = npy.dot(homVertices,homTransArray)
        
        # strip off homogenous coordinates, return new polygon
        newVertices = newHomVertices[:,:-1]
        return polygon(newVertices)
        
        