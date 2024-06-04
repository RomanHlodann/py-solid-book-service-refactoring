from app.display_book import BookDisplayer


class BookPrinter(BookDisplayer):
    def display(self, print_type: str) -> None:
        if print_type == "console":
            return self.display_in_console()
        elif print_type == "reverse":
            return self.display_in_reverse()
        else:
            raise ValueError(f"Unknown print type: {print_type}")

    def display_in_console(self):
        print(f"Printing the book: {self.book.title}...")
        super().display_in_console()

    def display_in_reverse(self):
        print(f"Printing the book in reverse: {self.book.title}...")
        super().display_in_reverse()
