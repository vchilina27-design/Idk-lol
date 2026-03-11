import zipfile
import os
import argparse

def pack_to_zip(source_path, output_filename):
    """
    Packs a file or a directory into a .zip archive.
    """
    if not os.path.exists(source_path):
        print(f"Error: Source path '{source_path}' does not exist.")
        return False

    if not output_filename.endswith('.zip'):
        output_filename += '.zip'

    try:
        with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            if os.path.isfile(source_path):
                zipf.write(source_path, os.path.basename(source_path))
            elif os.path.isdir(source_path):
                for root, dirs, files in os.walk(source_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, start=os.path.dirname(source_path))
                        zipf.write(file_path, arcname)
        print(f"Successfully created '{output_filename}' from '{source_path}'.")
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Pack files or directories into a .zip archive.")
    parser.add_argument("source", help="Path to the file or directory to pack.")
    parser.add_argument("output", help="Name of the output .zip file.")

    args = parser.parse_args()
    pack_to_zip(args.source, args.output)

if __name__ == "__main__":
    main()
