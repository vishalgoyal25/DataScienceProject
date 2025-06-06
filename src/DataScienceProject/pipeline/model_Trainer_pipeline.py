from src.DataScienceProject.config.configuration import ConfigurationManager
from src.DataScienceProject.components.model_Trainer import ModelTrainer
from src.DataScienceProject import logger


STAGE_NAME = "Model Trainer Stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_training(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()

        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()
        