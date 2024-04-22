class CustomWallpaper:
    def __init__(self, path):
        self.path = path

    def load_image(self):
        pass    
    
    def save_image(self):
        pass
    
    def blur(self):
        pass
    
    def replace_rect(self):
        pass
    
    def get_space_btw_rects(self):
        pass
    
    def get_rects_pos(self):
        pass
        
    def run(self):
        # 
        blur_image = self.blur()
        spaces = self.get_space_btw_rects()
        rects_pos = self.get_rects_pos()
        output = self.replace_rect()
        pass
    
    def __str__(self):
        return f"Wallpaper: {self.path}"