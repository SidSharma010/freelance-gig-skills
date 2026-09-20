---
name: proposal-writer
description: "Write a tailored freelance proposal, cover letter, or bid for a specific job post on Upwork, Fiverr (buyer requests), Freelancer.com, or any other platform. Triggers on \"write a proposal\", \"cover letter for this job\", \"bid on this\", \"pitch for this gig\", \"apply to this job post\". Not for rewriting a profile/portfolio (use portfolio-optimizer), not for pricing a job (use pricing-advisor), not for following up on a proposal already sent (use followup-drafter)."
---

# Proposal Writer

Turn a job post into a proposal that reads like it was written by someone who
actually read the job post — not a template with the client's name pasted in.

## When to use

- User pastes a job post (or its text/URL) and wants a proposal, cover letter,
  or bid drafted
- User says "help me pitch for this", "write my Upwork proposal", "respond to
  this buyer request", "bid on this Freelancer.com project"

## Input

- The job post text (paste, screenshot description, or URL if reachable)
- Platform: Upwork / Fiverr / Freelancer.com / other — ask if not stated,
  since format rules differ (see Platform rules below)
- Optional: the freelancer's relevant past work/experience to draw on. If
  none is given, ask for one real, specific detail rather than inventing one
  — a fabricated project name or result is the fastest way to lose a client's
  trust the moment they ask a follow-up question.

## Steps

1. **Read the job post closely.** Pull out: the actual problem they're
   solving (not just the skill list), any specifics they mention (a tool
   name, a deadline, a budget range, a phrase repeated twice), and what kind
   of client this is (first-timer vs. experienced hirer — tone differs).
2. **Pick one real hook.** The opening line should prove you read *this*
   post, not a generic one — reference the specific problem or a detail only
   someone who read it closely would mention. Never open with "I am
   excited to apply" or a restatement of the job title.
3. **Draft the proposal** following the platform's format rules (below).
4. **One clear next step.** End with a specific, low-friction CTA — a
   question about their setup, or an offer to start with a small first step
   — not "Let me know if interested."
5. **Show the draft** with a one-line note on which detail from the job post
   the hook is built on, so the user can swap it if the real experience
   doesn't back it up.

## Platform rules

### Upwork
- Cover letter, not a resume restatement — Upwork already shows the client
  your profile and work history.
- First 2-3 lines matter most: Upwork truncates the preview before "see
  more" on mobile.
- Mention connects efficiently — don't waste the message re-explaining
  skills visible on the profile.
- 150-300 words. Longer only for complex/technical jobs where depth signals
  competence.
- End with a specific question about their project, not a generic sign-off.

### Fiverr (buyer requests)
- Much shorter — buyer requests are skimmed fast among dozens of responses.
  50-120 words.
- Lead with the outcome you'd deliver, not your bio.
- Reference their stated budget/timeline directly if given; flag politely if
  the scope doesn't fit the stated budget rather than staying silent about it.
- No generic "Hi, I can do this for you" — name the specific deliverable.

### Freelancer.com
- Bid format expects a price and timeframe stated up front, then the pitch.
- Slightly more formal tone than Upwork/Fiverr; Freelancer.com's client base
  skews toward agencies and repeat outsourcers.
- Milestone-oriented language works well — break the deliverable into 2-3
  checkpoints if the scope supports it.

### Generic / other platforms
- Default to Upwork-style structure (hook → relevant proof → CTA) unless the
  user describes a different norm for that platform.
- Always ask which platform if truly ambiguous — the same proposal text
  posted on the wrong platform reads as copy-pasted spam.

## Hard rules

- Never invent a specific number, client name, or project result that the
  user hasn't given you. A vague-but-true line beats a specific-but-fake one.
- Never use "Dear Sir/Madam", "To whom it may concern", or any salutation
  that signals a mass-sent template.
- Mention the client's actual problem before mentioning your own skills.
- No more than one exclamation point per proposal, if any.
- Keep to the platform's expected length — a 400-word Fiverr buyer request
  response won't get read.

## Anti-patterns (skill will refuse)

- "I have read your job posting and I am very interested" — the single most
  recognized copy-paste opener on every platform
- Bullet-listing every skill from the user's profile regardless of relevance
  to this specific job
- Promising a turnaround time or price the user hasn't confirmed
- Generic flattery ("Your project sounds amazing!") with nothing concrete
  behind it
- Padding word count to look thorough on a platform that rewards brevity
  (Fiverr buyer requests especially)

## Output shape

1. The drafted proposal, ready to paste
2. Word/character count against the platform's norm
3. One line noting which real detail the hook draws on (so the user can
   verify or swap it before sending)
4. If no real supporting detail was given, a note saying so plainly rather
   than silently filling the gap


## Resources

- `../../references/platform-formats.md` — consolidated platform specs
  (length norms, fee structure, client-visibility notes) — keep this file
  as the source of truth if platform details ever need updating, rather
  than editing the per-platform notes above and here separately.
- `../../lib/check_proposal.py` — run a finished draft through this before
  sending: `python lib/check_proposal.py --platform upwork draft.txt`. It
  mechanically checks length and flags banned template phrases. It does
  not replace reading the draft yourself.
- `../../examples/upwork-example.md` — a worked weak-vs-strong example.
  Use it as a quality bar: a real draft that reads closer to the weak
  example than the strong one means this skill needs tightening.
