from metadata_creation import *

def novel_decade_counter(dictionary):

    count_dict = dict()
    count_dict["count_00s"] = 0
    count_dict["count_10s"] = 0
    count_dict["count_20s"] = 0
    count_dict["count_30s"] = 0
    count_dict["count_40s"] = 0
    count_dict["count_50s"] = 0
    count_dict["count_60s"] = 0
    count_dict["count_70s"] = 0
    count_dict["count_80s"] = 0
    count_dict["count_90s"] = 0
    count_dict["count_000s"] = 0
    count_dict["count_010s"] = 0

    for key in dictionary.keys():
        n = int(key[:4])
        if 1899 < n < 1950:
            if 1899 < n < 1910:
                count_dict["count_00s"] = count_dict["count_00s"] + 1
            if 1909 < n < 1920:
                count_dict["count_10s"] = count_dict["count_10s"] + 1
            if 1919 < n < 1930:
                count_dict["count_20s"] = count_dict["count_20s"] + 1
            if 1929 < n < 1940:
                count_dict["count_30s"] = count_dict["count_30s"] + 1
            if 1939 < n < 1950:
                count_dict["count_40s"] = count_dict["count_40s"] + 1
        if 1949 < n < 1999:
            if 1949 < n < 1960:
                count_dict["count_50s"] = count_dict["count_50s"] + 1
            if 1959 < n < 1970:
                count_dict["count_60s"] = count_dict["count_60s"] + 1
            if 1969 < n < 1980:
                count_dict["count_70s"] = count_dict["count_70s"] + 1
            if 1979 < n < 1990:
                count_dict["count_80s"] = count_dict["count_80s"] + 1
            if 1989 < n < 2000:
                count_dict["count_90s"] = count_dict["count_90s"] + 1
        if n > 2000:
            if 2000 < n < 2010:
                count_dict["count_000s"] = count_dict["count_000s"] + 1
            if n > 2009:
                count_dict["count_010s"] = count_dict["count_010s"] + 1

    decade_count_dict = dict()
    for key, value in count_dict.items():
        decade_count_dict[key] = dict()
        decade_count_dict[key]["decade"] = key[6:]
        decade_count_dict[key]["number of novels"] = value

    with open('novel_number_decade4.csv', 'w', newline="") as csvfile:
        fieldnames = ["decade", "number of novels"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in decade_count_dict.values():
            writer.writerow(i)

    return count_dict, decade_count_dict


dictio = metadata_dict_creation("hugo.csv", "retrohugo.csv", "nebula.csv", "concatenatedmeta.csv")
print(novel_decade_counter(dictio))
