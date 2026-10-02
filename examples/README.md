# Examples

One week of output for a made-up family: Maya (Year 9) and Leo (Year 4), the children in [`config.example.yaml`](../config.example.yaml). Every name, mark and date here is invented.

| File | What | Who sees it |
|---|---|---|
| [`2026-10-11-weekly-report.md`](2026-10-11-weekly-report.md) ([PDF](2026-10-11-weekly-report.pdf)) | The Sunday report: summary, points, homework, topics, mismatches, school updates, next week | Parents |
| [`2026-10-11-quiz-maya.md`](2026-10-11-quiz-maya.md) ([PDF](2026-10-11-quiz-maya.pdf)) | Maya's 15 minute quiz, from the topics she logged this week plus one review topic | Maya |
| [`2026-10-11-answers-maya.md`](2026-10-11-answers-maya.md) ([PDF](2026-10-11-answers-maya.pdf)) | Answer key with topic tags and two reading questions to ask out loud | Parents |
| [`2026-10-11-quiz-leo.md`](2026-10-11-quiz-leo.md) ([PDF](2026-10-11-quiz-leo.pdf)) | Leo's 10 minute quiz | Leo |
| [`2026-10-11-answers-leo.md`](2026-10-11-answers-leo.md) ([PDF](2026-10-11-answers-leo.pdf)) | Leo's answer key | Parents |

Things to notice in the report:

- Maya scored 15, below the 16 target. The report says what happens next (a short catch-up before weekend screen time) and does not punish.
- Her Tuesday check-in says 25 minutes of reading but only 3 pages. The report shows the mismatch and leaves the score alone.
- A page gap in her reading log is flagged, with the two likely reasons.
- School updates are cut down to what concerns each child, with the date and the action.

Make the PDFs with:

```bash
for f in examples/*.md; do [ "$(basename "$f")" = README.md ] || python3 scripts/md2pdf.py "$f" "${f%.md}.pdf"; done
```
