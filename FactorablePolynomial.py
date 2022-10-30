import AppUtils
from SyntheticDivisionMagicTermResult import SyntheticDivisionMagicTermResult
from SyntheticDivisionResult import SyntheticDivisionResult


class FactorablePolynomial:
    initial_terms_coefficients = []
    initial_degrees = []
    polynomial_degree = 0
    __terms_coefficients = []
    __degrees = []

    factorable_factors = []
    unfactorable_factors = []

    def __init__(
            self,
            terms_coefficients,
            degrees,
            factorable_factors=None,
            unfactorable_factors=None
    ):
        self.initial_terms_coefficients = terms_coefficients
        self.__terms_coefficients = terms_coefficients
        self.initial_degrees = degrees
        self.__degrees = degrees
        self.polynomial_degree = max(degrees)
        if factorable_factors is None: self.factorable_factors = []
        if unfactorable_factors is None:  self.unfactorable_factors = []
        self.factor_polynomial()

    def factor_polynomial(self, terms_coefficients=None, degrees=None, factorable_factors=None):
        if terms_coefficients is None: self.__terms_coefficients = self.initial_terms_coefficients
        if degrees is None: self.__degrees = self.initial_degrees
        if factorable_factors is None: self.factorable_factors = []
        magic_term = self.__get_synthetic_division_magic_term()
        if magic_term.residue == 0:
            self.__degrees = list(filter(AppUtils.greather_than_zero, map(AppUtils.substract_one, self.__degrees)))
            self.__terms_coefficients = magic_term.residues[0:self.__degrees.index(0) + 1]
            self.factorable_factors.extend([
                [self.__terms_coefficients, self.__degrees],
                [[1, -magic_term.magic_term], [1, 0]]
            ])
            if self.__terms_coefficients and max(self.__degrees) > 1:
                self.factor_polynomial(self.__terms_coefficients, self.__degrees, self.factorable_factors)
            else:
                return self.factorable_factors
        else:
            return None

    def get_zeros_by_factorization(self):
        zeros = []
        for factor in self.factorable_factors[-self.polynomial_degree:]:
            zeros.append(-factor[0][1] / factor[0][0])
        return zeros

    def get_zeros(self):
        zeros = []
        if self.factor_polynomial() is None:
            zeros.extend(self.__apply_quadratic_equation())
        zeros.extend(self.get_zeros_by_factorization())
        return zeros

    def __synthetic_division(self, divider_):
        residue = self.__terms_coefficients[0]
        residues = [residue]
        for index in range(1, len(self.__terms_coefficients)):
            num = self.__terms_coefficients[index]
            residue = (residue * divider_) + num
            residues.append(residue)
        return SyntheticDivisionResult(residue, residues)

    def __get_synthetic_division_magic_term(self):
        magic_term = 0
        residue = 0
        residues = []
        for divider in AppUtils.find_dividers(self.__terms_coefficients[-1:][0]):
            synthetic_division_result = self.__synthetic_division(divider)
            residue = synthetic_division_result.residue
            if residue == 0:
                magic_term = divider
                residues = synthetic_division_result.residues
                break
        return SyntheticDivisionMagicTermResult(magic_term, residue, residues)

    def __apply_quadratic_equation(self):
        if len(self.factorable_factors) > 0:
            self.unfactorable_factors.append(self.factorable_factors[0])
            self.factorable_factors.pop(0)
            a = self.__terms_coefficients[0]
            b = self.__terms_coefficients[1]
            c = self.__terms_coefficients[2]
            return AppUtils.get_zeros_from_quadratic_equation(a, b, c)
        else:
            print('Este polinomio no se puede factorizar por división sentética o ecuación cuadrática')
            return None
