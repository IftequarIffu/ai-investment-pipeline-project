import httpx
from typing import List, Dict

YC_COMPANY_BASE_URL = "https://www.ycombinator.com/companies"

def source_yc_by_algolia_curl(query_phrase: str, limit: int = 3) -> List[Dict]:
    """
    Executes a highly-targeted search on YC's production index 
    using the exact parameters extracted from network developer tools.
    """
    # 1. URL and query string parameters extracted from your curl command
    url = "https://45bwzj1sgc-dsn.algolia.net/1/indexes/*/queries"
    params = {
        "x-algolia-agent": "Algolia for JavaScript (3.35.1); Browser; JS Helper (3.16.1)",
        "x-algolia-application-id": "45BWZJ1SGC",
        "x-algolia-api-key": "NzllNTY5MzJiZGM2OTY2ZTQwMDEzOTNhYWZiZGRjODlhYzVkNjBmOGRjNzJiMWM4ZTU0ZDlhYTZjOTJiMjlhMWFuYWx5dGljc1RhZ3M9eWNkYyZyZXN0cmljdEluZGljZXM9WUNDb21wYW55X3Byb2R1Y3Rpb24lMkNZQ0NvbXBhbnlfQnlfTGF1bmNoX0RhdGVfcHJvZHVjdGlvbiZ0YWdGaWx0ZXJzPSU1QiUyMnljZGNfcHVibGljJTIyJTVE"
    }

    # 2. Strict Request Headers for Request Authenticity 
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://www.ycombinator.com",
        "Referer": "https://www.ycombinator.com/",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
    }

    # 3. Request Payload formatting 
    # Note: We omitted the restrictive batch year filters from your curl 
    # to ensure you capture ALL historic companies matching your query string.
    payload = {
        "requests": [
            {
                "indexName": "YCCompany_production",
                "params": f"hitsPerPage={limit}&page=0&query={query_phrase}"
            }
        ]
    }

    try:
        # Algolia handles the incoming payload as a JSON string, despite the x-www-form-urlencoded header
        response = httpx.post(url, params=params, headers=headers, json=payload, timeout=10.0)
        response.raise_for_status()
        
        raw_data = response.json()
        
        # Algolia returns an array of results matching the array of requests sent
        results_list = raw_data.get("results", [])
        if not results_list:
            return []
            
        hits = results_list[0].get("hits", [])
        
        candidates = []
        for hit in hits:
            candidates.append({
                "name": hit.get("name"),
                "slug": hit.get("slug"),
                "website": hit.get("website"),
                "yc_batch": hit.get("batch"),
                "yc_url": f"{YC_COMPANY_BASE_URL}/{hit.get("slug")}",
                "one_liner": hit.get("one_liner"),
                "description": hit.get("long_description"),
                "team": [],
                "launched_at": hit.get("launched_at"),
            })
            
        return candidates

    except Exception as e:
        print(f"[Error] Sourcing Layer Failed: {e}")
        return []




def source_yc_company_founders_by_algolia_curl(query_phrase: str, limit: int = 20) -> List[Dict]:
    """
    Executes a highly-targeted search on YC's founder index 
    using the exact parameters extracted from network developer tools.
    """
    # 1. URL and query string parameters extracted from your curl command
    url = "https://45bwzj1sgc-dsn.algolia.net/1/indexes/*/queries"
    params = {
        "x-algolia-agent": "Algolia for JavaScript (3.35.1); Browser; JS Helper (3.16.1)",
        "x-algolia-application-id": "45BWZJ1SGC",
        "x-algolia-api-key": "MTlmOGM5MTk5MjVlYWUyMDg4MGIzZDY4ODUzZTQ2ZWEzZWFlMjI0MTRhNTY2OGUyMTEwNTQ5NGVhZTdmYmFmNWFuYWx5dGljc1RhZ3M9eWNkYyZyZXN0cmljdEluZGljZXM9WUNVc2Vyc19wcm9kdWN0aW9uJnRhZ0ZpbHRlcnM9JTVCJTIyeWNkY19wdWJsaWMlMjIlNUQ="
    }

    # 2. Strict Request Headers for Request Authenticity 
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://www.ycombinator.com",
        "Referer": "https://www.ycombinator.com/",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
    }

    # 3. Request Payload formatting 
    # Note: We omitted the restrictive batch year filters from your curl 
    # to ensure you capture ALL historic companies matching your query string.
    payload = {
        "requests": [
            {
                "indexName": "YCUsers_production",
                "params": f"hitsPerPage={limit}&page=0&query={query_phrase}"
            }
        ]
    }

    try:
        # Algolia handles the incoming payload as a JSON string, despite the x-www-form-urlencoded header
        response = httpx.post(url, params=params, headers=headers, json=payload, timeout=10.0)
        response.raise_for_status()
        
        raw_data = response.json()
        
        # Algolia returns an array of results matching the array of requests sent
        results_list = raw_data.get("results", [])
        if not results_list:
            return []
            
        hits = results_list[0].get("hits", [])

        
        team = []
        for hit in hits:
            if(hit.get("company_slug") == query_phrase):
                team.append({
                    "first_name": hit.get("first_name"),
                    "last_name": hit.get("last_name"),
                    "avatar_url": hit.get("avatar_thumb"),
                    "role": hit.get("yc_titles")[0],
                    "linkedin_url": None,
                    "twitter_url": None
                })
            
        return team

    except Exception as e:
        print(f"[Error] Sourcing Layer Failed: {e}")
        return []

