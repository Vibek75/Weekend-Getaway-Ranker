def calculate_score(df):
    
    df['airport_score'] = df['Airport with 50km Radius'].apply(lambda x: 1 if x == 'Yes' else 0)

    df['distance_norm'] = 1 - (df['Distance_km'] / df['Distance_km'].max())

    
    df['rating_norm'] = (
        df['Google review rating'] /
        df['Google review rating'].max()
    )

    
    df['popularity_norm'] = (
        df['Number of google review in lakhs'] /
        df['Number of google review in lakhs'].max()
    )
    df['time_norm'] = (
        1 - (df['time needed to visit in hrs'] / df['time needed to visit in hrs'].max())
    )
    
    df['fee_norm'] = (
     1 - (
        df['Entrance Fee in INR'] /
        df['Entrance Fee in INR'].max()
      )
    )
    
    df['final_score'] = (
            0.25 * df['rating_norm'] +
            0.25 * df['popularity_norm'] +
            0.25 * df['distance_norm'] +
            0.15 * df['time_norm'] +
            0.10 * df['airport_score'] +
            0.05 * df['fee_norm']
    )

    return df
