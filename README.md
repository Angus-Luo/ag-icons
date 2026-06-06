# ag-icons

Inline-SVG icons for Django templates — a single-file registry of
Heroicons-style 24×24 outline paths plus an `{% icon %}` template tag.
Built to **replace ad-hoc emoji** in UI: icons inherit `currentColor` and
size via CSS classes, so one icon works in any theme, color and size
(emoji can't do any of that, and render differently per OS).

## Install

```sh
uv add "ag-icons @ git+https://github.com/Angus-Luo/ag-icons"
# or: pip install git+https://github.com/Angus-Luo/ag-icons
```

```python
# settings.py
INSTALLED_APPS = [
    ...
    "ag_icons",
]
```

## Use

```django
{% load icons %}

{% icon "sparkles" %}                          {# default class="w-5 h-5" #}
{% icon "trending-up" class="w-4 h-4" %}
{% icon "exclamation-triangle" class="w-5 h-5 text-error shrink-0" %}
```

Size/color come from the CSS class (Tailwind shown; any CSS works —
the SVG uses `stroke="currentColor"`, so set `color:` to tint it).

From Python (e.g. building HTML in a view or management command):

```python
from ag_icons import render_icon
html = render_icon("printer", "w-4 h-4")
```

Unknown names render a neutral fallback glyph instead of crashing.

## Migrating a template off emoji

`EMOJI_MAP` is the lookup table: grep the template for an emoji, find its
replacement, swap in `{% icon %}`.

```python
from ag_icons import EMOJI_MAP
EMOJI_MAP["🤖"]   # -> "sparkles"
EMOJI_MAP["📊"]   # -> "chart-bar"
```

## Icon set

`from ag_icons import ICONS; sorted(ICONS)` — currently:

academic-cap · adjustments · archive-box · arrow-down · arrow-down-tray ·
arrow-path · arrow-up · arrow-up-tray · arrow-uturn-left · banknotes ·
beach-umbrella · bell-alert · bolt · book-open · briefcase · building · cake ·
calendar · camera · chart-bar · chat-bubble · check · check-circle ·
clipboard · clock · cog · computer-desktop · cursor-arrow · device-phone ·
document-down · document-text · door · dot · envelope · exclamation-triangle ·
eye · eye-slash · factory · flag · folder · funnel · globe · hand-wave · home ·
hourglass · identification · information-circle · language · light-bulb · link ·
lock-closed · map-pin · medal · palm-tree · pencil · pencil-square · phone ·
photo · plus · presentation · printer · receipt · rocket-launch · scale ·
sparkles · squares · star · storefront · sun · tag · traffic-light ·
trending-down · trending-up · trophy · user · users · wrench · x-circle

## Adding an icon

Grab the inner path(s) of a [Heroicons](https://heroicons.com) 24px
*outline* icon (just the `<path .../>` elements, not the `<svg>` wrapper)
and add one line to `ICONS` in `src/ag_icons/__init__.py`. The shared
`<svg>` wrapper (viewBox, stroke width, `currentColor`) is applied by
`render_icon`. If it replaces an emoji somewhere, record it in `EMOJI_MAP`.

## Caveats

- **Not for HTML email.** Outlook (and most clients) strip `<svg>` —
  style emails with inline-CSS color/typography instead.
- Paths are stroke-based outline icons; `fill="none"` is hard-coded.

## License

MIT. Icon artwork derived from [Heroicons](https://heroicons.com),
MIT © Tailwind Labs.
