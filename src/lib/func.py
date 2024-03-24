def iterate(subtotal):
    total = 0 
    string = str(subtotal)
    print(f"Number: {subtotal}")
    for element in range(0, len(string)):
        #@print(string[element])
        total += int(string[element])
    if total > 21:
        iterate(total)
    else:
        return total