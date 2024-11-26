
# '''
#     This file contains the class definition for the StrawHat class.
# '''

# # from heapq import heapify
# from crewmate import CrewMate
# from heap import Heap
# from treasure import Treasure

# class StrawHatTreasury:
#     '''
#     Class to implement the StrawHat Crew Treasury
#     '''
    
#     def comp_SHT(self, a, b):
#         '''
#         Comparator function for comparing crew mates based on their load and last updated time.
#         Arguments:
#             a : CrewMate : First crew mate
#             b : CrewMate : Second crew mate
#         Returns:
#             bool : True if a has less load and earlier last updated time, False otherwise.
#         '''
#         return a.current_load + a.last_updated_time < b.current_load + b.last_updated_time
    
#     def __init__(self, m):
#         '''
#         Initializes the StrawHat crew with m crew mates.
#         Arguments:
#             m : int : Number of crew mates
#         Time Complexity:
#             O(m)
#         '''
#         self.hat = Heap(self.comp_SHT, [])
#         for _ in range(m):
#             self.hat.insert(CrewMate())
    
#     def add_treasure(self, treasure):
#         '''
#         Adds a treasure to the crew mate with the least load.
#         Arguments:
#             treasure : Treasure : The treasure to be added
#         Time Complexity:
#             O(log(m) + log(n))
#         '''
#         # Extract the crew mate with the least load
#         crew_mate = self.hat.extract()
        
#         # Add the treasure to this crew mate
#         crew_mate.crew_treasure.insert(treasure)
        
#         # Update crew mate's load and time
#         t = treasure.arrival_time
#         t_last = crew_mate.last_updated_time
#         crew_mate.current_load = treasure.size + max(0,crew_mate.current_load- t +t_last)
#         crew_mate.last_updated_time = t
        
#         # Reinsert the updated crew mate into the heap
#         self.hat.insert(crew_mate)
    
#     def get_completion_time(self):
#         '''
#         Calculates the completion time for all treasures.
#         Returns:
#             List[Treasure] : List of treasures sorted by their ids with updated completion times.
#         Time Complexity:
#             O(n(log(m) + log(n)))
#         '''
#         treasures = []  # List to store all treasures
        
#         # Loop through each crew mate and process their treasures
#         for crew_mate in self.hat.array:
#           crew_treasures = crew_mate.crew_treasure.array  # Get crew mate's treasures
#         #    print(crew_treasures)
#         #    print("Vinnu")
#           if len(crew_treasures):
#             # Create a priority heap based on treasure's processing priority
#             treasure_heap = Heap(crew_treasures[0].comp_T, [])
#             t = crew_treasures[0].arrival_time if crew_treasures else 0
#             # print(Vinuthna)
#             # print("Vinuthna_1")
#             for i in range(len(crew_treasures) - 1):
#                 # print(Vinuthna)
#                 # print("Vinuthna_2")
#                 # Insert treasures into the heap
#                 crew_treasures[i].add_attrib()
#                 treasure_heap.insert(crew_treasures[i])
#                 current_treasure = treasure_heap.top()
                
#                 # Calculate time gap between treasures
#                 t1 = crew_treasures[i].arrival_time
#                 t2 = crew_treasures[i + 1].arrival_time
                
#                 # Process the treasure's remaining size
#                 while current_treasure.remaining_size - (t2 - t1) <= 0:
#                     # print(Vinuthna)
#                     # print("Vinuthna_3")
#                     current_treasure.completion_time = t1 + current_treasure.remaining_size
#                     t1 += current_treasure.remaining_size
#                     current_treasure.remaining_size = 0
#                     treasures.append(treasure_heap.extract())
                    
#                     if len(treasure_heap.array):
#                         current_treasure = treasure_heap.top()
#                     else:
#                         break
                
#                 if len(treasure_heap.array):
#                     # print(Vinuthna)
#                     # print("Vinuthna_4")
#                     current_treasure.remaining_size -= (t2 - t1)
            
#             # Process the last treasure
#             if len(crew_treasures):
#                 # print(Vinuthna)
#                 # print("Vinuthna_5")
#                 crew_treasures[-1].add_attrib()
#                 treasure_heap.insert(crew_treasures[-1])
                
#                 t = crew_treasures[-1].arrival_time
            
#             # Process remaining treasures in the heap
#             while len(treasure_heap.array):
#                 # print("Vinuthna_6")
#                 last_treasure = treasure_heap.extract()
#                 # print(len(treasure_heap.array))
#                 last_treasure.completion_time = t + last_treasure.remaining_size
#                 t += last_treasure.remaining_size
#                 last_treasure.remaining_size = 0
#                 treasures.append(last_treasure)
            
#         # Return the processed treasures sorted by their IDs
#         # return sorted(treasures,)
#         # for crew_mate in self.hat.array:
#         #     crew_treasures = crew_mate.crew_treasure.array 
#         #     for i in range(len(crew_treasures)):
#         #         crew_treasures[i].add_attrib()
            
#         return sorted(treasures, key=lambda treasure: treasure.id)
'''
    This file contains the class definition for the StrawHat class.
'''

# from heapq import heapify
from crewmate import CrewMate
from heap import Heap
from treasure import Treasure

class StrawHatTreasury:
    '''
    Class to implement the StrawHat Crew Treasury
    '''
    
    def comp_SHT(self, a, b):
        '''
        Comparator function for comparing crew mates based on their load and last updated time.
        Arguments:
            a : CrewMate : First crew mate
            b : CrewMate : Second crew mate
        Returns:
            bool : True if a has less load and earlier last updated time, False otherwise.
        '''
        return a.current_load + a.last_updated_time < b.current_load + b.last_updated_time
    
    def __init__(self, m):
        '''
        Initializes the StrawHat crew with m crew mates.
        Arguments:
            m : int : Number of crew mates
        Time Complexity:
            O(m)
        '''
        self.hat = Heap(self.comp_SHT, [])
        for _ in range(m):
            self.hat.insert(CrewMate())
        self.c_t=[]
    
    def add_treasure(self, treasure):
        '''
        Adds a treasure to the crew mate with the least load.
        Arguments:
            treasure : Treasure : The treasure to be added
        Time Complexity:
            O(log(m) + log(n))
        '''
        # Extract the crew mate with the least load
        crew_mate = self.hat.extract()
        if len(crew_mate.crew_treasure.array)==0:
            self.c_t.append(crew_mate)
        # Add the treasure to this crew mate
        crew_mate.crew_treasure.insert(treasure)
        
        # Update crew mate's load and time
        t = treasure.arrival_time
        t_last = crew_mate.last_updated_time
        crew_mate.current_load = treasure.size + max(0,crew_mate.current_load- t +t_last)
        crew_mate.last_updated_time = t
        
        # Reinsert the updated crew mate into the heap
        self.hat.insert(crew_mate)
    
    def get_completion_time(self):
        '''
        Calculates the completion time for all treasures.
        Returns:
            List[Treasure] : List of treasures sorted by their ids with updated completion times.
        Time Complexity:
            O(n(log(m) + log(n)))
        '''
        treasures = []  # List to store all treasures
        
        # Loop through each crew mate and process their treasures
        for crew_mate in self.c_t:
           crew_treasures = crew_mate.crew_treasure.array  # Get crew mate's treasures
        #    print(crew_treasures)# m crew mates
        #    print("Vinnu")
           if len(crew_treasures):
            # Create a priority heap based on treasure's processing priority
            treasure_heap = Heap(crew_treasures[0].comp_T, [])
            t = crew_treasures[0].arrival_time if crew_treasures else 0
            # print(Vinuthna)
            # print("Vinuthna_1")
            for i in range(len(crew_treasures) - 1):
                # print(Vinuthna)
                # print("Vinuthna_2")
                # Insert treasures into the heap
                crew_treasures[i].add_attrib()
                treasure_heap.insert(crew_treasures[i])
                current_treasure = treasure_heap.top()
                
                # Calculate time gap between treasures
                t1 = crew_treasures[i].arrival_time
                t2 = crew_treasures[i + 1].arrival_time
                
                # Process the treasure's remaining size
                while current_treasure.remaining_size - (t2 - t1) <= 0:
                    # print(Vinuthna)
                    # print("Vinuthna_3")
                    current_treasure.completion_time = t1 + current_treasure.remaining_size
                    t1 += current_treasure.remaining_size
                    current_treasure.remaining_size = 0
                    treasures.append(treasure_heap.extract())
                    
                    if len(treasure_heap.array):
                        current_treasure = treasure_heap.top()
                    else:
                        break
                
                if len(treasure_heap.array):
                    # print(Vinuthna)
                    # print("Vinuthna_4")
                    current_treasure.remaining_size -= (t2 - t1)
            
            # Process the last treasure
            if len(crew_treasures):
                # print(Vinuthna)
                # print("Vinuthna_5")
                crew_treasures[-1].add_attrib()
                treasure_heap.insert(crew_treasures[-1])
                
                t = crew_treasures[-1].arrival_time
            
            # Process remaining treasures in the heap
            while len(treasure_heap.array):
                # print("Vinuthna_6")
                last_treasure = treasure_heap.extract()
                # print(len(treasure_heap.array))
                last_treasure.completion_time = t + last_treasure.remaining_size
                t += last_treasure.remaining_size
                last_treasure.remaining_size = 0
                treasures.append(last_treasure)
        return sorted(treasures, key=lambda treasure: treasure.id)


