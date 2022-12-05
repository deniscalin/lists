def parse(feet_inches_local):
    values = feet_inches_local.split(" ")
    feet = float(values[0])
    inches = float(values[1])
    return {"feet": feet, "inches": inches}