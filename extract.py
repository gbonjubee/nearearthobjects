"""Extract data on NEO and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the
command line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about
    near-Earth objects. :return: A collection of `NearEarthObject`s.
    """
    with open(neo_csv_path, 'r') as infile:
        reader = csv.DictReader(infile, skipinitialspace=True)
        neo_obj = []
        for elem in reader:
            neo = NearEarthObject(elem["pdes"], elem["name"], elem["diameter"],
                                  True if (elem["pha"] and elem["pha"] == "Y")
                                  else False)
            neo_obj.append(neo)
    return neo_obj


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close
    approaches. :return: A collection of `CloseApproach`es.
    """
    approaches = []
    with open(cad_json_path, 'r') as infile:
        cad_obj = json.load(infile)
        data = cad_obj["data"]
        for value in data:
            time = value[3]
            distance = value[4]
            velocity = value[7]
            designation = value[0]

            approach = CloseApproach(time, distance, velocity)
            approach._designation = designation
            approaches.append(approach)
    return approaches
