

def get_answer_by_test_name(testName):
    return ("""SELECT studentID,Timestamp,visualiztion_properties.text_id,visualiztions.type,visualiztion_properties.property_name,visualiztion_properties.property_value,StudentAnswers.question_id,is_correct,time_to_answer
     FROM StudentAnswers
     INNER JOIN questions on questions.question_id = StudentAnswers.question_id 
     INNER JOIN visualiztion_properties on visualiztion_properties.text_id = questions.text_id 
     INNER JOIN visualiztions on visualiztion_properties.visualiztion_id = visualiztions.id 
     WHERE test_name=""" + testName)
