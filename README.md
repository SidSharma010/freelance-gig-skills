# freelance-gig-skills

Claude skills for freelancers. 4 skills that write tailored Upwork/Fiverr/
Freelancer.com proposals, optimize your platform profile, help you price a
job with reasoning instead of a guess, and draft follow-ups that don't read
as pushy — all from a chat with Claude.

Built for freelancers on any platform, anywhere — not tied to one country
or one gig site.

## The 4 skills

| Skill | What it does |
|---|---|
| `proposal-writer` | Drafts a tailored proposal/cover letter/bid for a specific job post — Upwork, Fiverr buyer requests, Freelancer.com, or any other platform |
| `portfolio-optimizer` | Rewrites your profile/overview/bio to lead with outcomes instead of a skill list |
| `pricing-advisor` | Reasons through a price range for a specific job from its actual scope, not a round-number guess |
| `followup-drafter` | Drafts a follow-up for a proposal that's gone quiet, without sounding needy or pushy |

## Install

### Claude Code / Codex

```bash
git clone https://github.com/SidSharma010/freelance-gig-skills.git
cd freelance-gig-skills
```

Open this folder as your working directory — Claude Code finds the skills
under `skills/` automatically.

### claude.ai / Claude Desktop (as a plugin marketplace)

1. Open Customize → Plugins → Add → Add marketplace → Add from a repository
2. Paste `SidSharma010/freelance-gig-skills` and sync
3. Find it under Discover, install it, confirm it shows under Yours

### Any agent that reads SKILL.md files

```bash
npx skills add SidSharma010/freelance-gig-skills
```

## Usage

Once installed, just ask in plain language — the right skill activates
automatically.

Write a proposal:

> "Write me an Upwork proposal for this job: [paste job post]"

Price a job:

> "What should I charge for this? [paste job post] I'm mid-level, based in
> India, targeting US clients."

Fix a profile:

> "My Fiverr gig isn't getting orders, here's my current description: [...]"

Follow up on a quiet proposal:

> "I sent this proposal 5 days ago and haven't heard back: [paste proposal].
> Should I follow up?"

## Why this exists

Most freelance advice online is generic ("stand out from the crowd!").
These skills instead ask for the real, specific details of the job post,
the platform, and the user's actual experience — and refuse to invent
numbers, client names, or results that weren't given to them. A proposal
built on fabricated specifics is worse than a plain honest one, because it
falls apart the moment a client asks a follow-up question.

## License

MIT — see [LICENSE](LICENSE).

## Checking a draft before you send it

`proposal-writer` follows hard rules against generic openers and invented
specifics, but rules in a prompt aren't a guarantee. Before sending a real
proposal, run it through the mechanical checker:

```bash
python lib/check_proposal.py --platform upwork my-draft.txt
```

It flags length problems and known template phrases. It does not judge
whether the pitch is actually good — that's still on you. `examples/`
has a worked weak-vs-strong comparison to calibrate against.

## Repo structure

```
freelance-gig-skills/
├── skills/
│   ├── proposal-writer/SKILL.md
│   ├── portfolio-optimizer/SKILL.md
│   ├── pricing-advisor/SKILL.md
│   └── followup-drafter/SKILL.md
├── references/
│   ├── platform-formats.md      (shared platform specs, single source of truth)
│   └── pricing-benchmarks.md    (illustrative rate bands, not live data)
├── lib/
│   └── check_proposal.py        (mechanical draft checker, no dependencies)
└── examples/
    └── upwork-example.md        (worked weak vs. strong proposal)
```

## Status

This is a new, unproven bundle — not yet tested against real job posts at
volume. The structure and hard rules are deliberate (modeled on a proven
pattern), but "will this actually win more jobs" hasn't been validated.
If you use it and something reads generic or wrong, that's the signal to
fix — open an issue or edit the relevant SKILL.md directly.
