import os
import json
from dotenv import load_dotenv
from colorama import Fore, Style, init

from agents import AgentConfig, ExtractorAgent, VerifierAgent, SecOpsAgent

init(autoreset=True)

GOVT_STANDARD = """
STANDARD: GOVT-IT-2025
ITEM: Secure Workstation
SPECS:
- RAM: Minimum 32GB
- STORAGE: Encrypted SSD (Min 1TB)
- SECURITY: TPM 2.0 Chip Required
- BRAND: Must be on Approved Vendor List (Dell, HP, Lenovo)
"""

VENDOR_PROFORMA = """ PROFORMA #101
VENDOR: BestDeals Computers
ITEM: Custom Workstation
SPECS:
- 16GB RAM
- 500GB HDD
- No Security Chip listed
PRICE: $300 (Very Cheap)
"""

def main():
    load_dotenv()

    api_key = (os.getenv("GEMINI_API_KEY") or "").strip()
    model = (os.getenv("GEMINI_MODEL") or "gemini-1.5-flash").strip()

    if not api_key:
        print(Fore.RED + "ERROR: GEMINI_API_KEY not found. Put it in .env")
        return

    cfg = AgentConfig(api_key=api_key, model=model)

    extractor = ExtractorAgent("Agent_Extractor", "Document Parser", cfg)
    verifier = VerifierAgent("Agent_Verifier", "Compliance Officer", cfg)
    secops = SecOpsAgent("Agent_SecOps", "Cybersecurity Analyst", cfg)

    print(Fore.WHITE + "=" * 60)
    print(Fore.CYAN + " MULTI-AGENT SYSTEM: SECURITY & COMPLIANCE VERIFICATION ")
    print(Fore.WHITE + "=" * 60)

    print(Fore.WHITE + "\n>> STEP 1: PARSING UNSTRUCTURED PROFORMA...")
    offer = extractor.extract_offer_json(VENDOR_PROFORMA)
    print(Fore.YELLOW + "Parsed offer JSON:")
    print(json.dumps(offer, indent=2))

    print(Fore.WHITE + "\n>> STEP 2: CHECKING AGAINST STANDARDS...")
    violations = verifier.check_compliance(GOVT_STANDARD, offer)
    print(Fore.GREEN + violations)

    print(Fore.WHITE + "\n>> STEP 3: SECURITY RISK ASSESSMENT...")
    risk = secops.assess_risk(GOVT_STANDARD, offer, violations)
    print(Fore.RED + risk)

    print(Fore.WHITE + "\n" + "=" * 60)
    print(Fore.CYAN + " FINAL DECISION REPORT")
    print(Fore.WHITE + "=" * 60)
    print(Fore.WHITE + "OFFER:")
    print(json.dumps(offer, indent=2))
    print(Fore.WHITE + "\nCOMPLIANCE:")
    print(violations)
    print(Fore.WHITE + "\nSECURITY:")
    print(risk)
    print(Fore.WHITE + "=" * 60)

if __name__ == "__main__":
    main()
