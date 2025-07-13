from models.sources_enum import SourceEnum
FIELD_MAP = {
    SourceEnum.PUBCHEM : {"IUPACName": "name",
                          "MolecularFormula": "formula",
                           "MolecularWeight":"MolecularWeight",
                          "CID": "ID",
                        "searchScore": "searchScore",
                        "entityStar":"entityStar"},
    SourceEnum.CHEBI : {"chebiAsciiName": "name",
                        "MolecularFormula": "formula",
                        "MolecularWeight":"MolecularWeight",
                        "chebiId": "ID",
                        "searchScore": "searchScore",
                        "entityStar":"entityStar"}
}
