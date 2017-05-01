import pybel


def get_atoms(smile):
    molecule = pybel.readstring('smi', smile)
    molecule.make3D()
    return molecule.atoms

if __name__=="__main__":
    # SMILE - simplified molecular-input line-entry system
    smile = input("Enter molecule in SMILE format (e.g., Glucose -> OC[C@H]1OC(O)[C@H](O)[C@@H](O)[C@@H]1O:")
    print(get_atoms(smile))
    
