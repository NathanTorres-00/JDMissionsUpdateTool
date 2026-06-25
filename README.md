# JD Progress Ring

A self-contained, embeddable fundraising progress ring for the $1.2M campaign. It reads the live
amount from a Google Sheet, auto-refreshes every 5 minutes, and renders a segmented green/blue donut
with evenly-spaced milestone labels and the live total in the center.

## Files
- **`progress-ring.html`** — the entire widget (HTML + CSS + vanilla JS, no build step, no dependencies
  except the Google Sheets API call and the Geist webfont).
- **`ProgressRing.md`** — original product spec/notes.

## How it works
- Pulls `A2:B2` from the Google Sheet: **A2 = goal**, **B2 = current raised**.
- Endpoint: `https://sheets.googleapis.com/v4/spreadsheets/{SHEET_ID}/values/A2:B2?key={API_KEY}`.
- Milestone marks (`CONFIG.MILESTONES`) are spaced equally around the circle; the green fill
  interpolates piecewise between them so the fill tip lines up with the labels.
- Refreshes every 5 minutes; on a failed fetch it keeps the last good value (or shows a fallback
  message if it never loaded).

## Embedding in Wix
1. Wix Editor → **Add → Embed Code → Embed HTML**.
2. Choose **Code** (not "Website address").
3. Paste the full contents of `progress-ring.html`, then **Apply** and publish.
4. To update the displayed total, edit cell **B2** in the Google Sheet — the widget updates on its next
   refresh.

## Configuration
Edit the `CONFIG` block at the top of the `<script>` in `progress-ring.html` (API key, sheet ID,
milestones, refresh interval). Colors and fonts are CSS variables in the `:root` block.

## Notes
- The Sheets API key is embedded in the page (required for a client-side read). Restrict it to the
  **Google Sheets API** in Google Cloud Console. The sheet must stay shared as "Anyone with the link
  can view."
