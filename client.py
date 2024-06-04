from typing import Any, Optional
from requests import Response
import requests
import logging

logger = logging.getLogger(__name__)

class Klient:

    def __init__(self, server_url: str) -> None:
        self._server_url = server_url

    def get_student(self, student_id: int) -> Optional[dict[str,Any]]:
        url = self._build_url("/students", student_id)
        response = requests.get(url)
        return self._handle_json_object_response(response)

    def get_students(self) -> Optional[list[dict[str,Any]]]:
        url = self._build_url("/students")
        response = requests.get(url)
        if response.status_code == 200:
            return response.json() # type:ignore
        else:
            self._log_request_failed(response)
            return None

    def remove_student(self, student_id: int) -> Optional[dict[str,Any]]:
        url = self._build_url("/students", student_id)
        response = requests.delete(url)
        return self._handle_json_object_response(response)

    def create_student(self, student: dict[str,Any]) -> Optional[dict[str,Any]]:
        url = self._build_url("/students")
        response = requests.post(url, json=student)
        return self._handle_json_object_response(response, 201)

    def _handle_json_object_response(self, response: Response, expect_status_code: int = 200) -> Optional[dict[str, Any]]:
        if response.status_code == expect_status_code:
            return response.json() # type:ignore
        else:
            self._log_request_failed(response)
            return None

    def _log_request_failed(self, response: Response) -> None:
        raw_data = str(response.text)
        logger.warning(f"request failed: {response.status_code}: {raw_data}")

    def _build_url(self, path: str, suffix: Optional[Any] = None) -> str:
        """Helper routine to build server URL

        :param path: path behind the base server_url
        :param suffix: optional suffix, defaults to None
        :return: built url
        """
        if suffix is not None:
            return self._server_url + path + "/" + str(suffix)
        else:
            return self._server_url + path


klient = Klient("http://localhost:5000")
students = klient.get_students()
print(students)

new_student = {
    "id": 11,
    "aktivni": True,
    "jmeno": "Alois",
    "obor": "Literatura",
    "vek": 19
}

resp = klient.create_student(new_student)
print(f"odpoved na create_student: {resp}")

students = klient.get_students()
print(students)

resp = klient.remove_student(19)
print(f"odpoved na remove_student: {resp}")

