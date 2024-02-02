import pandas

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_colour = squirrel_data["Primary Fur Color"]
fur_list = fur_colour.to_list()
grey_num = 0
cinnamon_num = 0
black_num = 0

for colour in fur_list:
    if colour == "Gray":
        grey_num += 1

    if colour == "Cinnamon":
        cinnamon_num += 1

    if colour == "Black":
        black_num += 1
# We could instead find number of rows for each colour by
# e.g. using squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"],
# then passing it through len() as it is treated as an iterable.


colour_dict = {
    "Fur Colour": ["grey", "cinnamon", "black"],
    "Count": [grey_num, cinnamon_num, black_num]
}

new_data = pandas.DataFrame(colour_dict)
squirrel_colour_csv = new_data.to_csv("squirrel_count.csv")
