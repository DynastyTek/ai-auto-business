from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

lines = [
  "The 7-Day Social Media Launch Plan", "",
  "How to ship a credible launch in one week:", "",
  "Day 1 — Positioning: Define audience, offer, proof.",
  "Day 2 — Assets: Hero image, logo, value bullets.",
  "Day 3 — Website: Publish the landing page.",
  "Day 4 — Social Seed: 3 posts + 1 short video.",
  "Day 5 — Proof: Collect 2 testimonials or pilot quotes.",
  "Day 6 — Offer: Limited-time bonus or price anchor.",
  "Day 7 — Launch: Pin post + email blast + reply to comments.", "",
  "Templates and Tips:",
  "• Hook → Pain → Benefit → CTA",
  "• Add 3 relevant hashtags",
  "• Reply fast; save FAQs as canned responses",
]
out = "website/7-day-social-launch-plan.pdf"
c = canvas.Canvas(out, pagesize=LETTER)
width, height = LETTER; y = height - 1*inch
c.setFont("Helvetica-Bold", 18); c.drawString(1*inch, y, lines[0]); y -= 0.5*inch
c.setFont("Helvetica", 11)
for line in lines[1:]:
    if y < 1*inch: c.showPage(); y = height - 1*inch; c.setFont("Helvetica", 11)
    c.drawString(1*inch, y, line); y -= 0.25*inch
c.save(); print("Wrote", out)
