from photo import photo
filenames = [
    "a_example.txt", "b_lovely_landscapes.txt", "c_memorable_moments.txt",
    "d_pet_pictures.txt", "e_shiny_selfies.txt"
]


def getPhotoList(num):
    photos = []
    input = open(f"./inputs/{filenames[int(num)]}")
    for num, line in enumerate(input):
        if num is not 0:
            split = line.strip().split(' ')
            isVert = True if split.pop(0) == 'V' else False
            split.pop(0)
            photos.append(photo(split, isVert))
    return photos
