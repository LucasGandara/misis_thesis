import os
import glob

def read_gitignore():
    """Read patterns from .gitignore file"""
    with open('.gitignore', 'r') as f:
        # Skip comments and empty lines
        patterns = [line.strip() for line in f if line.strip() and not line.startswith('//')]
    return patterns

def expand_pattern(pattern):
    """Convert gitignore pattern to glob pattern"""
    if pattern.startswith('/'):
        pattern = pattern[1:]  # Remove leading slash
    if pattern.startswith('*'):
        pattern = f'**/{pattern}'  # Make it match in all subdirectories
    return pattern

def clean_files():
    """Remove files matching gitignore patterns"""
    patterns = read_gitignore()
    files_removed = 0
    
    for pattern in patterns:
        expanded_pattern = expand_pattern(pattern)
        matching_files = glob.glob(expanded_pattern, recursive=True)
        
        for file_path in matching_files:
            try:
                os.remove(file_path)
                print(f"Removed: {file_path}")
                files_removed += 1
            except OSError as e:
                print(f"Error removing {file_path}: {e}")
    
    print(f"\nTotal files removed: {files_removed}")

if __name__ == "__main__":
    clean_files()