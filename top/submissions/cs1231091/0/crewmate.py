'''
    Python file to implement the class CrewMate
'''
from heap import Heap
class CrewMate:
    '''
    Class to implement a crewmate
    '''
    
    def __init__(self):
        '''
        Arguments:
            None
        Returns:
            None
        Description:
            Initializes the crewmate
        '''
        self.crew_treasure=Heap(self.comp_CM,[])
        self.current_load=0
        self.last_updated_time=0
        # Write your code here
        # pass
    
    # Add more methods if required
    def comp_CM(self,a,b):
        if a.arrival_time<b.arrival_time:
            return True
        else:
            return False