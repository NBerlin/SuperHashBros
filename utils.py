from myIO import getPhotoList, printOutput

def onlyVertical(inList, bool):
    return list(filter(lambda a : a.isVertical() == bool, inList))

def photoListToTags(photoList):
    return [x.getTags() for x in photoList]

def photoListToIndex(photoList):
    return [x.getIndex() for x in photoList]

def addListLayer(inList):
    return [[x] for x in inList]


def pairVerticals(vertPhotos):
    if len(vertPhotos) % 2 == 1:
        vertPhotos.pop()
    return [[vertPhotos[i], vertPhotos[i+1]] for i in range(0, len(vertPhotos), 2)]

def dumbSolution(num):
    allPics = getPhotoList(num)
    ho = addListLayer(onlyVertical(allPics, False))
    ve = onlyVertical(allPics, True)
    printOutput(num, ho + pairVerticals(ve))

for x in range(5):
    dumbSolution(x)
