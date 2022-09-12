from utils.DNodes import DNodes
import cv2 as cv

class DTracker:
    TRACK_ALGORITHM = {
        "CSRT"  : cv.legacy.TrackerCSRT.create,
        "MOSSE" : cv.legacy.TrackerMOSSE.create,
        "KCF"   : cv.legacy.TrackerKCF.create
    }
    def __init__( self, img, nodes : DNodes, alg = 'KCF' ):
        self.nodes = nodes
        self.tracker = [ self.TRACK_ALGORITHM[ alg ]() for _ in self.nodes.nodes ]
        self.init_tracker( img )
        
    def init_tracker( self, img ):
        for i, rect in enumerate( self.nodes.nodes.items() ):
            self.tracker[i].init( img, rect[1].getBBox() )

    def update( self, img ):
        for i, rect in enumerate( self.nodes.nodes.items() ):
            success, bbox = self.tracker[i].update( img )
            if success: rect[1].setBBox( *bbox )