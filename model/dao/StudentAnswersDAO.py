

def get_answer_by_test_name(testName):
    return ("""SELECT StudentInfo.studentID,studentAge,studentGender,Timestamp,visualiztion_properties.text_id,visualiztions.type,visualiztion_properties.property_name,visualiztion_properties.property_value,StudentAnswers.question_id,is_correct,time_to_answer,Summary
     FROM StudentAnswers
     INNER JOIN StudentInfo on StudentAnswers.studentID = StudentInfo.studentID 
     INNER JOIN questions on questions.question_id = StudentAnswers.question_id 
     INNER JOIN visualiztion_properties on visualiztion_properties.text_id = questions.text_id 
     INNER JOIN visualiztions on visualiztion_properties.visualiztion_id = visualiztions.id 
     INNER JOIN StudentSummary on StudentSummary.studentID = StudentAnswers.studentID AND StudentSummary.text_id=visualiztion_properties.text_id
     WHERE test_name=""" + testName)
