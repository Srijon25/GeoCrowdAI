
# GeoCrowdAI

**GeoCrowdAI** is a modular, open-source Python package designed for real-time crowdsourced geospatial intelligence. It extracts and visualizes location-based insights from live or batch natural language streams such as tweets, messages, or reports.

## Features

- Real-time text stream processing
- NLP-based location extraction using Named Entity Recognition (NER)
- Custom keyword filtering for specific event detection (e.g., disaster alerts)
- Interactive map visualization with dynamic data overlay
- Clean modular design for easy extension and research use
- CLI and scriptable API support

## Installation

To install GeoCrowdAI:

```bash
git clone https://github.com/Srijon25/GeoCrowdAI.git
cd GeoCrowdAI
pip install -r requirements.txt
python setup.py install

Quick Start

from geocrowdai.stream import StreamProcessor

processor = StreamProcessor(
    keywords=["earthquake", "fire", "flood"],
    language="en"
)
processor.listen()

This starts the processor, filters for specific keywords, extracts locations, and visualizes results on a map.

Use Cases

Disaster detection: Earthquakes, floods, wildfires

Epidemiological surveillance: Disease outbreak mentions

Civic alerts: Protests, emergencies, public safety

Smart cities: Real-time citizen reports


Repository Structure

GeoCrowdAI/
├── geocrowdai/          # Main source code
├── tests/               # Unit tests
├── examples/            # Example scripts
├── docs/                # Documentation
├── paper.md             # JOSS paper
├── CITATION.cff         # Citation file
├── README.md            # Project overview
├── setup.py             # Package setup
└── requirements.txt     # Dependencies

Citation

If you use this software in your research, please cite:

@software{shill2025geocrowdai,
  author       = {Srijon Kumar Shill},
  title        = {{GeoCrowdAI: A Modular Open-Source Platform for Real-Time Crowdsourced Geospatial Intelligence}},
  year         = 2025,
  publisher    = {Zenodo},
  version      = {1.0.0},
  doi          = {10.5281/zenodo.15499120}
}

Author

Srijon Kumar Shill
Independent Researcher
ORCID: 0009-0004-8924-2272
Email: theunpredictable157@gmail.com


License

This project is licensed under the MIT License.

DOI and Archival

Zenodo DOI: https://doi.org/10.5281/zenodo.15499120
