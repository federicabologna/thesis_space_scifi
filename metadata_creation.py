from metadata_extraction import *
import csv

def metadata_creation(path1, path2, path3, path4):
    metadata_dict = dict()
    metadata_dict.update(hugo_extraction(path1))
    metadata_dict.update(hugo_extraction(path2))
    metadata_dict.update(nebula_extraction(path3))
    metadata_dict.update(finalmeta_extraction(path4))

    sorted_metadata_dict = dict(sorted(metadata_dict.items()))

    with open('metadata.csv', 'w', newline="") as csvfile:
        fieldnames = ["author", "date", "title"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in sorted_metadata_dict.values():
            writer.writerow(i)

    return sorted_metadata_dict

print(metadata_creation("hugo.csv", "retrohugo.csv", "nebula.csv", "finalmeta.csv"))