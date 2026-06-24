# Make `bhrdwj.net` the canonical site (keep `bhrdwj.net` in the URL)

Goal: serve the GitHub Pages site at the apex `bhrdwj.net` so the address bar
shows `bhrdwj.net` (no redirect to `portfolio.bhrdwj.net`). After this,
`portfolio.bhrdwj.net` 301-redirects up to the apex.

Why not "redirect bhrdwj.net → portfolio.bhrdwj.net": a redirect changes the
URL. To keep `bhrdwj.net` in the URL it must *be* the canonical Pages domain.

## Current state

- `portfolio.bhrdwj.net` → CNAME `bhrdj.github.io` → GitHub Pages (working).
- `bhrdwj.net` (apex) → `217.70.184.55` (Gandi, not GitHub Pages).
- Repo `CNAME` file = `portfolio.bhrdwj.net` (current canonical domain).

## Order matters

Do DNS first. If you flip the canonical domain before the apex DNS is live,
`portfolio.bhrdwj.net` starts redirecting to an apex that isn't serving yet.

## 1. Point the apex DNS at GitHub (Gandi LiveDNS)

Apex domains can't use a CNAME record, so use A (and optionally AAAA) records.

Remove the existing Gandi record:

```
@ ... IN A 217.70.184.55      <-- delete this
```

Add GitHub's four IPv4 A records:

```
@ 10800 IN A 185.199.108.153
@ 10800 IN A 185.199.109.153
@ 10800 IN A 185.199.110.153
@ 10800 IN A 185.199.111.153
```

Optionally add the four IPv6 AAAA records:

```
@ 10800 IN AAAA 2606:50c0:8000::153
@ 10800 IN AAAA 2606:50c0:8001::153
@ 10800 IN AAAA 2606:50c0:8002::153
@ 10800 IN AAAA 2606:50c0:8003::153
```

Leave `portfolio.bhrdwj.net`'s CNAME → `bhrdj.github.io` as-is.

(TTL `10800` = 3h is fine. Drop to `300` while testing for faster propagation,
then raise it back.)

## 2. Verify propagation

```
dig +short bhrdwj.net A      # should show the 185.199.x set, not 217.70.184.55
dig +short bhrdwj.net AAAA   # should show the 2606:50c0:800x::153 set (if added)
```

## 3. Flip the canonical domain to the apex

Only after step 2 confirms the apex resolves to GitHub.

- GitHub repo → Settings → Pages → Custom domain → set to `bhrdwj.net` → Save.
  This rewrites the repo `CNAME` file and re-provisions the HTTPS cert.
- Or edit the repo `CNAME` file directly to contain `bhrdwj.net`.

Wait for "Enforce HTTPS" to become available again (cert re-issue can take a few
minutes to ~an hour).

## Result

- `https://bhrdwj.net` serves the site, URL stays `bhrdwj.net`.
- `https://portfolio.bhrdwj.net` 301-redirects to `https://bhrdwj.net`.

## Avoid

iframe/proxy "cloaking" (URL stays put but content loaded from elsewhere) —
breaks HTTPS, SEO, and bookmarking. Don't.
