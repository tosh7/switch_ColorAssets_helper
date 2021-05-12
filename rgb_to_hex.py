
def rgb_to_hex(red, green, blue):
    rgb = (round(255*red), round(255*green), round(255*blue))
    return '#%02x%02x%02x' % rgb

def rgb_to_hex(value):
    # print(255*value)
    rgb_value = round(255*float(value))
    return '%02x' % rgb_value