from SyntheticDivisionResult import SyntheticDivisionResult


class SyntheticDivisionMagicTermResult(SyntheticDivisionResult):
    magic_term = 0

    def __init__(self, magic_term, residue, residues):
        super(SyntheticDivisionMagicTermResult, self).__init__(residue, residues)
        self.magic_term = magic_term