# Mounting Plate CAD

A browser-based 2D mechanical drawing and Python design utility for a
120 mm x 80 mm mounting plate.

## Overview

This project documents the design of a mechanical mounting plate through an
interactive HTML drawing, a research paper, a presentation, and a small Python
validation tool. It is intended as a semester project reference for students,
design reviewers, and anyone learning how a dimensioned CAD concept can be
translated into a repeatable design workflow.

The browser page focuses on visual communication. It shows the top view,
dimensions, center lines, hole locations, CAD command references, and a short
step-by-step construction guide. The Python module focuses on repeatability:
it stores the same dimensions in a typed data model, calculates derived values,
and checks basic geometric constraints.

## Design Summary

| Property | Value |
| --- | ---: |
| Component | Mechanical mounting plate |
| Overall length | 120 mm |
| Overall width | 80 mm |
| Thickness | 10 mm |
| Hole diameter | 20 mm |
| Hole spacing | 60 mm |
| Hole count | 4 |
| Drawing units | Millimetres |
| Reference CAD filename | `Mounting_Plate_2D.dwg` |

The four holes are arranged symmetrically around the plate center. The Python
utility reports their centers from the lower-left corner, which makes the
layout easier to check before a CAD drawing or manufacturing process is
started.

## Features

- Interactive 2D mounting-plate drawing with selectable visual layers
- Dimension callouts for overall size, hole spacing, and hole diameter
- CAD command reference for rectangle, circle, trim, dimension, and layer work
- Construction sequence suitable for a classroom or design review
- Python validation of positive dimensions and hole-spacing constraints
- JSON output for integrating the design summary with another tool
- Research paper and presentation material for project context

## Project Structure

```
.
├── mounting_plate_cad.html                 # interactive browser demo
├── src/
│   └── mounting_plate.py                   # design calculations and validation
├── assets/                                 # images and diagrams
│   └── .gitkeep
├── docs/
│   ├── Mounting_Plate_CAD_Research_Paper.pdf
│   └── Mounting_Plate_CAD_Presentation.pptx
├── LICENSE
└── README.md
```

## Getting Started

### Browser demo

The HTML page has no third-party dependencies or build step. Open
`mounting_plate_cad.html` directly in a browser, or serve the repository with
Python for a more realistic local web environment:

```bash
git clone https://github.com/mayankswaraj18cr-cmd/Semester--2-Project-.git
cd Semester--2-Project-
python3 -m http.server 8000
```

Open <http://localhost:8000/mounting_plate_cad.html> in a browser.

### Python utility

The Python module uses only the standard library and requires Python 3.9 or
newer. Run the human-readable design summary from the repository root:

```bash
python3 src/mounting_plate.py
```

For machine-readable output:

```bash
python3 src/mounting_plate.py --json
```

The command exits with status `0` when the dimensions pass validation and
status `1` when a design constraint fails. The `MountingPlate` dataclass can
also be imported into another Python script:

```python
from src.mounting_plate import MountingPlate

plate = MountingPlate()
print(plate.hole_centers)
print(plate.validate())
```

## Design Workflow

1. Set the drawing units to millimetres.
2. Draw a 120 mm x 80 mm rectangle for the plate boundary.
3. Establish horizontal and vertical center lines.
4. Locate the four symmetric hole centers using the 60 mm spacing.
5. Draw four circles with a 20 mm diameter.
6. Add dimensions, labels, and construction notes.
7. Run the Python validator to check the design data.
8. Review the drawing and supporting documentation before exporting CAD files.

## CAD Command Reference

| Command | Purpose |
| --- | --- |
| `UNITS` | Set the drawing units to millimetres |
| `RECTANGLE` | Create the plate boundary |
| `CIRCLE` | Create the four mounting holes |
| `TRIM` | Remove unwanted construction geometry |
| `DIMLINEAR` | Add length and width dimensions |
| `DIMDIAMETER` | Add the hole diameter callout |
| `LAYER` | Separate dimensions, center lines, and geometry |

## Validation Scope

The Python utility currently checks that every dimension is positive, the hole
spacing fits within both plate dimensions, and the hole diameter is smaller
than the plate. It calculates the face area, uncut volume, and symmetric hole
centers. It does not replace a manufacturing review, material analysis,
tolerance stack-up, or a full CAD constraint solver.

## Documentation

- [Research Paper](docs/Mounting_Plate_CAD_Research_Paper.pdf) - research and
  background behind the mounting plate design
- [Presentation](docs/Mounting_Plate_CAD_Presentation.pptx) - project overview
  and presentation material

## Development

Keep the dimensions in the HTML drawing and `src/mounting_plate.py` aligned
when the design changes. Before opening a pull request, run the Python utility,
check its JSON output, and inspect the browser page at desktop and mobile
widths.

```bash
python3 src/mounting_plate.py
python3 src/mounting_plate.py --json
git diff --check
```

Suggested branch purposes:

- `main` - stable project history
- `develop` - integration of completed work
- `docs/updates` - documentation and presentation changes
- `feature/python-validation` - Python design tooling
- `feature/cad-assets` - future CAD exports and rendered assets

## Roadmap

- [x] Publish the interactive 2D drawing
- [x] Add research and presentation documentation
- [x] Add a Python dimension validator
- [ ] Add downloadable CAD source files
- [ ] Add rendered project images to `assets/`
- [ ] Add automated tests for alternate plate dimensions
- [ ] Add material and tolerance information

## Contributing

1. Create a feature branch from `develop`.
2. Keep browser dimensions and Python defaults synchronized.
3. Run the documented validation commands.
4. Explain design changes in the pull request description.

## License

MIT - see [LICENSE](LICENSE).

## Contact

Mayank Swaraj - [mayankswaraj18cr@gmail.com](mailto:mayankswaraj18cr@gmail.com)