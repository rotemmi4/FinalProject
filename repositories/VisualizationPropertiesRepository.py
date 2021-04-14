from model.concrete import VisualizationPropertiesConcrete

def visualization_properties(properties):
    return VisualizationPropertiesConcrete.insert_visualization_properties(properties)

def get_visualiztion_by_id(id):
    return VisualizationPropertiesConcrete.get_visualiztion_by_id(id)