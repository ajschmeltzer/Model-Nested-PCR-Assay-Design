from pathlib import Path
import yaml
from src.assay_pipeline import batch_assay_pipeline

BASE_FOLDER = Path(__file__).parent
CONFIG_FILE = BASE_FOLDER / "config.yaml"

with open(CONFIG_FILE) as cf:
    config = yaml.safe_load(cf)

# Organism & pipeline settings
ORGANISMS = config.get("organisms", {})
PIPELINE_CONFIG = config.get("pipeline", {})
ASSAYS_PER_ORG = PIPELINE_CONFIG.get("assays_per_org", 5)
REGION_LENGTH = PIPELINE_CONFIG.get("region_length", 100)
EMAIL = PIPELINE_CONFIG.get("email", "your_email@example.com")

print(ORGANISMS)

# Primer3 settings
PRIMER3_CONFIG = config.get("primer3", {})
OUTER_SETTINGS = PRIMER3_CONFIG.get("outer", {})
INNER_SETTINGS = PRIMER3_CONFIG.get("inner", {})

# Pass all relevant config to pipeline function
batch_assay_pipeline(
    organisms=ORGANISMS,
    assays_per_org=ASSAYS_PER_ORG,
    region_length=REGION_LENGTH,
    email=EMAIL,
    outer_primer_settings=OUTER_SETTINGS,
    inner_primer_settings=INNER_SETTINGS
)
