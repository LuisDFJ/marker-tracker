from types import NoneType
from utils.DPoint import DPoint

class DTwoPointAbstract:
    def __init__( self, pa: DPoint | NoneType = None, pb : DPoint | NoneType = None ):
        self.pa = DPoint()
        self.pb = DPoint()
        if not isinstance( pa, NoneType ):
            self.pa = pa
        if not isinstance( pb, NoneType ):
            self.pb = pb

    def set( self, pa:DPoint, pb:DPoint ):
        self.pa = pa
        self.pb = pb

    def setBBox( self, x, y, w, h ):
        self.pa.set( x, y )
        self.pb.set( x + w, y + h )

    def getBBox( self ):
        pmin = DPoint.min( self.pa, self.pb )
        pdif = DPoint.max( self.pa, self.pb ) - pmin
        return pmin.x, pmin.y, pdif.x, pdif.y

    def get_centre( self ) -> DPoint:
        return self.pa + ( self.pb - self.pa ) // 2

    def draw( self, img ):
        pass

    def enum( self, iter ):
        try:
            n = next( iter )
        except StopIteration:
            raise Exception( "Max nodes reached" )
        return n

    def __bool__( self ) -> bool:
        if bool( self.pa ) and bool( self.pb ):
            return True
        return False
    def __str__(self) -> str:
        return f"{self.pa} : {self.pb}"

