import subprocess
import re
import sys


def get_ssd_data_units_written(disk="/dev/disk0"):
    try:
        result = subprocess.run(
            ["smartctl", "-A", disk],
            capture_output=True,
            text=True,
        )
    except FileNotFoundError:
        print("Error: 'smartctl' not found. Install with: brew install smartmontools")
        return None

    if result.returncode not in (0, 4):
        print(f"Error running smartctl: {result.stderr.strip()}")
        return None

    match = re.search(
        r"Data Units Written:\s+([\d\s,]+)\s+\[([\d.,]+ [TGMKP]?B)\]",
        result.stdout,
    )
    if not match:
        print("Data Units Written not found in smartctl output.")
        return None

    return match.group(1).strip(), match.group(2)


if __name__ == "__main__":
    disk = sys.argv[1] if len(sys.argv) > 1 else "/dev/disk0"
    info = get_ssd_data_units_written(disk)
    if info:
        print(f"Data Units Written: {info[0]} units, which is approximately {info[1]}")
    else:
        print("Failed to retrieve SSD data units written.")
