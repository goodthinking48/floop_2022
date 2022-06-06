class Item():
    
    all_Items = dict()
    
    def __init__(self, short_description):
        """ short_description is a string such as, "a key", "an apple", "some cheese"""
        self.short_description = short_description
        self.name = short_description.split(' ')[-1]
        self.description = None
        Item.all_Items[self.name] = self