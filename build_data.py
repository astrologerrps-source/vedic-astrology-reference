#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate the Vedic astrology reference data (JSON). Run: python3 build_data.py"""
import json, os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
os.makedirs(OUT, exist_ok=True)

def w(name, obj):
    p = os.path.join(OUT, name)
    with open(p, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
    print("wrote", p)

# ---- 12 Rashis (zodiac signs) ----
rashis = [
    {"n": 1,  "sanskrit": "Mesha",      "english": "Aries",       "lord": "Mars",    "element": "Fire",  "quality": "Movable", "symbol": "Ram"},
    {"n": 2,  "sanskrit": "Vrishabha",  "english": "Taurus",      "lord": "Venus",   "element": "Earth", "quality": "Fixed",   "symbol": "Bull"},
    {"n": 3,  "sanskrit": "Mithuna",    "english": "Gemini",      "lord": "Mercury", "element": "Air",   "quality": "Dual",    "symbol": "Twins"},
    {"n": 4,  "sanskrit": "Karka",      "english": "Cancer",      "lord": "Moon",    "element": "Water", "quality": "Movable", "symbol": "Crab"},
    {"n": 5,  "sanskrit": "Simha",      "english": "Leo",         "lord": "Sun",     "element": "Fire",  "quality": "Fixed",   "symbol": "Lion"},
    {"n": 6,  "sanskrit": "Kanya",      "english": "Virgo",       "lord": "Mercury", "element": "Earth", "quality": "Dual",    "symbol": "Maiden"},
    {"n": 7,  "sanskrit": "Tula",       "english": "Libra",       "lord": "Venus",   "element": "Air",   "quality": "Movable", "symbol": "Scales"},
    {"n": 8,  "sanskrit": "Vrishchika", "english": "Scorpio",     "lord": "Mars",    "element": "Water", "quality": "Fixed",   "symbol": "Scorpion"},
    {"n": 9,  "sanskrit": "Dhanu",      "english": "Sagittarius", "lord": "Jupiter", "element": "Fire",  "quality": "Dual",    "symbol": "Archer"},
    {"n": 10, "sanskrit": "Makara",     "english": "Capricorn",   "lord": "Saturn",  "element": "Earth", "quality": "Movable", "symbol": "Crocodile / Sea-goat"},
    {"n": 11, "sanskrit": "Kumbha",     "english": "Aquarius",    "lord": "Saturn",  "element": "Air",   "quality": "Fixed",   "symbol": "Water-bearer"},
    {"n": 12, "sanskrit": "Meena",      "english": "Pisces",      "lord": "Jupiter", "element": "Water", "quality": "Dual",    "symbol": "Fishes"},
]

# ---- 9 Grahas (planets / nodes) ----
grahas = [
    {"sanskrit": "Surya",   "english": "Sun",     "type": "Luminary",    "classical_nature": "Malefic", "own_signs": ["Leo"],                  "exaltation": "Aries",       "debilitation": "Libra",      "karaka": "Soul, father, authority, vitality, health"},
    {"sanskrit": "Chandra", "english": "Moon",    "type": "Luminary",    "classical_nature": "Benefic (waxing) / Malefic (waning)", "own_signs": ["Cancer"], "exaltation": "Taurus", "debilitation": "Scorpio", "karaka": "Mind, emotions, mother, nourishment"},
    {"sanskrit": "Mangala", "english": "Mars",    "type": "Planet",      "classical_nature": "Malefic", "own_signs": ["Aries", "Scorpio"],     "exaltation": "Capricorn",   "debilitation": "Cancer",     "karaka": "Energy, courage, siblings, land, drive"},
    {"sanskrit": "Budha",   "english": "Mercury", "type": "Planet",      "classical_nature": "Benefic (by association)", "own_signs": ["Gemini", "Virgo"], "exaltation": "Virgo", "debilitation": "Pisces", "karaka": "Intellect, speech, communication, commerce"},
    {"sanskrit": "Guru",    "english": "Jupiter", "type": "Planet",      "classical_nature": "Benefic", "own_signs": ["Sagittarius", "Pisces"], "exaltation": "Cancer",      "debilitation": "Capricorn",  "karaka": "Wisdom, wealth, children, dharma, teachers"},
    {"sanskrit": "Shukra",  "english": "Venus",   "type": "Planet",      "classical_nature": "Benefic", "own_signs": ["Taurus", "Libra"],      "exaltation": "Pisces",      "debilitation": "Virgo",      "karaka": "Love, marriage, comforts, arts, vehicles"},
    {"sanskrit": "Shani",   "english": "Saturn",  "type": "Planet",      "classical_nature": "Malefic", "own_signs": ["Capricorn", "Aquarius"],"exaltation": "Libra",       "debilitation": "Aries",      "karaka": "Discipline, longevity, karma, delay, labour"},
    {"sanskrit": "Rahu",    "english": "Rahu (North Node)", "type": "Shadow node", "classical_nature": "Malefic", "own_signs": [], "exaltation": "Taurus (tradition-dependent)", "debilitation": "Scorpio (tradition-dependent)", "karaka": "Desire, ambition, foreign, obsession"},
    {"sanskrit": "Ketu",    "english": "Ketu (South Node)", "type": "Shadow node", "classical_nature": "Malefic", "own_signs": [], "exaltation": "Scorpio (tradition-dependent)", "debilitation": "Taurus (tradition-dependent)", "karaka": "Detachment, moksha, past karma, spirituality"},
]

# ---- 27 Nakshatras (lunar mansions) ----
# Vimshottari lord cycle: Ketu, Venus, Sun, Moon, Mars, Rahu, Jupiter, Saturn, Mercury (x3)
nak_names = [
    ("Ashwini", "Ashwini Kumaras"), ("Bharani", "Yama"), ("Krittika", "Agni"),
    ("Rohini", "Brahma (Prajapati)"), ("Mrigashira", "Soma"), ("Ardra", "Rudra"),
    ("Punarvasu", "Aditi"), ("Pushya", "Brihaspati"), ("Ashlesha", "Nagas (Sarpa)"),
    ("Magha", "Pitris"), ("Purva Phalguni", "Bhaga"), ("Uttara Phalguni", "Aryaman"),
    ("Hasta", "Savitar"), ("Chitra", "Tvashtar"), ("Swati", "Vayu"),
    ("Vishakha", "Indra-Agni"), ("Anuradha", "Mitra"), ("Jyeshtha", "Indra"),
    ("Mula", "Nirriti"), ("Purva Ashadha", "Apas"), ("Uttara Ashadha", "Vishvedevas"),
    ("Shravana", "Vishnu"), ("Dhanishta", "Vasus"), ("Shatabhisha", "Varuna"),
    ("Purva Bhadrapada", "Aja Ekapada"), ("Uttara Bhadrapada", "Ahir Budhnya"), ("Revati", "Pushan"),
]
vim_cycle = ["Ketu", "Venus", "Sun", "Moon", "Mars", "Rahu", "Jupiter", "Saturn", "Mercury"]
def dms(total_arcmin):
    d = total_arcmin // 60
    m = total_arcmin % 60
    return f"{d}\u00b0{m:02d}'"
nakshatras = []
for i, (name, deity) in enumerate(nak_names):
    start = i * 800          # 13°20' = 800 arc-minutes
    end = (i + 1) * 800
    nakshatras.append({
        "n": i + 1,
        "name": name,
        "ruling_planet": vim_cycle[i % 9],
        "deity": deity,
        "span": "13\u00b020'",
        "start": dms(start),
        "end": dms(end),
        "padas": 4,
    })

# ---- Ashtakoota Guna Milan (marriage matching, 36 points) ----
guna_milan = {
    "system": "Ashtakoota Guna Milan",
    "total_points": 36,
    "minimum_generally_acceptable": 18,
    "note": "Points alone are not conclusive; doshas (e.g. Mangal, Bhakoot, Nadi) and the full chart must also be assessed.",
    "kootas": [
        {"n": 1, "koota": "Varna",        "max_points": 1, "assesses": "Spiritual/ego compatibility and work nature"},
        {"n": 2, "koota": "Vashya",       "max_points": 2, "assesses": "Mutual attraction and control"},
        {"n": 3, "koota": "Tara (Dina)",  "max_points": 3, "assesses": "Birth-star compatibility, health and fortune"},
        {"n": 4, "koota": "Yoni",         "max_points": 4, "assesses": "Physical/biological compatibility"},
        {"n": 5, "koota": "Graha Maitri", "max_points": 5, "assesses": "Mental compatibility and friendship of sign lords"},
        {"n": 6, "koota": "Gana",         "max_points": 6, "assesses": "Temperament (Deva, Manushya, Rakshasa)"},
        {"n": 7, "koota": "Bhakoot",      "max_points": 7, "assesses": "Emotional bond, love and family welfare"},
        {"n": 8, "koota": "Nadi",         "max_points": 8, "assesses": "Health, genes and progeny"},
    ],
}

# ---- Vimshottari Dasha (planetary period system, 120-year cycle) ----
vimshottari = {
    "system": "Vimshottari Dasha",
    "total_years": 120,
    "based_on": "Moon's nakshatra at birth",
    "sequence": [
        {"order": 1, "planet": "Ketu",    "years": 7},
        {"order": 2, "planet": "Venus",   "years": 20},
        {"order": 3, "planet": "Sun",     "years": 6},
        {"order": 4, "planet": "Moon",    "years": 10},
        {"order": 5, "planet": "Mars",    "years": 7},
        {"order": 6, "planet": "Rahu",    "years": 18},
        {"order": 7, "planet": "Jupiter", "years": 16},
        {"order": 8, "planet": "Saturn",  "years": 19},
        {"order": 9, "planet": "Mercury", "years": 17},
    ],
}

# ---- Glossary ----
glossary = [
    {"term": "Kundli", "definition": "A Vedic birth chart mapping planetary positions at the exact time and place of birth."},
    {"term": "Lagna", "definition": "The ascendant — the zodiac sign rising on the eastern horizon at birth; the 1st house."},
    {"term": "Rashi", "definition": "A zodiac sign; also the Moon-sign in common usage."},
    {"term": "Nakshatra", "definition": "One of 27 lunar mansions, each spanning 13°20' of the zodiac."},
    {"term": "Graha", "definition": "A planet or node used in Jyotish (the nine grahas)."},
    {"term": "Bhava", "definition": "A house — one of twelve divisions of the chart governing areas of life."},
    {"term": "Dasha", "definition": "A planetary period that times when results manifest; Vimshottari is the most common system."},
    {"term": "Gochar", "definition": "Transit — the current movement of planets relative to the natal chart."},
    {"term": "Yoga", "definition": "A specific planetary combination producing a defined result."},
    {"term": "Dosha", "definition": "An affliction or imbalance in the chart (e.g. Mangal Dosha)."},
    {"term": "Guna Milan", "definition": "Ashtakoota compatibility scoring (out of 36) used in marriage matching."},
    {"term": "Muhurat", "definition": "An auspicious electional time chosen for an important activity."},
    {"term": "Navamsa", "definition": "The D9 divisional chart, used especially for marriage and inner strength of planets."},
    {"term": "Panchanga", "definition": "The Hindu almanac: tithi, vara, nakshatra, yoga and karana."},
]

w("rashis.json", {"count": 12, "rashis": rashis})
w("grahas.json", {"count": 9, "note": "Classical natures are general; functional nature depends on the ascendant and the whole chart. Node exaltations vary by tradition.", "grahas": grahas})
w("nakshatras.json", {"count": 27, "ruling_planet_system": "Vimshottari", "nakshatras": nakshatras})
w("guna_milan.json", guna_milan)
w("vimshottari_dasha.json", vimshottari)
w("glossary.json", {"count": len(glossary), "glossary": glossary})
print("done")
