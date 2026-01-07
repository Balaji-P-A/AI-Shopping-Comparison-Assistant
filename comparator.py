def compare_products(products, priority):
    results = []

    for p in products:
        score = 0
        if priority == "calls" and p["mic_quality"] == "good":
            score += 2
        score += p["rating"]
        results.append((p, score))

    return sorted(results, key=lambda x: x[1], reverse=True)
