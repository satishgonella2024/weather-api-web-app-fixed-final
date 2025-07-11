def display_weather_info(weather_data):
    if not weather_data:
        return "No weather information available"
    
    city = weather_data.get("city", "")
    temperature = weather_data.get("temperature", "")
    description = weather_data.get("description", "")
    humidity = weather_data.get("humidity", "")

    if city and temperature != "":
        return f"Weather in {city}: {temperature}°C, {description}, Humidity: {humidity}%"
    else:
        raise Exception("Invalid weather data provided")