from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

import pandas as pd

class ReportGenerator:

    def __init__(
            self,
            csv_file):

        self.csv_file = csv_file

    def create_report(self):

        df = pd.read_csv(
            self.csv_file
        )

        doc = SimpleDocTemplate(
            "outputs/Vehicle_Report.pdf"
        )

        styles = getSampleStyleSheet()

        elements = []

        elements.append(
            Paragraph(
                "Vehicle Tracking Report",
                styles["Title"]
            )
        )

        elements.append(
            Spacer(1,20)
        )

        elements.append(
            Paragraph(
                f"Total Records: {len(df)}",
                styles["BodyText"]
            )
        )

        elements.append(
            Paragraph(
                f"Average Speed: {df['Speed'].mean():.2f}",
                styles["BodyText"]
            )
        )

        elements.append(
            Paragraph(
                f"Maximum Speed: {df['Speed'].max()}",
                styles["BodyText"]
            )
        )

        thefts = len(
            df[
                df["Status"]
                ==
                "THEFT"
            ]
        )

        elements.append(
            Paragraph(
                f"Theft Alerts: {thefts}",
                styles["BodyText"]
            )
        )

        doc.build(elements)

        print(
            "PDF Report Generated"
        )