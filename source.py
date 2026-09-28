import random
import pandas as pd

score_ranges = {
    '항목1': (7, 10),
    '항목2': (7, 10),
    '항목3': (7, 10),
    '항목4': (7, 10),
    '항목5': (16, 20),
    '항목6': (7, 10),
    '항목7': (7, 10),
    '항목8': (7, 10),
    '항목9': (7, 10),
}

num_students = 50
results = []

for _ in range(num_students):

    while True:
        scores = {}
        total_score = 0

        for item, (min_score, max_score) in score_ranges.items():
            mean = (min_score + max_score) / 2

            # 평균 중심 + 약간의 변동
            score = int(random.gauss(mean, 1))

            # 각 항목의 범위 안으로 제한
            score = max(min_score, min(score, max_score))

            scores[item] = score
            total_score += score

        # 총점이 80~100점이면 사용
        if 80 <= total_score <= 100:
            scores['총점'] = total_score
            results.append(scores)
            break

df = pd.DataFrame(results)

print(df)
