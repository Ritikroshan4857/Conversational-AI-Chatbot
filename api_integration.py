import requests
import json
import os

# 1. Weather API Integration
def get_weather(city_name, api_key=None):
    """
    Fetches weather information for a given city using OpenWeatherMap API.
    """
    if api_key is None:
        api_key = os.getenv("OPENWEATHER_API_KEY")  # Set this in your environment variables

    if not api_key:
        return "Weather API key is missing."

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        if data.get("cod") != 200:
            return f"Could not fetch weather for {city_name}. Reason: {data.get('message', 'Unknown error')}"
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        return f"The weather in {city_name} is {weather} with a temperature of {temp}°C."
    except Exception as e:
        return f"Error fetching weather: {str(e)}"

# 2. FAQ Search Integration (Simulated)
def get_faq_answer(user_question, faq_file='data/faq.json'):
    """
    Searches a local FAQ JSON file for a matching question.
    """
    try:
        with open(faq_file, 'r') as f:
            faqs = json.load(f)
        for faq in faqs.get("faqs", []):
            if user_question.lower() in faq["question"].lower():
                return faq["answer"]
        return "Sorry, I couldn't find an answer to your question."
    except Exception as e:
        return f"Error searching FAQ: {str(e)}"

# Example usage
if __name__ == "__main__":
    # Test weather
    print(get_weather("Chennai", api_key="YOUR_OPENWEATHERMAP_API_KEY"))

    # Test FAQ (make sure data/faq.json exists with correct format)
    print(get_faq_answer("What is your return policy?"))
