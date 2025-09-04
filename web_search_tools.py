import requests
import json
from typing import Dict, Any, List
from urllib.parse import quote_plus
import time

def web_search(query: str, num_results: int = 5) -> str:
    """Perform web search using DuckDuckGo instant answer API and web search.
    
    Args:
        query: The search query string
        num_results: Number of search results to return (default: 5)
    
    Returns:
        str: Search results in JSON format
    """
    try:
        # Use DuckDuckGo instant answer API for quick results
        instant_answer_url = f"https://api.duckduckgo.com/?q={quote_plus(query)}&format=json&no_html=1&skip_disambig=1"
        
        response = requests.get(instant_answer_url, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        results = {
            "query": query,
            "instant_answer": None,
            "web_results": [],
            "related_topics": []
        }
        
        # Extract instant answer if available
        if data.get("Abstract"):
            results["instant_answer"] = {
                "title": data.get("Heading", ""),
                "abstract": data.get("Abstract", ""),
                "url": data.get("AbstractURL", ""),
                "image": data.get("Image", "")
            }
        
        # Extract related topics
        if data.get("RelatedTopics"):
            for topic in data["RelatedTopics"][:3]:  # Limit to 3 related topics
                if isinstance(topic, dict) and topic.get("Text"):
                    results["related_topics"].append({
                        "text": topic.get("Text", ""),
                        "url": topic.get("FirstURL", "")
                    })
        
        # For more comprehensive results, we'll also try a simple web scraping approach
        # Note: This is a basic implementation. For production use, consider using
        # proper search APIs like Google Custom Search, Bing Search API, etc.
        
        # Add a simple web search simulation (since we can't use real search APIs without keys)
        # In a real implementation, you would use proper search APIs
        results["web_results"] = [
            {
                "title": f"Search result for: {query}",
                "url": f"https://duckduckgo.com/?q={quote_plus(query)}",
                "snippet": f"Search results for '{query}' - Click to view on DuckDuckGo"
            }
        ]
        
        return json.dumps(results, indent=2, ensure_ascii=False)
        
    except requests.exceptions.RequestException as e:
        error_result = {
            "error": f"Network error: {str(e)}",
            "query": query,
            "suggestion": "Please check your internet connection and try again"
        }
        return json.dumps(error_result, indent=2, ensure_ascii=False)
    
    except Exception as e:
        error_result = {
            "error": f"Search error: {str(e)}",
            "query": query
        }
        return json.dumps(error_result, indent=2, ensure_ascii=False)

def get_news(query: str = "technology", num_articles: int = 5) -> str:
    """Get recent news articles using DuckDuckGo news search.
    
    Args:
        query: News search query (default: "technology")
        num_articles: Number of articles to return (default: 5)
    
    Returns:
        str: News articles in JSON format
    """
    try:
        # Use DuckDuckGo news search
        news_url = f"https://api.duckduckgo.com/?q={quote_plus(query)}&format=json&t=duckduckgo"
        
        response = requests.get(news_url, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        news_results = {
            "query": query,
            "articles": [],
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # Extract news articles if available
        if data.get("RelatedTopics"):
            for topic in data["RelatedTopics"][:num_articles]:
                if isinstance(topic, dict) and topic.get("Text"):
                    news_results["articles"].append({
                        "title": topic.get("Text", ""),
                        "url": topic.get("FirstURL", ""),
                        "source": "DuckDuckGo"
                    })
        
        # If no specific news found, provide a general news search link
        if not news_results["articles"]:
            news_results["articles"].append({
                "title": f"Latest news about {query}",
                "url": f"https://duckduckgo.com/?q={quote_plus(query)}&t=h_&iar=news&ia=news",
                "source": "DuckDuckGo News"
            })
        
        return json.dumps(news_results, indent=2, ensure_ascii=False)
        
    except Exception as e:
        error_result = {
            "error": f"News search error: {str(e)}",
            "query": query
        }
        return json.dumps(error_result, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    # Test the functions
    print("Testing web search:")
    print(web_search("Python programming"))
    print("\n" + "="*50 + "\n")
    print("Testing news search:")
    print(get_news("artificial intelligence"))
