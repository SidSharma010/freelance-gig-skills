---
name: pricing-advisor
description: "Suggest how to price a specific gig, bid, or hourly rate based on the job's scope, the client's budget signals, and the platform's norms. Triggers on \"how much should I charge\", \"price this job\", \"is this budget fair\", \"what should my hourly rate be\". Not for writing the pitch itself (use proposal-writer)."
---

# Pricing Advisor

Freelancers usually either underprice out of fear of losing the bid, or
guess a round number with no reasoning behind it. This skill reasons through
a specific price from the actual scope, then explains the reasoning — not
just a number, so the user can defend it if a client pushes back.

## When to use

- User pastes a job post and asks what to charge or bid
- User asks whether a stated client budget is reasonable for the scope
- User wants help setting a base hourly or project rate for their profile

## Input

- The job post or scope description
- Platform (Upwork hourly vs. fixed, Fiverr package tiers, Freelancer.com bid)
- The user's experience level and existing rate, if any (don't assume —
  ask, since a fair rate depends heavily on where they already are)
- Their target market if known (e.g. US/EU clients vs. price-sensitive
  markets — this materially changes what's a reasonable ask)

## Steps

1. **Break the scope into real units of work.** Vague scopes ("build me a
   website") hide the actual hours; ask what's really included if unclear
   (pages, revisions, content written or supplied, ongoing support).
2. **Estimate effort honestly**, not optimistically — first-time scope
   estimates from freelancers are almost always too low; flag this
   explicitly rather than reinforcing an underestimate.
3. **Reason in a range, not a single number.** Give a floor (what covers
   the time at a fair rate) and a target (what a confident, in-demand
   freelancer would ask), with the reasoning shown, not just the numbers.
4. **Check platform fit.** A price that's fair in isolation can still be
   wrong for the platform's norms and the specific client's signals (a
   budget range stated in the post, their hiring history if visible,
   how many proposals are already in).
5. **Flag scope creep risk.** If the job post is vague or the deliverable
   list keeps growing, say so — this is often where underpricing actually
   happens (a fair initial price, then unpaid extra rounds).

## Platform notes

- **Upwork hourly**: platform takes a service fee that scales down with
  lifetime billings per client — factor this into the effective take-home
  when suggesting a rate, especially for a first job with a new client.
- **Upwork fixed-price**: milestone it if the scope allows — reduces risk
  of doing the full job before any payment.
- **Fiverr**: price in tiers (Basic/Standard/Premium) — the middle tier is
  usually what gets chosen most; price it as the "real" offer and use Basic
  to capture price-sensitive buyers without discounting the whole gig.
- **Freelancer.com**: bids cluster low fast on open projects — being the
  cheapest bid is rarely what wins; being the most specific and credible
  bid wins more often. Don't race to the bottom on price alone.

## Hard rules

- Never state a number as if it's an objective market rate — pricing is
  always a range with reasoning, since it depends on the user's experience,
  market, and the specific client.
- Always account for revisions/scope-creep risk explicitly, don't let it
  hide inside a single flat number.
- If the user's stated existing rate is already below a sustainable floor
  for their stated experience/market, say so plainly rather than just
  matching their anchor.

## Output shape

1. Scope breakdown (what's actually being asked for)
2. Estimated effort (hours or complexity tier), with the honesty flag if
   this looks like an underestimate-prone job
3. Suggested range: floor and target, with reasoning for each
4. One platform-specific note (fee impact, milestone structure, tier
   framing) relevant to where they're pricing this
