import random
import pandas as pd

# 각 항목별 점수의 min, max 정의
score_ranges = {
    '항목1': (7, 10),  # 10점 항목
    '항목2': (7, 10),  # 10점 항목
    '항목3': (7, 10),  # 10점 항목
    '항목4': (7, 10),  # 10점 항목
    '항목5': (16, 20), # 20점 항목
    '항목6': (7, 10),  # 10점 항목
    '항목7': (7, 10),  # 10점 항목
    '항목8': (7, 10),  # 10점 항목
    '항목9': (7, 10),  # 10점 항목
}

# 50명의 인원에게 점수를 랜덤으로 부여
num_students = 50
results = []

for _ in range(num_students):
    scores = {}
    total_score = 0
    for item, (min_score, max_score) in score_ranges.items():
        score = random.randint(min_score, max_score)  # 각 항목에 대해 랜덤 점수 생성
        scores[item] = score
        total_score += score
    
    # 각 학생의 점수와 총점을 results 리스트에 추가
    scores['총점'] = total_score
    results.append(scores)

# DataFrame으로 변환하여 보기 좋게 출력
df = pd.DataFrame(results)

# 출력
print(df)

