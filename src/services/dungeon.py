from random import randrange
from random import shuffle
from services.room import Room

map_height = 50
map_width = 50
min_room_size = 12
max_room_size = 15
max_rooms = 8
min_rooms = 6
max_iters = 3

class Dungeon:

    def __init__(self):

        self.map = {}
        self.rooms = []

    def create_map(self):

        """Initializes the map of key/value pairs."""    
    
        for y in range(map_height):
            for x in range(map_width):
                self.map[x,y] = 0 # set every square to a walldef generate_dungeon():

    def create_rooms(self):

        total_rooms = randrange(min_rooms,max_rooms)    
    
        while len(self.rooms) <= total_rooms:  
    
            x = randrange(0,map_width)
            y = randrange(0,map_height)
            
            width = randrange(min_room_size,max_room_size)
            height = randrange(min_room_size,max_room_size)        
            room = Room(x,y,width,height)
            
            if self.check_for_overlap(room):
                continue
            else:
                self.rooms.append(room)    
            
            for room in self.rooms:
                for y in range(room.y1, room.y2):
                    for x in range(room.x1, room.x2):
                        self.map[x,y] = 1

    def check_for_overlap(self, room):

        """Return false if the room overlaps any other room."""

        for current_room in self.rooms:
                   
            # If one rectangle is on left side of other
            if(room.x1> current_room.x2 or current_room.x1 > room.x2):
                return False
        
            # If one rectangle is above other
            if(room.y2 > current_room.y1 or current_room.x2 > room.y2):
                return False
        
            return True

    def connect_rooms(self):

        """Draws passages randomly between the rooms."""

        for i in range(len(self.rooms)-1):
            roomA = self.rooms[i]
            roomB = self.rooms[i+1]
            
            for x in range(roomA.x1,roomB.x1):
                self.map[x,roomA.y1] = 1
            for y in range(roomA.y1, roomB.y1):
                self.map[roomA.x1,y] = 1
                
            for x in range(roomB.x1,roomA.x1):
                self.map[x,roomA.y1] = 1
            for y in range(roomB.y1, roomA.y1):
                self.map[roomA.x1,y] = 1
