# REEDR: Ready-made, Easy Echocardiogram Data for Research

REEDR is a Python-based tool designed to simplify the collection and processing of echocardiogram data for research purposes. It extracts demographic and echocardiographic data from RTF files and organizes them into a structured Pandas DataFrame.

## Features
- Extracts patient demographics and echocardiographic measurements from RTF files.
- Parses interpretation summaries for key cardiac assessments.
- Supports data from LABHIST and PHILIPS contributor systems.
- Outputs data in a structured, sorted DataFrame for easy analysis.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mbrockman1/REEDR.git
   cd REEDR
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Place your echocardiogram RTF files in the `./echos/` directory.
2. Run the main script or Jupyter notebook:
   ```bash
   python REEDR.py
   ```
   OR
   ```bash
   jupyter notebook REEDR.ipynb
   ```
3. The script will process the RTF files and output a Pandas DataFrame (`df`) containing the extracted data, indexed by Medical Record Number (MRN).

## Data Output
The output DataFrame includes:
- **Demographic Data**: Name, MRN, DOB, Gender, Age, Height, Weight, BSA, Study Date, Location, etc.
- **Echocardiographic Measurements**: Over 100 parameters like LA volume, MV E/A, EF, RVSP, etc.
- **Interpretation Summaries**: Parsed assessments for wall motion, valves, pericardial effusion, and more.

## License

REEDR is licensed under the GNU General Public License v3.0. You are free to use, modify, and distribute this software, provided that any derivative works are also licensed under the GPL v3.0. See the [LICENSE](LICENSE) file for full details.

Key points:
- You must include the copyright notice and license in all copies or substantial portions of the software.
- Modified versions must be marked as changed and carry the same license.
- No warranty is provided; the software is distributed "AS IS."

## Citation

If you use REEDR in your research, please cite it as follows:

```bibtex
@software{Brockman_REEDR_2024,
  author = {Brockman, Michael},
  title = {Ready-made, Easy Echocardiogram Data for Research (REEDR)},
  version = {0.0.1},
  date = {2024-05-27},
  url = {https://github.com/mbrockman1/REEDR},
  orcid = {0000-0001-9707-1531}
}
```

## Dependencies

See `requirements.txt` for a complete list of dependencies. Key libraries include:
- `pandas`
- `striprtf`
- `numpy`
- `re`

## Contributing

Contributions are welcome! Please submit a pull request or open an issue on the GitHub repository.

## Contact

For questions or support, contact Michael Brockman via GitHub or the contact information provided in the [CITATION.cff](CITATION.cff) file.
