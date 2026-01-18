def validate_pin(pin):
    if pin.isdigit() and len(pin) in (4, 6):
        return True
    return False

if __name__ == "__main__":
    if validate_pin("1234"):
        print("Valid PIN")
    else:
        print("Invalid PIN")