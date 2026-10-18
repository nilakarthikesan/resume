# Nila Karthikesan - Public Resume

The public resume is [Resume_Official.pdf](Resume_Official.pdf). `index.html`
redirects visitors to that PDF; it does not contain the resume's content.

The editable source is `resume.json`, and `build_resume.py` renders the PDF using
ReportLab. The October 18, 2026 revision leads with selected AI safety and
evaluation work while retaining the existing professional roles and dates.
SafeLattice metrics are scoped to its saved six-model study; Never Trust the
Context describes an implemented ten-pair scoring prototype, not a measured
live-model defense. The grasp-recovery entry preserves the preliminary
simulation-only negative finding, and the GTSfM entry retains the ECCV 2026
SfM-DL workshop coauthor credit. New synthetic evaluation work is one short
in-progress line rather than separate unvalidated research results. See
[claim evidence](evidence/resume-claims-2026-10-18.md) for sources and limitations.

The build embeds Times New Roman on macOS or Liberation Serif on Linux when
those fonts are installed. It falls back to standard PDF Times fonts otherwise.

## Update and rebuild

1. Edit `resume.json` with verified experience or project contributions.
2. Install the build dependency and regenerate the PDF:

   ```bash
   python3 -m venv .venv
   .venv/bin/python -m pip install -r requirements.txt
   .venv/bin/python build_resume.py
   ```

3. Render and inspect the complete PDF before publishing. Confirm the text is
   legible, the document stays on one page, links open the intended destinations,
   and project claims match the referenced repository's current status.
4. Commit the source and generated PDF together. Editing the source alone does
   not update the served resume.

## Local preview

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

Open [http://localhost:8000](http://localhost:8000). The
[GitHub profile](https://github.com/nilakarthikesan) contains links to the project
repositories.
