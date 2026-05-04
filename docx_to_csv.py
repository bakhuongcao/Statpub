import csv
from docx import Document

docx_path = r"D:\bakhuongcao\Statpub\VN_map\Health faclities\Co-so-KCB-ban-dau-2026.docx"
csv_path  = r"D:\bakhuongcao\Statpub\VN_map\Health faclities\Co-so-KCB-ban-dau-2026.csv"

doc = Document(docx_path)

with open(csv_path, "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    for table in doc.tables:
        for row in table.rows:
            writer.writerow([cell.text.strip() for cell in row.cells])
        writer.writerow([])  # blank line between tables

print(f"Done! CSV saved to: {csv_path}")
