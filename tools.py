from langchain.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper

# Tool 1: Web Search
search_tool = DuckDuckGoSearchRun()

# Tool 2: Wikipedia
wiki = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=500)

@tool
def wikipedia_search(query: str) -> str:
    """Search Wikipedia for information about a topic."""
    return wiki.run(query)

# Export
all_tools = [search_tool, wikipedia_search]