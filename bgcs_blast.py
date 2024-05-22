import argparse
import concurrent.futures
import subprocess
import pandas as pd
import os

def run_tblastn(genome_path, output_prefix):
    """
    Function to run tblastn command.
    :param genome_path: Path to the genome file.
    :param output_prefix: Prefix for the output file.
    """
    output_file = f"{output_prefix}_tblastn.out"
    command = f"tblastn -query protein.fasta -db {genome_path} -out {output_file}"
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Completed: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error running tblastn on {genome_path}: {e}")

def main(input_file, threads):
    """
    Main function to read TSV file and execute tblastn in parallel.
    :param input_file: Input TSV file with genome paths and output prefixes.
    :param threads: Number of threads to use.
    """
    # Read the input TSV file
    df = pd.read_csv(input_file, sep='\t', header=None)
    df.columns = ['genome_path', 'output_prefix']
    
    # Run tblastn in parallel
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        futures = [
            executor.submit(run_tblastn, row['genome_path'], row['output_prefix'])
            for index, row in df.iterrows()
        ]
        for future in concurrent.futures.as_completed(futures):
            future.result()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run tblastn in parallel on multiple genome files.")
    parser.add_argument("input_file", type=str, help="Input TSV file with genome paths and output prefixes.")
    parser.add_argument("-t", "--threads", type=int, default=4, help="Number of threads to use.")
    
    args = parser.parse_args()
    
    main(args.input_file, args.threads)
