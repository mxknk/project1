from fltk import cree_fenetre, attend_fermeture, rectangle

filename = "test2.pbm"
scale = 20

white = "#FFFFFF"
black = "#000000"

file = open(filename)

data = file.read()

splited_data = data.split("\n")

format = splited_data[0]

if format != "P1":
    print("Unsupported format")
    exit()

dimensions = splited_data[1]

splitted_dimensions = dimensions.split()

width = int(splitted_dimensions[0])
height = int(splitted_dimensions[1])

# width, height = dimensions.split()
# width = int(width)
# height = int(height)

image_data = splited_data[2:]

for i in range(len(image_data)):
    image_data[i] = image_data[i].split()

print(image_data)
cree_fenetre(width * scale, height * scale)

for x in range(width):
    for y in range(height):
        if image_data[y][x] == "0":
            rectangle(
                x * scale,
                y * scale,
                (x + 1) * scale,
                (y + 1) * scale,
                couleur=white,
                remplissage=white,
            )
        else:
            rectangle(
                x * scale,
                y * scale,
                (x + 1) * scale,
                (y + 1) * scale,
                couleur=black,
                remplissage=black,
            )


attend_fermeture()
