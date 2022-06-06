class Room():
    
    number_of_rooms = 0
    
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.contents =[]
        Room.number_of_rooms = Room.number_of_rooms + 1
        
    def describe(self):
        print(self.description)
        
    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
        #print(self.name + " linked rooms : " + repr(self.linked_rooms))
        
    def display_details(self):
        print(self.name)
        print("=" * len(self.name))
        self.describe()
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The " + room.name + " is " + direction)
        print()
        if len(self.contents) > 0:
            for each in self.contents:
                print("You see " + each.short_description + ": " + each.description)
        print()
        if self.character is not None:
            self.character.describe()
            print()
            
    def move(self, direction):
        if direction in ["n", "e", "s", "w"]:
            direction = {"n":"north", "e":"east", "s":"south", "w":"west"}[direction]
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self

