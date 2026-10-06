# Design

How Fridge Door works, piece by piece. Every number here (minutes, points, times) is a starting value. Tune them to your family after the first two weeks of real data.

The examples use two children: an **older child** at secondary school and a **younger child** at primary school. Adapt the parts to your own kids' ages.

## Why this design

Most families try a tracking sheet first. It usually goes the same way: a burst of entries in the first weeks, then fewer, then none. Ask why and the answer is always some mix of these:

- The parent was the one doing the reminding. When the parent got busy, the reminders stopped.
- Filling it in was boring and took too long.
- Nobody checked what was written, so "done" stopped meaning anything.
- Nothing visible came out of it, for the child or the parents.

So the backbone of this design is to take reminding and checking away from the parent and give them to the system:

1. **Reminders are automatic**, never the parent.
2. **The daily record is short** (3 to 5 minutes), to keep it from being boring.
3. **Claims are verified** (a Sunday quiz and the school's own data). Saying "I did it" is not enough.
4. **The result is visible and rewarded** (a weekly points score). It rewards the process and never punishes.
5. **Parents only read the weekly summary** and set the goal for the coming week.

## Components

### 1. Daily check-in

One short form per child, filled in from a phone or tablet. Any form tool that writes into a database works (Notion, Airtable, Google Forms with a sheet behind it).

Older child:

- Date
- **Lessons today:** for each lesson, the topic covered (picked from this term's topic list) and how well it was understood (1: not at all, 2: partly, 3: got it)
- Homework done today: platform, subject, score or percentage
- Study block length (minutes)
- Reading: book, start and end page, minutes
- One question or topic I got stuck on (free text). It goes onto the stuck-on list for the parents, who pass it to whoever helps.

Younger child:

- Reading: book, pages, minutes
- Times tables or maths practice minutes
- Spelling done (yes or no)
- School homework done (yes or no)
- The thing I learned most today (one sentence)

Both children, optional and not scored:

- How I felt today (five options, from 😄 to 😢)
- What happened in my book today (one sentence)
- Who I spent time with today
- Something I want from my parents (help, a question, a request)

These keep the check-in from feeling like a test, and give the child a direct line to the parents. A request or a low mood reaches the parents the same evening.

If the form tool supports conditional questions, ask only about the lessons on today's timetable. If it does not, list all subjects and let the child fill in the ones they had.

### 2. Daily targets

| | Older child | Younger child |
|---|---|---|
| Weekday study block | 60 min: homework due soonest first, then review of today's lessons | 30 min: school homework, maths practice, spelling |
| Busy days (clubs, activities) | 30 min homework + 15 min reading | 20 min + 15 min reading |
| Reading | 25 min | 20 min |
| Homework rule | Finished at least one day before it is due | Weekly homework done by Sunday evening |
| Sunday | 15 min quiz + 10 min planning the week | 10 min quiz + planning the week |

### 3. Topic checkpoints

Knowing that homework was done is not the same as knowing a topic was understood. Four checkpoints close that gap:

1. **Daily topic log** (check-in): the topic covered and a self rating from 1 to 3.
2. **Sunday quiz:** 2 to 4 questions per subject, only from topics logged that week.
3. **The school's own measures:** class tests, end of term exams, homework platform scores.
4. **Review loop:** a topic that scores low goes onto next week's review list. A topic only counts as **known** after it is answered correctly in two different weeks.

The younger child gets a lighter version: a few reading and maths questions on Sunday.

### 4. Sunday quiz

1. On Sunday morning the agent sends the parents two documents per child: a printable quiz sheet, and an answer key with short explanations for the parents only.
2. The child answers on paper, at a shared table, without a phone (about 15 minutes). A parent is in the room as an invigilator: no questions, no debate. Paper and no phone also mean no asking an AI for the answers.
3. Most questions are multiple choice or short answer. A parent takes a photo of the sheet and sends it to the agent. The agent marks it and the result goes into the report. Fallback: the parent marks it with the answer key and enters the score in a short form.
4. Reading is the one exception: a parent asks two questions about the book out loud, as a chat rather than a test.
5. The result is not argued about at home. Low topics move to next week's review list on their own.

Why paper and not a spoken quiz: older kids' questions get technical fast. Asking them puts the parent in the examiner's chair, and the paper sheet stays as evidence.

### 5. Weekly points and rewards

- Each day: check-in +1, study block +2, reading target +1. At most 4 a day, 20 for a school week.
- Weekly bonus: all homework on time and complete, +3.
- **16 or more:** a weekend reward the child chose at the start of the week.
- **Below 16:** no punishment. Weekend screen time starts once the missing work is done ("responsibility first, then freedom"). Agree this rule with the child before you start.

The parents and the children set the reward list together. The report only says whether the target was reached.

### 6. Reminders

| When | To | What |
|---|---|---|
| Weekdays, after school | Each child | Today's tasks: today's lessons and upcoming deadlines |
| Every evening | Each child | Check-in reminder with the form link |
| Every evening, later | Parents | Who has not filled in the check-in yet, and a short note if a child asked for something, picked a low mood or complained about something. The same job also adds new homework and notices from the last two days of school email to the records, without sending anything |
| Monday morning | Each child | The week's plan: targets per day, short days, quiz time |
| Sunday morning | Parents | Weekly report, quiz sheets, answer keys |
| Sunday evening | Each child | Quiz time |

Rules for messages to children: short, positive, never blaming. The system reminds; the parent does not. Every new message text is approved by a parent before its first send.

### 7. School updates and the weekly calendar

Most of what school sends is noise for any one family, and the important bits hide inside it: a form due Friday, a trip that needs a packed lunch, an exam date moved. Every evening a short sweep adds new homework, tests and forms to the records, so the Monday plan and the daily reminders see them the same week. Each week the agent:

- Reads that week's school emails and newsletters.
- Keeps only what concerns your children: dates, exams, trips, events, forms, payments, and any message about your child (awards, absences, incidents).
- Turns dates into events in the family calendar.
- Lists the coming week's events, deadlines and forms in the report, so that nothing lives only in an inbox.

### 8. Weekly report

Every Sunday, one page per child:

- Points table, day by day
- Total study and reading minutes, pages read
- Homework status: what the child logged, checked against the school's own data where you have it
- Topics: covered, self ratings, quiz results, waiting for review
- In their own words: requests, complaints and low days from the check-ins
- From school: updates that concern this child
- Next week: events, deadlines, forms and payments
- Things to watch, and a suggested goal for the week

The report is saved as Markdown and PDF and shared with the parents as a link or a file.

## Architecture

### Inputs, agent, outputs

| Layer | Parts |
|---|---|
| Inputs | Daily check-in database, school email inbox, parent portals, school calendar and newsletters, the quiz photo |
| Agent | An AI agent with skills for: reading the inbox, checking portals, writing the quiz and the answer key, marking the quiz, writing the report |
| Outputs | Messages to children and parents, report and quiz PDFs, calendar events, the review list |

### Messaging

Reminders go through a small `notifier` interface with one adapter per app, so the rest of the system calls `send(to, text)` and does not care which app is behind it.

| App | Notes |
|---|---|
| Telegram | Recommended default. Official bot API, free, easy to set up |
| Discord | Official bot API, free. Good if the kids already use it |
| WhatsApp | Use only the official WhatsApp Business Platform. Unofficial bridges break WhatsApp's terms and can get the account banned |

### Reading school email

Most school systems send their updates by email, so the inbox is the richest input. Give the agent **read-only** access to the inbox the school writes to (for Gmail, the API with a read-only scope). Two things to expect:

- Some school messaging systems put the full text only in the HTML part of the email, and a placeholder in the plain text part. Read the HTML.
- Newsletters often arrive as a link or a PDF attachment, not as text in the email.
- School portals often ship parent accounts with email notifications switched off. At setup, open the notification settings of every parent account and turn on new homework, missed homework, grades and notices. Otherwise the homework never reaches the inbox.
- Do not leave the inbox for the weekly report alone. Homework set on a Tuesday and due on Thursday is gone before Sunday, and a weekly plan built from the records never sees it. Sweep the inbox every evening and add only what is missing: if a record with the same title exists, skip it. When an email names the task but not the due date, leave the date empty rather than guess.

### Parent portals

Schools use homework and learning platforms with a parent or student view. Most have no public API. The agent can still read **what you, the parent, can already see**: a **browser agent** (an AI driving a real browser, such as Claude in Chrome or a Playwright script) opens the portal with your own login, reads the dashboard and writes down the numbers.

Ground rules:

- Only accounts you legitimately own, and only what the parent view shows you.
- Read the platform's terms first. Many forbid automated access. If yours does, check it by hand once a week and type the numbers into the check-in.
- Never work around bot protection, CAPTCHAs or rate limits. If the site pushes back, stop.
- Never call a platform's private internal API.
- Keep logins in a password manager, never in this repository or in prompts.

This repository describes the pattern and does not ship scrapers for any specific platform.

### Where things run

An AI agent does not run in the background on its own. Something has to wake it up. Three layers, each with a job:

| Layer | Does | Notes |
|---|---|---|
| Small always-on server (a cheap VM) | Fixed reminders on a schedule (cron) | Reliable, cheap, needs no AI |
| The family computer | Agent jobs: reading email, checking portals, the report, the quiz | Has your logins and the browser. Must be awake at that time |
| A cloud agent | Backup when the computer is off | Usually cannot reach your local logins or browser |

Start by running the weekly report by hand on Sunday. Once the steps settle, turn them into a skill, then schedule it.

## Data sources and trust

| Source | How | Trust |
|---|---|---|
| Daily check-in | Database | A claim, checked by the quiz |
| Sunday quiz | Paper, marked by the agent or a parent | High for that week's topics |
| School emails (absences, awards, notices) | Inbox | High |
| Newsletters | Email link or PDF | High, may arrive a few days late |
| Homework platforms | Parent view, by browser agent or by hand | Depends on the platform. A tick the child can set themselves is not proof |
| Timetable | Once per term, by hand | Manual |

## Privacy

The data in this system is about children. Keep it with the family:

- Reports, quiz sheets and photos stay in your own storage, outside any public repository.
- Private parent notes (anything meant for the parents only) never appear in anything sent to a child or in a shared link.
- Shared report links never contain passwords or links to where passwords live.
- Everything sent to an AI model is about your own children, for your own family's use.

See [`docs/privacy.md`](privacy.md) for the full checklist.

## Phases

1. **Basics:** check-in forms, database, fixed reminders.
2. **Report:** the weekly report and the Sunday quiz, run by hand at first.
3. **Checks:** missing check-in alert, nightly inbox sweep into the homework records (full read in the weekly report), homework platform checks.
4. **Tuning:** adjust targets and times after two weeks of data.
