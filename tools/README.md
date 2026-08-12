# Asset generators

The SVGs in `assets/` are generated, not hand-edited. Text is converted to
vector paths with fontTools so the banner renders identically for everyone,
including visitors who do not have Geist installed.

```sh
pip install fonttools
python3 tools/build_header.py
python3 tools/build_buttons.py
python3 tools/build_stack.py
```

Brand tokens live at the top of each script: navy `#0A0E1A`, amber
`#F59E0B`, failure red `#EF4444`, light `#F8FAFC`. Fonts are read from
`~/Library/Fonts`, so adjust the paths in `textpath.py` on another machine.
