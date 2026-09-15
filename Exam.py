import pandas as pd
import numpy as np

#malformed score data, duplicates 

#the code must clean, refuse the data that it cannot and never crash due to a bad single row

#student_record = (self, name, score) [NumPy array] || if record is built = .lock() || .add_score() method that adheres to the .lock()

#if .lock() = true, then .add_score() is false

#.average() method using np.mean() that gets the average per student once .lock() is true 

#class InvalidScoreError(Exception): whenever the score in the row of the student[name] is invalid || __str__ "that score is not a number" or "the score is not within 0 - 100" || __repr__ same error but for debugging 

#class StudentRecordLockedError(Exception): whenever a value is added to a .lock() student record || __str__ "The student record is locked and cannot be added any new scores"

#function that cleans the raw_rows with pandas trimming, parsing, and dropping of duplicates. It then builds the cleaned rows 

#exception handling that tracks whenever the rows get them for (student, failures) format: {"row": <original raw dict>, "error": <reason>} duplicates are not part of the failure list but must be cleaned 

#function ranking uses sorted() with lambda key to sort average() 

raw_rows = [
    {"name": " Amara ", "scores": "92,85,78"},
    {"name": "Leo", "scores": "88,91,73"},
    {"name": "Priya", "scores": "65,72,150"},         
    {"name": "Sam", "scores": "70,not_a_number,60"},  
    {"name": "Amara", "scores": "95,90,88"},          
    {"name": "Jade", "scores": "81,77,84,90"},
]

class InsufficientFundsError(Exception):

class StudentRecordLockedError(Exception):