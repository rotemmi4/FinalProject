from model.concrete import VisualizationPropertiesConcrete

def insert_visualization_properties(properties):
    return VisualizationPropertiesConcrete.insert_visualization_properties(properties)

def get_test_properties(testName):
    return VisualizationPropertiesConcrete.get_test_properties(testName)

def delete_test_properties(testName):
    return VisualizationPropertiesConcrete.delete_test_by_name(testName)

def get_visualiztion_by_id(id):
    return VisualizationPropertiesConcrete.get_visualiztion_by_id(id)