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
    usedPhotos=[]
    noUsePhotos=[]
    for photo in vertPhotos:
        if photo in noUsePhotos:
            continue
        maxTags=0
        secondPhoto=photo

        for index in range(-100,100):
            if(photo.getIndex()+index>len(vertPhotos)-2 or photo.getIndex()+index<0):
                break
            photo2=vertPhotos[photo.getIndex()+index]
            if photo2 in noUsePhotos:
                continue
            score= len(set(photo.getTags()+photo2.getTags()))
            if(score>maxTags):
                secondPhoto=photo2
                maxTags=score
        usedPhotos.append([photo,secondPhoto])
        noUsePhotos.append(photo)
        noUsePhotos.append(secondPhoto)




    return noUsePhotos

def dumbSolution(num):
    allPics = getPhotoList(num)
    ve = onlyVertical(allPics)
    ho = onlyHorizontal(allPics)
    printOutput(num, ho + pairVerticals(ve))

for x in range(5):
    dumbSolution(x)

