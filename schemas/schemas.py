from typing import List, Dict
from pydantic import BaseModel, HttpUrl, Field
from typing import Literal


class InvestmentThesis(BaseModel):
    thesis_name: str
    investment_rationale: str
    scoring_categories: dict


class TeamMember(BaseModel):
    name: str
    role: str
    experience: str
    # avatar_url: str
    # linkedin_url: Optional[HttpUrl]
    # twitter_url: Optional[HttpUrl]

class TracktionSignal(BaseModel):
    signal_type: str
    details: str

class Risk(BaseModel):
    risk_category: str
    description: str

class StartupResearch(BaseModel):
    startup_name: str
    founder_backgrounds: List[TeamMember]
    competitive_landscape: str
    traction_signals: list[TracktionSignal]
    risks: list[Risk]

class Startup(BaseModel):
    name: str
    slug: str
    website: str
    one_liner: str
    description: str
    yc_url: str
    yc_batch: str
    team: List[TeamMember]
    launched_at: str
    startup_research: StartupResearch


class StartupEvaluation(BaseModel):
    startup_name: str = Field(description="The name of the company being evaluated")

    team_analysis: list[str] = Field(description="2-3 short bullet points about team")
    product_analysis: list[str] = Field(description="2-3 short bullet points about product")
    market_analysis: list[str] = Field(description="2-3 short bullet points about market")

    risks: list[str] = Field(description="List of 2-4 specific risks identified")

    team_score: int = Field(ge=1, le=10)
    product_score: int = Field(ge=1, le=10)
    market_score: int = Field(ge=1, le=10)
    traction_score: int = Field(ge=1, le=10)
    timing_score: int = Field(ge=1, le=10)

    total_score: int = Field(ge=1, le=10)

    recommendation: Literal["PASS", "WATCH", "TAKE_MEETING"]

    rationale: str = Field(description="Executive summary")
    key_things: list[str] = Field(description="2-3 important things that can change investor's mind")



class InvestmentReport(BaseModel):
    topic: str
    thesis: InvestmentThesis
    startups: list[StartupEvaluation]