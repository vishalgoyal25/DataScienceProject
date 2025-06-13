from src.DataScienceProject.config.configuration import ConfigurationManager
from src.DataScienceProject.components.model_Evaluation import ModelEvaluation
from src.DataScienceProject import logger


STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()