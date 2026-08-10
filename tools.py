from langchain.tools import tool
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
import os
from rich import print
from dotenv import load_dotenv
load_dotenv()
tavily=TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def sweb_search(query: str) -> str:
    """
    Search the web for a recent and reliable answer to the given query and return titles,URLs and Snippets.
    """
    results =tavily.search(query=query, max_results=5)

    out=[]
    for result in results["results"]:
        title = result['title']
        url = result['url']
        snippet = result['content']
        out.append(f"Title: {title}\nURL: {url}\nSnippet: {snippet}\n")
    return "\n".join(out)





@tool
def scrape_url(url: str) -> str:
    """Scrape and return clean text content from a given URL for deeper reading."""
    try:
        resp = requests.get(
            url,
            timeout=8,
            headers={"User-Agent": "Mozilla/5.0"}
        )

        soup = BeautifulSoup(resp.text, "html.parser")

        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()

        return soup.get_text(separator=" ", strip=True)[:3000]

    except Exception as e:
        return f"Could not scrape URL: {str(e)}"

