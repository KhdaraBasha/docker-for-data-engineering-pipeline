# Import necessary modules
from pathlib import Path

current_dir = Path.cwd()
current_file = Path(__file__).name

print(f"Current directory: {current_dir}")    
print(f"Current file: {current_file}")

for filepath in current_dir.iterdir():
    print(filepath.name)
    if filepath.name == current_file:
        continue

    if filepath.is_file():
        content = filepath.read_text(encoding='utf-8')
        print(f" content : {content}")