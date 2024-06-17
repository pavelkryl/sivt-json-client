from typing import Any


class Student: 
    vek: int
    aktivni: bool

def vypis_studenta(student: dict[str,Any]) -> None:
    print(str(student))


def student_ma_narozeniny(student: dict[str,Any]) -> None:
    # zvetsi vek studenta o 1, se vsemi proveditelnymi kontrolami
    ...


new_student = {
    "id": 11,
    "aktivni": True,
    "jmeno": "Alois",
    "obor": "Literatura",
    "vek": 19
}

vypis_studenta(new_student)

student_ma_narozeniny(new_student)

vypis_studenta(new_student)

requests.post("", json=new_student)