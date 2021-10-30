"""Demonstrating dictionary capabilities."""


# Declaring the type of a dictionary
schools: dict[str, int]

# Initialize to an empty dictionary
schools = dict()

# Set a key-value pairing in the dictionary
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26500

# Print dictionary literal representation
print(schools)

# Access a value by its key - "lookup"
print(schools["UNC"])

# Remove key-value pair from dictionary
# By its key
schools.pop("Duke")

# Test for the existence of a key
is_duke_present: bool = "Duke" in schools

# Reassign a key-value pair
schools["UNC"] = 20000
schools["NCSU"] += 200