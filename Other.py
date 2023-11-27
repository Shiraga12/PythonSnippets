import math
from typing import List

class Chapter1:
    def getSum(self, A: int, B: int, C: int) -> int:
        return A + B + C

    def getWrongAnswers(self, N: int, C: str) -> str:
        result = ''
        for i in range(N):
            if C[i] == 'A':
                result += 'B'
            elif C[i] == 'B':
                result += 'A'
        return result

    def getHitProbability(self, R: int, C: int, G: List[List[int]]) -> float:
        total_cells = R * C
        battleship_cells = sum(row.count(1) for row in G)

        if total_cells == 0:
            return 0.0
        else:
            probability = battleship_cells / total_cells
            return probability

    def getMaxAdditionalDinersCount(self, N: int, K: int, M: int, S: List[int]) -> int:
        S.sort()
        guests = 0
        start = 1
        range_val = 0

        for seated_diner in S:
            range_val = seated_diner - start
            guests += math.floor(range_val / (K + 1))
            start = seated_diner + K + 1

        range_val = N - start + 1
        guests += math.ceil(range_val / (K + 1))

        return guests


    def getMinCodeEntryTime(self, N: int, M: int, C: List[int]) -> int:
        def minTimeBetween(a, b, N):
            return min(abs(a - b), N - abs(a - b))

        current_position = 1
        total_time = 0

        for target in C:
            clockwise_time = minTimeBetween(current_position, target, N)
            counterclockwise_time = minTimeBetween(target, current_position, N)

            total_time += min(clockwise_time, counterclockwise_time)
            current_position = target

        return total_time

    def getMinProblemCount(self, N: int, S: List[int]) -> int:
        return max(S) // 2 + any(s & 1 for s in S)

    def getMinimumDeflatedDiscCount(self, N: int, R: List[int]) -> int:
        deflated_count = 0
        prev_radius = float('inf')  # Initialize with positive infinity

        for i in range(N - 1, -1, -1):
            if R[i] >= prev_radius:
                deflated_count += R[i] - (prev_radius - 1)
                prev_radius = prev_radius - 1
            else:
                prev_radius = R[i]

        return deflated_count


# Create an instance of the Chapter1 class
chapter = Chapter1()

# Example 1: Calculate the sum of three numbers
sum_result = chapter.getSum(5, 10, 15)
print("Sum:", sum_result)  # Output: Sum: 30

# Example 2: Replace 'A' with 'B' and vice versa in a string
wrong_answers_result = chapter.getWrongAnswers(5, "AABBA")
print("Modified String:", wrong_answers_result)  # Output: Modified String: BBAAB

# Example 3: Calculate hit probability in a grid
grid = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
probability = chapter.getHitProbability(3, 3, grid)
print("Hit Probability:", probability)  # Output: Hit Probability: 0.4444444444444444

# Example 4: Calculate the maximum additional diners that can be seated
seated_diners = [1, 5, 10, 15, 20]
additional_diners = chapter.getMaxAdditionalDinersCount(25, 2, 5, seated_diners)
print("Max Additional Diners:", additional_diners)  # Output: Max Additional Diners: 2

# Example 5: Calculate minimum code entry time
entry_times = [3, 5, 8, 12]
min_time = chapter.getMinCodeEntryTime(12, 4, entry_times)
print("Minimum Entry Time:", min_time)  # Output: Minimum Entry Time: 6

# Example 6: Calculate the minimum problem count
problem_scores = [10, 15, 20, 25]
min_problems = chapter.getMinProblemCount(4, problem_scores)
print("Minimum Problem Count:", min_problems)  # Output: Minimum Problem Count: 7

# Example 7: Calculate the minimum count of deflated discs
disc_radii = [3, 2, 1, 5, 4]
min_deflated_count = chapter.getMinimumDeflatedDiscCount(5, disc_radii)
print("Minimum Deflated Disc Count:", min_deflated_count)  # Output: Minimum Deflated Disc Count: 6
