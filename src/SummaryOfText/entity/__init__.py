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
    
    
#from model_trainer
@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    data_path: Path
    model_ckpt: Path
    num_train_epochs: int
    warmup_steps: int
    per_device_train_batch_size: int
    weight_decay: float
    logging_steps: int
    evaluation_strategy: str
    eval_steps: int
    save_steps: float
    gradient_accumulation_steps: int
    # gradient_checkpointing: bool
    


# for modle evaluation
@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    data_path: Path
    model_path: Path
    tokenizer_path: Path
    metric_file_name: Path