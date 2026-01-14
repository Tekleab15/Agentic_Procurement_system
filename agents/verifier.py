from .base import BaseAgent

class VerifierAgent(BaseAgent):
    def check_compliance(self, standard_text: str, offer: dict) -> str:
        prompt = f"""
            You are {self.name}, a {self.role}.

            Compare OFFER against STANDARD.

            Output:
            1) Bullet list of violations (each bullet: requirement → offer value)
            2) A short compliance status: COMPLIANT or NON-COMPLIANT
            No extra commentary.

            STANDARD: {standard_text}
            OFFER (parsed JSON): {offer}""".strip()

        return self.generate(prompt)
