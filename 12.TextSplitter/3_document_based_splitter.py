from langchain.text_splitter import RecursiveCharacterTextSplitter, Language

text = """
class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return 0

    def describe(self):
        return f"{self.name} has area {self.area()}"


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

"""

splitter = RecursiveCharacterTextSplitter.from_language(
    chunk_size=100,
    language=Language.PYTHON,
    chunk_overlap=0
)

result = splitter.split_text(text)

print(result)