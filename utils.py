from myIO import getPhotoList

def onlyVertical(inList, bool):
    return list(filter(lambda a : a.isVertical() == bool, inList))


