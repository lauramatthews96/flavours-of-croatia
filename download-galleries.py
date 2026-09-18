#!/usr/bin/env python3
import os
import urllib.request

DEST = os.path.join(os.path.dirname(__file__), "assets", "gallery")
os.makedirs(DEST, exist_ok=True)

FILES = {
    "gourmet-hero.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2018/07/Screenshot-2024-12-05-at-23.03.35.png",
    "gourmet-map.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2025/04/Gourmet-Itinery.png",
    "d1-1.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2018/07/Sibenik.png",
    "d1-2.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2018/07/Marina-Mandalina-in-Sibenik.png",
    "d1-3.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/10/Sail52-1.png",
    "d1-4.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2018/07/St.James_.png",
    "d1-5.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2018/07/Sibenik-3.png",
    "d1-6.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2018/07/Sibenik-2.png",
    "d2-1.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/12/Split-2.png",
    "d2-2.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/12/Taste56-low.png",
    "d2-3.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/12/Sail40-low.png",
    "d2-4.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/12/Flavours-of-Croatia-Tasting.png",
    "d2-5.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/12/Sail35-low.png",
    "d2-6.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/12/Split-1.png",
    "d3-1.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/12/primosten-croatia.png",
    "d3-2.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/12/Screenshot-2024-12-05-at-23.44.50.png",
    "d3-3.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/12/Taste11-low.png",
    "d3-4.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/11/1.png",
    "d3-5.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/12/Screenshot-2024-12-05-at-23.44.11.png",
    "d3-6.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/12/primosten-3.png",
    "d4-1.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/12/Kastela-4.png",
    "d4-2.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/12/5N4A1152-scaled-1.png",
    "d4-3.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/12/kastela-2.png",
    "d4-4.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/12/5N4A0996-scaled-1.png",
    "d4-5.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/12/Kastela.png",
    "d4-6.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/12/5N4A1465-scaled-1.png",
    "d5-1.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/12/kasjuni-beach-split.png",
    "d5-2.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/12/Split-Croatia-Day.png",
    "d5-3.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/12/Riva-promenade.png",
    "d5-4.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/12/Split_Diocletian_Palace_Croatia.png",
    "d5-5.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/12/Riva-promenade-2.png",
    "d5-6.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/12/Kasjuni-Beach-1-2.png",
    "d6-1.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/12/skradin-2.png",
    "d6-2.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/12/Ante-Sladic-Vino.png",
    "d6-3.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/12/Screenshot-2024-12-05-at-23.47.43.png",
    "d6-4.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/12/Screenshot-2024-12-05-at-23.47.53.png",
    "d6-5.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/12/Screenshot-2024-12-05-at-23.46.39.png",
    "d6-6.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/12/Skradin-.png",
    "d7-1.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/12/Sibenik-3.png",
    "d7-2.jpeg": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/11/Must-See-Islands-When-Sailing-Croatia.jpeg",
    "d7-3.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/12/Sibenik-at-night-.png",
    "d7-4.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/11/5.png",
    "d7-5.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/12/Sibenik-6.png",
    "d7-6.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/12/St-Micheals-Fortress-2.png",
}

opener = urllib.request.build_opener()
opener.addheaders = [("User-Agent", "Mozilla/5.0 (compatible; FlavoursRemake/1.0)")]
urllib.request.install_opener(opener)

ok = fail = 0
for name, url in FILES.items():
    path = os.path.join(DEST, name)
    if os.path.exists(path) and os.path.getsize(path) > 1000:
        print(f"SKIP {name}")
        ok += 1
        continue
    try:
        urllib.request.urlretrieve(url, path)
        print(f"OK   {name} ({os.path.getsize(path)} bytes)")
        ok += 1
    except Exception as e:
        print(f"FAIL {name}: {e}")
        fail += 1

print(f"\nDone. {ok} ok, {fail} failed")
