from gemini_chat.chat import generate_chat_content
from utils.markdown_file_generator import MarkdownFileGenerator
from schemas.schemas import StartupEvaluation


def get_evaluation_prompt(thesis, startup, research):
    return f"""
    You are a seed-stage venture capital analyst.

    Investment Thesis:
    {thesis}

    Startup Information:
    {startup}

    Research Data:
    {research}

    Evaluate this startup. You MUST structure your answer clearly under the following markdown headers so it can be mechanically parsed later:

    ## Startup Name
    [Name here]

    ## Analyses
    - Team Analysis: 2-3 short but important points
    - Product Analysis: 2-3 short but important points
    - Market Analysis: 2-3 short but important points

    ## Scores (Give an integer out of 10 for each)
    - Team Score: 
    - Product Score: 
    - Market Score: 
    - Traction Score: 
    - Timing Score: 
    - Total Score: 

    ## Risks (short and concise points)
    - [Risk 1] 
    - [Risk 2]

    ## Recommendation
    Must strictly be exactly one of these tokens: PASS, WATCH, or TAKE_MEETING

    ## Rationale (short and concise)
    [Provide the final executive rationale summary]

    ## Key things that can change investors' mind
    2-3 short but very important points which can change investors' mind
    """


def get_evaluation_data_json_prompt(evaluation_data):
    return f"""
    You are an expert data parsing assistant. 
    Analyze the raw Venture Capital analyst report below and extract the information into the requested structured JSON object format matching the schema properties exactly.

    Raw Analyst Report:
    {evaluation_data}
    """

def get_evaluation_data(thesis, startup, research):

    company = startup["name"]

    evaluation_prompt = get_evaluation_prompt(thesis, startup, research)
    response = generate_chat_content(prompt=evaluation_prompt, enable_search=True, response_schema=None)
    evaluation_data = response.text

    evaluation_data_pydantic = generate_chat_content(prompt=get_evaluation_data_json_prompt(evaluation_data), enable_search=False, response_schema=StartupEvaluation)
    json_string = evaluation_data_pydantic.model_dump_json(indent=4)

    MarkdownFileGenerator.create_md_file(f"outputs/evaluations/{company}.json", json_string)
