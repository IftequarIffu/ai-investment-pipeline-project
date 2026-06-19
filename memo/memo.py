
# from utils.markdown_file_generator import MarkdownFileGenerator
# import json

# def generate_memo(startup, evaluation):

#     company = startup["name"]
#     evaluation = json.loads(evaluation)

#     memo = f"""
#     #{startup["name"]}

#     **Website:** {startup["website"]}
#     **Batch:** {startup["yc_batch"]}
#     **Score:** {evaluation["total_score"]}

#     #Recommendation: {evaluation["recommendation"]}

#     ##Summary
#     {evaluation["rationale"]}

#     ##Team
#     {evaluation["team_analysis"]}

#     ##Product
#     {evaluation["product_analysis"]}

#     ##Market
#     {evaluation["market_analysis"]}

#     ##Risks / Open Questions
#     {evaluation["risks"]}

#     ##What would change our mind
#     {evaluation["key_things"]}
#     """

#     MarkdownFileGenerator.create_md_file(f"outputs/memos/{company}.md", memo)

#     return memo



from utils.markdown_file_generator import MarkdownFileGenerator
import json


def generate_memo(startup, evaluation):
    company = startup["name"]
    evaluation = json.loads(evaluation)

    team_analysis_md = "\n".join([f"- {analysis}" for analysis in evaluation["team_analysis"]])
    product_analysis_md = "\n".join([f"- {item}" for item in evaluation["product_analysis"]])
    market_analysis_md = "\n".join([f"- {item}" for item in evaluation["market_analysis"]])
    

    risks_md = "\n".join([f"- {risk}" for risk in evaluation["risks"]])
    key_things_md = "\n".join([f"- {item}" for item in evaluation["key_things"]])

    memo = f"""
# {startup["name"]}

---

## Company Overview

| Field | Value |
|-------|-------|
| **Website** | {startup["website"]} |
| **Batch** | {startup["yc_batch"]} |
| **Score** | **{evaluation["total_score"]}/10** |
| **Recommendation** | **{evaluation["recommendation"]}** |

---

# Investment Recommendation: **{evaluation["recommendation"]}**

## Executive Summary
{evaluation["rationale"]}

---

## Score Breakdown

| Category | Score |
|----------|-------|
| Team     | {evaluation["team_score"]}/10 |
| Product  | {evaluation["product_score"]}/10 |
| Market   | {evaluation["market_score"]}/10 |
| Traction | {evaluation["traction_score"]}/10 |
| Timing   | {evaluation["timing_score"]}/10 |

---

## Team Analysis
{team_analysis_md}

---

## Product Analysis
{product_analysis_md}

---

## Market Analysis
{market_analysis_md}

---

## Risks / Open Questions
{risks_md}

---

## What Would Change Our Mind
{key_things_md}

---
    """

    MarkdownFileGenerator.create_md_file(
        f"outputs/memos/{company}.md",
        memo
    )

    return memo