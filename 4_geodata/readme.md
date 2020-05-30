# Stage 4. Urban geographic locations

Analysis of the occurrence of urban geographic locations in the science fiction corpus compared to a random corpus.

The geographic locations contained in both corpora were easily accessed thanks to the [<i>Textual Geographies</i>](http://www.txtgeo.net/ "Textual Geographies") project.

Textual Geographies makes available the geographic data related to the HathiTrust digital library. The data is produced by first extracting the named locations from the volumes using [Stanford’s named entity recognizer (NER)](https://nlp.stanford.edu/ner/ "Stanford's NER"). Then, the resulting location strings are associated with geographic data from Google’s Places and Geocoding APIs. Once the geographic data is retrieved, the addresses are manually checked for greater accuracy. A more complete description of this process can be found in Elizabeth Evans and Matthew Wilkens. ["Nation, Ethnicity, and the Geography of British Fiction, 1880-1940,"](https://culturalanalytics.org/article/11037-nation-ethnicity-and-the-geography-of-british-fiction-1880-1940) 16.

The code for a further cleaninf of the addresses for the purposes of this study is available in [geodata_correction.ipynb](https://github.com/federicabologna/thesis_space_scifi/blob/master/4_geodata/geodata_correction.ipynb).

Whereas, the code for analyzing the occurrences of urban locations in the science fiction and random corpora is available in [geodata_stats.ipynb](https://github.com/federicabologna/thesis_space_scifi/blob/master/4_geodata/geodata_stats.ipynb). For the purposes of this study, we defined urban locations as those associated with a [third-level administrative area or lower](https://developers.google.com/places/supported_types#table3, "Google's Places API documentation") (including all localities).
