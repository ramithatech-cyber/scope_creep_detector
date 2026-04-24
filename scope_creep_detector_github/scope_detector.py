from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def detect_scope_creep(initial_scope: list[str], new_scope: list[str]) -> tuple[bool, list[str]]:
    """
    Detect scope creep by comparing new features against the initial scope.

    Uses TF-IDF vectorization and cosine similarity to identify features
    that are semantically dissimilar from the original project scope.

    Args:
        initial_scope: List of features in the original project scope.
        new_scope: List of features proposed for addition.

    Returns:
        A tuple (creep_detected, extra_features) where:
            - creep_detected (bool): True if scope creep is detected.
            - extra_features (list): Features considered out of scope.
    """
    extra_features = []

    for feature in new_scope:

        if feature not in initial_scope:

            documents = initial_scope + [feature]
            vectorizer = TfidfVectorizer().fit_transform(documents)
            similarity_matrix = cosine_similarity(vectorizer)
            similarity_scores = similarity_matrix[-1][:-1]
            max_similarity = max(similarity_scores)

            # If similarity is low → treat as scope creep
            if max_similarity < 0.5:
                extra_features.append(feature)

    if len(extra_features) > 0:
        return True, extra_features
    else:
        return False, []
