import csv 

jobs = []
with open("./to_save.csv", "r", encoding="cp949") as file: 
    csv_reader = csv.reader(file)

    for row in csv_reader:
        job = {
            
            "company_title" : row[1],
            "title": row[2],
            "location": row[3], 
            "link": row[4]
        }
        jobs.append(job)
    
print(len(jobs[1:]))


