import Commun.variables as VAR
class CCordonnees:
    def __init__(self, x, y, offX, offY):
        self.x, self.y = x, y
        self.offsetX, self.offsetY = offX, offY
        
    # ---------------------------------------------------------------------------------------------------------------------------------------------------------
    # --- proprietes de position
    # - en pixel
    def position_pixel_x(self):
        return self.position_int_x() - VAR.dimDiv2 
    def position_pixel_y(self):
        return self.position_int_y() - VAR.dimMul2 + (self.image_mask.get_height() // 2)         
    def position_int_x(self):
        return int(round((self.x * VAR.dim))) + VAR.dimDiv2
    def position_int_y(self):
        return int(round((self.y * VAR.dim))) + VAR.dimDiv2    
    # - en cellule
    def position_x(self):
        return int(round(self.x))
    def position_y(self):
        return int(round(self.y))