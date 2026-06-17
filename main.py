import argparse

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

if __name__ == "__main__":
    main()