# Zeka Emo — Portfolio

Personal portfolio covering software engineering, applied AI, and research projects. Built with HTML, CSS, and JavaScript.

## Run locally

```sh
python3 -m http.server 4174 --bind 127.0.0.1 --directory public
```

Open http://127.0.0.1:4174.

## Project structure

```text
public/
  index.html          Portfolio home
  slides.html         Printable slide deck
  assets/
    css/              Website and print styles
    js/               Project content and page rendering
    documents/        Thesis and research paper
    work/             Project figures
  work/               Individual project pages
scripts/
  check.py            Local asset and route checks
```

Project content lives in `public/assets/js/app.js`. The slide deck uses the same project data. To export the deck, open the slides page and use its PDF export button.

## GitHub Pages

Create a public repository named `zekaemo.github.io` under the `zekaemo` account. Push this repository, then select **Settings → Pages → Source → GitHub Actions**. The included workflow publishes only `public/`.

This site uses root-relative URLs and is configured for the account site, `https://zekaemo.github.io/`. Hosting it under a repository subpath requires adjusting those URLs.

## Image credits

SAR figures: Windarto et al., *GA-SAR-Det* (2026), DOI [10.22266/ijies2026.0930.71](https://doi.org/10.22266/ijies2026.0930.71), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Figures are reproduced unchanged. Other project media comes from the supplied project documentation.
