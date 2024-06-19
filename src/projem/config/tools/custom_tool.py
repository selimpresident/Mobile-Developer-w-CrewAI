from crewai_tools import BaseTool

class CustomTool(BaseTool):
    def __init__(self, name):
        self.name = name
        self.description = f"{name} aracı."

    def _run(self, argument: str) -> str:
        return f"{self.name} aracı ile işlem yapıldı: {argument}"
