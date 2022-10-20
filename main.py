from covid_data_loader import CovidDataLoader
from country_iso_data_loader import CountryIsoDataLoader
from elastic_helper import ElasticHelper
import pandas as pd 

INDEX_NAME = "covid-data"

covid_data = CovidDataLoader.load()
iso_data = CountryIsoDataLoader.load()

exit()

covid_data_with_iso = pd.merge(
    left= covid_data,
    right = iso_data[["name", "alpha-2"]],
    how= "inner",
    left_on = "Country/Region",
    right_on = "name"
)



covid_data_with_iso = covid_data_with_iso.dropna(subset=["Country/Region"])
covid_data_with_iso = covid_data_with_iso.drop("name", axis=1)
print(covid_data_with_iso.info())


es = ElasticHelper()
#es.create_index(index_name="covid-data", mappings=mappings)

answ = input("Recreate index? (y/n) ")
if answ == "y":
    mappings = {
        'properties': {
            'SNo': {'type': 'keyword'},
            'ObservationDate': {'type': 'date'},
            'Province/State': {'type': 'keyword'},
            'Country/Region': {'type': 'keyword'},
            'Last Update': {'type': 'date'},
            'Confirmed': {'type': 'long'},
            'Deaths': {'type': 'long'},
            'Recovered': {'type': 'long'},
            'alpha-2': {'type': 'keyword'},
        }
    }
    es.delete_index(INDEX_NAME)
    es.create_index(INDEX_NAME, mappings)
es.bulk_insert(INDEX_NAME, covid_data_with_iso)

