'''Lecture Hall Objects/Classes'''

from typing import List, Dict, Tuple

# Developed by Smit Rao.


class Place:
    '''A place.'''
    
    def __init__(place, long=0, lat=0):
        place.longitude = long
        place.latitude = lat
        
    def __repr__(place):
        return ('Longitude is {}. Latitude is {}.').format(place.longitude, \
                                                         place.latitude)
        

class LectureHall(Place):
    '''A lecture hall.'''
    
    def __repr__(hall):
        return 'A lecture hall.'