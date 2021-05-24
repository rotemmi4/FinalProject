

def get_answer_by_test_name_SUM(testName, visualization, set_num):
    return ("""SELECT StudentInfo.studentID, studentAge, studentGender, visualiztions.type, is_correct, SUM(time_to_answer)
     FROM StudentAnswers
     INNER JOIN StudentInfo on StudentAnswers.studentID = StudentInfo.studentID 
     INNER JOIN questions on questions.question_id = StudentAnswers.question_id 
     INNER JOIN visualiztion_properties on visualiztion_properties.text_id = questions.text_id 
     INNER JOIN visualiztions on visualiztion_properties.visualiztion_id = visualiztions.id 
     WHERE test_name={} AND visualiztions.type= {} AND visualiztion_properties.set_num={} GROUP BY StudentInfo.studentID """.format(testName, "\'" + visualization + "\'", set_num))

def get_placing_by_test_name(test_name):
    return ("SELECT * FROM studentRank WHERE test_name=" + str(test_name))

def get_answer_by_test_name_COUNT(testName, visualization, set_num):
    return ("""SELECT StudentInfo.studentID, studentAge, studentGender, visualiztions.type, COUNT(is_correct)*1.25
     FROM StudentAnswers
     INNER JOIN StudentInfo on StudentAnswers.studentID = StudentInfo.studentID 
     INNER JOIN questions on questions.question_id = StudentAnswers.question_id 
     INNER JOIN visualiztion_properties on visualiztion_properties.text_id = questions.text_id 
     INNER JOIN visualiztions on visualiztion_properties.visualiztion_id = visualiztions.id 
     WHERE test_name={} AND visualiztions.type= {} AND visualiztion_properties.set_num={} AND StudentAnswers.is_correct=1 GROUP BY StudentInfo.studentID """.format(testName, "\'" + visualization + "\'", set_num))

def get_answer_by_test_name_AVG(testName, visualization, set_num):
    return ("""SELECT StudentInfo.studentID, studentAge, studentGender, visualiztions.type, is_correct, AVG(time_to_answer)
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
    return ("""SELECT StudentInfo.studentID, studentAge, studentGender, visualiztions.type, ReadingTime, SummaryTime
     FROM StudentAnswers
     INNER JOIN StudentInfo on StudentAnswers.studentID = StudentInfo.studentID 
     INNER JOIN StudentSummary on StudentAnswers.studentID = StudentSummary.studentID
     INNER JOIN questions on questions.question_id = StudentAnswers.question_id 
     INNER JOIN visualiztion_properties on visualiztion_properties.text_id = questions.text_id 
     INNER JOIN visualiztions on visualiztion_properties.visualiztion_id = visualiztions.id 
     WHERE test_name={} AND visualiztions.type= {} AND visualiztion_properties.set_num={} GROUP BY StudentInfo.studentID """.format(testName, "\'" + visualization + "\'", set_num))