def get_recommendation(extra_features: list[str]) -> str:
    """
    Generate a project management recommendation based on the scope creep count.

    Args:
        extra_features: List of features identified as scope creep.

    Returns:
        A recommendation string for the project manager.
    """
    count = len(extra_features)

    if count == 1:
        return "✅ Low Risk — Feature can likely be included in the current sprint with minimal impact."
    elif count <= 3:
        return "⚠️ Medium Risk — Review added features with the team. Consider timeline and budget adjustments."
    else:
        return "🔴 High Risk — Move excess features to Phase 2. Current scope risks project delivery."
