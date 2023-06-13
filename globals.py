from dotenv import load_dotenv
import os
load_dotenv()

GLOBALS = {
    "TRANSFORMERS_CACHE": os.environ.get("TRANSFORMERS_CACHE"),
    "HF_DATASETS_CACHE": os.environ.get("HF_DATASETS_CACHE"),
    "PORT": os.environ.get("PORT", "5002"),
    "HOST": os.environ.get("HOST", "0.0.0.0")
}