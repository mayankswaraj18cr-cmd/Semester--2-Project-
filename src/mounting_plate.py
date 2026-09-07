"""Validate and summarize the mounting plate design."""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class MountingPlate:
    """Dimensions for the mounting plate, expressed in millimetres."""

    length: float = 120.0
    width: float = 80.0
    thickness: float = 10.0
    hole_diameter: float = 20.0
    hole_spacing: float = 60.0

    @property
    def area(self) -> float:
        """Return the plate face area in square millimetres."""
        return self.length * self.width

    @property
    def volume(self) -> float:
        """Return the uncut plate volume in cubic millimetres."""
        return self.area * self.thickness

    @property
    def hole_centers(self) -> tuple[tuple[float, float], ...]:
        """Return the four symmetric hole centers from the lower-left corner."""
        x_offset = (self.length - self.hole_spacing) / 2
        y_offset = (self.width - self.hole_spacing) / 2
        return (
            (x_offset, y_offset),
            (x_offset + self.hole_spacing, y_offset),
            (x_offset, y_offset + self.hole_spacing),
            (x_offset + self.hole_spacing, y_offset + self.hole_spacing),
        )

    def validate(self) -> list[str]:
        """Return design constraint errors, or an empty list when valid."""
        errors: list[str] = []
        dimensions = {
            "length": self.length,
            "width": self.width,
            "thickness": self.thickness,
            "hole_diameter": self.hole_diameter,
            "hole_spacing": self.hole_spacing,
        }
        for name, value in dimensions.items():
            if value <= 0:
                errors.append(f"{name} must be greater than zero")

        if self.hole_spacing > self.length or self.hole_spacing > self.width:
            errors.append("hole_spacing must fit within both plate dimensions")
        if self.hole_diameter >= min(self.length, self.width):
            errors.append("hole_diameter must be smaller than the plate dimensions")
        return errors

    def summary(self) -> dict[str, object]:
        """Return a serializable summary for scripts and design reviews."""
        errors = self.validate()
        return {
            **asdict(self),
            "area_mm2": self.area,
            "volume_mm3": self.volume,
            "hole_centers_mm": self.hole_centers,
            "valid": not errors,
            "errors": errors,
        }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--json", action="store_true", help="print the design summary as JSON"
    )
    arguments = parser.parse_args()
    plate = MountingPlate()
    result = plate.summary()

    if arguments.json:
        print(json.dumps(result, indent=2))
    else:
        print("Mounting Plate Design")
        print(f"Dimensions: {plate.length:g} x {plate.width:g} x {plate.thickness:g} mm")
        print(f"Hole diameter: {plate.hole_diameter:g} mm")
        print(f"Hole spacing: {plate.hole_spacing:g} mm")
        print(f"Face area: {plate.area:g} mm^2")
        print(f"Uncut volume: {plate.volume:g} mm^3")
        print(f"Validation: {'PASS' if result['valid'] else 'FAIL'}")

    if result["errors"]:
        for error in result["errors"]:
            print(f"Error: {error}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())