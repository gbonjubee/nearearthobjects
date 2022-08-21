"""Represent models for near-Earth objects and their close approaches.

The `NearEarthObject` class represents a near-Earth object. Each has a unique
primary designation, an optional unique name, an optional diameter, and a flag
for whether the object is potentially hazardous.

The `CloseApproach` class represents a close approach to Earth by an NEO. Each
has an approach datetime, a nominal approach distance, and a relative approach
velocity.

A `NearEarthObject` maintains a collection of its close approaches, and a
`CloseApproach` maintains a reference to its NEO.

The functions that construct these objects use information extracted from the
data files from NASA, so these objects should be able to handle all of the
quirks of the data set, such as missing names and unknown diameters.

You'll edit this file in Task 1.
"""
from helpers import cd_to_datetime, datetime_to_str


class NearEarthObject:
    """A near-Earth object (NEO).

    An NEO encapsulates semantic and physical parameters about the object, such
    as its primary designation (required, unique), IAU name (optional), diameter
    in kilometers (optional - sometimes unknown), and whether it's marked as
    potentially hazardous to Earth.

    A `NearEarthObject` also maintains a collection of its close approaches -
    initialized to an empty collection, but eventually populated in the
    `NEODatabase` constructor.
    """
    # If you make changes, be sure to update the comments in this file.
    def __init__(self, designation, name, diameter, hazardous, **info):
        """Create a new `NearEarthObject`.

        :param info: A dictionary of excess keyword arguments supplied to the constructor.
        """
        # onto attributes named `designation`, `name`, `diameter`, and `hazardous`.
        # You should coerce these values to their appropriate data type and
        # handle any edge cases, such as a empty name being represented by `None`
        # and a missing diameter being represented by `float('nan')`.
        self.designation = designation if designation else ''
        self.name = name if name else None
        self.diameter = float(diameter if diameter else float('nan'))
        self.hazardous = bool(hazardous if hazardous else False)
        for key,value in info.items():
            self.key = value

        # Create an empty initial collection of linked approaches.
        self.approaches =  []

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""
        return f"{self.designation}({self.name})" if (f"{self.name}" and f"{self.name}"!= "None") else f"{self.designation}"

    def __str__(self):
        """Return `str(self)`."""
        # The project instructions include one possibility. Peek at the __repr__
        # method for examples of advanced string formatting.
        return f" NEO {self.fullname} has a diameter of {self.diameter:.3f} km and "  +  (f"is" if (self.hazardous and self.hazardous =="Y") else f"is not") + f" potentially hazardous."

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return (f"NearEarthObject(designation={self.designation!r}, name={self.name!r}, "
                f"diameter={self.diameter:.2f}, hazardous={self.hazardous!r})")

    def to_json(self):
        return {
            "designation": self.designation,
            "name": self.name,
            "diameter_km":self.diameter,
            "potentially_hazardous": self.hazardous
        }

class CloseApproach:
    """A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about the NEO's close approach to
    Earth, such as the date and time (in UTC) of closest approach, the nominal
    approach distance in astronomical units, and the relative approach velocity
    in kilometers per second.

    A `CloseApproach` also maintains a reference to its `NearEarthObject` -
    initally, this information (the NEO's primary designation) is saved in a
    private attribute, but the referenced NEO is eventually replaced in the
    `NEODatabase` constructor.
    """
    # If you make changes, be sure to update the comments in this file.
    def __init__(self, time, distance, velocity, neo = None, **info):
        """Create a new `CloseApproach`.

        :param info: A dictionary of excess keyword arguments supplied to the constructor.
        """
        # onto attributes named `_designation`, `time`, `distance`, and `velocity`.
        # You should coerce these values to their appropriate data type and handle any edge cases.
        # The `cd_to_datetime` function will be useful.
        self._designation = '' if neo is None else neo.designation
        self.time = cd_to_datetime(time) if time else None
        self.distance = float(distance if distance else 0.0)
        self.velocity = float( velocity if velocity else 0.0)
        for key,value in info.items():
            self.key = value

        # Create an attribute for the referenced NEO, originally None.
        self.neo = neo


    @property
    def time_str(self):
        """Return a formatted representation of this `CloseApproach`'s approach time.

        The value in `self.time` should be a Python `datetime` object. While a
        `datetime` object has a string representation, the default representation
        includes seconds - significant figures that don't exist in our input
        data set.

        The `datetime_to_str` method converts a `datetime` object to a
        formatted string that can be used in human-readable representations and
        in serialization to CSV and JSON files.
        """
        # build a formatted representation of the approach time.
        return datetime_to_str(self.time)

    def __str__(self):
        """Return `str(self)`."""
        # The project instructions include one possibility. Peek at the __repr__
        # method for examples of advanced string formatting.
        return f"At {self.time_str!r}, {self.neo!r} approaches Earth at a distance of {self.distance:.2f} au and a velocity of {self.velocity:.2f} km/s."

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return (f"CloseApproach(time={self.time_str!r}, distance={self.distance:.2f}, "
                f"velocity={self.velocity:.2f}, neo={self.neo!r})")

    def to_json(self):
        """
        Formats CloseApproach to a dictionary mapping the keys 'datetime_utc', 'distance_au', 'velocity_km_s' to the associated values on the CloseApproach object
        and the key neo to a dictionary mapping the keys 'designation', 'name', 'diameter_km', 'potentially_hazardous'
        to the associated values on the close approach's NEO.

        :return: A JSON formatted value of CloseApproach object.
        """
        return {
            "datetime_utc": self.time_str,
            "distance_au":self.distance,
            "velocity_km_s": self.velocity,
            "neo": self.neo.to_json()
        }

    def to_csv(self):
        """
        The header columns are : 'datetime_utc', 'distance_au', 'velocity_km_s', 'designation', 'name', 'diameter_km', 'potentially_hazardous'
        - A missing name is represented as empty string
        - A missing diameter is represented as the string 'nan'.
        - The potentially_hazardous flag is represented the string 'False' or 'True'.
        """
        return {
            "datetime_utc": self.time_str,
            "distance_au": self.distance,
            "velocity_km_s": self.velocity,
            "designation": self.neo.designation,
            "name": self.neo.name,
            "diameter_km": self.neo.diameter,
            "potentially_hazardous": self.neo.hazardous
        }


