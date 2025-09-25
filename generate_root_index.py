import os

root = "."  # root of your repo
output_file = os.path.join(root, "index.html")

html_start = """<!DOCTYPE html>
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

card_template = """
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

html_end = """
    </div>
  </div>
</body>
</html>
"""

# Optional: you can define custom descriptions per folder
folder_descriptions = {
    "PSCA_CNN_Framework": "Papers and documentation on CNN-based PSCA detection framework.",
    "Folder2": "Description for Folder 2",
    "Folder3": "Description for Folder 3",
    "Folder4": "Description for Folder 4",
}

# Scan top-level folders
folders = [f for f in os.listdir(root) if os.path.isdir(os.path.join(root, f)) and not f.startswith(".")]

cards = ""
for folder in sorted(folders):
    desc = folder_descriptions.get(folder, "Research papers in this collection.")
    cards += card_template.format(folder=folder, description=desc)

# Combine HTML
html = html_start + cards + html_end

# Write root index.html
with open(output_file, "w", encoding="utf-8") as f:
    f.write(html)

print(f"✅ Root index.html generated with {len(folders)} folder cards.")
