import requests
import json
from typing import Dict, Any, Optional
from datetime import datetime, timedelta
import config

def get_weather(city: str, country_code: str = "", api_key: str = "") -> str:
    """Get current weather information for a city.
    
    Args:
        city: City name (e.g., "Beijing", "New York")
        country_code: Country code (optional, e.g., "CN", "US")
        api_key: OpenWeatherMap API key (optional, will use config or demo data if not provided)
    
    Returns:
        str: Weather information in JSON format
    """
    try:
        # Use provided API key, or get from config, or use demo data
        if not api_key:
            api_key = config.get_weather_api_key()
        
        if not api_key or config.is_demo_mode():
            return get_demo_weather(city, country_code)
        
        # Use OpenWeatherMap API
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        
        # Build query parameters
        params = {
            "q": f"{city},{country_code}" if country_code else city,
            "appid": api_key,
            "units": "metric"  # Use Celsius
        }
        
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        # Format the weather data
        weather_info = {
            "location": {
                "city": data["name"],
                "country": data["sys"]["country"],
                "coordinates": {
                    "lat": data["coord"]["lat"],
                    "lon": data["coord"]["lon"]
                }
            },
            "current_weather": {
                "temperature": data["main"]["temp"],
                "feels_like": data["main"]["feels_like"],
                "humidity": data["main"]["humidity"],
                "pressure": data["main"]["pressure"],
                "description": data["weather"][0]["description"],
                "main": data["weather"][0]["main"],
                "icon": data["weather"][0]["icon"]
            },
            "wind": {
                "speed": data["wind"]["speed"],
                "direction": data["wind"].get("deg", "N/A")
            },
            "visibility": data.get("visibility", "N/A"),
            "timestamp": datetime.fromtimestamp(data["dt"]).strftime("%Y-%m-%d %H:%M:%S"),
            "sunrise": datetime.fromtimestamp(data["sys"]["sunrise"]).strftime("%H:%M:%S"),
            "sunset": datetime.fromtimestamp(data["sys"]["sunset"]).strftime("%H:%M:%S")
        }
        
        return json.dumps(weather_info, indent=2, ensure_ascii=False)
        
    except requests.exceptions.RequestException as e:
        error_result = {
            "error": f"Weather API error: {str(e)}",
            "city": city,
            "suggestion": "Please check your internet connection or try a different city name"
        }
        return json.dumps(error_result, indent=2, ensure_ascii=False)
    
    except Exception as e:
        error_result = {
            "error": f"Weather service error: {str(e)}",
            "city": city
        }
        return json.dumps(error_result, indent=2, ensure_ascii=False)

def get_demo_weather(city: str, country_code: str = "") -> str:
    """Get demo weather data when no API key is available.
    
    Args:
        city: City name
        country_code: Country code (optional)
    
    Returns:
        str: Demo weather information in JSON format
    """
    # Demo weather data for demonstration purposes
    demo_data = {
        "location": {
            "city": city,
            "country": country_code or "Demo",
            "coordinates": {
                "lat": 39.9042,
                "lon": 116.4074
            }
        },
        "current_weather": {
            "temperature": 22.5,
            "feels_like": 24.0,
            "humidity": 65,
            "pressure": 1013,
            "description": "partly cloudy",
            "main": "Clouds",
            "icon": "02d"
        },
        "wind": {
            "speed": 3.2,
            "direction": 180
        },
        "visibility": 10000,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "sunrise": "06:30:00",
        "sunset": "18:45:00"
    }
    
    # Add a note that this is demo data
    demo_data["note"] = "This is demo weather data. To get real weather data, please provide an OpenWeatherMap API key."
    demo_data["api_info"] = {
        "service": "OpenWeatherMap",
        "website": "https://openweathermap.org/api",
        "signup": "https://openweathermap.org/api_keys"
    }
    
    return json.dumps(demo_data, indent=2, ensure_ascii=False)

def get_weather_forecast(city: str, days: int = 5, api_key: str = "") -> str:
    """Get weather forecast for a city.
    
    Args:
        city: City name
        days: Number of forecast days (1-5)
        api_key: OpenWeatherMap API key (optional)
    
    Returns:
        str: Weather forecast in JSON format
    """
    try:
        # Use provided API key, or get from config, or use demo data
        if not api_key:
            api_key = config.get_weather_api_key()
        
        if not api_key or config.is_demo_mode():
            return get_demo_forecast(city, days)
        
        # Use OpenWeatherMap 5-day forecast API
        base_url = "http://api.openweathermap.org/data/2.5/forecast"
        
        params = {
            "q": city,
            "appid": api_key,
            "units": "metric"
        }
        
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        # Process forecast data
        forecast_info = {
            "location": {
                "city": data["city"]["name"],
                "country": data["city"]["country"]
            },
            "forecast_days": days,
            "forecast": []
        }
        
        # Group forecasts by day
        daily_forecasts = {}
        for item in data["list"]:
            date = datetime.fromtimestamp(item["dt"]).strftime("%Y-%m-%d")
            if date not in daily_forecasts:
                daily_forecasts[date] = []
            daily_forecasts[date].append(item)
        
        # Get forecast for requested days
        forecast_dates = sorted(daily_forecasts.keys())[:days]
        
        for date in forecast_dates:
            day_forecasts = daily_forecasts[date]
            # Get the forecast closest to noon for each day
            noon_forecast = min(day_forecasts, key=lambda x: abs(12 - datetime.fromtimestamp(x["dt"]).hour))
            
            forecast_info["forecast"].append({
                "date": date,
                "temperature": {
                    "min": min(f["main"]["temp"] for f in day_forecasts),
                    "max": max(f["main"]["temp"] for f in day_forecasts),
                    "current": noon_forecast["main"]["temp"]
                },
                "description": noon_forecast["weather"][0]["description"],
                "humidity": noon_forecast["main"]["humidity"],
                "wind_speed": noon_forecast["wind"]["speed"]
            })
        
        return json.dumps(forecast_info, indent=2, ensure_ascii=False)
        
    except Exception as e:
        error_result = {
            "error": f"Forecast error: {str(e)}",
            "city": city
        }
        return json.dumps(error_result, indent=2, ensure_ascii=False)

def get_demo_forecast(city: str, days: int = 5) -> str:
    """Get demo weather forecast data.
    
    Args:
        city: City name
        days: Number of forecast days
    
    Returns:
        str: Demo forecast data in JSON format
    """
    forecast_info = {
        "location": {
            "city": city,
            "country": "Demo"
        },
        "forecast_days": days,
        "forecast": [],
        "note": "This is demo forecast data. To get real forecast data, please provide an OpenWeatherMap API key."
    }
    
    # Generate demo forecast for the requested number of days
    for i in range(days):
        date = (datetime.now() + timedelta(days=i)).strftime("%Y-%m-%d")
        forecast_info["forecast"].append({
            "date": date,
            "temperature": {
                "min": 15 + i,
                "max": 25 + i,
                "current": 20 + i
            },
            "description": ["sunny", "partly cloudy", "cloudy", "rainy", "clear"][i % 5],
            "humidity": 60 + (i * 5),
            "wind_speed": 2.0 + (i * 0.5)
        })
    
    return json.dumps(forecast_info, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    # Test the functions
    print("Testing current weather (demo):")
    print(get_weather("Beijing"))
    print("\n" + "="*50 + "\n")
    print("Testing weather forecast (demo):")
    print(get_weather_forecast("Shanghai", 3))
