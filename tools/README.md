# Audit tooling

The scripts that produced `content/records/` and the measurements behind the Socrata evaluations.
They are kept here so the numbers on the site can be reproduced, not because the site runs them.

    profile_dataset.py   download N rows of each dataset in a sample and profile it
    gen_records.py       merge catalogue metadata + profiles into content/records/*.md

Both expect working files (catalogue pulls, samples, profiles) alongside them; paths are at the top
of each script. The sample is drawn with a fixed seed so a re-run selects the same datasets.
