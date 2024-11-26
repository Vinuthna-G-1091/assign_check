# '''
#     Python file to implement the Treasure class
# '''

# class Treasure:
#     '''
#     Class to implement a treasure
#     '''
    
#     def __init__(self, id, size, arrival_time):
#         '''
#         Arguments:
#             id : int : The id of the treasure (unique positive integer for each treasure)
#             size : int : The size of the treasure (positive integer)
#             arrival_time : int : The arrival time of the treasure (non-negative integer)
#         Returns:
#             None
#         Description:
#             Initializes the treasure
#         '''
#         # DO NOT EDIT THE __init__ method
#         self.id = id
#         self.size = size
#         self.arrival_time = arrival_time
#         self.completion_time = None
    
#     # You can add more methods if required
#     def add_attrib(self):
#         self.remaining_size=self.size
#         # return self.remainin
#         # self.last=0
#     def comp_T(self,a,b):
        
#         if (a.remaining_size+a.arrival_time<b.remaining_size+b.arrival_time):
#             return True
#         else:
#             return False
   # '''
#     Python file to implement the Treasure class
# '''

# class Treasure:
#     '''
#     Class to implement a treasure
#     '''
    
#     def __init__(self, id, size, arrival_time):
#         '''
#         Arguments:
#             id : int : The id of the treasure (unique positive integer for each treasure)
#             size : int : The size of the treasure (positive integer)
#             arrival_time : int : The arrival time of the treasure (non-negative integer)
#         Returns:
#             None
#         Description:
#             Initializes the treasure
#         '''
#         # DO NOT EDIT THE __init__ method
#         self.id = id
#         self.size = size
#         self.arrival_time = arrival_time
#         self.completion_time = None
    
#     # You can add more methods if required
#     def add_attrib(self):
#         self.remaining_size=self.size
#         # return self.remainin
#         # self.last=0
#     def comp_T(self,a,b):
        
#         if (a.remaining_size+a.arrival_time<b.remaining_size+b.arrival_time):
#             return True
#         else:
#             return False
        
'''
    Python file to implement the Treasure class
'''

class Treasure:
    '''
    Class to implement a treasure
    '''
    
    def __init__(self, id, size, arrival_time):
        '''
        Arguments:
            id : int : The id of the treasure (unique positive integer for each treasure)
            size : int : The size of the treasure (positive integer)
            arrival_time : int : The arrival time of the treasure (non-negative integer)
        Returns:
            None
        Description:
            Initializes the treasure
        '''
        # DO NOT EDIT THE __init__ method
        self.id = id
        self.size = size
        self.arrival_time = arrival_time
        self.completion_time = None
    
    # You can add more methods if required
    def add_attrib(self):
        self.remaining_size=self.size
        # return self.remainin
        # self.last=0
    def comp_T(self,a,b):
        
        if (a.remaining_size+a.arrival_time<b.remaining_size+b.arrival_time):
            return True
        elif (a.remaining_size+a.arrival_time==b.remaining_size+b.arrival_time):
            if a.id<b.id:
                return True
            else:
                return False
        else:
            return False
        
         
    