# Zero-Human Business Build — STATUS

**Project:** ai-auto-business  
**Owner:** DynastyTek  
**Live URL:** [https://DynastyTek.github.io/ai-auto-business/](https://DynastyTek.github.io/ai-auto-business/)  
**Repo:** [https://github.com/DynastyTek/ai-auto-business](https://github.com/DynastyTek/ai-auto-business)

---

## 1) Executive Summary
We shipped a revenue-capable static storefront with automation scaffolding. Site is live on GitHub Pages. Payments, delivery, social, and email are wired as placeholders until credentials are supplied. Next actions are credential drops + one-click runs.

**Ship Confidence:** Medium → High once PayPal Merchant ID + Payhip URL are in place.  
**Time-to-Revenue:** < 30 minutes after credentials.

---

## 2) What's Done (Green)
- Repo created and structured (`/website`, `/automation`, `/prompts`, `/.github/workflows`).
- Static site committed with Tailwind and PayPal **demo** CTA.
- Social campaign **dry-run** JSON committed and scheduled plan documented.
- Mailchimp **TODO** template committed.
- Payhip **redirect/TODO** notes committed.
- GitHub Pages workflow active and verified.
- Live site reachable.

---

## 3) Open Items (Yellow/Red)
- **PayPal Merchant ID** → replace placeholder in `website/index.html` (`{{PAYPAL_MERCHANT_ID}}`).
- **Product PDF** → generate/commit `website/7-day-social-launch-plan.pdf` (script is TODO; see Runbook below).
- **Payhip product** → upload PDF; write final `PAYHIP_PRODUCT_URL` into `website/product.txt` and `automation/payment_redirect.txt`.
- **Social scheduling (prod)** → log into SocialSync and schedule posts from `automation/social_posts.json` (analytics ON).
- **Mailchimp automation (prod)** → create post-purchase flow using `automation/email_template.txt`.
- **Optional analytics** → add Plausible/Umami snippet to `index.html` for basic funnel visibility.

---

## 4) Go-Live Acceptance Criteria (check when done)
- [ ] `index.html` PayPal link contains real `business=<MERCHANT_ID>`.
- [ ] `website/7-day-social-launch-plan.pdf` committed and downloadable directly.
- [ ] Payhip product URL saved in `website/product.txt`; redirect configured in Payhip → After Purchase Redirect.
- [ ] Social posts scheduled (2/day starting tomorrow) with analytics enabled; screenshot or export captured.
- [ ] Mailchimp welcome/thank-you automation live; template matches repo copy.
- [ ] CTA smoke test: opens PayPal checkout (no pay), completes redirect (when Payhip live).
- [ ] STATUS updated to **Green** with links/screenshots.

---

## 5) QA Checklist (Manual)
1. **Site UI/UX**
   - Load on mobile + desktop; hero, bullets, CTA visible above the fold.
   - Lighthouse quick check: performance > 90, accessibility > 90.
2. **Payment**
   - Click **Buy Now** → PayPal checkout opens with correct item and $29.
3. **Delivery**
   - After-purchase redirect in Payhip points to the product download page.
   - Download starts; PDF opens cleanly.
4. **Social**
   - Verify 10 posts scheduled; cadence 2/day starting tomorrow.
5. **Email**
   - Mailchimp automation triggers on purchase; template renders variables.
6. **Telemetry**
   - (If configured) Analytics shows pageviews and outbound click on CTA.

---

## 6) Runbook (Comet-first)
**A) Inject PayPal Merchant ID**
- Edit `website/index.html`: set `{{PAYPAL_MERCHANT_ID}}` to the real value.
- Commit message: `chore: inject PayPal Merchant ID`

**B) Generate Product PDF**
- Use Python runner:
  - If `automation/generate_pdf.py` exists, run it and commit output to `website/7-day-social-launch-plan.pdf`.
  - If not, create it (ReportLab), generate, then commit.
- Commit: `feat: add 7-day social launch plan PDF`

**C) Upload to Payhip**
- Create product "Small Business Marketing Toolkit" and upload the PDF.
- Copy the product URL; write to:
  - `website/product.txt` → `PAYHIP_PRODUCT_URL=<url>`
  - Update `automation/payment_redirect.txt` Status with final URL.
- Commit: `chore: record Payhip product URL and redirect config`

**D) SocialSync Scheduling**
- Log in → import `automation/social_posts.json` → schedule (2/day from tomorrow) with analytics ON.
- Export schedule or screenshot and store as `automation/socialsync_proof.txt` (URL list) or `proof.png`.
- Commit: `chore: social scheduling proof`

**E) Mailchimp**
- Create automated "Post-Purchase Thank You" flow using `automation/email_template.txt`.
- Record audience + campaign IDs in `automation/mailchimp_status.txt`.
- Commit: `chore: mailchimp automation live`

**F) Optional Analytics**
- Add Plausible/Umami snippet to `<head>` of `index.html`.
- Commit: `feat: add privacy-friendly analytics`

---

## 7) Links & Evidence
- **Live Site:** [https://DynastyTek.github.io/ai-auto-business/](https://DynastyTek.github.io/ai-auto-business/)
- **Payhip Product:** _TBD_
- **Social Proof (schedule export):** _TBD_
- **Mailchimp Automation:** _TBD_

---

## 8) Risks & Mitigations
- Missing credentials → **Mitigation:** Non-blocking placeholders + TODO files with exact next actions.
- No analytics → **Mitigation:** Add snippet for basic funnel visibility.
- Single CTA price point → **Mitigation:** Add price anchor/bonus block after first sales.

---

## 9) Owner Inputs Needed
- PayPal Merchant ID  
- Payhip credentials (or share link post-creation)  
- SocialSync credentials (optional)  
- Mailchimp audience/list ID (optional)

---

## 10) Changelog (human-readable)
- Bootstrap repo + Pages workflow
- Static site + CTA
- Social campaign dry run
- Email template + Payhip redirect TODOs
- Live deploy verified
