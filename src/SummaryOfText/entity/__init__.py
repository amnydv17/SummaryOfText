from dataclasses import dataclass
from pathlib import Path


# from data_ingestion
@dataclass(frozen=True)
class DataIngestionConfig:
  root_dir : Path
  source_URL : str  # all are get from config.yaml
  local_data_file: Path
  unzip_dir : Path
  

#from data_validation
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: list
    
    
# from data_transformation
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    tokenizer_name: Path