

def get_answer_by_test_name_SUM(testName, visualization, set_num):
    return ("""SELECT StudentInfo.studentID, name, studentAge, studentGender, studentDivision, visualiztions.type, is_correct, SUM(time_to_answer)
     FROM StudentAnswers
     INNER JOIN StudentInfo on StudentAnswers.studentID = StudentInfo.studentID 
     INNER JOIN questions on questions.question_id = StudentAnswers.question_id 
     INNER JOIN visualiztion_properties on visualiztion_properties.text_id = questions.text_id 
     INNER JOIN visualiztions on visualiztion_properties.visualiztion_id = visualiztions.id 
     WHERE test_name={} AND visualiztions.type= {} AND visualiztion_properties.set_num={} GROUP BY StudentInfo.studentID """.format(testName, "\'" + visualization + "\'", set_num))

def get_placing_by_test_name(test_name):
    return ("""SELECT * FROM studentRank
     INNER JOIN StudentInfo on StudentRank.student_id = StudentInfo.studentID 
     WHERE test_name={} GROUP BY StudentInfo.studentID """.format(test_name))

def get_answer_by_test_name_COUNT(testName, visualization, set_num):
    return ("""SELECT StudentInfo.studentID, name, studentAge, studentGender, studentDivision, visualiztions.type, SUM(is_correct)
     FROM StudentAnswers
     INNER JOIN StudentInfo on StudentAnswers.studentID = StudentInfo.studentID 
     INNER JOIN questions on questions.question_id = StudentAnswers.question_id 
     INNER JOIN visualiztion_properties on visualiztion_properties.text_id = questions.text_id 
     INNER JOIN visualiztions on visualiztion_properties.visualiztion_id = visualiztions.id 
     WHERE test_name={} AND visualiztions.type= {} AND visualiztion_properties.set_num={}  GROUP BY StudentInfo.studentID """.format(testName, "\'" + visualization + "\'", set_num))

def get_answer_by_test_name_AVG(testName, visualization, set_num):
    return ("""SELECT StudentInfo.studentID, name, studentAge, studentGender, studentDivision, visualiztions.type, is_correct, AVG(time_to_answer)
     FROM StudentAnswers
     INNER JOIN StudentInfo on StudentAnswers.studentID = StudentInfo.studentID 
     INNER JOIN questions on questions.question_id = StudentAnswers.question_id 
     INNER JOIN visualiztion_properties on visualiztion_properties.text_id = questions.text_id 
     INNER JOIN visualiztions on visualiztion_properties.visualiztion_id = visualiztions.id 
     WHERE test_name={} AND visualiztions.type= {} AND visualiztion_properties.set_num={} GROUP BY StudentInfo.studentID """.format(testName, "\'" + visualization + "\'", set_num))

def correct_answers_count(testName):
    return ("""SELECT COUNT(is_correct) FROM StudentAnswers
     WHERE test_name={} AND is_correct=1 """.format(testName))

def get_answer_by_test_name_reading_time(testName, visualization, set_num):
    return ("""SELECT StudentInfo.studentID, name, studentAge, studentGender, studentDivision, visualiztions.type, ReadingTime, SummaryTime
     FROM StudentInfo
     INNER JOIN StudentSummary on StudentInfo.studentID = StudentSummary.studentID
     INNER JOIN visualiztion_properties on StudentSummary.text_id = visualiztion_properties.text_id
     INNER JOIN visualiztions on visualiztion_properties.visualiztion_id = visualiztions.id 
     WHERE test_id={} AND visualiztions.type= {} AND visualiztion_properties.set_num={} GROUP BY StudentInfo.studentID """.format(testName, "\'" + visualization + "\'", set_num))

# def get_student_details(testName):
#     return ("""SELECT StudentInfo.studentID, name, studentAge, studentGender
#      FROM StudentAnswers
#      INNER JOIN StudentInfo on StudentAnswers.studentID = StudentInfo.studentID
#      WHERE test_name={} GROUP BY StudentInfo.studentID """.format(testName))