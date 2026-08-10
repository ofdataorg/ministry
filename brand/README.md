# Brand assets

`ministry-of-data-arms.png` is the master artwork: the full arms with the wordmark set
beneath, navy (#051A38) on transparency at 1536×1024.

It is dark ink on a transparent ground, so it is invisible composited on a dark
background — this is why the site is light. Everything in `static/logo/` is derived
from it:

    crest.png / crest@2x.png     arms only, no rule, no wordmark — masthead
    lockup.png / lockup@2x.png   the full lockup — hero and footer
    static/favicon.png           arms, squared and padded

To regenerate after editing the master:

    convert brand/ministry-of-data-arms.png -trim +repage /tmp/trim.png
    convert /tmp/trim.png -crop 1339x757+0+0 +repage -trim +repage /tmp/crest.png
    convert /tmp/crest.png -resize 320x  -strip -colors 48 static/logo/crest.png
    convert /tmp/crest.png -resize 640x  -strip -colors 48 static/logo/crest@2x.png
    convert /tmp/trim.png  -resize 560x  -strip -colors 48 static/logo/lockup.png
    convert /tmp/trim.png  -resize 1120x -strip -colors 48 static/logo/lockup@2x.png
    convert /tmp/crest.png -resize 108x -background none -gravity center \
            -extent 128x128 -strip -colors 32 static/favicon.png
