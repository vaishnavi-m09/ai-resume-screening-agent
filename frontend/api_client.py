import requests

BASE_URL = "http://127.0.0.1:8000"


def analyze_resume(
    file,
    jd_text
):

    files = {
        "file": file
    }

    data = {
        "jd_text": jd_text
    }

    response = requests.post(
        f"{BASE_URL}/analyze_resume",
        files=files,
        data=data
    )

    return response.json()