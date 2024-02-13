"""
# XML Dataclass designer

Design a XML-like dataclass to create a XML file.
"""

from dataclasses import dataclass

@dataclass
class Tag:
    """
    Tag dataclass.
    :param tag: Tag name.
    :type tag: str
    :param text: Text content.
    :type text: str, optional
    :param attributes: Attributes.
    :type attributes: dict[str, str], optional
    :param children: Children.
    :type children: list[Tag], optional
    :param is_comment: Is comment.
    :type is_comment: bool, optional
    """

    tag: str
    text: str = ""
    attributes: dict[str, str] = None
    children: list["Tag"] = None
    is_comment: bool = False

    def add_child(self, child: "Tag"):
        """
        Add a child.
        :param child: Child to add.
        :type child: Tag
        :return: None
        :rtype: None
        """

        if self.children is None:
            self.children = []

        self.children.append(child)

    @staticmethod
    def sanitize_text(text: str) -> str:
        """
        Sanitize text.
        :param text: Text to sanitize.
        :type text: str
        :return: Sanitized text.
        :rtype: str
        """

        return text.replace("&", "&amp;").replace("<", "&lt;")\
            .replace(">", "&gt;").replace("\"", "&quot;").replace("'", "&apos;")

    def to_string(self) -> str:
        """
        Convert to string.
        :return: XML string.
        :rtype: str
        """

        attributes = ""
        if self.attributes is not None:
            for k, v in self.attributes.items():
                v = self.sanitize_text(v)
                attributes += f'{k}="{v}" '
            attributes = attributes.strip()

        children = ""
        if self.children is not None:
            children = "".join([child.to_string() for child in self.children])

        self.text = self.sanitize_text(self.text)
        final = f"{self.tag} {attributes}>{self.text}{children}</{self.tag}"
        if self.is_comment:
            return f"<!-- {final} -->"
        return f"<{final}>"


@dataclass
class XML:
    """
    XML dataclass.
    :param version: XML version.
    :type version: str, optional
    :param encoding: XML encoding.
    :type encoding: str, optional
    :param children: Children.
    :type children: list[Tag], optional
    """

    version: str = "1.0"
    encoding: str = "UTF-8"
    children: list[Tag] = None

    def add_child(self, child: Tag):
        """
        Add a child.
        :param child: Child to add.
        :type child: Tag
        :return: None
        :rtype: None
        """

        if self.children is None:
            self.children = []

        self.children.append(child)

    def to_string(self) -> str:
        """
        Convert to string.
        :return: XML string.
        :rtype: str
        """

        children = "".join([child.to_string() for child in self.children])
        return f'<?xml version="{self.version}" encoding="{self.encoding}"?>{children}'
