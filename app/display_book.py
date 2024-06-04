from app.book import Book


class BookDisplayer:
    def __init__(self, book: Book):
        self.book = book

    def display(self, display_type: str):
        if display_type == "console":
            return self.display_in_console()
        elif display_type == "reverse":
            return self.display_in_reverse()
        raise ValueError(f"Unknown display type: {display_type}")

    def display_in_console(self):
        print(self.book.content)

    def display_in_reverse(self):
        print(self.book.content[::-1])
