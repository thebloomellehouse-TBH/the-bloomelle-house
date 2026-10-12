#!/usr/bin/env python3
"""Run inside your website folder (next to index.html):  python3 update_site.py
Updates favicon, header logo and share image in EVERY .html file (index, service pages, blogs, sitemap).
Originals are saved in ./backup_before_logo/ first. Safe to run more than once."""
import re, glob, os, shutil

HEAD = '''<!-- Favicon / app icon -->
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<meta name="theme-color" content="#3a0718">
'''
os.makedirs('backup_before_logo', exist_ok=True)
for p in sorted(glob.glob('**/*.html', recursive=True)):
    if p.startswith('backup_before_logo'): continue
    s = open(p, encoding='utf-8').read(); o = s
    shutil.copy(p, os.path.join('backup_before_logo', p.replace(os.sep, '_')))
    # 1 favicon block
    s = re.sub(r'<!--\s*Favicon[^>]*-->\s*', '', s)
    s = re.sub(r'<link[^>]+rel="(?:shortcut icon|icon|apple-touch-icon|manifest)"[^>]*>\s*', '', s)
    s = re.sub(r'<meta[^>]+name="theme-color"[^>]*>\s*', '', s)
    s = s.replace('</head>', HEAD + '</head>', 1)
    # 2 header logo -> emblem (inside <a class="...logo...">)
    s = re.sub(r'(<a[^>]*class="[^"]*\blogo\b[^"]*"[^>]*>\s*<img[^>]*?src=")([^"]*?)logo(?:-emblem)?\.png',
               r'\1\2logo-emblem.png', s)
    # remove the old extra ring (new logo already has one)
    s = s.replace('.logo img{width:44px;height:44px;border-radius:50%;border:1.5px solid var(--rose)}',
                  '.logo img{width:44px;height:44px;border-radius:50%}')
    # 3 share image
    s = re.sub(r'(<meta property="og:image" content=")[^"]*(")',
               r'\1https://thebloomellehouse.com/assets/og-image.png\2', s)
    if '"og:image"' in s and 'og:image:width' not in s:
        s = s.replace('<meta property="og:image" content="https://thebloomellehouse.com/assets/og-image.png">',
            '<meta property="og:image" content="https://thebloomellehouse.com/assets/og-image.png">\n<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="630">')
    open(p, 'w', encoding='utf-8').write(s)
    print(('updated  ' if s != o else 'no change ') + p)
