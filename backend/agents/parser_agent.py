import os
from backend.utils.pdf_utils import (
    extract_pdf_text
)

from backend.utils.docx_utils import (
    extract_docx_text
)


class ParserAgent:

    def parse(
        self,
        file_path
    ):

        if not os.path.exists(file_path):
            return ""

        try:
            if file_path.endswith(".pdf"):
                return extract_pdf_text(file_path)

            elif file_path.endswith(".docx"):
                return extract_docx_text(file_path)

            return ""

        except Exception as e:
            print(f"Error parsing {file_path}: {e}")
            return ""