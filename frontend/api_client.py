import requests

BASE_URL = "http://127.0.0.1:8000"


def analyze_resume(file, jd_text):

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

    print("STATUS:", response.status_code)
    print("RAW RESPONSE:")
    print(response.text)

    if response.status_code != 200:
        raise Exception(
            f"Backend Error:\n{response.text}"
        )

    return response.json()