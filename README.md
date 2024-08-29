Netflix Movie Recommendation API
Welcome to the Netflix Movie Recommendation API! This project provides a RESTful API for recommending movies based on tags and other features using machine learning techniques. The API is built using FastAPI, and it leverages cosine similarity and the CountVectorizer from scikit-learn to deliver movie recommendations similar to what you'd experience on Netflix.

Features
Movie Recommendations: Get personalized movie recommendations based on movie tags.
Cosine Similarity: Efficiently calculate the similarity between movies using cosine similarity.
FastAPI Framework: A modern, fast (high-performance) web framework for building APIs with Python 3.6+.
Scikit-learn Integration: Leverages the power of scikit-learn for vectorization and similarity calculations.
Extensible: Easily extendable to include more features such as user preferences, ratings, and genres.
Installation
To run the project locally, follow these steps:

Clone the repository:

bash
Copy code
git clone https://github.com/RajdevDhakar/Netflix-Movie-recommendation-API.git
cd Netflix-Movie-recommendation-API
Create a virtual environment:

bash
Copy code
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
Install the required packages:

bash
Copy code
pip install -r requirements.txt
Run the FastAPI server:

bash
Copy code
uvicorn main:app --reload
Access the API:

Open your browser and go to http://127.0.0.1:8000/docs to explore the API documentation and test the endpoints.

Usage
/recommend: This endpoint takes movie tags as input and returns a list of recommended movies.

Example request:

bash
Copy code
curl -X POST "http://127.0.0.1:8000/recommend" -H "Content-Type: application/json" -d '{"tags": "comedy, action"}'
Example response:

json
Copy code
{
    "recommended_movies": [
        "Movie 1",
        "Movie 2",
        "Movie 3"
    ]
}
Project Structure
main.py: The main entry point for the FastAPI application.
recommendation.py: Contains the logic for movie recommendation using cosine similarity and CountVectorizer.
models.py: Defines the data models used in the API.
requirements.txt: Lists the dependencies required to run the project.
Contributing
Contributions are welcome! If you have any ideas for improvements or new features, feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for more details.
