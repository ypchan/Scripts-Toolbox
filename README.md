# A collection of useful scripts for daiily work and genomic tasks.
## filter_spades_assembly.py
To remove short and low-coverage contigs from SPAdes assembly.

Usage:
```
$ filter_spades_assembly.py  -h
usage: filter_spades_assembly.py [-h] [--min_length MIN_LENGTH] [--min_coverage MIN_COVERAGE] input_file

Filter sequences by length and coverage.

positional arguments:
  input_file            Input file containing sequences

options:
  -h, --help            show this help message and exit
  --min_length MIN_LENGTH
                        Minimum sequence length
  --min_coverage MIN_COVERAGE
                        Minimum sequence coverage

```
Example:

```
filter_spades_assembly.py --min_length 150 --min_coverage 20 spades.assembly.fasta > spades.filtered.assembly.fasta
filter_spades_assembly.py --min_length 150 spades.assembly.fasta > spades.filtered.assembly.fasta
filter_spades_assembly.py --min_coverage 20 spades.assembly.fasta > spades.filtered.assembly.fasta
```
## split_pdf_into_chunks.R
To split a long PDF with many pages into multiple PDF with a  smaller number of pages
