from metadata_extraction import *
import csv


def metadata_dict_creation(path1, path2, path3, path4):
    metadata_dict1 = dict()
    metadata_dict1.update(nebula_extraction(path3))
    metadata_dict1.update(hugo_extraction(path1))
    metadata_dict1.update(hugo_extraction(path2))
    metadata_dict1.update(finalmeta_extraction(path4))

    metadata_dict2 = dict()

    for value in metadata_dict1.values():
        dictid = value["date"] + "_" + value["title"]
        metadata_dict2[dictid] = dict()
        metadata_dict2[dictid].update(value)

    sorted_metadata_dict = dict(sorted(metadata_dict2.items()))

    return sorted_metadata_dict


def metadata_csv_creation(dictionary):

    with open('metadata4.csv', 'w', newline="") as csvfile:
        fieldnames = ["htid", "author", "date", "title"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in dictionary.values():
            writer.writerow(i)


#dictio = metadata_dict_creation("hugo.csv", "retrohugo.csv", "nebula.csv", "concatenatedmeta.csv")

#print(metadata_csv_creation(dictio))
