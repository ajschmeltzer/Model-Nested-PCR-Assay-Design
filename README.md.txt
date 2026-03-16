PCR Assay Designer

Automated nested PCR assay design pipeline built with Python and Primer3.
The pipeline downloads genomes from NCBI, randomly samples genome regions, and designs two-level nested PCR assays with annotated outputs.

**Primer design for specific user-input genome sequences is not currently supported.**

<<<<<<< HEAD
-----------------------------------------------------------------------
Features:
=======
- Downloads genomes from NCBI
- Randomly samples genome regions
- Designs two level nested PCR assays
- Outputs primer sequences and amplicons
- Generates ApE annotated files
- YAML config file for organism genomes and Primer3 settings
>>>>>>> b384dd6a8d10c890e61cb5b684003e1fe7c5baba

-Automatic genome download from NCBI
-Local genome caching to avoid repeated downloads
-Random genome region sampling
-Automated outer and inner nested PCR primer design
-Configurable Primer3 parameters via config.yaml
-Multiple assays per organism
-Annotated ApE plasmid files for visualization
-CSV and TXT primer reports
-Project Structure

-----------------------------------------------------------------------
Usage

Run the pipeline from the repository root:
	python run_pipeline.py

The pipeline will:
	-Download genomes if not already present
	-Sample random genome regions
	-Design nested PCR assays
	-Export results

-----------------------------------------------------------------------
Project Structure
Nested-PCR-Assay-Design
│
├── config.yaml
├── run_pipeline.py
│
├── src
│   └── assay_pipeline.py
│
└── Designed Assays
    ├── Genomes
    └── Assays by Organism
	├──Assay 1
	└──Assay 2 etc...

-----------------------------------------------------------------------
File and Folder Descriptions

config.yaml
	Pipeline configuration including organisms and primer settings.

run_pipeline.py
	Entry point for running the pipeline.

src/assay_pipeline.py
	Core primer design pipeline.

Designed Assays/Genomes
	Downloaded genomes stored locally.

Designed Assays/Assays by Organism
	Generated assay output folders.

-----------------------------------------------------------------------
Installation

Clone the repository:
	git clone https://github.com/ajschmeltzer/Nested-PCR-Assay-Design
	cd Nested-PCR-Assay-Design

Install dependencies:
	pip install -r requirements.txt

Dependencies include:
	Biopython
	primer3-py
	PyYAML

<<<<<<< HEAD
-----------------------------------------------------------------------
Configuration

All pipeline settings are controlled through config.yaml.

Example config.yaml:
=======
##Configuration

Update setting in the config.yaml file

## Usage

python run_pipeline.py
>>>>>>> b384dd6a8d10c890e61cb5b684003e1fe7c5baba

	ORGANISMS:
		E_coli: NC_000913.3

<<<<<<< HEAD
	pipeline:
		assays_per_org: 5
		region_length: 10000
		email: your_email@example.com

	primer3:
=======
Assays for each organism are saved to:

PCR_Assay_Design/organisms/
>>>>>>> b384dd6a8d10c890e61cb5b684003e1fe7c5baba

		outer:
			PRIMER_OPT_SIZE: 20
			PRIMER_MIN_SIZE: 18
			PRIMER_MAX_SIZE: 25
			PRIMER_PRODUCT_SIZE_RANGE: [[230, 400]]

<<<<<<< HEAD
		inner:
			PRIMER_PRODUCT_SIZE_RANGE: [[120, 200]]
-----------------------------------------------------------------------
Organisms

The ORGANISMS section is a dictionary of organism names and NCBI genome accessions.

Format:
	Organism_name : NCBI_accession

Example:
	E_coli : NC_000913.3
	Human_chr1 : NC_000001.11

-----------------------------------------------------------------------
Output
Generated assays are stored in:
	data/organisms

Each assay folder contains:
info.txt
	*_primers.txt
	*_primers.csv
	*.ape
	*_feature_library.txt

-----------------------------------------------------------------------
File Descriptions

*_primers.txt
	Human-readable primer report.

*_primers.csv
	Structured primer data.

*.ape
	Annotated ApE sequence file showing primer binding sites.

*_feature_library.txt
	Feature library for importing primers into ApE.

info.txt
	Genome location and metadata for the assay.

-----------------------------------------------------------------------
Genome Storage

Downloaded genomes are stored locally in:
	data/genomes

Genomes are downloaded once and reused for future runs.

-----------------------------------------------------------------------
Requirements

-Python 3.9 or newer
-Internet connection for initial genome download
-Primer3 installed via primer3-py
-----------------------------------------------------------------------
Future Improvements

-Primer design for user defined genome regions
-BLAT specificity checking

-----------------------------------------------------------------------
License

MIT License
=======
PCR_Assay_Design/genomes/
>>>>>>> b384dd6a8d10c890e61cb5b684003e1fe7c5baba
