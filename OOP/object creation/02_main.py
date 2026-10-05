class teacher:
    def greet(self, name):
        print(f"Hello {name}")

class student:
    @staticmethod
    def greet(name):
        print(f"Hello {name}")

JIS = student()

JISU = teacher()
JIS.greet("Subhamoy")
JISU.greet("ABC")