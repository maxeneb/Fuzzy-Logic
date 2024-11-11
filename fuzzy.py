
## membership functions

summative = {
    #[above average, average, below average]
    0:[0,0,1], 10:[0,0,0.5], 20:[0,0.5,0], 30:[0,1,0], 40:[0,0.5,0], 50:[1,0,0]
}

performance = {
    #[poor, good, excellent]
    0:[1,0,0], 1:[0.5,0,0], 2:[0,0.5,0], 3:[0,1,0], 4:[0,0.5,0], 5:[0,0,1]
}

remarks = {
    #[no Honor, honor, high honor]
    0:[1,0,0], 10:[0.8,0.2,0], 20:[0.6,0.4,0], 30:[0.4,0.6,0], 40:[0.2,0.8,0], 50:[0,1,0],
    60:[0,0.8,0.2], 70:[0,0.6,0.4], 80:[0,0.4,0.6], 90:[0,0.2,0.8], 100:[0,0,1]
}

centroid = {
    0:{"value":0}, 10:{"value":0}, 20:{"value":0}, 30:{"value":0}, 40:{"value":0}, 50:{"value":0},
    60:{"value":0}, 70:{"value":0}, 80:{"value":0}, 90:{"value":0}, 100:{"value":0}
}

grading = {
    "noHonor":[],
    "honor":[],
    "highHonor":[]
}

#defining rules

def rules(summative,performance,grading):
    #no honor
    grading["noHonor"].append(min(summative[2],performance[0]))
    grading["noHonor"].append(min(summative[2],performance[1]))

    #honor
    grading["honor"].append(min(summative[0],performance[0]))
    grading["honor"].append(max(summative[1],performance[0]))
    grading["honor"].append(min(summative[1],performance[1]))
    grading["honor"].append(min(summative[2],performance[2]))

    #high honor
    grading["highHonor"].append(max(summative[0],performance[1]))
    grading["highHonor"].append(max(summative[0],performance[2]))
    grading["highHonor"].append(min(summative[1],performance[2]))
    return

def calculate_centroid(remarks,scores,centroid):
    for i in range(len(scores)):
        for index in remarks:
            if(remarks[index][i] == 0 or scores[i] == 0):
                continue
            if(remarks[index][i] > scores[i]):
                centroid[index]['value'] = scores[i]
            elif(remarks[index][i] <= scores[i]):
                if(centroid[index]['value'] <= remarks[index][i]):
                    centroid[index]['value'] = remarks[index][i]
    num=0
    denum=0
    for index in centroid:
        num = num + (centroid[index]['value'] * (index))
    for index in centroid:
            denum+=centroid[index]['value']
    return num/denum

def get_user_input():
    summative_exam = int(input("Enter your summative exam score (0-50): "))
    performance_task = int(input("Enter your performance task score (0-5): "))
    return summative_exam, performance_task

def categorize_centroid(centroid_value):
    if centroid_value < 25:
        return "No Honor"
    elif 25 <= centroid_value < 75:
        return "With Honors"
    else:
        return "With High Honors"

summative_exam, performance_task = get_user_input()

if 0 <= summative_exam <= 50 and 0 <= performance_task <= 5:
    summative_values = summative[summative_exam]
    performance_values = performance[performance_task]
    scores = []
    (rules(summative_values, performance_values, grading))

    for key in grading:
        scores.append(max(grading[key]))

    total = calculate_centroid(remarks, scores, centroid)
    print(f"CENTROID = {total}")

    category = categorize_centroid(total)
    print(f"REMARKS = {category}")

else:
    print("Invalid input. Please enter values within the specified ranges.")
