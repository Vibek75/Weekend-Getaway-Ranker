from src.recommend import recommend_places

if __name__ == "__main__":
    
    source_city = input("Enter Source City: ").strip()

    
    recommendations = recommend_places(source_city)

    
    output = recommendations[
        [
            'City',
            'Name',
            'Distance_km',
            'Google review rating',
            'Number of google review in lakhs',
            'final_score'
        ]
    ].copy()

    
    output['Distance_km'] = output['Distance_km'].round(2)
    output['Google review rating'] = output['Google review rating'].round(1)
    output['final_score'] = output['final_score'].round(3)

    
    output.rename(columns={
        'Google review rating': 'Rating',
        'Number of google review in lakhs': 'Reviews (Lakhs)',
        'final_score': 'Score'
    }, inplace=True)

    
    output = output.sort_values(by='Score', ascending=False)

    print("\nTop 10 Weekend Getaway Destinations:\n")
    print(output.to_string(index=False))
