# moonshiftstudio.com

The Moonshift Studio website. Static HTML, hosted on Vercel.

- `site/` is what gets published (Vercel serves this folder).
- `builder/` makes `site/`: edit the words in `builder/build_v2.py`, `builder/site_data.py` and `builder/app_extra.py`, styles in `builder/v2/assets/ms.css`, then run `python3 builder/build_v2.py`.
- App store links live in `builder/v2/assets/ms.js` (`MOONSHIFT_APPS`). Fill them in when an app launches; printed QR codes keep working.
- Tester sign-ups are saved to the `studio_signups` table in the Firefly Dash Supabase project.
