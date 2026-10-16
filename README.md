# Nila Karthikesan - Public Resume

The public resume is [Resume_Official.pdf](Resume_Official.pdf). `index.html`
redirects visitors to that PDF; it does not contain the resume's content.

The editable source is `resume.json`, and `build_resume.py` renders the PDF using
ReportLab. Existing content was retained from the repository's previous PDF,
except the Georgia Tech research description and paper attribution were updated
to reflect the current [GTSfM](https://github.com/borglab/gtsfm) contribution and
ECCV 2026 SfM-DL workshop paper. The **Grasp Recovery under Delayed Feedback** entry now describes an implemented MuJoCo pilot with released branch data and episode-clustered evaluation. Results are preliminary and simulation only; latency-aware selection did not improve completion over its latency-agnostic baseline. Source evidence: [pilot report](https://github.com/nilakarthikesan/grasp-recovery-under-delayed-feedback/blob/54aa4b1c6c3e7c0aba5de881ea3025954090e6a0/results/pilot_v1/report.json).

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
