from random import randint
from types import NoneType
from utils.DPoint import DPoint
from utils.DTwoPointAbstract import DTwoPointAbstract

import cv2 as cv

class DRectangle (DTwoPointAbstract):
    MAX_ENUM = 10
    __enumarator = ( i for i in range( 1, MAX_ENUM + 1 ) )

    def __init__(self, pa: DPoint | NoneType = None, pb: DPoint | NoneType = None):
        super().__init__(pa, pb)
        self.n = self.enum( self.__enumarator )
        self.color = ( randint( 0,255 ), randint( 0,255 ), randint( 0,255 ) )
        self._flag = False

    def mouse_callback( self, event, x, y, *_ ):
        if event == cv.EVENT_LBUTTONDOWN:
            self.pa.set( x,y )
            self.pb.unset()
            self._flag = True
        elif event == cv.EVENT_LBUTTONUP:
            self.pb.set( x,y )
            self._flag = False
            return True

        if self._flag:
            if event == cv.EVENT_MOUSEMOVE:
                self.pb.set( x,y )

        return False

    def draw( self, img ):
        if bool( self ):
            cv.rectangle( img, tuple( self.pa ), tuple( self.pb ), self.color, 2 )
            cv.rectangle( img, tuple( self.pa + DPoint( -1, 0 ) ), tuple( self.pa + DPoint( 15,-10 ) ), self.color, -1 )
            cv.putText( img, str( self.n ), tuple( self.pa ), cv.FONT_HERSHEY_SIMPLEX, 0.4, (255,255,255), 1, cv.LINE_AA )
