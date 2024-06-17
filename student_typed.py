from dataclasses import dataclass
from typing import Any

from pydantic import BaseModel

class Student(BaseModel):
    id: int
    vek: int
    aktivni: bool
    jmeno: str
    obor: str
    

def student_ma_narozeniny(student: Student) -> None:
    # zvetsi vek studenta o 1, se vsemi moznymi kontrolami
    ...

def vypis_studenta(student: Student) -> None:
    print(str(student))

def vypis_studenta_json(student: dict[str,Any]) -> None:
    print(str(student))

new_student_json = {
    "id": 11,
    "vek": 19,
    "aktivni": True,
    "jmeno": "Alois",
    "obor": "Literatura",
}
# jak z tohoto objektu/JSONu dostat instanci Student

new_student = Student(id=11, vek=19, aktivni=True, jmeno="Alois", obor="Literatura")

vypis_studenta(new_student)
student_ma_narozeniny(new_student)
vypis_studenta(new_student)

# jak z new_student dostat instanci JSON/dict?