from myIO import getPhotoList, printOutput
import random
false = False
true = True
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

def pickNext(prev, photoList):
    unused = list(filter(lambda a : not a.isUsed, photoList))
    bestValue = len(prev.getTags())//2
    if len(unused) is 0:
        return True, None
    bestPhoto = photoList[0]
    bestScore = abs(bestValue - len(set(prev.getTags()).union(set(bestPhoto.getTags()))))

    for p in unused:
        curr = abs(bestValue - len(set(prev.getTags()).union(set(p.getTags()))))
        if curr < bestScore:
            bestScore = curr
            bestPhoto = p

    if bestPhoto.isUsed:
        return False, random.choice(unused)

    return False, bestPhoto



def greedSort(photoList):
    bestList = []
    photoList[0].use()
    bestList.append(photoList[0])

    count = 0
    while(True):
        count = count + 1
        print(count)
        isDone, picked = pickNext(bestList[-1], photoList)
        if isDone:
            break
        if picked is not None:
            picked.use()
            bestList.append(picked)
        photoList = list(filter(lambda a : not a.isUsed, photoList))

    return bestList


def dumbSolution(num):
    allPics = getPhotoList(num)
    ve = onlyVertical(allPics)
    ho = onlyHorizontal(allPics)
    finalForm = ho + pairVerticals(ve)
    printOutput(num, greedSort(finalForm))

dumbSolution(1)
dumbSolution(2)
dumbSolution(3)
dumbSolution(4)
dumbSolution(5)

