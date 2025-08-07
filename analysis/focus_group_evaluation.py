import csv
input_file="responses.csv"
output_file="evaluation_report.txt"

total_responses = 0
understood_yes, understood_no = 0, 0
pace_yes, pace_no = 0, 0
clarity_yes, clarity_no = 0, 0
materials_helpful_yes, materials_helpful_no = 0, 0
engaged_yes, engaged_no = 0, 0
difficulty_easy, difficulty_medium, difficulty_hard = 0, 0, 0

with open(input_file, "r") as file:
    reader = csv.reader(file)
    header = next(reader)

    for row in reader:
        total_responses += 1

        if row[4].strip().lower() == "yes":
            understood_yes += 1
        else:
            understood_no += 1

        if row[5].strip().lower() == "yes":
            pace_yes += 1
        else:
            pace_no += 1
        if row[6].strip().lower() == "yes":
            clarity_yes += 1
        else:
            clarity_no += 1
        if row[7].strip().lower() == "yes":
            materials_helpful_yes += 1
        else:
            materials_helpful_no += 1
        if row[8].strip().lower() == "yes":
            engaged_yes += 1
        else:
            engaged_no += 1
        if row[9].strip().lower() == "easy":
            difficulty_easy += 1
        elif row[9].strip().lower() == "moderate":
            difficulty_medium += 1
        elif row[9].strip().lower() == "difficult":
            difficulty_hard += 1

def calculate_percentage(part, total):
    return(part/ total) * 100 if total > 0 else 0

understood_no_percent = calculate_percentage(understood_no, total_responses)
pace_no_percent = calculate_percentage(pace_no, total_responses)
clarity_no_percent = calculate_percentage(clarity_no, total_responses)
materials_helpful_no_percent = calculate_percentage(materials_helpful_no, total_responses)
engaged_no_percent = calculate_percentage(engaged_no, total_responses)

difficulty_easy_percent = calculate_percentage(difficulty_easy, total_responses)
difficulty_medium_percent = calculate_percentage(difficulty_medium, total_responses)
difficulty_hard_percent = calculate_percentage(difficulty_hard, total_responses)

report = f"""
CLASS EVALUATION REPORT
-----------------------
Total Responses : {total_responses}
1. Understanding of Concepts:
 - Yes: {understood_yes}
 - No: {understood_no} ({understood_no_percent:.2f}% found it difficult)
2. Pace of Class:
 - Yes (Good pace): {pace_yes}
 - No (Too fast/slow): {pace_no} ({pace_no_percent:.2f}% had issues with the pac
3. Instructor's Clarity:
 - Yes (Clear): {clarity_yes}
 - No (Unclear): {clarity_no} ({clarity_no_percent:.2f}% found explanations uncl
4. Were Learning Materials Helpful?
 - Yes: {materials_helpful_yes}
 - No: {materials_helpful_no} ({materials_helpful_no_percent:.2f}% found materia
5. Did Students Feel Engaged?
 - Yes: {engaged_yes}
 - No: {engaged_no} ({engaged_no_percent:.2f}% did not feel engaged)
6. Course Difficulty Level:
 - Easy: {difficulty_easy} ({difficulty_easy_percent:.2f}%)
 - Moderate: {difficulty_medium} ({difficulty_medium_percent:.2f}%)
 - Hard: {difficulty_hard} ({difficulty_hard_percent:.2f}%)
------------------------
"""
with open(output_file, "w") as report_file:
 report_file.write(report)
print(f"Report generated and saved as '{output_file}'")

print(report)