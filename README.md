# Askar Dauletbek — Full-stack & AI developer

Personal portfolio: **[askardk.github.io](https://askardk.github.io/)** · [English](https://askardk.github.io/en/)

Three project case studies:

- **[Lumo](https://askardk.github.io/projects/lumo/)** — speech processing, live call assistance, a Windows client, web workspaces and a mobile application. Private application source.
- **[Kilogr.app](https://askardk.github.io/projects/kilogr/)** — food and activity tracking, training, AI features and Telegram integration. Private application source.
- **[KEZEN](https://askardk.github.io/projects/kezen/)** — a local-events platform with profiles, interests and community features. [Public project repository](https://github.com/AskarDK/projectKezen).

## Local preview

The site uses static HTML, CSS and JavaScript. Python 3.10+ is only needed to regenerate pages; no third-party Python or npm packages are required.

```sh
python build.py
python -m http.server 8099 --directory docs --bind 127.0.0.1
```

Visit `http://127.0.0.1:8099/`. Run `python verify.py` to check generated routes, local assets, language alternates and metadata.

## Editing

- `content.py` — project descriptions and Russian / English copy.
- `build.py` — static HTML templates and generation.
- `assets/style.css` — responsive layout and product diagrams.
- `assets/app.js` — mobile navigation and email-copy interaction.
- `docs/` — generated files, published by GitHub Pages from `main` / `/docs`.

After editing source files, run `python build.py`, then commit both source and generated `docs/` files. All routes render without client-side JavaScript. Fonts are served locally; their license is included in `assets/fonts/`.

## Publication boundary

This repository contains the portfolio website and original illustrative product diagrams. It does **not** contain application source from Lumo or Kilogr.app, production configuration, databases, audio recordings, authentication material or customer data. The diagrams are labelled as illustrations and use no real user data. No unverified performance figures or business outcomes are claimed.

## Contact

[GitHub](https://github.com/AskarDK) · [Telegram](https://t.me/AskarDK) · [Email](mailto:dauletbekoffa@gmail.com)
