import zipfile
import os
import argparse

def pack_to_archive(source_path, output_filename):
    if not os.path.exists(source_path):
        return False
    try:
        with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(source_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, start=os.path.dirname(source_path))
                    zipf.write(file_path, arcname)
        return True
    except:
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("source")
    parser.add_argument("output")
    args = parser.parse_args()
    pack_to_archive(args.source, args.output)
