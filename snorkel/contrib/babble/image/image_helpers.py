import numpy as np

from image_objects import Point
#Point takes in x and y (left/right and top/bottom)

#Extractor Helper Functions
def extract_edge(bbox, side):
    coord = getattr(bbox, side)

    if side in ['top','bottom']:
        return Point(None,coord)
    elif side in ['left','right']:
        return Point(coord,None)
    else:
        raise Exception('Side is invalid')
        
        
def extract_corner(bbox, side1, side2):
    coord1 = getattr(bbox, side1)
    coord2 = getattr(bbox, side2)

    if side1 in ['top','bottom']:
        if side2 in ['left','right']:
            return Point(coord2,coord1)
        else:
            raise Exception('Side 2 is invalid')
            
    elif side1 in ['left','right']:
        if side2 in ['top','bottom']:
            return Point(coord1,coord2)
        else:
            raise Exception('Side 2 is invalid')
    else:
        raise Exception('Side 1 is invalid')

        
def extract_center(bbox):
    coordx = (getattr(bbox,'left') + getattr(bbox,'right')/2.0)
    coordy = (getattr(bbox,'top') + getattr(bbox,'bottom')/2.0)
    return Point(coordx,coordy)

  
#Point Comparison Helper Functions
def is_below(point1, point2):
    if None in (point1.y,point2.y):
        raise Exception('Invalid Comparison')
    else:
        return point1.y > point2.y

def is_above(point1, point2):
    return not is_below(point1, point2)

def is_right(point1, point2):
    if None in (point1.x, point2.x):
        raise Exception('Invalid Comparison')
    else:
        return point1.x > point2.x

def is_left(point1, point2):
    return not is_left(point1,point2)

def is_near(point1, point2,thresh=30.0):
    coord1 = (point1.x,point1.y)
    coord2 = (point2.x,point2.y)
    
    if (None in coord1) or (None in coord2):
        raise Exception('Invalid Distance Comparison')
    else:
        dist = np.linalg.dist([point1.x,point1.y],[point2.x,point2.y])
        return dist <= thresh:

def is_far(point1, point2):
    return not is_near(point1,point2,thresh=100.)





#BBox Comparison Helper Functions
def is_aligned(bbox1,bbox2,thresh=10.):
    thresh = 10

def is_within(bbox1,bbox2):
    pass

  
helpers = {
    'extract_edge': extract_edge,
    'extract_corner': extract_corner,
    'extract_center': extract_center,
    'is_below': is_below,
    'is_above': is_above,
    'is_right': is_right,
    'is_left': is_left,
    'is_near': is_near,
    'is_far': is_far,
    'is_aligned': is_aligned,
    'is_within': is_within,
}