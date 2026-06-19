from pathlib import Path


class MarkdownFileGenerator:

    @staticmethod
    def create_md_file(file_path, content):

        file_path = Path(file_path)
        file_path.parent.mkdir(parents=True, exist_ok=True)

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)
