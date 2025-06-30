def rule_based_triage(text: str) -> str:
    """
    A basic keyword-based classifier to assist AI decisioning.
    """
    text = text.lower()

    if "emergency" in text or "surgery" in text:
        return "ESCALATE"
    elif "routine checkup" in text or "general consultation" in text:
        return "APPROVE"
    elif "missing info" in text or "incomplete" in text:
        return "REVIEW"
    else:
        return "REVIEW"
