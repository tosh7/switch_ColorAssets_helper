import glob
import yaml

def main():
    with open('config/directory.yml') as yml:
        config = yaml.safe_load(yml)['directory']
        old_assets = yaml.safe_load(yml)['oldAssets']
        new_assets = yaml.safe_load(yml)['newAssets']

    storyboard_directories = glob.glob(f"{config}**/*.storyboard", recursive=True)
    xib_dictionaries = glob.glob(f"{config}**/*.xib", recursive=True)

main()