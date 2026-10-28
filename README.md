# Team I: PR Summarizer Bot

> GitHub webhook that summarises pull requests

**Hack4Haldia'26** is a 3-hour build challenge. This is your starter repository. Build new features on top of it, integrate them, **deploy the working project**, and open a **Pull Request** on this repository. AI tools and open-source / open-weight models are fully allowed.

## The Problem

Reviewers hate reading huge diffs. Build a bot that receives GitHub webhooks, reads the diff and writes a short summary with risk flags.

## Must-have (core, do these first)

- [ ] Receive GitHub webhook and VERIFY the HMAC signature
- [ ] Fetch the PR diff via the GitHub API
- [ ] LLM summary + risk level
- [ ] Store and list summaries

## Bonus (only after the core works end to end)

- [ ] Post the summary back as a PR comment
- [ ] Suggest labels automatically
- [ ] Ignore bot PRs and huge diffs gracefully
- [ ] Retry with backoff on API failures

## Industry-level tech we expect you to use

- Webhooks + HMAC
- GitHub REST API
- LLM summarisation
- Secrets handling (.env)

A toy in-memory demo is not enough. Use real tools (database, auth, queue, model etc.) where it makes sense.

## What is already here

| File | Purpose |
|---|---|
| `index.html` | Starter UI with an API tester. Replace it with your real frontend. |
| `app.py` + `requirements.txt` | **Python / Flask** starter |
| `script.js` + `package.json` | **Node / Express** starter |

Pick **ONE** stack and delete the other, or keep both if you want. Both expose the same endpoints:

| Method | Path | What it should do |
|---|---|---|
| `GET` | `/health` | Already working |
| `POST` | `/webhook/github` | GitHub webhook receiver |
| `GET` | `/api/summaries` | List generated summaries |

All the endpoints above return `501 Not Implemented` until you build them. Add more endpoints if you need.

## Run locally

**Python**
```bash
pip install -r requirements.txt
python app.py        # http://localhost:5000
```

**Node**
```bash
npm install
npm start            # http://localhost:3000
```

Put secrets in a `.env` file. **Never commit API keys.**

## Deploy (required)

Your project must be live on a public URL. Easiest options:
- **Render**: Web Service, connect the repo. Python start command: `gunicorn app:app`. Node: `npm start`.
- Vercel / Railway / Fly.io also fine.

Add the live URL at the top of your PR description.

## Submit

1. Create a branch: `git checkout -b team-i-solution`
2. Commit and push your work.
3. Open a **Pull Request** against `main` of **this** repository.
4. PR description must include: live URL, what you built, tech used, team members.
5. Also submit on the official **MLH platform (OrganizerHQ)**. Instructions will be given at the start of the event.

## Rules

- Teams of 3 to 4. Every member must be present.
- 3 hours total. Commit often.
- AI tools are open. You must still understand and be able to explain your code.

## Judging

Working demo (35%) | Technical depth (25%) | Completeness of core features (20%) | Deployment (10%) | Presentation (10%)

Good luck, build something great!
