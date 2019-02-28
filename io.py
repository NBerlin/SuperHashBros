import photo
filenames = [
    "a_example.txt", "b_lovely_landscapes.txt", "c_memorable_moments.txt",
    "d_pet_pictures.txt", "e_shiny_selfies.txt"
]


def getInput(num):
    photos = []
    input = open(f"./inputs/{filenames[int(num)]}")
    for num, line in enumerate(input):
        if num is not 0:
            print(photo)



    return photos


print(getInput(2))
