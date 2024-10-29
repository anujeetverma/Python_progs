if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    print("\nList of Students and their Scores:")
    for name, scores in student_marks.items():
        print(f"Name: {name}, Scores: {scores}")
        
