def assign_letter_grade(score):
    if score >= 96:
        return 'A+'
    elif score >= 88:
        return 'A'
    elif score >= 85:
        return 'B+'
    elif score >= 80:
        return 'B'
    elif score >= 77:
        return 'C+'
    elif score >= 70:
        return 'C'
    elif score >= 66:
        return 'D'
    elif score >= 50:
        return 'F'
    else:
        return 'I'

print(assign_letter_grade(100))
        
