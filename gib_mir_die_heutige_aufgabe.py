from datetime import date
from argparse import ArgumentParser

def hole_aktuellen_tag_im_advent() -> int:
    heute = date.today()
    if heute.month != 12:
        raise ValueError("Advent ist nur im Dezember")
    if heute.day > 24:
        raise ValueError("Advent geht nur bis 24. Dezember")
    return heute.day


def aktualisiere_problem_tag(tag: int) -> None:
    print("Aktualisiere auf Tag {}".format(tag))
    # Neue Datein: tag{tag}, tag{tag-1}_loesung und test_tag{tag} und evtl mehr
    # Geaendert: in test_tag{tag-1} wird aus tag{tag-1} -> tag{tag-1}_loesung
    raise NotImplementedError("Das fehlt noch...")


def _verarbeite_kommandozeilenparameter() -> int:
    parser = ArgumentParser("Aktualisiere auf die Aufgabe von einem bestimmten Tag.")
    parser.add_argument("--tag",
                        type=int,
                        help="Wähle diesen Tag im Advent",
                        default=None,
                        )
    args = parser.parse_args()

    if args.tag is None:
        tag = hole_aktuellen_tag_im_advent()
    else:
        tag = args.tag

    return tag


if __name__ == "__main__":
    try:
        tag = _verarbeite_kommandozeilenparameter()
        aktualisiere_problem_tag(tag)
    except ValueError:
        print("Sicher, dass es grade Advent ist?")
        print("Lass das Programm mit --help laufen, um mehr zu sehen.")
