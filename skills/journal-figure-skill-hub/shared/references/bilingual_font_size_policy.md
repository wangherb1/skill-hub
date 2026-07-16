# Bilingual Font And Word-Width Policy

Use this policy for every future journal figure unless the user explicitly overrides it.

## Language Switching

- Keep all visible figure text in `source/label_map.json`.
- Generate Chinese, English, or bilingual variants from the same figure code and layout.
- Do not hard-code final labels directly into plotting code when a label may need translation.
- Preserve the same panel geometry between language variants whenever possible.

## Fonts

- Chinese text: SimSun/宋体.
- English letters, numbers, units, symbols, and formulas: Times New Roman.
- Normal figure text must not exceed Word Chinese size 5, treated as `10.5 pt`.
- Axis tick labels, colorbar ticks, legends, and panel labels should usually be `7-9 pt`.

## Word Width

- Single-column large figure for Word: maximum width `15.5 cm`.
- Two figures side by side in a double-column layout: maximum single-figure width `7.5 cm`.
- Height is flexible, but text and line weights must remain readable at the target Word width.

## QA

The preflight check must flag missing label maps, fonts outside this policy, or figure width above the selected Word insertion mode.

