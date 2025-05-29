def exam_score_needed(final_grade, classwork_avg, exam_weight):
    x = (final_grade - classwork_avg) / exam_weight

    if x < 0:
        return f"You can get 0% on the exam and still pass! 🎉 (Needed exam score: {x:.2f})"
    elif x > 100:
        return f"It's not possible to pass unless the teacher gives extra credit. (Needed exam score: {x:.2f})"
    else:
        return f"You need to score at least {x:.2f}% on the exam. You got this! 💪"

# Example usage:
S = float(input("Average of quarter 1 and 2: "))
y = float(input("Final grade wanted: "))   
w = float(input("Weight of the exam (as a decimal): "))

result = exam_score_needed(y, S, w)
print(result)
