import re

class color_set:
        
    def __init__(self, color_name, color_hex):
        def make_swiftGen_color_name(name):
            lower_name = name.lower()
            swiftGen_color_name = re.sub("_(.)",lambda x:x.group(1).upper(),lower_name)
            return swiftGen_color_name

        self.color_name = color_name
        self.color_hex = color_hex
        self.swiftGen_color_name = make_swiftGen_color_name(color_name)

    def __eq__(self, other):
        return self.color_hex == other.color_hex