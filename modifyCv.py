from docx import Document
from docx.shared import RGBColor
import os


class ModifyCv:
    def __init__(self):
        self.doc = Document("cv/cv.docx")

    def generateCv(self, env):
        name = "cv/" + env["NAME"] + " CV.docx"
        if not os.path.exists(name):
            for paragraph in self.doc.paragraphs:
                if "waos" in paragraph.text:
                    new_text = paragraph.text.replace("waos", "" + env["REPLACED_TEXT"])
                    paragraph.text = new_text
                    for run in paragraph.runs:
                        run.font.color.rgb = RGBColor(255, 255, 255)  # Blanco

            # Guardar el documento modificado
            self.doc.save(name)
