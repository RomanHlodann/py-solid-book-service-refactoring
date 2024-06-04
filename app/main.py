from app.book import Book
from app.display_book import BookDisplayer
from app.print_book import BookPrinter
from app.serialize_book import BookSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    book_displayer = BookDisplayer(book)
    book_printer = BookPrinter(book)
    book_serializer = BookSerializer(book)

    for cmd, method_type in commands:
        if cmd == "display":
            book_displayer.display(method_type)
        elif cmd == "print":
            book_printer.display(method_type)
        elif cmd == "serialize":
            return book_serializer.serialize(method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
