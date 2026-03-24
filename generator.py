import urllib.request
import json
import datetime

def fetch_quote():
    url = "https://zenquotes.io/api/random"
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read())[0]
    return data["q"], data["a"]

def get_bg_image_url():
    today = datetime.date.today()
    seed = today.strftime("%Y%m%d")
    # Picsum: grayscale cinematic photo, seeded by date so same image all day
    return f"https://picsum.photos/seed/{seed}/1920/1080?grayscale"

def generate_html(quote, author):
    date = datetime.date.today().strftime("%B %d, %Y")
    bg_url = get_bg_image_url()
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
    .bg-film {{
      background-image: url('{bg_url}');
      background-size: cover;
      background-position: center;
    }}
  </style>
</head>
<body class="bg-film min-h-screen flex flex-col items-center justify-center px-6">
  <!-- dark overlay for readability -->
  <div class="fixed inset-0 bg-black/55"></div>

  <main class="relative z-10 max-w-2xl w-full text-center space-y-10">

    <div class="inline-block border border-white/30 text-white/60 text-xs tracking-[0.3em] uppercase px-4 py-1.5 rounded-full backdrop-blur-sm">
      Daily Word
    </div>

    <blockquote class="quote-font italic text-3xl md:text-4xl leading-relaxed text-white drop-shadow-lg">
      &ldquo;{quote}&rdquo;
    </blockquote>

    <div class="flex items-center justify-center gap-4">
      <span class="block h-px w-10 bg-white/30"></span>
      <p class="text-sm tracking-widest uppercase text-white/60">{author}</p>
      <span class="block h-px w-10 bg-white/30"></span>
    </div>

  </main>

  <footer class="relative z-10 absolute bottom-8 text-xs tracking-widest uppercase text-white/30">
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
