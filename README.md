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

archive-box · arrow-down-tray · arrow-uturn-left · banknotes · book-open ·
building · calendar · chart-bar · check · check-circle · clock · cog ·
document-down · exclamation-triangle · eye · funnel · globe · language ·
light-bulb · pencil · pencil-square · plus · presentation · printer ·
sparkles · squares · trending-up

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
