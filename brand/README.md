# Brand assets

`ministry-of-data-arms.png` is the master artwork: the full arms with the wordmark set
beneath, navy (#051A38) on transparency at 1536×1024.

It is dark ink on a transparent ground, so it is invisible composited on a dark
background — this is why the site is light. Everything in `static/logo/` is derived
from it:

    crest.png            arms only, no rule, no wordmark — masthead mask
    lockup@2x.png        the full lockup — hero and footer mask
    static/favicon.png   arms, squared and padded

The two logo files are used as CSS `mask-image` and filled with the current ink, so one
asset serves both light and dark. Sizes are chosen for the largest place each is drawn:
the crest never exceeds ~90px, the lockup reaches 480px in the hero.

To regenerate after editing the master:

    convert brand/ministry-of-data-arms.png -trim +repage /tmp/trim.png
    convert /tmp/trim.png -crop 1339x757+0+0 +repage -trim +repage /tmp/crest.png
    convert /tmp/crest.png -resize 320x  -strip -colors 48 static/logo/crest.png
    convert /tmp/trim.png  -resize 1120x -strip -colors 48 static/logo/lockup@2x.png
    convert /tmp/crest.png -resize 108x -background none -gravity center \
            -extent 128x128 -strip -colors 32 static/favicon.png
