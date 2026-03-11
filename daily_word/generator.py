import urllib.request
import json
import datetime

def fetch_quote():
    url = "https://zenquotes.io/api/random"
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read())[0]
    return data["q"], data["a"]

def generate_html(quote, author):
    date = datetime.date.today().strftime("%B %d, %Y")
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Daily Word</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;1,400&family=Inter:wght@300;400&display=swap');
    body {{ font-family: 'Inter', sans-serif; }}
    .quote-font {{ font-family: 'Playfair Display', serif; }}
  </style>
</head>
<body class="min-h-screen bg-gradient-to-br from-amber-50 via-orange-50 to-rose-50 flex flex-col items-center justify-center px-6">
  <main class="max-w-2xl w-full text-center space-y-10">

    <div class="inline-block bg-orange-400 text-white text-xs tracking-[0.3em] uppercase px-4 py-1.5 rounded-full">
      Daily Word
    </div>

    <blockquote class="quote-font italic text-3xl md:text-4xl leading-relaxed text-stone-800">
      &ldquo;{quote}&rdquo;
    </blockquote>

    <div class="flex items-center justify-center gap-4">
      <span class="block h-px w-10 bg-orange-300"></span>
      <p class="text-sm tracking-widest uppercase text-orange-500 font-medium">{author}</p>
      <span class="block h-px w-10 bg-orange-300"></span>
    </div>

  </main>

  <footer class="absolute bottom-8 text-xs tracking-widest uppercase text-stone-400">
    {date}
  </footer>
</body>
</html>"""
    return html

if __name__ == "__main__":
    print("Fetching quote...")
    quote, author = fetch_quote()
    print(f'"{quote}" — {author}')

    html = generate_html(quote, author)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)

    print("Generated index.html")
