---
name: weekly-report
description: Prepares the Sunday weekly school report for parents and each child's Sunday quiz with its answer key, from the family's daily check-ins, homework records, school emails and school updates, and marks a quiz from a photo of the answer sheet. Part of Fridge Door, an agentic workflow for busy parents. Use whenever the parents ask for the weekly report, the Sunday quiz, or to mark a quiz. Triggers on "weekly report", "sunday report", "prepare the quiz", "make the quiz", "mark the quiz", "score this quiz", "how did the kids do this week".
---

# Weekly report and Sunday quiz

Reads `config.yaml` (copied from `config.example.yaml`) for the children, targets, points, sources and storage folder. The design behind every step is in `docs/design.md` of the Fridge Door repository.

Two modes:

- **A. Prepare** the report and the quiz (Sunday, the default).
- **B. Mark** a quiz (when a parent sends a photo of the answer sheet, or typed answers).

## Rules that never change

- **Private parent notes never reach a child.** The report goes to the parents only, and even there it does not repeat a private note unless it is needed. See `docs/privacy.md`.
- **Answer keys go to the parents only.** Children get quiz sheets, nothing else from this skill.
- **Never invent data.** No data means "no data". Anything you could not check is marked "not verified".
- **Never change a score to punish a mismatch.** Show it; the parents decide.
- **Never touch passwords** or the page where they are kept.
- **Phone friendly:** every message is short bullet lines with blank lines between sections. Parents often read it on a phone.
- Dates are absolute ("12 October"), never relative ("last Tuesday").

## A. Prepare the report and the quiz

### 1. Pick the week

The week is Monday to Sunday ending on the report's Sunday, in `family.timezone`. Name files with that Sunday's date: `<reports_dir>/YYYY-MM-DD-...`. If today is not Sunday, or it is too late for the quiz to be taken today, skip the quiz, prepare only the report and say so in it.

### 2. Collect

1. **Daily check-ins** for each child. Use the `Date` field, or the submission time when it is empty. If a day has several entries, the last one counts, and the report notes it. A check-in counts for points once a day.
   - An empty "understood" field means unknown, never 3.
   - A ticked subject means "logged", not "taught at school": children also tick subjects they studied at home.
   - The optional fields (mood, what happened in my book, who I spent time with, something I want from my parents) are never scored. An empty one means nothing.
   - If "what happened in my book" repeats the same sentence for days, or the pages do not move, list it under mismatches.
2. **Homework and tests:** everything due this week and in the next 7 days.
3. **School email** from the last 8 days, from the senders in `sources.email.school_senders`, read-only. Look for: homework platform summaries, awards, absences, incidents, forms, trips, payments, newsletters. Some school systems keep the full text only in the HTML part of the email. Newsletters are often a link or a PDF.
4. **Parent portals,** only as configured in `sources.parent_portals`:
   - `by_hand`: do not open the site. Use what the parents typed into the homework database.
   - `browser_agent`: open the parent view in the parents' own logged-in browser, read only, click nothing that changes anything (no forms, no "mark as read" if avoidable). If the site asks for a login, shows a bot check or refuses, stop and write "portal not checked" in the data notes. Never try to get around it.
5. **School updates:** add each item that matters (form, payment, trip, exam date, event) as a row in the School updates database, skipping titles already there. Put key dates into the family calendar if one is configured.
6. **Topics:** everything marked "needs review", and every topic logged this week.

### 3. Score the week (Monday to Friday)

Per child, per day, with the child's `targets`, and the `short_day` targets on their `short_days`:

| Item | Points |
|---|---|
| Check-in filled in | `points.per_day.check_in` |
| Study minutes at or above target | `points.per_day.study_block` |
| Reading minutes at or above target | `points.per_day.reading` |

**Weekly bonus** (`points.weekly_bonus`): every piece of homework due this week done on time and complete. If you cannot verify it, write "bonus not verified" and do not award it.

**Mismatch check:** compare what the child logged with the school's own data (the check-in says "done" but the platform shows the homework not started; the start page does not follow last time's end page; minutes that do not add up). List mismatches in their own section. Do not change the score.

### 4. Update topics

For each topic logged this week, find or add its row: "not yet covered" becomes "in progress", and the last self rating is updated. Only mode B moves a topic to "known".

### 5. Write the quiz

Per child, with the child's `quiz` settings:

- **Where the topics come from,** in this order: topics logged this week; topics marked "needs review" (at least one question each); next week's tests; and if there is nothing else, this half term's topics from the topic list.
- **Questions:** 2 to 4 per subject. Mostly multiple choice or short answer, with one or two short written answers. Pitch them at the child's year and level.
- **Tag every question** with subject and topic, for example `[Science · Atoms and ions]`. Marking uses the tags.
- **Number the questions with the child's prefix** from `config.yaml` (for example `M1, M2 ...` and `L1, L2 ...`). Put the child's name in large letters at the top and at the start of each block of questions, and end with "Last question: M15". A photo of any single page then shows whose it is and whether a page is missing.

**Reading:** at the end of each answer key, add two questions about the child's current book for a parent to ask **out loud**, as a chat.

Files, in `storage.reports_dir`:

- `YYYY-MM-DD-quiz-<child id>.md` and `.pdf`: name, date, "N minutes, no phone", questions and space for answers. No answers.
- `YYYY-MM-DD-answers-<child id>.md` and `.pdf`: each question's answer, a short explanation, its tag, and the two reading questions.

### 6. Write the report

`YYYY-MM-DD-weekly-report.md` and `.pdf`:

1. **Summary, at the top, five bullets:** the best news, the main thing to watch, next week's tests, the points, a suggested goal for the week.
2. **Points table:** per child, day by day, the total, the bonus, and whether the reward threshold was reached.
3. **Study and reading:** total minutes, pages, the book.
4. **Homework:** due this week, status, scores, anything late. Leave out items that are not really homework (club sign-ups, surveys).
5. **Topics:** what was logged, self ratings, waiting for review.
6. **Mismatches.**
7. **In their own words:** what each child told the parents through the check-in, so that a request or a complaint gets an answer that week. Per child:
   - Requests from "something I want from my parents", with the date, in the child's own words.
   - Complaints and problems written in any field (about the form, an app that does not work, school, friends). Children often write these in the wrong field, so read all of them.
   - Questions that were clearly misunderstood: the answer does not fit the question. The form may need a clearer question.
   - The week's moods in one line, for example "😄 2, 🙂 2, 😕 1 (Thursday)". Two or more low days go into the summary too.
   - If there is nothing: "No requests or complaints this week."
8. **From school:** updates that concern each child, newest and still to do first.
9. **Next week:** tests, deadlines, events, forms, payments.
10. **Data notes:** which sources you could check and which you could not.

If a child asked for something or complained, add it to the summary as one bullet: many parents only read the summary.

Keep it short. Someone will read it on a phone.

### 7. Save and send

- Add a row to Weekly reports with the week, the Sunday, the points and `Sent` unticked. Put the report in the row's page, followed by the full answer keys under the headings "Answer key: `<child>`". Mode B reads the keys from here, so marking still works if the files are gone.
- Send the parents' group the report summary, the report PDF, the quiz sheets and the answer keys through the configured `messaging.app`. Then tick `Sent`.
- Nothing goes to the children from this skill. Their "quiz time" message is a separate scheduled reminder.

## B. Mark a quiz

1. Read the photo (or the typed answers). Use the question prefix to tell which child and which questions. If "Last question" is not visible, ask whether a page is missing before marking.
2. Read that week's answer key from the Weekly reports row.
3. Mark each question right, partly right or wrong. Be fair to handwriting and to answers that are right in different words.
4. Per topic: a right answer adds the week to the topic's quiz results. A topic reaches **known** after right answers in two different weeks. A wrong answer sets it to "needs review" and puts it on next week's review list.
5. Send the parents a short result: score per child, the topics to review next week, one thing to praise. Do not send results to the children; the parents talk about it with them.
