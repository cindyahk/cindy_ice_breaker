from langchain_community.tools.tavily_search import TavilySearchResults


def get_profile_url_tavily(name: str):
<<<<<<< Updated upstream
    """Searches for Linkedin or Twitter Profile Page."""
    search = TavilySearchResults()
    res = search.run(f"{name}")
    return res[0]["url"]
=======
    """searches for Linkedin Profile url"""
    search = TavilySearchResults();
    res = search.run(f'{name}')
    return res[0]['url']
>>>>>>> Stashed changes
