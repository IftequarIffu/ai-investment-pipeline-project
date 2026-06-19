import argparse
from sourcing.yc_sourcing import source_yc_by_algolia_curl, source_yc_company_founders_by_algolia_curl
import json
from research.research import get_research_data
from evaluation.evaluation import get_evaluation_data
from thesis.thesis_generator import generate_thesis
from memo.memo import generate_memo
from utils.markdown_file_generator import MarkdownFileGenerator
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        description="Generate content for a given topic"
    )

    parser.add_argument(
        "--topic",
        type=str,
        required=True,
        help="Topic to generate content for"
    )

    args = parser.parse_args()

    print(f"Topic received: {args.topic}")

    yc_list = source_yc_by_algolia_curl(args.topic)

    # Update team data
    print("Updating the team information...\n\n")
    for i in range(len(yc_list)):

        team = source_yc_company_founders_by_algolia_curl(yc_list[i].get("slug"))
        yc_list[i]["team"] = team
        break

    print("Generating thesis...\n")
    generate_thesis()

    file = open('outputs/thesis.json', 'r')
    thesis_json = json.load(file)

    print("Getting the research data for all startups...\n")
    # Get research data for each startup
    for startup in yc_list:
        research_data = get_research_data(thesis_json, startup)

    print("Getting the evaluation data for all startups...\n")
    # Evaluation of each startup using thesis, company data and company's research data
    for startup in yc_list:
        name = startup["name"]
        research_file_path = Path(f"outputs/research/{name}.json")
        research_file = open(research_file_path, 'r')
        research_data = research_file.read()

        evaluation_data = get_evaluation_data(thesis_json, startup, research_data)

    
    # Generate memos
    for startup in yc_list:
        name = startup["name"]
        evaluation_file_path = Path(f"outputs/evaluations/{name}.json")
        evaluation_file = open(evaluation_file_path, 'r')
        evaluation_data = evaluation_file.read()

        memo = generate_memo(startup, evaluation_data)

    print("Memos generation is completed\n")

if __name__ == "__main__":
    main()