import json
import xml.etree.ElementTree as ET # noqa n817

from abc import ABC, abstractmethod

from app.book import Book


class Serializer(ABC):
    @abstractmethod
    def serialize(self) -> None:
        pass


class BookJSONSerializer(Serializer):
    def __init__(self, book: Book) -> None:
        self.book = book

    def serialize(self) -> str:
        return json.dumps(
            {"title": self.book.title,
             "content": self.book.content}
        )


class BookXMLSerializer(Serializer):
    def __init__(self, book: Book) -> None:
        self.book = book

    def serialize(self) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = self.book.title
        content = ET.SubElement(root, "content")
        content.text = self.book.content
        return ET.tostring(root, encoding="unicode")
