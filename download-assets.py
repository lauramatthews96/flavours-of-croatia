#!/usr/bin/env python3
import os
import urllib.request

DEST = os.path.join(os.path.dirname(__file__), "assets")
os.makedirs(DEST, exist_ok=True)

FILES = {
    "logo.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/12/FOC-Logo-02-1536x870-1.png",
    "hero.jpg": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/12/Flavours-of-Craotia-Header-Image-.png",
    "hero-welcome.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/11/Banner-Text-5.png",
    "signature-1.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/12/Flavours-of-Croatia-Signature.png",
    "signature-2.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/12/Second-Signature-Flavours-of-Croatia.png",
    "footer-logo.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/12/Flavours-of-Croatia-Sailing-Holidays-1.png",
    "quote-bg.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/12/Travel-is-not-just-about-seeing-new-places-its-about-tasting-feeling-and-living-them.-Let-Croatias-flavors-awaken-your-senses-and-enrich-your-soul.png",
    "feature-1.jpg": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/12/Flavours-of-Croatia-Sailing-Holidays-Sea-1024x683.png",
    "feature-2.jpg": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/12/Taste30-low-1024x683.png",
    "feature-3.jpg": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/12/03.-Seamless-Travel-Planning-1024x683.jpg",
    "landscape-band.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/12/unnamed-file.png",
    "testimonial-bg.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/12/adjusted_banner_gradient_image_with_transparency.png",
    "sam-g.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/12/Sam-G-Review.png",
    "g1.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/11/1.png",
    "g2.jpg": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/11/FlavoursOfCroatia-Sailing-Holidays-2.jpeg",
    "g3.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/10/Sail52-1.png",
    "g4.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/10/Taste18.png",
    "g5.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/10/Screenshot-2024-10-31-at-09.07.06.png",
    "g6.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/10/Taste52.png",
    "g7.jpg": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/11/FlavoursOfCroatia-Sailing-Holidays.5.jpeg",
    "g8.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/12/Sail28-low.png",
    "g9.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/12/Taste59-low.png",
    "g10.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/12/Sail45-low.png",
    "g11.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/11/7.png",
    "g12.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/12/Sail40-low.png",
    "g13.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/11/4.png",
    "g14.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/12/Taste56-low.png",
    "g15.jpg": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/12/03.-Seamless-Travel-Planning.jpg",
    "blog-packing.jpg": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/11/The-Ultimate-Packing-List-for-a-Sailing-Holiday-in-Croatia-3.jpg",
    "blog-season.jpg": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/11/The-Best-Time-of-Year-to-Sail-in-Croatia-and-Why-It-Matters-2.jpg",
    "blog-food.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/06/Peka-fdish.png",
    "why-choose.png": "https://flavoursofcroatiasailingholidays.com/wp-content/uploads/2024/12/unnamed-file.png",
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
        size = os.path.getsize(path)
        print(f"OK   {name} ({size} bytes)")
        ok += 1
    except Exception as e:
        print(f"FAIL {name}: {e}")
        fail += 1

print(f"\nDone. {ok} ok, {fail} failed")
