class photo():
    def __init__(self, tags, isVert, index):
        self.tags = tags
        self.isVert = isVert
        self.index = index
        self.isUsed = False
        self.other = None

    def getTags(self):
        if self.other is not None:
            return list(set(self.tags + self.other.tags))
        return self.tags 

    def isVertical(self):
        return self.isVert

    def getIndex(self):
        if self.other is not None:
            return str(self.other.index) + ' ' + str(self.index)
        return self.index

    def isUsed(self):
        return self.isUsed

    def use(self):
        self.isUsed = True
    
    def merge(self, other):
        if not self.isVert or not other.isVertical():
            raise Exception('only merge verts!!')
        self.other = other

    def isMerged(self):
        return self.other is not None

    def setOtherPhotos(self,otherPhotos):
        self.otherPhotos=otherPhotos
     
    def __str__(self):
        return str(self.getIndex()) + str(self.getTags())
