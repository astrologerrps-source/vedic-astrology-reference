# Vedic Astrology Reference Data (Jyotish)

Open, clean, machine-readable reference data for **Vedic astrology (Jyotish)** — the foundational tables every birth-chart (Kundli) tool needs, as plain JSON. Free to use in apps, scripts, research and learning.

Curated by **Dr. R.P. Sharma**, a Vedic astrologer practising since 1979 (Ph.D., Acharya in Phalit Jyotish). Reference site: **https://drrpsharma.com**

## What's inside

| File | Contents |
|------|----------|
| [`data/rashis.json`](data/rashis.json) | The 12 **rashis** (zodiac signs) — Sanskrit & English names, ruling planet, element, quality (movable/fixed/dual), symbol |
| [`data/grahas.json`](data/grahas.json) | The 9 **grahas** (planets & nodes) — type, classical nature, own signs, exaltation/debilitation, significations (karaka) |
| [`data/nakshatras.json`](data/nakshatras.json) | The 27 **nakshatras** (lunar mansions) — Vimshottari ruling planet, deity, exact start/end degrees, padas |
| [`data/guna_milan.json`](data/guna_milan.json) | **Ashtakoota Guna Milan** — the 8 kootas, points (out of 36), and what each assesses |
| [`data/vimshottari_dasha.json`](data/vimshottari_dasha.json) | **Vimshottari Dasha** — the 9 planetary periods and their years (120-year cycle) |
| [`data/glossary.json`](data/glossary.json) | Plain-English definitions of common Jyotish terms |

All data is UTF-8 JSON. Regenerate it any time with `python3 build_data.py`.

## Quick example

```python
import json

rashis = json.load(open("data/rashis.json"))["rashis"]
for r in rashis:
    print(f"{r['n']:>2}. {r['sanskrit']} ({r['english']}) — lord: {r['lord']}, element: {r['element']}")

# Nakshatra spans (each 13°20')
naks = json.load(open("data/nakshatras.json"))["nakshatras"]
print(naks[0]["name"], naks[0]["start"], "-", naks[0]["end"])  # Ashwini 0°00' - 13°20'
```

```javascript
// Node / browser
import rashis from "./data/rashis.json" assert { type: "json" };
console.log(rashis.rashis.find(r => r.english === "Aries"));
```

## Notes on accuracy

This is **classical reference data** drawn from standard Jyotish tradition. A few points (e.g. the exaltation signs of the lunar nodes Rahu and Ketu, and whether the Moon counts as benefic when waning) vary between schools — those are flagged inline in the data. The sign elements, lords, nakshatra degrees, Guna-Milan points and Vimshottari years are well-settled and consistent across traditions.

This dataset is descriptive reference material. It is not astrological advice. For a personal consultation, see https://drrpsharma.com.

## Contributing

Corrections and additions (more divisional-chart tables, regional naming variants, translations) are welcome — open an issue or a pull request.

## License

[MIT](LICENSE) — free for any use, including commercial, with attribution. © 2026 Dr. R.P. Sharma · https://drrpsharma.com
