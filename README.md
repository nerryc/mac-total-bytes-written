# mac-total-bytes-written

## Overview
This Python script retrieves the total number of data units written to an SSD and displays the value in terabytes (TB). It uses the `smartctl` command from the `smartmontools` package to fetch the data.

## Prerequisites
- Ensure `smartmontools` is installed on your system. You can install it using:
  ```bash
  brew install smartmontools
  ```

## Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/nerryc/mac-total-bytes-written.git
   ```
2. Navigate to the project directory:
   ```bash
   cd mac-total-bytes-written
   ```
3. Run the script:
   ```bash
   python3 main.py
   ```

## Example Output
```
Data Units Written: 1,234,567 units, which is approximately 12.34 TB
```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
