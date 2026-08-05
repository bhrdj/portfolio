# Steven Bhardwaj's Full-Stack Data Science Portfolio

### Portfolio portal links:
- portfolio webpage
  - [portfolio.bhrdwj.net](https://portfolio.bhrdwj.net)
- web resume
  - [resume.bhrdwj.net](https://resume.bhrdwj.net) 

---

### Purpose-built Web Framework
- This portfolio is custom html using a bootswatch theme.
- I built a basic python web framework in a [notebook](/gen_html/gen_html.ipynb) to maintain and update it.

### Regenerating the one-page PDF

`Bhardwaj_Resume.pdf` is rendered from `index.html` — the `@media print` block in
`styles.css` is the only place page geometry lives, so the web and PDF versions
can't drift:

    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
      --headless --disable-gpu --no-pdf-header-footer \
      --print-to-pdf=Bhardwaj_Resume.pdf file://$PWD/index.html

The print base font-size (9.6pt) is tuned to fill exactly one letter page; 9.7pt
spills onto a second. Re-check the page count after editing content.
