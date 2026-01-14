import json
from .base import BaseAgent

class ExtractorAgent(BaseAgent):
    def extract_offer_json(self, proforma_text: str) -> dict:
        prompt = f"""
            You are {self.name}, a {self.role}.

            Extract vendor + offer specs into STRICT JSON only (no prose).
            Use this schema exactly:
            {{
              "vendor": {{"name": "", "approved_list_status": "unknown"}},
              "item": {{"name": "", "ram_gb": null, "storage_type": "", "storage_gb": null, "tpm": "unknown"}},
              "price_usd": null
            }}

            If missing, use null or "unknown".

            PROFORMA:
            {proforma_text}
            """.strip()

        text = self.generate(prompt)

        try:
            return json.loads(text)
        except Exception:
            start = text.find("{")
            end = text.rfind("}")
            if start != -1 and end != -1 and end > start:
                return json.loads(text[start:end+1])
            raise ValueError(f"Extractor output was not valid JSON:\n{text}")
