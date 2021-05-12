import glob
import yaml
import os
import re
import rgb_to_hex as rh

def main():
    with open('config/directory.yml') as yml:
        config = yaml.safe_load(yml)['directory']
    with open('config/directory.yml') as yml:
        old_assets = yaml.safe_load(yml)['old_assets']
    with open('config/directory.yml') as yml:
        new_assets = yaml.safe_load(yml)['new_assets']

    print(old_assets)
    print(new_assets)
    storyboard_directories = glob.glob(f"{config}**/*.storyboard", recursive=True)
    xib_dictionaries = glob.glob(f"{config}**/*.xib", recursive=True)

    old_color_sets = glob.glob(f"{old_assets}/*.colorset")
    new_color_sets = glob.glob(f"{new_assets}/*.colorset")

    read_color_assets(old_color_sets)
    read_color_assets(new_color_sets)

def read_color_assets(color_sets):
    for color in color_sets:
        print(os.path.splitext(os.path.basename(color))[0])

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
                    blue = rh.rgb_to_hex(redValue)
            elif 'green' in line:
                if '0x' in line:
                    green = re.findall('0x(.*)"', line)[0]
                else:
                    greenValue = re.findall(': "(.*)"', line)[0]
                    green = rh.rgb_to_hex(redValue) 
            
        print(f'#{red}{green}{blue}')

main()