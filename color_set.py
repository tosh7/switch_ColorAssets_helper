
class color_set:
    def __init__(self, color_name, color_hex):
        self.color_name = color_name
        self.color_hex = color_hex

    def __eq__(self, other):
        return self.color_hex == other.color_hex