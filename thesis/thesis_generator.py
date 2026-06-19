from pydantic import BaseModel
from typing import List, Dict
from gemini_chat.chat import generate_chat_content
import json
from pathlib import Path



class ScoringCategory(BaseModel):
    name: str
    weight: int
    criteria: List[str]

class InvestmentThesis(BaseModel):
    thesis_name: str
    target_customers: List[str]
    preferred_founder_traits: List[str]
    preferred_product_traits: List[str]
    preferred_market_traits: List[str]
    negative_signals: List[str]

    team: ScoringCategory
    product: ScoringCategory
    market: ScoringCategory
    traction: ScoringCategory
    timing: ScoringCategory

    investment_rationale: str

def generate_thesis(topic):

    prompt = f"""
    You are a partner at an early-stage venture capital fund.

    Your task is to create an investment thesis for a startup sourcing and evaluation pipeline.

    The investment area is:

    {topic}

    Requirements:

    1. Make the thesis specific.
    2. Define ideal customers.
    3. Define ideal founder profiles.
    4. Define ideal product characteristics.
    5. Define ideal market characteristics.
    6. Define negative signals.
    7. Define scoring weights that sum to 100.
    8. The thesis should be suitable for evaluating seed-stage startups.

    Return only JSON matching the provided schema.
    """

    response = generate_chat_content(prompt=prompt, response_schema=InvestmentThesis)
    file_path = Path("outputs/thesis.json")
    file_path.parent.mkdir(parents=True, exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as f:
        # print(response.model_dump_json(indent=4))
        f.write(response.model_dump_json(indent=4))


