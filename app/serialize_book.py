import json
import xml.etree.ElementTree as ET

from app.book import Book


class BookSerializer:
    def __init__(self, book: Book):
        self.book = book

    def serialize(self, serialize_type: str) -> str:
        if serialize_type == "json":
            return self.serialize_in_json()
        elif serialize_type == "xml":
            return self.serialize_in_xml()
        raise ValueError(f"Unknown serialize type: {serialize_type}")

    def serialize_in_json(self):
        return json.dumps(
            {"title": self.book.title,
             "content": self.book.content}
        )

    def serialize_in_xml(self):
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = self.book.title
        content = ET.SubElement(root, "content")
        content.text = self.book.content
        return ET.tostring(root, encoding="unicode")
