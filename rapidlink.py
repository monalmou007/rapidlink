import os
import argparse

def get_size(start_path='.'):
    """Calculate the total size of files and folders in the given directory."""
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # Skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size

def analyze_disk_usage(path):
    """Analyze the disk usage of the given path and print the results."""
    if not os.path.exists(path):
        print(f"The path {path} does not exist.")
        return
    
    if os.path.isfile(path):
        size = os.path.getsize(path)
        print(f"File: {path} - Size: {size} bytes")
    else:
        print(f"Disk usage for directory: {path}")
        for dirpath, dirnames, filenames in os.walk(path):
            for dirname in dirnames:
                dir_full_path = os.path.join(dirpath, dirname)
                dir_size = get_size(dir_full_path)
                print(f"Directory: {dir_full_path} - Size: {dir_size} bytes")
            for filename in filenames:
                file_full_path = os.path.join(dirpath, filename)
                file_size = os.path.getsize(file_full_path)
                print(f"File: {file_full_path} - Size: {file_size} bytes")

def main():
    parser = argparse.ArgumentParser(description="Analyze disk usage and report on space consumption by different files and folders.")
    parser.add_argument('path', type=str, help='The path to analyze')
    args = parser.parse_args()
    
    analyze_disk_usage(args.path)

if __name__ == '__main__':
    main()