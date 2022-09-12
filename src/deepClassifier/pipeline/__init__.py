from deepClassifier.config import ConfigurationManager
from deepClassifier.components.dataIngestion import DataIngestion


try:
    config = ConfigurationManager()
    data_ingestion_config = config.get_data_ingestion_config()
    data_ingestion = DataIngestion(config=data_ingestion_config)
    data_ingestion.download_file()
    data_ingestion.unzip_and_clean()
except Exception as e:
    raise e