from model.db import sqlliteDButils
from model.dao import VisualiztionPropertiesDAO
from model.dao import VisualiztionDAO


def insert_visualization_properties(properties):
    queryVisualizationID = VisualiztionDAO.get_visualiztion_by_type("\""+get_visualization_type(properties.visualizationType)+"\"")
    VisualizationID = sqlliteDButils.execute_select(queryVisualizationID)
    id= VisualizationID[0]["id"]
    queryVisualizationProperties= VisualiztionPropertiesDAO.insert(properties.testName,properties.textID,id,properties.propName,properties.propVal,properties.propType,properties.threshold,properties.setNum)
    val=[properties.testName,properties.textID,id,properties.propName,properties.propVal,properties.propType,properties.threshold,properties.setNum]
    return sqlliteDButils.execute_run(queryVisualizationProperties,val)


def get_test_properties(testName):
    query = VisualiztionPropertiesDAO.get_test_properties(testName)
    return sqlliteDButils.execute_select(query)

def delete_test_by_name(testName):
    query = VisualiztionPropertiesDAO.delete_test_by_name(testName)
    val = (testName,)
    return sqlliteDButils.execute_run(query,val)


def get_visualization_type(visualization):
    if (visualization == "Without Visualization"):
        return "WithoutVisualization"
    elif (visualization == "Highlight"):
        return "Highlight"
    elif (visualization == "Gradual Highlight"):
        return "GradualHighlight"
    elif (visualization == "Font"):
        return "IncreasedFont"
    elif (visualization == "Gradual Font"):
        return "GradualFont"
    elif (visualization == "Summary Only"):
        return "SummaryOnly"

def get_visualiztion_by_id(id):
    query = VisualiztionDAO.get_visualiztion_by_id(id)
    return sqlliteDButils.execute_select(query)


