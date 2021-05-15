# switch_ColorAsset_helper

If you switch Xcode project's color xcassets, you have to switch all of colors initialized from xcassets manually. It takes a lot of your effort. 
This program helps you to switch color xcassets. All you need is just project and new and old color xcassets.

## Requirements
- Python3.x.x(In this project I suggest to use 3.8.5, but still works another python3 version)
- pip3

## How to use

1. clone this repository.
2. make directoy, which name should be `config`, and make `directory.yml` file.  put xcode project directory path that you want to use this for.
such as
```
directory: 'your project directory path'
old_assets: 'your old color xcassets file path'
new_assets: 'your new color xcassets file path'
```
I also suggest you to make directory named assets just under the switch_ColorAsset_helper directory, and put xcassets file in the repository.
3. use pip3 to install `pyyaml`. make sure yaml directory should be put on right under the switch_ColorAsset_helper directory.
4. make a command `python3 main.py` on your terminal, and you will get `file.txt` file which has custom color codes.

## Contacts
If you have any question about this program, just email me.(zlia.6.lj.425@gmail.com)  
Or you can contact me via Twitter.[@tosh_3](https://twitter.com/tosh_3)