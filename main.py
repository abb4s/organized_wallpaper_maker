import argparse
from src.custom_wallpaper import CustomWallpaper



parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')

parser.add_argument('filename')           # positional argument
parser.add_argument('-n', '--numberofrects')      # option that takes a value

args = parser.parse_args()

path = args.filename
num_of_rect = int(args.numberofrects)
custom_wallpaper = CustomWallpaper(path, num_of_rect)
custom_wallpaper.run()
