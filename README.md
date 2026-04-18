# mac-total-bytes-written

A Python script that reads the total bytes written to your Mac's SSD and displays it in terabytes (TB). Useful for tracking drive wear over time.

## Requirements

- macOS
- Python 3
- [smartmontools](https://formulae.brew.sh/formula/smartmontools)

```bash
brew install smartmontools
```

## Usage

```bash
git clone https://github.com/nerryc/mac-total-bytes-written.git
cd mac-total-bytes-written
python3 main.py
```

## Example output

```
Data Units Written: 1,234,567 units, which is approximately 12.34 TB
```

## Notes

- Reads from `/dev/disk0` by default — edit `main.py` if your SSD is at a different path
- Uses `smartctl -A` under the hood; requires no root on most Macs but may prompt for permissions on some systems

## License

MIT — see [LICENSE](LICENSE).
