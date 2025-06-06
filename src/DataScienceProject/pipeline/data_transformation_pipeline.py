
from pathlib import Path

from src.DataScienceProject.config.configuration import ConfigurationManager
from src.DataScienceProject.components.data_transformation import DataTransformation
from src.DataScienceProject import logger

STAGE_NAME="Data Transformation Stage"

class DataTransformationTrainingPipeline:

    def __init__(self):
        pass

    def initiate_data_transformation(self):

        try:
            with open(Path("artifacts/data_validation/status.txt"),'r') as f:
                status=f.read().split(" ")[-1]

            if status=="True":
                config=ConfigurationManager()
                data_transformation_config=config.get_data_transformation_config()

                data_transformation=DataTransformation(config=data_transformation_config)
                data_transformation.train_test_splitting()
                
            else:
                raise Exception("Your Data Scheme is Not Valid")
            
        except Exception as e:
            print(e)