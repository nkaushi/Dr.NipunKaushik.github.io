import os

root = "."  # Root of your site repo

# ------------------------ Folder page templates ------------------------
folder_html_start = """<!DOCTYPE html>
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

folder_card_template = """
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

folder_html_end = """
  </div>
</body>
</html>
"""

# ------------------------ Root page templates ------------------------
root_html_start = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>My Publications</title>
  <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
</head>
<body class="bg-gray-100 p-6">
  <div class="max-w-6xl mx-auto">
    <h1 class="text-3xl font-bold mb-8">Publications & Projects</h1>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
"""

root_card_template = """
      <div class="bg-white rounded-xl shadow-md p-6 hover:shadow-xl transition">
        <h4 class="text-lg font-semibold mb-2">{folder}</h4>
        <p class="text-gray-600 mb-4">{description}</p>
        <a href="{folder}/"
           onclick="gtag('event', 'click', {{
             'event_category': 'folder',
             'event_label': '{folder}'
           }});"
           class="inline-block px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition">
          View Papers →
        </a>
      </div>
"""

root_html_end = """
    </div>
  </div>
</body>
</html>
"""

# Optional: custom folder descriptions
folder_descriptions = {
    "PSCA_CNN_Framework": "Papers and documentation on CNN-based PSCA detection framework.",
    # Add more folders descriptions here
}

# ------------------------ Process folders ------------------------
folders = [f for f in os.listdir(root) if os.path.isdir(os.path.join(root, f)) and not f.startswith(".")]

root_cards = ""

for folder in sorted(folders):
    folder_path = os.path.join(root, folder)
    pdfs = [f for f in os.listdir(folder_path) if f.lower().endswith(".pdf")]
    
    if not pdfs:
        print(f"⚠️ No PDFs found in {folder}, skipping folder page.")
        continue

    # Generate folder index.html
    folder_cards = ""
    for pdf in sorted(pdfs):
        title = os.path.splitext(pdf)[0].replace("-", " ").replace("_", " ")
        folder_cards += folder_card_template.format(title=title, filename=pdf, folder=folder)

    folder_html = folder_html_start.format(folder=folder) + folder_cards + folder_html_end
    with open(os.path.join(folder_path, "index.html"), "w", encoding="utf-8") as f:
        f.write(folder_html)
    print(f"✅ Folder index.html generated for {folder} with {len(pdfs)} PDFs.")

    # Add folder to root page
    description = folder_descriptions.get(folder, "Research papers in this collection.")
    root_cards += root_card_template.format(folder=folder, description=description)

# Generate root index.html
root_html = root_html_start + root_cards + root_html_end
with open(os.path.join(root, "index.html"), "w", encoding="utf-8") as f:
    f.write(root_html)
print(f"✅ Root index.html generated with {len(folders)} folder cards.")
