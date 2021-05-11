import glob
import yaml
import os

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
    
    for old_color in old_color_sets:
        // print out color names
        print(os.path.splitext(os.path.basename(old_color))[0])

main()