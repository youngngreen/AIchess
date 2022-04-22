class Cell:

    pieceonCell= None
    tileCorrdinate= None

    def __init__(self,coordinate, piece):
        self.tileCorrdinate=coordinate
        self.pieceonCell=piece