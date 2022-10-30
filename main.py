from FactorablePolynomial import FactorablePolynomial

if __name__ == '__main__':

    factorable_polynomial = FactorablePolynomial([1, -6, 13, -10], [3, 2, 1, 0])
    print(factorable_polynomial.get_zeros())

    factorable_polynomial_2 = FactorablePolynomial([1, 9, 27, 35], [3, 2, 1, 0])
    print(factorable_polynomial_2.get_zeros())

    factorable_polynomial_2 = FactorablePolynomial([1, -1, -2], [7, 6, 5])
    print(factorable_polynomial_2.get_zeros())

    factorable_polynomial = FactorablePolynomial([1, -1, -2], [2, 1, 0])
    print(factorable_polynomial.get_zeros())

    factorable_polynomial_2 = FactorablePolynomial([2, -1, -2], [7, 6, 5])
    print(factorable_polynomial_2.get_zeros())

    factorable_polynomial_2 = FactorablePolynomial([2, -1, -2], [2, 1, 0])
    print(factorable_polynomial_2.get_zeros())
