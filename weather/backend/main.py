from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return jsonify({"status": "Weather API Running"})


# Weather Endpoint

@app.route("/weather")
def weather():

    city = request.args.get("city")

    if not city:
        return jsonify({"error": "City required"}), 400

    try:
        # Step 1 — Get coordinates from city name
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
        geo_data = requests.get(geo_url).json()

        if "results" not in geo_data:
            return jsonify({"error": "City not found"}), 404

        lat = geo_data["results"][0]["latitude"]
        lon = geo_data["results"][0]["longitude"]

        # Step 2 — Get weather
        weather_url = (
            f"https://api.open-meteo.com/v1/forecast?"
            f"latitude={lat}&longitude={lon}"
            f"&current_weather=true"
        )

        weather_data = requests.get(weather_url).json()
        current = weather_data["current_weather"]

        result = {
            "city": city,
            "latitude": lat,
            "longitude": lon,
            "temperature": current["temperature"],
            "windspeed": current["windspeed"],
            "winddirection": current["winddirection"],
            "weathercode": current["weathercode"],
            "time": current["time"]
        }

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
