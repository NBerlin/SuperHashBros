
def combineTags(tags1,tags2):
    return set(tags1, tags2)

def getPoints(tags1,tags2):
    same = set(tags1).intersection(tags2).length
    different1=removeCommonElements(tags1,tags2).length
    different2=removeCommonElements(tags2.tags1).length
    return min(same,different1,different2)
def removeCommonElements(a, b):
    for e in a[:]:
        if e in b:
            a.remove(e)
    return a

def setOtherPhotosHorizontal(list):
    for photo in list:
        otherPhotos=[]
        for photo2 in list:
            otherPhotos.append([getPoints(photo.getTags(),photo2.getTags()),photo2])
        photo.setOtherPhotos(otherPhotos)
