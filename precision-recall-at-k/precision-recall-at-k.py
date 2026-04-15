def precision_recall_at_k(recommended, relevant, k):
    predicted_k = recommended[:k]
    relevant_set = set(relevant)
    hits = sum(1 for item in predicted_k if item in relevant_set)
    b = []
    b.append(hits/k)
    b.append(hits/len(relevant))
    return b
    