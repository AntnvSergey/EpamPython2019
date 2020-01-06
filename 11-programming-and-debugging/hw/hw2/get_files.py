from os import walk, path
import hashlib
import argparse


def get_file_hash(file_name):
    file = open(file_name, "rb")
    data = file.read()
    file.close()
    hash_from_file = hashlib.sha256(data).hexdigest()
    return hash_from_file


description = """
The utility that takes the path to the directory and sha256 hash as an argument. \
The utility goes through all the files inside the directory and displays in stdout \
the absolute path to the files whose hash is specified as an argument.
"""

parser = argparse.ArgumentParser(description=description)
parser.add_argument('directory_path', type=str, help='Path to directory')
parser.add_argument('file_hash', type=str, help='Hash of the file or files')
args = parser.parse_args()
directory_path = args.directory_path
file_hash = args.file_hash

paths = []
tree = walk(directory_path)
for root, dirs, files in tree:
    for file in files:
        file_path = path.abspath(root)
        absolute_path = file_path + '/' + file
        hash = get_file_hash(absolute_path)
        if hash == file_hash:
            paths.append(absolute_path)

if paths:
    print('files were found: ')
    for p in paths:
        print(p + '\n')
else:
    print('not found any files')
