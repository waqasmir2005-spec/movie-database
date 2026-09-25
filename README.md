# Movie Database 🎬

A movie-search application prototype built with React, Vite, Python, Flask, and the TMDB API.

The project is designed to provide a React frontend with a Flask backend that searches TMDB and returns simplified movie data, including titles, release dates, ratings, descriptions, and poster images.

> **Project status:** Work in progress. The Flask search API is implemented. The React frontend and rating features are still being developed.

---

## ✨ Features

### Currently implemented

- Search movies using the TMDB API
- Flask backend API
- CORS support for frontend-backend communication
- Environment-variable support for API credentials
- Cleaned movie response data
- Movie title, release date, rating, overview, and poster URL
- Error responses for empty queries and failed API requests

### Planned improvements

- Complete React search interface
- Movie result cards
- Movie details page
- User rating functionality
- Loading and error states
- Responsive design
- Database support for storing user ratings
- Deployment configuration

---

## 🛠️ Tech Stack

### Frontend

- React
- Vite
- HTML
- JavaScript

### Backend

- Python
- Flask
- Flask-CORS
- Requests
- python-dotenv

### External service

- [TMDB API](https://developer.themoviedb.org/docs)

---

## 🏗️ How It Works

The application uses a frontend-backend architecture:

1. The user enters a movie search query in the React frontend.
2. The frontend sends the query to the Flask API.
3. Flask requests matching movies from TMDB.
4. The backend selects the relevant movie information.
5. Flask returns a simplified JSON response to the frontend.
6. The frontend displays the movie results.

### API endpoint

```text
GET /api/movies/search?q=movie-name
```

### Example request

```text
http://localhost:5000/api/movies/search?q=inception
```

### Example response

```json
[
  {
    "id": 27205,
    "title": "Inception",
    "release_date": "2010-07-15",
    "vote_average": 8.4,
    "overview": "A skilled thief who steals corporate secrets through dream-sharing technology...",
    "poster_path": "https://image.tmdb.org/t/p/w500/example.jpg"
  }
]
```

---

## 📁 Project Structure

```text
movie-database/
├── movie-database_app.py
├── movie-database_index.html
├── movie-database_package.json
├── movie-database_requirements.txt
├── README.md
└── src/
    ├── main.jsx
    ├── App.jsx
    └── App.css
```

> The `src/` directory is required by the Vite entry file. If it is not currently in the repository, add the React source files before running the frontend.

---

## ⚙️ Requirements

Before running the project, install:

- Python 3.9 or newer
- Node.js 18 or newer
- npm
- A TMDB API key

Create a TMDB account and generate an API key from the [TMDB developer dashboard](https://www.themoviedb.org/settings/api).

---

## 🔐 Environment Variables

Create a file named `.env` in the project root:

```env
TMDB_API_KEY=your_tmdb_api_key_here
```

Never commit your real API key to GitHub.

Create a `.gitignore` file containing:

```gitignore
.env
__pycache__/
*.pyc
node_modules/
dist/
.DS_Store
```

---

## 🚀 Backend Setup

Open a terminal in the project directory.

### 1. Create a virtual environment

#### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

#### macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install Python dependencies

```bash
pip install -r movie-database_requirements.txt
```

### 3. Start the Flask backend

```bash
python movie-database_app.py
```

The backend will run at:

```text
http://localhost:5000
```

---

## 💻 Frontend Setup

The frontend uses React and Vite.

### 1. Install JavaScript dependencies

If the package file remains named `movie-database_package.json`, run:

```bash
npm install --package-lock=false
```

For a standard Vite setup, rename the file to:

```text
package.json
```

Then run:

```bash
npm install
```

### 2. Start the development server

```bash
npm run dev
```

The frontend will usually be available at:

```text
http://localhost:5173
```

> The React frontend requires the `src/main.jsx`, `src/App.jsx`, and `src/App.css` files referenced by the HTML entry file.

---

## 📸 Screenshots

Add a screenshot after the React frontend is working:

```markdown
![Movie Database homepage](./docs/homepage.png)
```

Recommended screenshot location:

```text
docs/homepage.png
```

---

## 🔒 Security Notes

- Store the TMDB API key in `.env`.
- Do not commit `.env` to GitHub.
- Do not expose private API credentials in frontend JavaScript.
- Use a production WSGI server instead of Flask debug mode when deploying.
- Add request validation and rate limiting before deploying publicly.

---

## 📝 Current Limitations

- The backend currently uses Flask's development server.
- User ratings are not yet stored in a database.
- Authentication is not implemented.
- The frontend source files may still need to be added.
- The application is not yet configured for production deployment.
- The TMDB API key is required for movie searches.

---

## 🔮 Future Improvements

- Add React movie cards and search controls.
- Add a movie details view.
- Add rating storage with a database.
- Add user authentication.
- Add automated tests.
- Add loading and error states.
- Add pagination.
- Deploy the frontend and backend.
- Add CI checks with GitHub Actions.

---

## 🔗 Links

- GitHub: https://github.com/waqas-mir/movie-database
- LinkedIn: https://www.linkedin.com/in/waqasmir-dev/
- Email: [waqasmir2005@gmail.com](mailto:waqasmir2005@gmail.com)

---

## 📄 License

This project is currently for learning and demonstration purposes.
