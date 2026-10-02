# Privacy

fridge-door handles data about children: their school, their marks, what they find hard, and notes that only parents should see. Treat it the way you would treat their medical records. This page is the checklist to set it up that way.

## Where data lives

| Data | Where | Never |
|---|---|---|
| Daily check-ins, homework, topics | Your own database (for example a private Notion workspace) | In a public page or a public repository |
| Weekly reports, quiz sheets, answer keys, quiz photos | Your own storage (a private cloud folder or the family computer) | In git. The `.gitignore` in this repository excludes `reports/` for this reason |
| Logins for school portals and platforms | A password manager | In config files, prompts, reports, or shared links |
| Private parent notes | One page only the parents can open | Anywhere a child or anyone else can see it |

If you fork this repository to build your own system, keep your fork **private**. Your config file names your children, their schools and their timetable.

## Private parent notes

Some notes are for the parents only, such as feedback from school or the parents' own worries. Keep these in a separate page that only the parents can open, and give the agent one rule:

> Nothing from the private parent notes ever appears in a message, form, quiz or shared link that a child can see. The weekly report goes to the parents only, and even there it does not repeat a private note unless it is needed.

## What goes to the children

- Only messages the parents have approved. Every new message text is approved before its first send.
- Quiz sheets only, never answer keys.
- Short, positive, never blaming. The report and the scores are for the parents. Talk about them with your child; do not forward them.

## Shared links

Partners who do not use your database often read the report through a shared link. Before you share:

- No passwords and no links to where passwords live.
- No private parent notes.
- Prefer links that only the people you send them to can open. A "public with the link" page can be forwarded.

## Sending data to an AI model

The agent reads your children's check-ins, school emails and quiz photos, and that data goes to the AI model you use.

- Read your AI provider's data policy and choose the settings that fit your family (for example, whether your conversations may be used for training).
- Give the agent access only to what it needs: a read-only scope for email, only the databases of this system, only the folders it writes reports into.
- Use it for your own children only. Do not add other children's data, such as a class list or a friend's marks.

## Talking with your kids about it

A system that watches homework can feel like surveillance to a child. It works much better as an agreement:

- Explain why: fewer reminders from you, fewer arguments at home.
- Agree the targets, the points and the rewards together before you start.
- Let them see their own scores and their own review list.
- Promise what the system will not do (for example, read their private messages) and keep that promise.

## Before you share anything publicly

If you write about your own setup (a blog post, a talk, a screenshot), check that it contains no names, schools, class codes, phone numbers, group ids, database ids or real marks. Use made-up data, like the examples in this repository.

## Not legal advice

This page is a practical checklist, not legal advice. Data protection rules for children's data differ by country. Check the rules where you live, your school's own policies, and the terms of every service you connect.
