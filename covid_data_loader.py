import pandas as pd
DATA_SAVE_PATH = "data/covid_19_data.csv"

class CovidDataLoader:
    @staticmethod
    def load() -> pd.DataFrame:
        covid_data = CovidDataLoader._read_data()
        covid_data = CovidDataLoader._cast_data_types(covid_data) 
        return covid_data

    @staticmethod
    def _read_data() -> pd.DataFrame:
        return pd.read_csv(DATA_SAVE_PATH, encoding="utf-8")

    @staticmethod
    def _cast_data_types(covid_data: pd.DataFrame) -> pd.DataFrame:

        print(covid_data.notna())

        covid_data = covid_data.dropna() # TODO Make more granular than deleting everything. 
        covid_data["ObservationDate"] = pd.to_datetime(covid_data["ObservationDate"])
        covid_data["Last Update"] = pd.to_datetime(covid_data["Last Update"])
        covid_data["Province/State"] = covid_data["Province/State"].astype(str)
        covid_data["Country/Region"] = covid_data["Country/Region"].astype(str)

        return covid_data