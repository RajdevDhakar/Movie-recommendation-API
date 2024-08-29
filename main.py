from fastapi import FastAPI
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load your dataset
movies = pd.read_csv('dataset.csv')
movies = movies[['id', 'title', 'genre', 'overview']]
movies['tags'] = movies['genre'] + movies['overview']
new_data = movies.drop(columns=['genre', 'overview'])

# Vectorize the tags
cv = CountVectorizer(max_features=10000, stop_words='english')
vector = cv.fit_transform(new_data['tags'].values.astype('U')).toarray()

# Calculate similarity
similarity = cosine_similarity(vector)

def recommend(movie_title):
    index = new_data[new_data['title'] == movie_title].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    recommended_movies = [new_data.iloc[i[0]].title for i in distances[1:11]]
    return recommended_movies

app = FastAPI()

# FastAPI route for movie recommendation
@app.get("/recommend/{movie_title}")
async def get_recommendations(movie_title: str):
    try:
        recommendations = recommend(movie_title)
        return {"recommended_movies": recommendations}
    except IndexError:
        return {"error": "Movie not found"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
