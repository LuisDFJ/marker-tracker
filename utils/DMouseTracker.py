from utils.DRectangle import DRectangle
from utils.DNodes import DNodes

class DMouseTracker:
    def __init__( self, n ):
        self.n = n
        self.rectangles = [ DRectangle() for _ in range( n ) ]
        self.pRect = self.gen_iter()
        self.cRect = next( self.pRect )

    def gen_iter( self ):
        while True:
            for rect in self.rectangles:
                yield rect

    def mouse_callback( self, event, x, y, *args ):
        if self.cRect.mouse_callback( event, x, y, *args ):
            self.cRect = next( self.pRect )

    def draw( self, img ):
        for rect in self.rectangles:
            rect.draw( img )

    def get( self, *args ):
        return DNodes( self.rectangles, *args )