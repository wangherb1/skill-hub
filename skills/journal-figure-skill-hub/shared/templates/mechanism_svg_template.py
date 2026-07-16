from pathlib import Path

SVG = '''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="360" viewBox="0 0 1000 360">
<rect width="100%" height="100%" fill="white"/>
<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#333"/></marker></defs>
<g font-family="Arial" font-size="22">
<rect x="60" y="120" width="190" height="90" rx="8" fill="#E8F1FA" stroke="#0072B2"/>
<text x="95" y="170">Initial state</text>
<line x1="260" y1="165" x2="390" y2="165" stroke="#333" stroke-width="3" marker-end="url(#arrow)"/>
<rect x="405" y="120" width="190" height="90" rx="8" fill="#FCE8D8" stroke="#D55E00"/>
<text x="450" y="170">Mechanism</text>
<line x1="605" y1="165" x2="735" y2="165" stroke="#333" stroke-width="3" marker-end="url(#arrow)"/>
<rect x="750" y="120" width="190" height="90" rx="8" fill="#E9F6EF" stroke="#009E73"/>
<text x="790" y="170">Observable</text>
</g></svg>'''

Path("editable").mkdir(exist_ok=True)
Path("final").mkdir(exist_ok=True)
(Path("editable") / "mechanism.svg").write_text(SVG, encoding="utf-8")
(Path("final") / "mechanism.svg").write_text(SVG, encoding="utf-8")
