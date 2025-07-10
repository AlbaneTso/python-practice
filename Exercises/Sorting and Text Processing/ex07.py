attempts = [
    ('Alice', 'Math', 'Q1'),
    ('Alice', 'Math', 'Q1'),
    ('Alice', 'Math', 'Q2'),
    ('Bob', 'Math', 'Q1'),
    ('Bob', 'Math', 'Q2'),
    ('Bob', 'Math', 'Q2'),
    ('Charlie', 'History', 'Q3'),
    ('Charlie', 'History', 'Q3'),
    ('Charlie', 'History', 'Q4'),
    ('Alice', 'History', 'Q3')
]

results = {}

for student, subject, question in attempts:
    if subject not in results:
        results[subject] = {}
    if student not in results[subject]:
        results[subject][student] = {}
    if question not in results[subject][student]:
        results[subject][student][question] = 0
    results[subject][student][question] += 1


for subject in results:
    print(f"{subject}:")
    for student in results[subject]:
        print(f"  {student}:")
        for question in results[subject][student]:
            print(f"    {question}: {results[subject][student][question]}")


# from collections import defaultdict
# results = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))

# for student, subject, question in attempts:
#     results[subject][student][question] += 1

# for subject in results:
#     print(f"{subject}:")
#     for student in results[subject]:
#         print(f"  {student}:")
#         for question in results[subject][student]:
#             print(f"    {question}: {results[subject][student][question]}")