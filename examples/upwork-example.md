# Worked example — Upwork proposal

A concrete before/after so the skill's quality has an anchor, not just
abstract rules. This is the kind of test case `proposal-writer` should be
checked against — run it yourself with real job posts and compare.

## The job post (hypothetical, for illustration)

> **Fix slow-loading WordPress site**
> Our WooCommerce store takes 8-12 seconds to load on mobile. We've tried a
> caching plugin already, didn't help much. Need someone to actually
> diagnose what's slow and fix it, not just install another plugin. Budget:
> $200-400, ideally done this week.

## Weak proposal (what proposal-writer should never produce)

> Hi, I have read your job posting and I am very interested. I am a
> hardworking, detail-oriented WordPress developer with 5 years of
> experience. I can definitely help speed up your website. I have worked
> on many similar projects and gotten great results for my clients. Please
> let me know if interested and we can discuss further. Looking forward to
> hearing from you!

**Why this fails**: generic opener from the banned-phrases list, no
engagement with the specific detail (caching plugin already tried and
didn't help), no plan, vague "great results" with no specifics, weak CTA.
Run through `lib/check_proposal.py --platform upwork` and it would flag the
opener phrase and the "hardworking, detail-oriented" phrase immediately.

## Strong proposal (what it should produce instead)

> A caching plugin alone won't fix an 8-12 second WooCommerce load time if
> the actual bottleneck is unoptimized database queries or unoptimized
> product images — caching just delays when you notice the problem again.
>
> Before touching any plugins, I'd run a proper diagnostic first: GTmetrix
> waterfall plus a look at your slow query log, to find out whether this is
> a hosting/database issue, an image weight issue, or plugin bloat from
> everything installed so far. That tells us what's actually worth fixing
> versus what's noise.
>
> Given the $200-400 range and this-week timeline, I'd scope it as: 1)
> diagnostic + findings write-up (fast, tells us the real problem), 2) fix
> the top 2-3 issues found, 3) re-test and confirm the improvement with
> numbers, not just "feels faster."
>
> Quick question before I bid the full amount — do you have server access
> (hosting control panel) you can share, or is this WordPress-admin-only
> access? That changes what's fixable in this budget.

**Why this works**: opens with a specific technical claim that proves the
post was actually read (the caching-didn't-help detail), proposes a real
method instead of "I'll fix it", scopes to the stated budget/timeline
explicitly, and the CTA is a real, specific, answerable question — not
"let me know if interested."

## How to use this file

If a real draft from `proposal-writer` reads closer to the weak example
than the strong one, that's a signal the skill needs tightening — open an
issue or just note what went wrong and fix the relevant SKILL.md section.
