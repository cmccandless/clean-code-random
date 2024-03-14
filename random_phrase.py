import random
from pathlib import Path
from book_phrases import Book


def from_list(phrases_dir: Path) -> str:
    """New method, all phrases equal weight"""
    phrases_list_file = phrases_dir / "phrases_list.txt"
    return random.choice([
        line.strip()
        for line in phrases_list_file.read_text().splitlines()
    ])


if __name__ == "__main__":
    current_script = Path(__file__)
    if current_script.is_absolute():
        phrases_dir = current_script.parent
    else:
        phrases_dir = (Path.cwd() / current_script).parent
    phrase = from_list(phrases_dir)
    print(phrase)
