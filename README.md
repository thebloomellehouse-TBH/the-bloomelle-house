# The Bloomelle House website

Static website (HTML, CSS and a little JavaScript). No build step.

## Files
- `index.html` : the whole website
- `assets/` : logo, hero video, hero poster and gallery photos
- `.nojekyll` : tells GitHub Pages to serve the files as they are

## Publish on GitHub Pages
1. Create a new public repository on github.com (for example `bloomelle-house`).
2. Click **Add file > Upload files** and drag in everything from this folder (`index.html`, `.nojekyll` and the `assets` folder). Click **Commit changes**.
3. Go to **Settings > Pages**. Under **Build and deployment**, set Source to **Deploy from a branch**, Branch to **main** and folder to **/ (root)**, then Save.
4. After a minute your site is live at `https://YOUR-USERNAME.github.io/bloomelle-house/`.

## Settings to edit
Near the bottom of `index.html`, find `var CFG = {` and update:
- `phone`: WhatsApp and call number with country code (currently 918318042886)
- `facebook` and `messenger`: replace `YOUR_FACEBOOK_PAGE_NAME` with your page name. Until then these icons stay hidden.
- `instagram`, `linkedin`, `youtube`, `reviews`: already set.

## Replace the photos
Swap the files in `assets/` with the same names (for example `bridal-after.jpg`) to change the gallery or hero video.

## Custom domain (thebloomellehouse.com)
`CNAME` already contains `thebloomellehouse.com`. In GoDaddy DNS add:
- 4 `A` records, Name `@`, Values `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
- 1 `CNAME` record, Name `www`, Value `YOUR-USERNAME.github.io`
Then in GitHub: Settings > Pages > Custom domain = `thebloomellehouse.com`, tick **Enforce HTTPS** once available.
