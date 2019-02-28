from myIO import getPhotoList, printOutput

def onlyVertical(inList):
    return list(filter(lambda a : a.isVertical() == True, inList))

def onlyHorizontal(inList):
    return list(filter(lambda a : a.isVertical() == False, inList))

def photoListToTags(photoList):
    return [x.getTags() for x in photoList]

def photoListToIndex(photoList):
    return [x.getIndex() for x in photoList]

def pairVerticals(vertPhotos):
    if len(vertPhotos) % 2 == 1:
        vertPhotos.pop()
    merged=[]
    for i in range(0, len(vertPhotos), 2):
        vertPhotos[i].merge(vertPhotos[i+1])
        merged.append(vertPhotos[i])
    return merged

def dumbSolution(num):
    allPics = getPhotoList(num)
    ve = onlyVertical(allPics)
    ho = onlyHorizontal(allPics)
    printOutput(num, ho + pairVerticals(ve))

for x in range(5):
    dumbSolution(x)

