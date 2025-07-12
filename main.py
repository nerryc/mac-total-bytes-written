import subprocess
import re


def get_ssd_data_units_written():
    """
    Retrieve the number of data units written to the SSD using smartctl.

    Returns:
        tuple: A tuple containing the number of data units written (str) and the equivalent in terabytes (str),
               or None if the information could not be retrieved.
    """
    command = "smartctl -A /dev/disk0"  # Adjust if your SSD is at a different location.

    try:
        # Run the command
        result = subprocess.run(command.split(), capture_output=True, text=True, check=True)
    except FileNotFoundError:
        print("Error: 'smartctl' command not found. Please install smartmontools.")
        return None
    except subprocess.CalledProcessError as e:
        print(f"Error executing smartctl: {e.stderr}")
        return None

    # Parse the output
    output = result.stdout
    written_line = re.search(
        r"Data Units Written:\s+(\d+,\d+,\d+) \[([\d.]+ TB)\]", output
    )
    if written_line:
        written_units = written_line.group(1)
        written_tb = written_line.group(2)
        return written_units, written_tb
    else:
        print("Data Units Written information not found in the smartctl output.")
        return None


if __name__ == "__main__":
    written_info = get_ssd_data_units_written()
    if written_info is not None:
        print(
            f"Data Units Written: {written_info[0]} units, which is approximately {written_info[1]}"
        )
    else:
        print("Failed to retrieve SSD data units written.")
