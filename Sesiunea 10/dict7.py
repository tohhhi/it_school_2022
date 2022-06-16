colors = {
    "red": "#FF0000",
    "green": "#00FF00",
    "blue": "#0000FF"
}

colors["blue"] = colors["blue"].strip("#")

print(colors)


def noner(dict_in, key):
    if key in dict_in.keys():
        dict_in[key] = None


noner(colors, "gray")

print(colors)