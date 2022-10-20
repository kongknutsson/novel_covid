import pandas as pd

ISO_DATA_PATH = "data/country_iso_translations.csv"

class CountryIsoDataLoader:
    @staticmethod
    def load():
        iso_data = pd.read_csv(ISO_DATA_PATH, encoding="utf-8")
        iso_data = CountryIsoDataLoader._cast(iso_data)
        return iso_data

    @staticmethod
    def _cast(iso_data):
        return iso_data.astype(str)

