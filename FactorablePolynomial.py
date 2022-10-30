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
            possible_factorable_factors=None,
            possible_unfactorable_factors=None
    ):
        self.initial_terms_coefficients = terms_coefficients
        self.__terms_coefficients = terms_coefficients
        self.initial_degrees = degrees
        self.__degrees = degrees
        self.polynomial_degree = max(degrees)
        if possible_factorable_factors is None: self.factorable_factors = []
        if possible_unfactorable_factors is None:  self.unfactorable_factors = []

    def factor_polynomial(self, terms_coefficients=None, degrees=None, possible_factorable_factors=None):
        if terms_coefficients is None: self.__terms_coefficients = self.initial_terms_coefficients
        if degrees is None: self.__degrees = self.initial_degrees
        if possible_factorable_factors is None: self.factorable_factors = []
        last_degree = self.__degrees[-1:][0]
        if last_degree != 0:
            self.__degrees = list(map(lambda n: AppUtils.substract(n, last_degree), self.__degrees))
            self.factorable_factors.extend([[[1, 0], [1, 0]]])
        magic_term = self.__get_synthetic_division_magic_term()
        if magic_term.residue == 0:
            self.__degrees = list(
                filter(
                    AppUtils.greather_or_equal_than_zero,
                    map(
                        lambda n: AppUtils.substract(n, 1),
                        self.__degrees)
                )
            )
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
            unfactorable_factor = [self.__terms_coefficients, self.__degrees]
            self.unfactorable_factors.extend(unfactorable_factor)
            if unfactorable_factor in self.factorable_factors:
                self.factorable_factors.remove(unfactorable_factor)
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

    def get_factors(self):
        factors = []
        for factor in self.factorable_factors:
            factors.append(factor)
        for factor in self.unfactorable_factors:
            factors.append(factor)
        return factors

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
        a = self.__terms_coefficients[0]
        b = self.__terms_coefficients[1]
        c = self.__terms_coefficients[2]
        return AppUtils.get_zeros_from_quadratic_equation(a, b, c)
