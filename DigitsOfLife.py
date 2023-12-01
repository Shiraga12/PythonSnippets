def digitsoflife_Date(_Month, _Day, _Year):
    A = []
    B = []
    C = []
    TOTAL = 0

    # Convert each input to a list of digits
    A = [int(digit) for digit in str(_Month)]
    B = [int(digit) for digit in str(_Day)]
    C = [int(digit) for digit in str(_Year)]

    # Sum the digits in each list
    TOTAL += sum(A)
    TOTAL += sum(B)
    TOTAL += sum(C)

    return TOTAL
def digitsoflife(_Digits):
    A = []
    TOTAL = 0

    # Convert each input to a list of digits
    A = [int(digit) for digit in str(_Digits)]

    # Sum the digits in each list
    TOTAL += sum(A)

    return TOTAL
