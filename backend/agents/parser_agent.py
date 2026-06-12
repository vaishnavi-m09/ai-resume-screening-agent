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

        if file_path.endswith(".pdf"):
            return extract_pdf_text(file_path)

        elif file_path.endswith(".docx"):
            return extract_docx_text(file_path)

        raise ValueError(
            "Unsupported file format"
        )