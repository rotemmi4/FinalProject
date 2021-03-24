from model.concrete import VisualizationPropertiesConcrete

def visualization_properties(properties):
    return VisualizationPropertiesConcrete.insert_visualization_properties(properties)

def get_test_properties(testName):
    return VisualizationPropertiesConcrete.get_test_properties(testName)