low = 0
high = 100

def water_state(temperature):
    if low < temperature < high:
        state_local = "Liquid"
    elif temperature <= low:
        state_local = "Solid"
    else:
        state_local = "Gas"
    return state_local

