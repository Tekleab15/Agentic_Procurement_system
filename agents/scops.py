from .base import BaseAgent

class SecOpsAgent(BaseAgent):
    def assess_risk(self, standard_text: str, offer: dict, violations_report: str) -> str:
        prompt = f"""
            You are {self.name}, a {self.role}.

            Assess procurement security risk (counterfeit/supply-chain/fraud) based on:
            - Missing security requirements (TPM, encryption, approved vendor)
            - Suspicious pricing
            - Vendor opacity

            Output format:
            - Risk signals (bullets)
            - Recommended action (APPROVE or REJECT)
            - One-sentence justification

            STANDARD: {standard_text}

            OFFER: {offer}

            VIOLATIONS: {violations_report} """.strip()

        return self.generate(prompt)
