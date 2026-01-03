import pandas as pd
from src.distance import haversine
from src.scoring import calculate_score

def recommend_places(source_city, max_distance=500):
    
    df = pd.read_csv("dataset/processed/weekend_places_processed.csv")

    
    source = df[df['City'] == source_city].iloc[0]
    src_lat, src_lng = source['Latitude'], source['Longitude']

    
    df['Distance_km'] = df.apply(
        lambda row: haversine(src_lat, src_lng, row['Latitude'], row['Longitude']),
        axis=1
    )

    
    df = df[df['Distance_km'] <= max_distance]

    
    df = calculate_score(df)

    
    return df.sort_values('final_score', ascending=False).head(10)
