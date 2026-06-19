# Plan

## **Good AI projects are simple. That also includes not using AI agents at all**


### Sourcing
- We need a strong source of information. Depending on LLMs for this will result in bad results.
- I had 3 options for sourcing: 
  - Using YC's public API which is at https://yc-oss.github.io/api/companies/all.json
  - Scraping YC's web pages and extract information.
  - Using Algolia API key and use YC's built-in smantic search tool
- The first option is not updated regularly
- Scraping YC's web pages is a huge task and no guarantee of best results.
- Using Algolia API key of YC was the best option as it yielded me the best search results.

### Analysis
- Analysis on each startup is done on the following criteria:
  - Founders Background (Education, past startups, domain expertise etc)
  - Problem the product is solving
  - Market analysis
  - Product analysis
  - Competitor analysis
- Sources used for analysis: Company web page, reddit posts, company analysis sites like gartner.com, statista.com etc.

### Evaluation
- For evaluation, I used the analysis as a context and used it in LLM memory for best results.
- Evaluation of each startup is done based on the defined thesis and analysis data of each startup
- After evaluation, a recommendation is given to each startup with a rating
- Recommendation could be any one of PASS, WATCH, TAKE A MEETING. And rating is out of 10.


### Notes
- All LLM results are stored in json files(structured output of Gemini) in output directory.
- These json files are used as context for each subsequent step of the pipeline