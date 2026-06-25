# Fundraising Progress Ring Widget — Claude Code PRD

## Project Overview
Build a self-contained, embeddable HTML web component that displays a circular progress ring for a $1.2M fundraising campaign. The component pulls live data from Google Sheets, auto-refreshes every 5 minutes, and displays the current fundraising progress.

---

## Configuration
**FILL IN THESE VALUES BEFORE RUNNING:**

```javascript
const CONFIG = {
  API_KEY: "YOUR_GOOGLE_API_KEY_HERE",
  SHEET_ID: "AIzaSyCKStQUULr43JTBg9m4iZc1Q10kPlZeBfo",
  SHEET_RANGE: "A2:B2", // Goal in A2, Current in B2
  GOAL_AMOUNT: 1200000, // $1.2 million
  CURRENT_AMOUNT: $257,945,
  REFRESH_INTERVAL: 300000 // 5 minutes in milliseconds
};
```

---

## Design Specifications

### Visual Reference
Figma mockup: https://www.figma.com/design/1ZaFzFdWGgbE9QL89g3w8C/TR-ANAHEIM?node-id=1007-1838

### Layout & Sizing
- **Container**: 200px × 200px (centered with 64px padding)
- **Ring diameter**: 276px (SVG circle)
- **Background**: White (#FFFFFF)

### Colors
- **Track ring** (background): Light gray (#E5E7EB)
- **Progress arc** (fill): Blue (#3B82F6)
- **Accent gradient** (optional top): Green (#10B981)
- **Text**: Dark gray/black (#111827)

### Typography
- **Label text**: "Together we've raised"
  - Font size: 14px
  - Font weight: Bold (700)
  - Color: #111827
  
- **Amount text**: "$250,787.27"
  - Font size: 28px
  - Font weight: Bold (700)
  - Color: #111827
  - Format: US currency (e.g., $625,000.00)

---

## Technical Requirements

### Functionality
1. **On page load:**
   - Fetch current raised amount from Google Sheets API
   - Calculate percentage: (Current / Goal) × 100
   - Render SVG progress ring with animated arc
   - Display formatted dollar amount

2. **Progress ring animation:**
   - SVG circle with animated stroke-dashoffset
   - Smooth animation from 0% to target percentage (1-2 second easing)
   - Use CSS or JavaScript transitions (no external animation libraries)

3. **Auto-refresh (every 5 minutes):**
   - Refetch Google Sheets data
   - Smoothly animate ring to new percentage
   - Update dollar amount text
   - No page flicker or jump

4. **Error handling:**
   - If API fails, display fallback text: "Unable to load fundraising data"
   - Log errors to browser console
   - Retry automatically on next refresh interval

5. **Responsive:**
   - Component adapts to container size (use CSS transforms, not hardcoded pixels)
   - Minimum width: 250px
   - Maximum width: 600px

### Google Sheets Data Structure
Your sheet (ID: `1cytKQII53YLwpFn1g_KlTAyG9k9_ohxZNH2IObRHNhQ`) should have:

```
Row 1 (Headers):
  A1: "Goal"
  B1: "Current"

Row 2 (Data):
  A2: 1200000
  B2: [Your current amount, e.g., 625000]
```

**API Endpoint:**
```
https://sheets.googleapis.com/v4/spreadsheets/1cytKQII53YLwpFn1g_KlTAyG9k9_ohxZNH2IObRHNhQ/values/A2:B2?key=YOUR_API_KEY
```

### Output Format
- **Single HTML file** (self-contained, no external CSS/JS dependencies except Google Sheets API)
- **File name**: `progress-ring.html`
- **Embeddable**: Can be hosted anywhere and embedded as an iframe in Wix or any website
- **Size**: ~10-15KB (minified)

### Embedding Instructions (for later)
```html
<iframe 
  src="https://[your-domain]/progress-ring.html"
  width="500"
  height="500"
  frameborder="0"
  style="border: none;">
</iframe>
```

---

## Implementation Details

### SVG Structure
```
<svg viewBox="0 0 276 276">
  <!-- Track ring (light gray background) -->
  <circle cx="138" cy="138" r="130" fill="none" stroke="#E5E7EB" stroke-width="20" />
  
  <!-- Progress arc (animated, blue) -->
  <circle cx="138" cy="138" r="130" fill="none" stroke="#3B82F6" 
    stroke-width="20" stroke-dasharray="..." stroke-dashoffset="..." 
    stroke-linecap="round" />
  
  <!-- Optional accent segment (green at top, 0-5% of ring) -->
  <circle cx="138" cy="138" r="130" fill="none" stroke="#10B981" 
    stroke-width="20" stroke-dasharray="..." stroke-dashoffset="..." />
</svg>
```

### JavaScript Flow
1. Fetch Google Sheets data via API
2. Parse JSON response → extract current & goal amounts
3. Calculate percentage
4. Animate SVG stroke-dashoffset from 0 to final offset
5. Format and display dollar amount
6. Set interval for 5-minute refresh

### Accessibility
- Use semantic HTML (`<main>`, `<section>`)
- Add ARIA labels for screen readers: `aria-label="Fundraising progress: 52% of $1.2 million raised"`
- Ensure text contrast meets WCAG AA (dark gray on white ✅)

---

## Dependencies
- **None** (except Google Sheets API, which is called via HTTPS)
- No npm packages
- No external CSS frameworks
- Pure HTML, CSS, and vanilla JavaScript

---

## Testing Checklist
- [ ] Component loads without errors
- [ ] Progress ring displays at 0% initially (or matches current data)
- [ ] Ring animates smoothly to calculated percentage on load
- [ ] Dollar amount displays correctly (formatted with commas and cents)
- [ ] Auto-refresh fires every 5 minutes
- [ ] Ring animates smoothly on refresh (no jumps)
- [ ] Works in Chrome, Firefox, Safari
- [ ] Works when embedded as iframe in Wix
- [ ] Error message displays if API key is invalid
- [ ] Mobile responsive (tested on 375px width)

---

## Deliverables
1. **progress-ring.html** — Single file, ready to deploy
2. **Setup instructions** — How to embed in Wix
3. **Optional:** Deployment link (host on GitHub Pages, Vercel, or similar for free)

---

## Notes
- The component is **read-only** — it only pulls data from Google Sheets, it never writes back
- API key is embedded in the HTML file. Since it's read-only and public-facing, this is safe
- The Google Sheet must remain shared as "Anyone with link can view"
- To update the fundraising amount, just edit cell B2 in your Google Sheet; the widget updates automatically on the next refresh cycle

---

## Ready to Build?
Paste this PRD into Claude Code with your API key and current amount filled in, and the tool will generate `progress-ring.html`.