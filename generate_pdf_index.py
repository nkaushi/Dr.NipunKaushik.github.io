import os

# Change this to your folder name
folder = "PSCA_CNN_Framework"

html_start = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{folder} Papers</title>
  <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
</head>
<body class="bg-gray-100 p-6">
  <div class="max-w-4xl mx-auto space-y-4">
    <h2 class="text-2xl font-bold mb-6">{folder} – Papers</h2>
"""

card_template = """
    <div class="bg-white rounded-xl shadow p-6 hover:shadow-lg transition">
      <h4 class="text-lg font-semibold mb-2">{title}</h4>
      <p class="text-gray-600 mb-4">Research paper in {folder} collection.</p>
      <a href="{filename}"
         target="_blank"
         onclick="gtag('event', 'click', {{
           'event_category': 'pdf',
           'event_label': '{folder} - {title}'
         }});"
         class="inline-block px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 transition">
        Read PDF →
      </a>
    </div>
"""

html_end = """
  </div>
</body>
</html>
"""

# Collect all PDFs
pdfs = [f for f in os.listdir(folder) if f.lower().endswith(".pdf")]

cards = ""
for pdf in sorted(pdfs):
    title = os.path.splitext(pdf)[0].replace("-", " ").replace("_", " ")
    cards += card_template.format(title=title, filename=pdf, folder=folder)

html = html_start.format(folder=folder) + cards + html_end

# Write index.html inside the folder
with open(os.path.join(folder, "index.html"), "w", encoding="utf-8") as f:
    f.write(html)

print(f"✅ index.html generated in {folder}/ with {len(pdfs)} PDFs.")
