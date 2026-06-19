from pydantic import BaseModel, Field
from typing import Optional


class TeamMember(BaseModel):
    name: str = Field(description="full name of the team member")
    role: str = Field(description="role of the team member in the company")
    bio: str = Field(description="a brief bio about the team member")
    linkedin_url: str = Field(description="linkedin profile url of the team member of found")
    twitter_url: Optional[str] = Field(default=None, description="twitter profile url of the team member if found")
    technical_depth: str = Field(description="a brief and informative data about how good his technical depth is in building things")
    domain_expertise: str = Field(description="a brief info about the amount of domain expertise he has")