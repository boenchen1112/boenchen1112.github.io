"""
MuseScore to PNG Exporter
Converts .mscz files to PNG images using MuseScore command line
"""

import subprocess
import os
import glob

# Get the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Configuration - uses the same folder as the script
INPUT_FILE = os.path.join(SCRIPT_DIR, "sheet image producer.mscz")
OUTPUT_FOLDER = SCRIPT_DIR

# MuseScore executable path (adjust if needed)
# Common locations:
# Windows: C:\Program Files\MuseScore 4\bin\MuseScore4.exe
# Windows: C:\Program Files\MuseScore 3\bin\MuseScore3.exe
MUSESCORE_PATH = r"C:\Program Files\MuseScore 4\bin\MuseScore4.exe"

# Alternative paths to try
MUSESCORE_PATHS = [
    r"C:\Program Files\MuseScore 4\bin\MuseScore4.exe",
    r"C:\Program Files\MuseScore 3\bin\MuseScore3.exe",
    r"C:\Program Files (x86)\MuseScore 4\bin\MuseScore4.exe",
    r"C:\Program Files (x86)\MuseScore 3\bin\MuseScore3.exe",
    "musescore4",
    "musescore3",
    "musescore",
]


def find_musescore():
    """Find MuseScore executable"""
    for path in MUSESCORE_PATHS:
        if os.path.exists(path):
            return path
        # Try running it (for PATH-based commands)
        try:
            result = subprocess.run([path, "--version"], capture_output=True, timeout=5)
            if result.returncode == 0:
                return path
        except:
            continue
    return None


def export_mscz_to_png(input_file, output_folder, musescore_path=None):
    """
    Export a .mscz file to PNG

    Args:
        input_file: Path to .mscz file
        output_folder: Folder to save PNG files
        musescore_path: Path to MuseScore executable (auto-detect if None)

    Returns:
        List of created PNG files
    """
    # Find MuseScore
    if musescore_path is None:
        musescore_path = find_musescore()

    if musescore_path is None:
        print("ERROR: MuseScore not found!")
        print("Please install MuseScore from: https://musescore.org/")
        print("Or set the MUSESCORE_PATH variable in this script.")
        return []

    print(f"Using MuseScore: {musescore_path}")

    # Check input file exists
    if not os.path.exists(input_file):
        print(f"ERROR: Input file not found: {input_file}")
        return []

    # Create output folder
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created output folder: {output_folder}")

    # Get base filename
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    output_file = os.path.join(output_folder, f"{base_name}.png")

    # Find next available version number (001, 002, 003, etc.)
    version = 1
    while True:
        version_str = f"{version:03d}"
        output_file = os.path.join(output_folder, f"{version_str}.png")
        # Also check for multi-page pattern
        multi_page_pattern = os.path.join(output_folder, f"{version_str}-*.png")
        if not os.path.exists(output_file) and not glob.glob(multi_page_pattern):
            break
        version += 1

    print(f"Using version number: {version_str}")

    # Build command
    # MuseScore exports multi-page scores as name-1.png, name-2.png, etc.
    cmd = [
        musescore_path,
        "-o", output_file,
        input_file
    ]

    print(f"Exporting: {input_file}")
    print(f"Output: {output_file}")

    try:
        # Run MuseScore export
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=60
        )

        if result.returncode != 0:
            print(f"Export failed with error:")
            print(result.stderr)
            return []

        # Find all created PNG files (MuseScore creates name-1.png, name-2.png for multi-page)
        created_files = []

        # Check for single page output
        if os.path.exists(output_file):
            created_files.append(output_file)

        # Check for multi-page output (001-1.png, 001-2.png, etc.)
        pattern = os.path.join(output_folder, f"{version_str}-*.png")
        created_files.extend(glob.glob(pattern))

        if created_files:
            print(f"\nSuccess! Created {len(created_files)} PNG file(s):")
            for f in created_files:
                print(f"  - {f}")
        else:
            print("Warning: No PNG files were created.")

        return created_files

    except subprocess.TimeoutExpired:
        print("ERROR: Export timed out")
        return []
    except Exception as e:
        print(f"ERROR: {e}")
        return []


def batch_export(input_folder, output_folder, musescore_path=None):
    """
    Export all .mscz files in a folder to PNG
    """
    pattern = os.path.join(input_folder, "*.mscz")
    mscz_files = glob.glob(pattern)

    if not mscz_files:
        print(f"No .mscz files found in: {input_folder}")
        return

    print(f"Found {len(mscz_files)} .mscz file(s)")

    all_created = []
    for mscz_file in mscz_files:
        created = export_mscz_to_png(mscz_file, output_folder, musescore_path)
        all_created.extend(created)

    print(f"\nTotal: Created {len(all_created)} PNG file(s)")


if __name__ == "__main__":
    print("=" * 50)
    print("MuseScore to PNG Exporter")
    print("=" * 50)
    print()

    # Export the specified file
    export_mscz_to_png(INPUT_FILE, OUTPUT_FOLDER)

    print()
    print("Done!")
