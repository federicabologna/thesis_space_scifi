import csv

def finalmeta_extraction(file_path):

    with open(file_path, 'r', encoding='utf-8') as csvfile:  # csvfile it's a variable
        reader = csv.DictReader(csvfile)  # DictReader it's a module needed for reading .csv files
        finalmeta_dict = dict() # our data structure: in  the values assigned to keys are dictionaries
        for row in reader:  # iteration over "rows" in .csv file
            if row["date"] > "1899" and "scifi" in row["tags"]:
                dictid = row["title"].lower()
                finalmeta_dict[dictid] = dict()
                finalmeta_dict[dictid]["htid"] = row["docid"]
                finalmeta_dict[dictid]["author"] = row["author"]
                finalmeta_dict[dictid]["date"] = row["date"]
                finalmeta_dict[dictid]["title"] = row["title"]

        return finalmeta_dict


def hugo_extraction(file_path):

    with open(file_path, 'r', encoding='utf-8') as csvfile:  # csvfile it's a variable
        reader = csv.DictReader(csvfile)  # DictReader it's a module needed for reading .csv files
        hugo_dict = dict()  # our data structure: in  the values assigned to keys are dictionaries
        for row in reader:  # iteration over "rows" in .csv file
            year = str(int(row["Year"]) - 1)
            title = title_polisher(row["Novel"])
            dictid = title.lower()
            name = name_polisher(row["Author(s)"])
            if dictid in hugo_dict.keys():
                hugo_dict[dictid]["author"] = hugo_dict[dictid]["author"] + ", " + name
            else:
                hugo_dict[dictid] = dict()
                hugo_dict[dictid]["htid"] = " "
                hugo_dict[dictid]["author"] = name
                hugo_dict[dictid]["date"] = year
                hugo_dict[dictid]["title"] = row["Novel"]

        return hugo_dict


def nebula_extraction(file_path):

    with open(file_path, 'r', encoding='utf-8') as csvfile:  # csvfile it's a variable
        reader = csv.DictReader(csvfile)  # DictReader it's a module needed for reading .csv files
        nebula_dict = dict()  # our data structure: in  the values assigned to keys are dictionaries
        for row in reader:  # iteration over "rows" in .csv file
            year = str(int(row["Year"]) - 1)
            name = name_polisher(row["Author"])
            dictid = row["Novel"].lower()
            if dictid in nebula_dict.keys():
                nebula_dict[dictid]["author"] = nebula_dict[dictid]["author"] + ", " + name
            else:
                nebula_dict[dictid] = dict()
                nebula_dict[dictid]["htid"] = " "
                nebula_dict[dictid]["author"] = name
                nebula_dict[dictid]["date"] = year
                nebula_dict[dictid]["title"] = row["Novel"]

        return nebula_dict


def name_polisher(name):
    name_wo_stars = name.replace("*", "")
    name_split = name_wo_stars.split(" ")
    if name_split[len(name_split)-2].lower() == "van" or name_split[len(name_split)-2].lower() == "le":
        last_name = name_split[len(name_split) - 2] + " " + name_split[len(name_split) - 1]
        name_split.insert(0, last_name)
        name_split.pop()
        name_split.pop()
    else:
        last_name = name_split[len(name_split)-1] + ","
        name_split.insert(0, last_name)
        name_split.pop()

    polished_name = " ".join(name_split)

    return polished_name

def title_polisher(title):
    title_split = title.split(" (")
    new_title = title_split[0]

    return new_title

