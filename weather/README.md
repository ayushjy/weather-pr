# Weather App

A simple weather application that provides real-time weather information for a given city. The project consists of a Python Flask backend and a vanilla HTML/CSS/JavaScript frontend.

## 📂 Folder Structure

```
weather/
├── backend/            # Backend API (Flask)
│   ├── .venv/          # Virtual environment (managed by uv)
│   ├── main.py         # Main application entry point
│   ├── pyproject.toml  # Project dependencies and configuration
│   └── uv.lock         # Dependency lock file for uv
├── frontend/           # Frontend Application
│   ├── index.html      # Main HTML file
│   └── style.css       # Styles
└── README.md           # Project documentation
```

## 🚀 Workflows

### 1. Backend Workflow
The backend is built with **Flask** and uses **uv** for dependency management. It acts as an intermediary between the frontend and the Open-Meteo API.

*   **Input**: Receives a city name via the `/weather` endpoint.
*   **Processing**:
    1.  Calls `https://geocoding-api.open-meteo.com` to convert the city name to latitude and longitude.
    2.  Calls `https://api.open-meteo.com` with the coordinates to fetch current weather data (temperature, wind speed, etc.).
*   **Output**: Returns a JSON object with the city's weather details.

### 2. Frontend Workflow
The frontend is a lightweight web interface.

*   **User Action**: User enters a city name and clicks "Check".
*   **Request**: `index.html` (via JavaScript) sends an HTTP GET request to `http://127.0.0.1:5000/weather?city={city}`.
*   **Display**: The received JSON data is dynamically rendered into the HTML DOM.

## 📦 Installed Packages

The backend utilizes the following Python packages (managed via `uv`):

*   **flask**: Web framework for creating the API.
*   **requests**: HTTP library for making calls to the Open-Meteo API.
*   **flask-cors**: Extension to handle Cross-Origin Resource Sharing (CORS), allowing the frontend to communicate with the backend.

## 🛠️ Setup & Installation

## Running the Project After Cloning

The backend uses `uv` for ultra-fast Python package management.

1.  Clone Repository
    ```bash
    git clone https://github.com/ayushjy/weather-pr.git
    cd weather-pr
    ```

2.  Setup Backend Environment
    Navigate to backend folder:
    ```bash
    cd backend
    ```
3.  Recreate the exact environment from project metadata:
    ```bash
    uv sync
    ```
    This installs dependencies based on:
        pyproject.toml
        uv.lock
    and creates a local .venv.

4.  Run the application:
    ```bash
    uv run python main.py
    ```
    The server will start at `http://127.0.0.1:5000`.

### Frontend Setup

1.  Simply open the `frontend/index.html` file in any modern web browser.
2.  Ensure the backend server is running.
3.  Enter a city name to see the weather.

## 🔌 API Endpoints

### `GET /`
**Description**: Checks if the API is running.
*   **Response**: `{"status": "Weather API Running"}`

### `GET /weather`
**Description**: Fetches weather data for a specific city.
*   **Parameters**:
    *   `city` (query param): Name of the city (e.g., `?city=London`)
*   **Response**:
    ```json
    {
      "city": "London",
      "latitude": 51.50853,
      "longitude": -0.12574,
      "temperature": 15.2,
      "windspeed": 10.5,
      "winddirection": 240,
      "weathercode": 3,
      "time": "2023-10-27T14:00"
    }
    ```
