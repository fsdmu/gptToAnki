class ConvertToAnki:
    """Convert a given question and answer to an Anki readable format."""
    def __init__(self, separator: str = ";", is_html: bool = True):
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
