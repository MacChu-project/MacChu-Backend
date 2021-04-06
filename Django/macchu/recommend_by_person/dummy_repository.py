class DummyRepository:

    def select_dummy_data(self):

        import csv
        import pandas as pd

        beer_df = pd.read_csv('recommend_by_person/beers.csv', encoding="utf-8")
        beer_drop_df = beer_df.dropna(axis=0)
        result = beer_drop_df.to_dict('records')

        return result

    # 0 ~ 1142
    def select_dummy_data_one(self, key):

        import csv
        import pandas as pd

        beer_df = pd.read_csv('recommend_by_person/beers.csv', encoding="utf-8")
        beer_drop_df = beer_df.dropna(axis=0)
        result = beer_drop_df.iloc[int(key)].to_dict()

        return result