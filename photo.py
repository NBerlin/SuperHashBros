class photo():
    def __init__(self, tags, isVert, index):
        self.tags = tags
        self.isVert = isVert
        self.index = index
        self.isUsed = False

    def getTags(self):
        return self.tags

    def isVertical(self):
        return self.isVert

    def getIndex(self):
        return self.index

    def isUsed(self):
        return self.isUsed

    def use(self):
        self.isUsed = True
