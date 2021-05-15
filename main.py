import glob
import yaml
import os
import re
import rgb_to_hex as rh
import color_set as cs

def main():
    with open('config/directory.yml') as yml:
        config = yaml.safe_load(yml)['directory']
    with open('config/directory.yml') as yml:
        old_assets = yaml.safe_load(yml)['old_assets']
    with open('config/directory.yml') as yml:
        new_assets = yaml.safe_load(yml)['new_assets']

    storyboard_directories = glob.glob(f"{config}**/*.storyboard", recursive=True)
    xib_dictionaries = glob.glob(f"{config}**/*.xib", recursive=True)
    swift_dictionaries = glob.glob(f"{config}**/*.swift", recursive=True)

    old_color_sets = glob.glob(f"{old_assets}/*.colorset")
    new_color_sets = glob.glob(f"{new_assets}/*.colorset")

    old_colors = read_color_assets(old_color_sets)
    new_colors = read_color_assets(new_color_sets)

    for old_color in old_colors:
        for new_color in new_colors:
            if old_color == new_color:
                old_color.replace_color_name = new_color.color_name
                old_color.replace_swiftGen_color_name = new_color.swiftGen_color_name

    def replace_colors(dictionaries):
        for dictionary in dictionaries:
            with open(dictionary, 'r') as xml:
                tmp_list = []
                for line in xml.readlines():
                    tmp_list.append(line)
                    for old_color in old_colors:
                        if f'name="{old_color.color_name}' in line:
                            new_line = line.replace(old_color.color_name, old_color.replace_color_name)
                            tmp_list[-1] = new_line

            with open(dictionary, 'w') as new_xml:
                for i in range(len(tmp_list)):
                    new_xml.write(tmp_list[i])

    replace_colors(storyboard_directories)
    replace_colors(xib_dictionaries)

    for swift_file in swift_dictionaries:
        with open(swift_file, 'r') as swift:
            tmp_list = []
            for line in swift.readlines():
                tmp_list.append(line)
                for old_color in old_colors:
                    if f'Asset.Colors.{old_color.swiftGen_color_name}' in line:
                        new_line = line.replace(old_color.swiftGen_color_name, old_color.replace_swiftGen_color_name)
                        tmp_list[-1] = new_line
        
        with open(swift_file, 'w') as new_swift:
            for i in range(len(tmp_list)):
                new_swift.write(tmp_list[i])

def read_color_assets(color_sets):
    colors = []
    for color in color_sets:
        color_name = os.path.splitext(os.path.basename(color))[0]

        contents_json = open((f"{color}/Contents.json"))
        for line in contents_json.readlines():
            if 'red' in line:
                if '0x' in line:
                    red = re.findall('0x(.*)"', line)[0]
                else:
                    redValue = re.findall(': "(.*)"', line)[0]
                    red = rh.rgb_to_hex(redValue)
            elif 'blue' in line:
                if '0x' in line:
                    blue = re.findall('0x(.*)"', line)[0]
                else:
                    blueValue = re.findall(': "(.*)"', line)[0]
                    blue = rh.rgb_to_hex(blueValue)
            elif 'green' in line:
                if '0x' in line:
                    green = re.findall('0x(.*)"', line)[0]
                else:
                    greenValue = re.findall(': "(.*)"', line)[0]
                    green = rh.rgb_to_hex(greenValue) 
            
        color_hex = f'#{red}{green}{blue}'

        colors.append(cs.color_set(color_name, color_hex))

    return colors

main()