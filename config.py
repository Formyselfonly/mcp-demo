"""
Configuration file for MCP tools.
Set your API keys here to enable real-time data.
"""

# OpenWeatherMap API Configuration
# Get your free API key at: https://openweathermap.org/api_keys
OPENWEATHER_API_KEY = "fb105ff5efb97d5490f53072bf095c6f"

# Google Custom Search API Configuration (optional)
# Get your API key at: https://developers.google.com/custom-search/v1/introduction
GOOGLE_SEARCH_API_KEY = ""
GOOGLE_SEARCH_ENGINE_ID = ""

# Bing Search API Configuration (optional)
# Get your API key at: https://www.microsoft.com/en-us/bing/apis/bing-web-search-api
BING_SEARCH_API_KEY = ""

# Configuration for demo mode
USE_DEMO_MODE = False  # Set to False when you have API keys configured

def get_weather_api_key():
    """Get the OpenWeatherMap API key."""
    return OPENWEATHER_API_KEY

def get_google_search_config():
    """Get Google Search API configuration."""
    return {
        "api_key": GOOGLE_SEARCH_API_KEY,
        "engine_id": GOOGLE_SEARCH_ENGINE_ID
    }

def get_bing_search_config():
    """Get Bing Search API configuration."""
    return {
        "api_key": BING_SEARCH_API_KEY
    }

def is_demo_mode():
    """Check if demo mode is enabled."""
    return USE_DEMO_MODE or not OPENWEATHER_API_KEY
