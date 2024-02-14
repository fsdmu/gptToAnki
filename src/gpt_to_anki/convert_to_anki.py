"""Contains the ConvertToAnki class."""
from pathlib import Path
from typing import Union


class ConvertToAnki:
    """Convert a given question and answer to an Anki readable format."""

    def __init__(self, separator: str = ";", is_html: bool = True):
        """Sets the default parameters given by the user."""
        self.separator = separator
        self.is_html = is_html
        self.file_content = ""

    def _initialize_file(self):
        """Initializes the file content with the default parameters."""
        if self.is_html:
            self.file_content += "#html:true\n"
        self.file_content += "#seperator:" + self.separator + "\n"
        self.file_content += f"#columns:Deck{self.separator}Front{self.separator}Back\n"

    def add_card(self, deck: str, front: str, back: str) -> None:
        """
        Adds the given information as card to Anki.
        :param deck: The deck to which the file wil be added. Childdecks must be written as follows 'parent::child'.
        :param front: The front of the card.
        :param back: The back of the card.
        :returns: None
        """
        self.file_content += f"{deck}{self.separator}{front}{self.separator}{back}\n"

    def output_to_file(self, path: Union[str, Path]) -> None:
        """
                Write the output of your class to a file.
                :param path: The path to the file or directory where the output should be written.
                    If a directory path is provided, a file named 'output.txt' will be created inside that directory.
                :raises ValueError: If the file already exists.
                :return: None
        """
        path = Path(path)
        if path.suffix == "":
            path = path / "output.txt"
        if path.is_file():
            raise ValueError("The given path leads to an existing file.")
        path.parent.mkdir(exist_ok=True)

        with path.open("w", encoding="utf-8") as f:
            f.write(self.file_content)
