# Seat badges

Persona badges for the Domestic Threat seats. Every issue, PR and comment an
agent posts from the owner's account opens with its seat's badge, so the owner
can see who suggested what.

| Badge | Seat | Lane |
|---|---|---|
| ![Lighthouse](https://github.com/francoisdevlin/seat-badges/blob/main/32x32/lighthouse.png?raw=true) | Lighthouse | orchestrator |
| ![Drydock](https://github.com/francoisdevlin/seat-badges/blob/main/32x32/drydock.png?raw=true) | Drydock | engine |
| ![Promenade](https://github.com/francoisdevlin/seat-badges/blob/main/32x32/promenade.png?raw=true) | Promenade | content |
| ![Fish Market](https://github.com/francoisdevlin/seat-badges/blob/main/32x32/fish-market.png?raw=true) | Fish Market | assets |
| ![North Pier](https://github.com/francoisdevlin/seat-badges/blob/main/32x32/north-pier.png?raw=true) | North Pier | code review |
| ![South Pier](https://github.com/francoisdevlin/seat-badges/blob/main/32x32/south-pier.png?raw=true) | South Pier | test review |
| ![Train Station](https://github.com/francoisdevlin/seat-badges/blob/main/32x32/train-station.png?raw=true) | Train Station | CI/CD |
| ![Chart Room](https://github.com/francoisdevlin/seat-badges/blob/main/32x32/chart-room.png?raw=true) | Chart Room | control centre |

## The badge line

Paste as the first line of a body or comment, with the seat's name and file:

```markdown
# ![Name](https://github.com/francoisdevlin/seat-badges/blob/main/32x32/<seat>.png?raw=true) Name
```

For example:

```markdown
# ![Fish Market](https://github.com/francoisdevlin/seat-badges/blob/main/32x32/fish-market.png?raw=true) Fish Market
```

## Layout

- `svg/<seat>.svg`: the hand-written source, a 64-unit view box: a cream
  round tile with an ink outline, in the game's palette (cream `#FFF3DE`,
  ink `#393047`, teal `#4DA89B`, coral `#E97B69`, butter `#E8BE60`,
  Ick `#A586BE`).
- `32x32/<seat>.png` and `64x64/<seat>.png`: baked from the SVG.
- `bake.py`: re-bakes both sizes from every SVG.

## Re-bake

```sh
uv run --no-project --with cairosvg python bake.py
```

cairosvg needs the cairo library. On macOS with Homebrew, prefix the command
with `DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib`.

The PNGs are small, plain git objects (no LFS), so the raw links render inline
on GitHub.
