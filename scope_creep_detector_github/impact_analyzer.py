def analyze_impact(extra_features: list[str]) -> tuple[int, int, str, int]:
    """
    Estimate the impact of scope creep based on the number of extra features.

    Uses fixed per-feature estimates for time and cost, and a threshold-based
    risk classification.

    Args:
        extra_features: List of features identified as scope creep.

    Returns:
        A tuple (extra_time, extra_cost, risk_label, risk_score) where:
            - extra_time (int): Estimated additional days required.
            - extra_cost (int): Estimated additional cost in INR.
            - risk_label (str): Human-readable risk category.
            - risk_score (int): Numeric risk score (0–100).
    """
    TIME_PER_FEATURE = 3      # days
    COST_PER_FEATURE = 10000  # INR

    count = len(extra_features)

    extra_time = count * TIME_PER_FEATURE
    extra_cost = count * COST_PER_FEATURE

    if count >= 4:
        risk = "High Risk"
        risk_score = 90
    elif count >= 2:
        risk = "Medium Risk"
        risk_score = 60
    else:
        risk = "Low Risk"
        risk_score = 30

    return extra_time, extra_cost, risk, risk_score
