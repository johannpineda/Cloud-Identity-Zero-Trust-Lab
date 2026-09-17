#!/usr/bin/env python3
"""Render the portfolio architecture diagram with Pillow."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "assets" / "diagrams" / "identity-architecture.png"
W, H = 1600, 900

def font(size, bold=False):
    path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    return ImageFont.truetype(path, size)

img = Image.new("RGB", (W, H), "#07111f")
d = ImageDraw.Draw(img)
for y in range(H):
    r = int(7 + 5 * y / H); g = int(17 + 11 * y / H); b = int(31 + 20 * y / H)
    d.line((0, y, W, y), fill=(r, g, b))

d.text((72, 55), "Cloud Identity & Zero Trust Administration Lab", font=font(48, True), fill="#f8fafc")
d.text((74, 118), "Identity is the control plane • verify explicitly • least privilege • assume breach", font=font(22), fill="#9fb3c8")

def box(x, y, w, h, title, lines, accent):
    d.rounded_rectangle((x, y, x+w, y+h), 18, fill="#101f33", outline="#29415d", width=2)
    d.rounded_rectangle((x, y, x+9, y+h), 5, fill=accent)
    d.text((x+28, y+22), title, font=font(25, True), fill="#f8fafc")
    for i, line in enumerate(lines):
        d.text((x+28, y+66+i*31), line, font=font(17), fill="#b9c9d9")

def arrow(x1, y1, x2, y2, color="#47a7ff"):
    d.line((x1, y1, x2, y2), fill=color, width=5)
    import math
    a = math.atan2(y2-y1, x2-x1)
    p1 = (x2-18*math.cos(a-0.55), y2-18*math.sin(a-0.55))
    p2 = (x2-18*math.cos(a+0.55), y2-18*math.sin(a+0.55))
    d.polygon([(x2,y2), p1, p2], fill=color)

box(70, 225, 300, 200, "Identities & Devices", ["Workforce users", "Privileged identities", "Managed devices", "Service principals"], "#38bdf8")
box(485, 205, 360, 240, "Microsoft Entra ID", ["Authentication & MFA", "Directory and groups", "RBAC / PIM", "Identity risk signals"], "#8b5cf6")
box(960, 225, 310, 200, "Conditional Access", ["Identity + risk", "Device compliance", "Application context", "Grant / session controls"], "#22c55e")
box(1300, 225, 240, 200, "Cloud Services", ["Microsoft 365", "Enterprise apps", "Microsoft Graph", "Admin portals"], "#f59e0b")

arrow(370, 325, 485, 325)
arrow(845, 325, 960, 325)
arrow(1270, 325, 1300, 325)

box(230, 585, 350, 190, "Governance", ["Joiner / mover / leaver", "Access reviews", "Group-based licensing", "App consent review"], "#e879f9")
box(625, 585, 350, 190, "Automation", ["PowerShell", "Microsoft Graph API", "Policy validation", "Evidence export"], "#06b6d4")
box(1020, 585, 350, 190, "Monitoring & Response", ["Sign-in and audit logs", "Risk detections", "Health reporting", "Incident workflow"], "#fb7185")

arrow(660, 445, 500, 585, "#8b5cf6")
arrow(665, 445, 790, 585, "#06b6d4")
arrow(1110, 425, 1180, 585, "#22c55e")

d.text((72, 837), "SANITIZED REFERENCE ARCHITECTURE", font=font(16, True), fill="#7dd3fc")
d.text((1335, 837), "LAB DEMO", font=font(18, True), fill="#94a3b8")
OUT.parent.mkdir(parents=True, exist_ok=True)
img.save(OUT, quality=95)
print(OUT)
