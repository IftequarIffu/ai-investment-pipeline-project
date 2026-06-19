
from gemini_chat.chat import generate_chat_content
from utils.markdown_file_generator import MarkdownFileGenerator
from schemas.schemas import StartupResearch

def get_research_prompt(thesis, startup_json):


    research_prompt = f"""
    You are a venture capital research analyst.

    Investment Thesis:
    {thesis}

    Startup Information:
    {startup_json}


    Research this company using public information.

    Focus only on:

    1. Founder backgrounds
    2. Competitive landscape
    3. Traction signals
    4. Major risks

    Return JSON matching the schema.

    Do not score the company.
    Do not make an investment recommendation.
    """

    return research_prompt

def get_research_data_json_prompt(research_data):

    prompt = f"""

    Convert the following research data into JSON:
    {research_data}

    """

    return prompt



def get_research_data(thesis, startup_json):

    company = startup_json["name"]

    research_prompt = get_research_prompt(thesis, startup_json)
    response = generate_chat_content(prompt=research_prompt, enable_search=True)
    research_data = response.text

    research_data_pydantic = generate_chat_content(prompt=get_research_data_json_prompt(research_data), response_schema=StartupResearch)
    json_string = research_data_pydantic.model_dump_json(indent=4)

    MarkdownFileGenerator.create_md_file(f"outputs/research/{company}.json", json_string)




# with open(file_path, "w", encoding="utf-8") as f:
#     print(response.model_dump_json(indent=4))
#     f.write(response.model_dump_json(indent=4))