"""Sitemap generator for regulation.zjktravel.com MkDocs build."""
import os
from datetime import datetime

TODAY = "2026-07-30"
SITE_URL = "https://regulation.zjktravel.com"
SITE_DIR = os.path.join(os.path.dirname(__file__), "site")

EXCLUDE = set()

def generate_sitemap():
    urls = set()
    for root, dirs, files in os.walk(SITE_DIR):
        for f in files:
            if f == "index.html":
                rel_path = os.path.relpath(os.path.join(root, f), SITE_DIR)
                url_path = rel_path.replace("index.html", "")
                if any(ex in url_path for ex in EXCLUDE):
                    continue
                urls.add(f"{SITE_URL}/{url_path}")

    urls = sorted(urls)
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for url in urls:
        xml += "  <url>\n"
        xml += f"    <loc>{url}</loc>\n"
        xml += f"    <lastmod>{TODAY}</lastmod>\n"
        xml += "    <changefreq>monthly</changefreq>\n"
        xml += "    <priority>0.8</priority>\n"
        xml += "  </url>\n"
    xml += "</urlset>"

    with open(os.path.join(SITE_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(xml)
    print(f"Sitemap generated: {len(urls)} URLs")

if __name__ == "__main__":
    generate_sitemap()
