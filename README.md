# Explore Close Approaches of Near-Earth Objects

This project is used to search for and explore close approaches of near-Earth objects (NEOs), using data from NASA/JPL's Center for Near-Earth Object Studies.

### Data  
The data used to complete this project can be found under the `/data` folder.

- Small-Bodies Dataset (`neos.csv`) - A subset of small bodies are near-Earth objects (NEOs):
"comets and asteroids that have been nudged by the gravitational attraction of nearby planets into orbits that allow them to enter the Earth's neighborhood."


- Close Approach Dataset(`cad.json`) : A close approach occurs when a NEO's orbit path brings it near Earth. 
From this dataset, you can answer questions such as "On which date(s) does Halley's Comet pass near to Earth?" or "How fast does Eros pass by Earth, on average?"

### Filters
- Date (--date, --start-date, --end-date)
- Distance (--min-distance, --max-distance)
- Velocity (--min-velocity, --max-velocity)
- Diameter (--min-diameter, --max-diameter)
- Hazardous (--hazardous, --not-hazardous)

### Sample Usage
```
# Query for close approaches on 2020-01-01
$ python3 main.py query --date 2020-01-01

# Query for close approaches in 2020 with a velocity of <=50 km/s.
$ python3 main.py query --start-date 2020-01-01 --end-date 2020-12-31 --max-velocity 50

# Multiple filters
$ python3 main.py query --max-distance 0.1 --min-velocity 35 --min-diameter 2.5 --hazardous

# Save (the first) five close approaches on 2020-01-01 to a CSV file.
$ python3 main.py query --date 2020-01-01 --limit 5 --outfile results.csv

# Save (the first) five close approaches on 2020-01-01 to a JSON file.
$ python3 main.py query --date 2020-01-01 --limit 5 --outfile results.json
```

### Unit test
All tests are located in the `/tests` folder
Run `python3 -m unittest` to run all unit tests  