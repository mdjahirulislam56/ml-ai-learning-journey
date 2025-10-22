import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    popu_area = world.loc[:,['name','population','area']]
    output = popu_area.loc[((popu_area['area']>=3000000)|(popu_area['population']>=25000000))]
    return output

world = pd.read_csv("Big_Countries.csv")

cleaned_data = big_countries(world=world)

print(cleaned_data)