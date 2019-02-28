from photo import photo
filenames = [
    "a_example.txt", "b_lovely_landscapes.txt", "c_memorable_moments.txt",
    "d_pet_pictures.txt", "e_shiny_selfies.txt"
]


def getPhotoList(num):
    photos = []
    input = open(f"./inputs/{filenames[int(num)]}")
    lines = input.read().split('\n')
    lines.pop()  # remove blank line at end
    lines.pop(0)  # remove first line
    for num, line in enumerate(lines):
        split = line.strip().split(' ')
        isVert = True if split.pop(0) == 'V' else False
        split.pop(0)
        photos.append(photo(split, isVert, num))
    input.close()
    return photos


def printOutput(num, listOfSlides):
    solveFile = open(f"./outputs/SOLUTION_{filenames[int(num)]}", 'w')
    solveFile.write(str(len(listOfSlides)) + '\n')

    for slideList in listOfSlides:
        solveFile.write(" ".join([str(x.getIndex()) for x in slideList]) + '\n')
    solveFile.close()


