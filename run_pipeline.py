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

import argparse
from pathlib import Path
import yaml
from Bio import Entrez, SeqIO
import primer3

# -----------------------------
# Load config
# -----------------------------
def load_config(config_file="config.yaml"):
    with open(config_file, "r") as f:
        return yaml.safe_load(f)

# -----------------------------
# Argument parser (optional overrides)
# -----------------------------
def parse_args():
    parser = argparse.ArgumentParser(description="PCR Assay Pipeline")
    parser.add_argument(
        "--base_folder", type=str, help="Override default base folder from config"
    )
    parser.add_argument(
        "--config_file", type=str, default="config.yaml", help="Path to YAML config"
    )
    return parser.parse_args()

# -----------------------------
# NCBI genome fetcher
# -----------------------------
class NCBISequenceFetcher:
    def __init__(self, email, genome_dir):
        Entrez.email = email
        self.genome_dir = Path(genome_dir)
        self.genome_dir.mkdir(parents=True, exist_ok=True)

    def fetch_genome(self, accession):
        genome_file = self.genome_dir / f"{accession}.fasta"
        if genome_file.exists():
            print(f"Genome already exists: {genome_file}")
            return genome_file

        print(f"Downloading genome {accession}...")
        handle = Entrez.efetch(db="nucleotide", id=accession, rettype="fasta", retmode="text")
        seq_data = handle.read()
        handle.close()

        with open(genome_file, "w") as f:
            f.write(seq_data)
        print(f"Saved genome to {genome_file}")
        return genome_file

# -----------------------------
# Primer design (example)
# -----------------------------
def design_primers(sequence, primer3_settings):
    primers = primer3.bindings.designPrimers(
        {"SEQUENCE_TEMPLATE": sequence},
        primer3_settings
    )
    return primers

# -----------------------------
# Main pipeline
# -----------------------------
def main():
    args = parse_args()
    config = load_config(args.config_file)

    # Base folder logic
    repo_root = Path(__file__).parent.resolve()
    base_folder = Path(args.base_folder) if args.base_folder else repo_root / config["general"]["base_folder"]
    genome_folder = base_folder / config["general"]["genome_folder"]
    output_folder = base_folder / config["general"]["output_folder"]
    region_length = config["general"].get("region_length", 1000)

    genome_folder.mkdir(parents=True, exist_ok=True)
    output_folder.mkdir(parents=True, exist_ok=True)

    # NCBI setup
    ncbi_email = config["ncbi"]["email"]
    fetcher = NCBISequenceFetcher(email=ncbi_email, genome_dir=genome_folder)

    organisms = config["organisms"]
    num_assays = config["assays"]["num_assays_per_organism"]
    primer3_settings = config["primer3_settings"]

    print(f"Base folder: {base_folder}")
    print(f"Region length: {region_length}")
    print(f"Running {num_assays} assays for {len(organisms)} organisms\n")

    for org in organisms:
        print(f"Processing {org['name']} ({org['accession']})")
        genome_file = fetcher.fetch_genome(org["accession"])

        # Load genome sequence (first record)
        seq_record = next(SeqIO.parse(genome_file, "fasta"))
        sequence = str(seq_record.seq[:region_length])  # truncate to region length

        # Design primers
        primers = design_primers(sequence, primer3_settings)
        print(f"Designed primers for {org['name']} (example output)\n")

if __name__ == "__main__":
    main()

