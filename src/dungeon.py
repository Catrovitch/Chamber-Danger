from random import randrange
from random import shuffle
from room import Room

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
    
        for r in range(total_rooms):
            if len(self.rooms) >= max_rooms:
                break    
    
            x = randrange(0,map_width)
            y = randrange(0,map_height)
            
            width = randrange(min_room_size,max_room_size)
            height = randrange(min_room_size,max_room_size)        
            room = Room(x,y,width,height)
            
            if self.check_for_overlap(room):
                pass
            else:
                self.rooms.append(room)    
            
            for room in self.rooms:
                for y in range(room.y, room.y+room.height):
                    for x in range(room.x, room.x+room.width):
                        self.map[x,y] = 1

    def check_for_overlap(self, room):

        """Return false if the room overlaps any other room."""

        for current_room in self.rooms:
            xmin1 = room.x
            xmax1 = room.x + room.width
            xmin2 = current_room.x
            xmax2 = current_room.x + current_room.width
            
            ymin1 = room.y
            ymax1 = room.y + room.height
            ymin2 = current_room.y
            ymax2 = current_room.y + current_room.height
            
            if (xmin1 <= xmax2 and xmax1 >= xmin2) and (ymin1 <= ymax2 and ymax1 >= ymin2) and xmax1 <= map_width-10 and ymax1 <= map_height-10:
                return True
                
            return False

    def connect_rooms(self):

        """Draws passages randomly between the rooms."""

        for i in range(len(self.rooms)-1):
            roomA = self.rooms[i]
            roomB = self.rooms[i+1]
            
            for x in range(roomA.x,roomB.x):
                self.map[x,roomA.y] = 1
            for y in range(roomA.y, roomB.y):
                self.map[roomA.x,y] = 1
                
            for x in range(roomB.x,roomA.x):
                self.map[x,roomA.y] = 1
            for y in range(roomB.y, roomA.y):
                self.map[roomA.x,y] = 1
