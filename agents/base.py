from dataclasses import dataclass
from google import genai

@dataclass
class AgentConfig:
    api_key: str
    model: str = "gemini-1.5-flash"

class BaseAgent:
    def __init__(self, name: str, role: str, config: AgentConfig):
        self.name = name
        self.role = role
        self.config = config
        self.client = genai.Client(api_key=config.api_key)

    def generate(self, prompt: str) -> str:
        resp = self.client.models.generate_content(
            model=self.config.model,
            contents=prompt
        )
        return (resp.text or "").strip()
