"""Build assets/profile-light.svg and assets/profile-dark.svg.

Edit the text, ORDER or THEMES below, then run:  python scripts/build_profile.py
Icon markup lives in scripts/icons.json (24x24 viewBox, filled with currentColor).
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ICONS = json.loads((ROOT / "scripts" / "icons.json").read_text(encoding="utf-8"))

# Technical index, most-liked first (8 per row, the last row is centered).
ORDER = [
    "Python", "TypeScript", "Elixir", "React", "JavaScript", "Next.js", "Node.js", "LangChain",
    "Docker", "Git", "C", "C++", "Java", "Supabase", "Pandas", "NumPy",
    "HTML5", "CSS3", "Vite", "Figma", "LaTeX", "Arduino", "Go", "OCaml",
    "Firebase", "Google Cloud", "MySQL", "SQLite", "PHP", "WordPress",
]

# Backgrounds stay transparent so the image takes the colour of any GitHub theme.
THEMES = {
    "dark": {
        "text": "#E6EDF3", "muted": "#8B949E", "line": "rgba(139,148,158,.3)",
        "accent": "#CDB88E", "accent-bg": "rgba(205,184,142,.12)",
        "hero-text": "#F0F6FC", "hero-muted": "#8B949E",
        "ghost": "rgba(255,255,255,.05)", "code": "rgba(255,255,255,.32)",
        "hero-accent": "#D8C7A3", "vein": "rgba(1,4,9,.55)",
    },
    "light": {
        "text": "#111110", "muted": "#4A4843", "line": "rgba(74,72,67,.2)",
        "accent": "#C4AE80", "accent-bg": "rgba(196,174,128,.18)",
        "hero-text": "#111110", "hero-muted": "#5E5A52",
        "ghost": "rgba(17,17,16,.05)", "code": "rgba(17,17,16,.38)",
        "hero-accent": "#B89F6E", "vein": "rgba(255,255,255,.75)",
    },
}

WIDTH, HEIGHT = 1200, 2190
LOGO_A = (
    "M201 420Q173.2 420 152.1 409.8Q130.9 399.6 119 381.8Q107.1 364.1 107.1 341.2Q107.1 314.9 120.7 299.9"
    "Q134.3 284.8 164.5 278.2Q194.6 271.7 244.7 271.7H263.2V264.8Q263.2 247.3 254.2 240Q245.2 232.7 223.3 232.7"
    "Q211.7 232.7 197.1 235.4Q182.5 238.1 164.5 244.9Q151.3 249.8 142.1 246.4Q132.9 243 127.8 234.7"
    "Q122.6 226.4 122.9 216.7Q123.1 207 129.2 198.2Q135.3 189.5 147.9 184.6Q171.3 175.8 191 172.9"
    "Q210.7 170 227.2 170Q267.1 170 293.1 181.4Q319.1 192.9 332 216.4Q344.9 240 344.9 277V375.3"
    "Q344.9 396.7 334.7 407.8Q324.5 419 305 419Q285.1 419 274.9 407.8Q265.6 398.1 264.2 380.6"
    "Q261.3 389.4 255.9 396.2Q247.2 407.4 233.1 413.7Q218.9 420 201 420ZM263.2 321.3V312.5H244.7"
    "Q225.8 312.5 213.4 315.2Q201 317.9 195.1 323.5Q189.3 329 189.3 337.8Q189.3 349 197.3 356.3"
    "Q205.3 363.6 220.4 363.6Q232.6 363.6 242.1 358.2Q251.5 352.9 257.4 343.4Q263.2 333.9 263.2 321.3Z"
)
LEAF = "M0-72C38-39.6 38 39.6 0 72C-38 39.6-38-39.6 0-72Z"

STYLE = """
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&amp;family=IBM+Plex+Serif:ital,wght@0,400;0,600;0,700;1,400&amp;family=Nunito:wght@900&amp;display=swap');
:root{%(vars)s}
.serif{font-family:'IBM Plex Serif',Georgia,serif}.mono{font-family:'IBM Plex Mono',Consolas,monospace}.brand{font-family:Nunito,'Arial Rounded MT Bold',sans-serif}
.text{fill:var(--text)}.muted{fill:var(--muted)}.line{stroke:var(--line)}.rule{stroke:var(--accent);stroke-width:2}.icon{color:var(--text);fill:currentColor}
.tiny{font-size:10px;letter-spacing:2px}.label{font-size:11px;letter-spacing:1.4px}
.htext{fill:var(--hero-text)}.hmuted{fill:var(--hero-muted)}.ghost{fill:var(--ghost)}.code{fill:var(--code)}
.leaf{fill:var(--hero-accent)}.vein{stroke:var(--vein);fill:none;stroke-linecap:round}.hacc{stroke:var(--hero-accent);stroke-width:2}
/* hero code types itself line by line, then a cursor blinks */
.type{clip-path:inset(0 100%% 0 0);animation:type .6s steps(18,end) forwards}
@keyframes type{to{clip-path:inset(0 0 0 0)}}
.cursor{fill:var(--hero-accent);opacity:0;animation:blink 1.1s step-end 3.6s infinite}
@keyframes blink{0%%,100%%{opacity:1}50%%{opacity:0}}
/* the leaf in About sways from its stem */
.sway{transform-box:fill-box;transform-origin:50%% 100%%;animation:sway 7s ease-in-out infinite}
@keyframes sway{0%%,100%%{transform:rotate(-5deg)}50%%{transform:rotate(5deg)}}
@media (prefers-reduced-motion:reduce){.type{animation:none;clip-path:none}.cursor{animation:none;opacity:1}.sway{animation:none}}
"""


def leaf(veins=True):
    out = [f'<path class="leaf" d="{LEAF}"/>', '<path class="vein" d="M0 61.9V-57.6" stroke-width="5"/>']
    if veins:
        out.append('<path class="vein" d="M0-26L14-40M0-26L-14-40M0 4L19-12M0 4L-19-12M0 34L15 20M0 34L-15 20" stroke-width="3"/>')
    return "".join(out)


def hero():
    code = [
        (932, "const acronoxx = {"),
        (952, 'based: "Brest",'),
        (952, 'gym: "5x / week",'),
        (952, 'fuel: "shakes",'),
        (932, "};"),
    ]
    lines = "\n".join(
        f'<text class="mono code type" x="{x}" y="{196 + 31 * i}" font-size="17" style="animation-delay:{0.4 + 0.65 * i:.2f}s">{t.replace(chr(34), "&quot;")}</text>'
        for i, (x, t) in enumerate(code)
    )
    return f"""<!-- HERO -->
<line class="line" x1="55" y1="42" x2="1145" y2="42"/>
<line class="line" x1="55" y1="378" x2="1145" y2="378"/>
<text class="mono hmuted" x="55" y="27" font-size="9" letter-spacing="2">ACRONOX / PROFILE EDITION 001</text>
<text class="mono hmuted" x="1145" y="27" text-anchor="end" font-size="9" letter-spacing="2">BREST · FRANCE</text>
<text class="brand htext" x="76" y="182" font-size="79" font-weight="900" letter-spacing="-2">Alexis Baret</text>
<text class="mono hmuted" x="80" y="229" font-size="16" font-weight="500" letter-spacing="2">SOFTWARE ENGINEERING STUDENT</text>
<text class="mono hmuted" x="80" y="259" font-size="16" font-weight="500" letter-spacing="2">DISTRIBUTED SYSTEMS · INTERFACES · AI AGENTS</text>
<line class="hacc" x1="80" y1="302" x2="432" y2="302"/>
<text class="mono hmuted" x="80" y="337" font-size="13" letter-spacing="1">IMT ATLANTIQUE · ACRONOXX.GITHUB.IO</text>
<g transform="translate(720 -58) scale(1.12)">
<path class="ghost" d="{LOGO_A}"/>
<g transform="translate(358.3 142.8) rotate(36)">{leaf(veins=False)}</g>
</g>
{lines}
<rect class="cursor" x="956" y="306" width="9" height="17"/>"""


def section(num, name, title, rule_x, y):
    return f"""<text class="mono muted tiny" x="70" y="{y}">{num} / {name}</text>
<text class="serif text" x="70" y="{y + 53}" font-size="34" font-weight="700">{title}</text>
<line class="rule" x1="{rule_x}" y1="{y + 43}" x2="1130" y2="{y + 43}"/>"""


def toolkit(y):
    # 8 columns spanning the content width (70 -> 1130)
    col = (1130 - 70) / 8
    out = [section("02", "TOOLKIT", "Technical Index", 350, y),
           f'<text class="mono muted" x="1130" y="{y + 23}" text-anchor="end" font-size="10" letter-spacing="1.5">{len(ORDER)} TOOLS / FAVOURITES FIRST</text>']
    rows = [ORDER[i:i + 8] for i in range(0, len(ORDER), 8)]
    for r, row in enumerate(rows):
        top = y + 105 + 128 * r
        last = r == len(rows) - 1
        shift = (8 - len(row)) / 2
        for c, name in enumerate(row):
            left = 70 + col * (c + shift)
            cx = left + col / 2
            n = r * 8 + c + 1
            out.append(
                f'<g class="icon" transform="translate({cx - 21:g} {top}) scale(1.75)">{ICONS[name]}</g>'
                f'<text class="mono text" x="{cx:g}" y="{top + 70}" text-anchor="middle" font-size="11">{name}</text>'
                f'<text class="mono muted" x="{cx:g}" y="{top + 89}" text-anchor="middle" font-size="8" letter-spacing="1">{n:02d}</text>'
            )
            if not last:
                out.append(f'<line class="line" x1="{left + 8:g}" y1="{top + 106}" x2="{left + col - 8:g}" y2="{top + 106}"/>')
            if c < len(row) - 1:
                out.append(f'<line class="line" x1="{left + col:g}" y1="{top - 6}" x2="{left + col:g}" y2="{top + 94}"/>')
    return "\n".join(out)


def build(theme):
    vars_ = ";".join(f"--{k}:{v}" for k, v in THEMES[theme].items())
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-labelledby="title desc">
<title id="title">Acronox — Alexis Baret</title>
<desc id="desc">GitHub profile of Alexis Baret, software engineering student at IMT Atlantique in Brest</desc>
<style>{STYLE % {"vars": vars_}}</style>

{hero()}

<!-- side rails -->
<line class="line" x1="28" y1="450" x2="28" y2="1995"/>
<line class="line" x1="1172" y1="450" x2="1172" y2="1995"/>
<text class="mono muted tiny" x="17" y="1200" transform="rotate(-90 17 1200)">ACRONOX / ENGINEERING NOTEBOOK</text>
<text class="mono muted tiny" x="1183" y="1480" transform="rotate(90 1183 1480)">BREST · 48.39°N 4.49°W</text>

<!-- INTRO -->
<text class="mono muted tiny" x="70" y="485">00 / HELLO</text>
<text class="serif text" x="70" y="555" font-size="44" font-weight="600">I build things to understand them.</text>
<text class="mono muted" x="70" y="600" font-size="13">SCHOOL LABS, SIDE PROJECTS, AND WHAT I LEARN FROM BOTH</text>
<line class="rule" x1="70" y1="640" x2="1130" y2="640"/>

<!-- ABOUT -->
{section("01", "ABOUT", "About", 190, 735)}
<text class="serif text" x="70" y="850" font-size="24">I like knowing what happens under the hood:</text>
<text class="serif text" x="70" y="885" font-size="24">how nodes agree, how interfaces feel, how agents decide.</text>
<text class="serif muted" x="70" y="933" font-size="17" font-style="italic">Right now: failure detection in Elixir, a generative banking UI, and too many lab reports.</text>
<circle cx="1042" cy="878" r="88" fill="var(--accent-bg)"/>
<g transform="translate(1042 870) rotate(30) scale(.78)"><g class="sway">{leaf()}<path d="M0 66V92" stroke="var(--hero-accent)" stroke-width="5" stroke-linecap="round"/></g></g>

<!-- TOOLKIT -->
{toolkit(1045)}

<!-- OFF HOURS -->
{section("03", "OFF HOURS", "When I'm Not Coding", 450, 1705)}
<line class="line" x1="335" y1="1790" x2="335" y2="1963"/>
<line class="line" x1="600" y1="1790" x2="600" y2="1963"/>
<line class="line" x1="865" y1="1790" x2="865" y2="1963"/>
<g transform="translate(0 -485)">
<text class="mono muted label" x="70" y="2305">01 / GYM</text>
<text class="serif text" x="70" y="2350" font-size="25" font-weight="600">Push · Pull · Legs</text>
<text class="serif muted" x="70" y="2380" font-size="14">Five sessions a week, no skipping.</text>
<g fill="var(--accent)"><rect x="70" y="2411" width="38" height="4"/><rect x="116" y="2411" width="38" height="4"/><rect x="162" y="2411" width="38" height="4"/><rect x="208" y="2411" width="38" height="4"/><rect x="254" y="2411" width="38" height="4"/></g>
<text class="mono muted label" x="365" y="2305">02 / GAMES</text>
<text class="serif text" x="365" y="2350" font-size="25" font-weight="600">Two extremes</text>
<text class="serif muted" x="365" y="2380" font-size="14">The Finals · Animal Crossing</text>
<circle cx="551" cy="2411" r="20" fill="var(--accent-bg)"/><path d="M540 2411h22M551 2400v22" stroke="var(--accent)" stroke-width="2"/>
<text class="mono muted label" x="630" y="2305">03 / READING</text>
<text class="serif text" x="630" y="2350" font-size="25" font-weight="600">On the shelf</text>
<text class="serif muted" x="630" y="2380" font-size="14">Atomic Habits · Bridgerton</text>
<path d="M788 2400h13c8 0 13 4 13 11v29c-4-5-8-7-13-7h-13zM814 2411c0-7 5-11 13-11h13v33h-13c-5 0-9 2-13 7z" fill="none" stroke="var(--accent)" stroke-width="2"/>
<text class="mono muted label" x="895" y="2305">04 / DOWNTIME</text>
<text class="serif text" x="895" y="2350" font-size="25" font-weight="600">Shake &amp; lo-fi</text>
<text class="serif muted" x="895" y="2380" font-size="14">After the gym, before the next lab.</text>
<path d="M1077 2394h25l-4 43h-17zM1080 2387h19v7h-19z" fill="none" stroke="var(--accent)" stroke-width="2"/>
</g>

<!-- SIGNATURE -->
<line class="line" x1="55" y1="2015" x2="1145" y2="2015"/>
<g transform="translate(20 2015) scale(.32)">
<path class="htext" d="{LOGO_A}"/>
<g transform="translate(358.3 142.8) rotate(36)">{leaf(veins=False)}</g>
</g>
<text class="serif htext" x="190" y="2110" font-size="30" font-weight="700">See you in the commits.</text>
<text class="mono hmuted" x="190" y="2144" font-size="10" letter-spacing="1.5">ALEXIS BARET · ACRONOX · BREST, FRANCE</text>
<line class="hacc" x1="735" y1="2114" x2="1130" y2="2114"/>
<text class="mono htext" x="1130" y="2098" text-anchor="end" font-size="10" letter-spacing="1.5">ACRONOXX.GITHUB.IO</text>
<text class="mono hmuted" x="1130" y="2145" text-anchor="end" font-size="9" letter-spacing="1.5">PROFILE / EDITION 001</text>
</svg>
"""


if __name__ == "__main__":
    for theme in THEMES:
        path = ROOT / "assets" / f"profile-{theme}.svg"
        path.write_text(build(theme), encoding="utf-8")
        print("wrote", path.relative_to(ROOT))
