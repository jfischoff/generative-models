bank_state = "none"

def set_bank_state(value):
    global bank_state
    bank_state = value

def get_bank_state():
    global bank_state
    return bank_state