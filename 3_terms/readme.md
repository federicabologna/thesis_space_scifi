# Stage 3. Urban terms

Analysis of the occurrence of "urban terms" in the science fiction corpus compared to a random corpus.

The random corpus was created by randomly selecting fiction books for the HathiTrust catalog. The random fiction corpus was 50 times the size of the science fiction corpus.

By “urban terms”, I indicate terms that can commonly be found in narratives that focus on cityspace. Such terms define places and objects that belong to highly urbanized areas and characterize the urban experience. The list of urban terms used in this study was created by using Williams’ The Country and the City as main reference, as well as Eisner’s comics on New York – New York: The Big City specifically –, and the thesaurus of the MacMillan Dictionary of English Language. The terms were listed in their lemmatized form in order to easily include all the different inflections without having to singularly enlist them.

The occurrences of all the lemmas contained in all the books from both corpora were retrieved and stored in a CSV file. The code for this process is available in [terms_extraction.ipynb](https://github.com/federicabologna/thesis_space_scifi/blob/master/3_terms/terms_extraction.ipynb).

Then, this data was analyzed and compared statistically across the corpora. The code for this analysis is available in [terms_stats.ipynb](https://github.com/federicabologna/thesis_space_scifi/blob/master/3_terms/terms_stats.ipynb).

* [“Areas in Towns or Cities - Synonyms and Related Words.”](https://www.macmillandictionary.com/thesaurus-category/british/areas-in-towns-or-cities) Macmillan Dictionary.
* Eisner, Will. New York: The Big City. WW Norton & Company, 2006.
* Williams, Raymond. The country and the city. Vol. 423. Oxford University Press, 
USA, 1975.
