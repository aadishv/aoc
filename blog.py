import os
import re


def extract_imports(code):
    # Regular expression to match import statements
    import_pattern = r"^(?:from\s+[\w.]+\s+import\s+[\w,\s*]+|import\s+[\w,\s]+)"

    # Find all imports
    imports = []
    for line in code.split("\n"):
        line = line.strip()
        if re.match(import_pattern, line):
            imports.append(line)

    return imports


# Process each day's code
for day in range(1, 26):
    filepath = f"./2024/d{day}/main.py"
    with open(filepath, "r") as f:
        code = f.read()
        imports = extract_imports(code)

        if imports:
            print(f"\nDay {day} imports:")
            for imp in imports:
                print(f"  {imp}")
