# Databases

The system runs on six databases. The names and fields below are for Notion, but any database with forms works (Airtable, a spreadsheet behind a form). Create them in a private workspace that only the parents can open.

The children fill in **only** their own check-in form. They never get access to the databases themselves.

## 1. Daily check-in: older child

One row per day, filled in through a form.

| Field | Type | Notes |
|---|---|---|
| Date | Date | Defaults to today. If empty, the agent uses the submission time |
| Lessons today | Multi-select | The subjects on today's timetable, or all subjects if your form tool has no conditions |
| `<Subject>` topic | Select, one field per subject | Options come from this term's topic list (`config.yaml`) |
| `<Subject>` understood | Select, one field per subject | 1 not at all, 2 partly, 3 got it. Empty means unknown, not 3 |
| Homework done | Text | Platform, subject, score |
| Study minutes | Number | The study block |
| Book | Text | |
| Start page, end page | Number | The agent checks that the start page follows last time's end page |
| Reading minutes | Number | |
| Stuck on | Text | One question or topic. Goes onto the parents' stuck-on list |

Tip: children sometimes tick a subject they studied at home that day, not one they had at school. In reports, say "logged" rather than "taught at school".

## 2. Daily check-in: younger child

| Field | Type | Notes |
|---|---|---|
| Date | Date | |
| Study minutes | Number | Say in the question whether it includes maths practice, and keep it that way |
| Maths practice minutes | Number | |
| Spelling done | Checkbox | |
| School homework done | Checkbox | |
| Book, pages, reading minutes | Text, number, number | |
| Learned today | Text | One sentence |
| Stuck on | Text | |

## 3. Homework and tests

One row per piece of homework or test, for both children.

| Field | Type | Notes |
|---|---|---|
| Title | Title | |
| Child | Select | |
| Subject | Select | |
| Type | Select | Homework, test, project |
| Due | Date | |
| Status | Select | Not started, in progress, done, late |
| Score | Number | Percentage where the platform gives one |
| Source | Select | Check-in, school email, portal, by hand |
| Note | Text | For example the first attempt score |

## 4. Topics

One row per topic per subject, filled from the term's topic list.

| Field | Type | Notes |
|---|---|---|
| Topic | Title | |
| Child, subject, term | Select | |
| Status | Select | Not yet covered, in progress, needs review, known |
| Last self rating | Number | 1 to 3, from the check-in |
| Quiz results | Text | One line per week: date and right or wrong |
| Correct weeks | Number | A topic becomes **known** at 2 different weeks |

## 5. School updates

One row per thing school sent that matters to your family.

| Field | Type | Notes |
|---|---|---|
| Title | Title | |
| Received | Date | |
| School, child | Select | |
| Key date | Date | The trip, the deadline, the exam |
| To do | Text | Sign a form, pay, pack something |
| Summary | Text | Two lines at most |
| Status | Select | New, done, no action needed |
| Source | URL or text | The email or the newsletter |

The agent skips a row whose title is already there.

## 6. Weekly reports

One row per week. Only the parents can open it.

| Field | Type | Notes |
|---|---|---|
| Week | Title | For example "6 to 12 October" |
| Sunday | Date | |
| Points per child | Number, one field per child | |
| Sent | Checkbox | |
| Page content | | The full report, then the answer keys for that week's quiz. The marking step reads the keys from here |

## 7. Private parent notes

A single page, not a database. Only the parents can open it. See [`docs/privacy.md`](../../docs/privacy.md).
