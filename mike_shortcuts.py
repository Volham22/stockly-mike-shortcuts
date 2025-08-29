def mike_shortcuts(n: int, shortcuts: list[int]) -> list[int]:
    mins = [(2**32 - 1) for _ in range(n)]
    mins[0] = 0
    queue = [(0, 0)]

    while len(queue) != 0:
        current_intersection, consumed_energy = queue.pop(0)
        mins[current_intersection] = min(mins[current_intersection], consumed_energy)

        # Walk to next intersection
        if (
            current_intersection + 1 < n
            and mins[current_intersection + 1] > consumed_energy + 1
        ):
            queue.append(
                (
                    current_intersection + 1,
                    consumed_energy + 1,
                )
            )

        # Use shortcuts
        if mins[shortcuts[current_intersection] - 1] > consumed_energy + 1:
            queue.append((shortcuts[current_intersection] - 1, consumed_energy + 1))

        # Try to go back
        if (
            current_intersection - 1 > 0
            and mins[current_intersection - 1] > consumed_energy + 1
        ):
            queue.append(
                (
                    current_intersection - 1,
                    consumed_energy + 1,
                )
            )

    return mins


if __name__ == "__main__":
    n = int(input())
    shortcuts = [int(e) for e in input().split(" ")]
    result = mike_shortcuts(n, shortcuts)
    print(" ".join(str(n) for n in result))
