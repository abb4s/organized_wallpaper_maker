from custom_wallpaper import CustomWallpaper

num_of_rect = int(input("inter the number of rectangle : "))
path = input("inter the path of your image : ")
function = CustomWallpaper(path, num_of_rect)
function.run()
