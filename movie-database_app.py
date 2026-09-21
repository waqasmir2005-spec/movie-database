import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
CORS(app)  # Allows your React frontend to connect securely

TMDB_API_KEY = os.getenv("TMDB_API_KEY")
TMDB_BASE_URL = "https://api.themoviedb.org/3"

@app.route('/api/movies/search', methods=['GET'])
def search_movies():
    query = request.args.get('q', '')
    if not query:
        return jsonify({"error": "Search query cannot be empty"}), 400
        
    try:
        url = f"{TMDB_BASE_URL}/search/movie"
        params = {"api_key": TMDB_API_KEY, "query": query, "language": "en-US"}
        response = requests.get(url, params=params)
        
        if response.status_code != 200:
            return jsonify({"error": "Failed to fetch data from TMDB"}), response.status_code
            
        data = response.json()
        results = data.get('results', [])
        
        cleaned_movies = []
        for movie in results:
            cleaned_movies.append({
                "id": movie.get("id"),
                "title": movie.get("title"),
                "release_date": movie.get("release_date", "N/A"),
                "vote_average": movie.get("vote_average", 0.0),
                "overview": movie.get("overview", "No description available."),
                "poster_path": f"https://image.tmdb.org/t/p/w500{movie.get('poster_path')}" if movie.get('poster_path') else None
            })
            
        return jsonify(cleaned_movies), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
