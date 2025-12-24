import heapq


def minimize_cost(cables, verbose=False):
    # Обчислює мінімальні витрати на з'єднання мережевих кабелів.
    # Використовується мін-купа (heapq).
    
    if not cables or len(cables) <= 1:
        return 0

    heap = list(cables)
    heapq.heapify(heap)

    total_cost = 0

    while len(heap) > 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)

        cost = first + second
        total_cost += cost

        heapq.heappush(heap, cost)

        if verbose:
            print(
                f"З'єднуємо {first} і {second} → {cost}, "
                f"загальні витрати: {total_cost}"
            )

    return total_cost


if __name__ == "__main__":
    cables = [4, 3, 2, 6]
    print("Початкові кабелі:", cables)

    result = minimize_cost(cables, verbose=True)
    print("Мінімальні витрати на з'єднання:", result)