from pathlib import Path
import yaml
from src.assay_pipeline import batch_assay_pipeline

base_folder = Path(__file__).parent
config_file = base_folder / "config.yaml"

with open(config_file) as cf:
    config = yaml.safe_load(cf)

# Organism & pipeline settings
organisms = config.get("organisms", {})
pipeline_config = config.get("pipeline", {})
assays_per_org = pipeline_config.get("assays_per_org", 5)
region_length = pipeline_config.get("region_length", 100)
email = pipeline_config.get("email", "your_email@example.com")

print(organisms)

# Primer3 settings
primer3_config = config.get("primer3", {})
outer_settings = primer3_config.get("outer", {})
inner_settings = primer3_config.get("inner", {})

# Pass all relevant config to pipeline function
batch_assay_pipeline(
    organisms=organisms,
    assays_per_org=assays_per_org,
    region_length=region_length,
    email=email,
    outer_primer_settings=outer_settings,
    inner_primer_settings=inner_settings
)
