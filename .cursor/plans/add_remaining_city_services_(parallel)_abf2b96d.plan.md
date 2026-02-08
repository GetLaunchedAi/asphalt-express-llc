---
name: Add Remaining City Services (Parallel)
overview: Create remaining city service pages for seven new cities across all other services, update service-area lists, and verify consistency using parallel work paths.
todos:
  - id: shared-setup
    content: Confirm service templates + rules
    status: pending
  - id: path-a
    content: Build millings + resurfacing city pages + lists
    status: pending
    dependencies:
      - shared-setup
  - id: path-b
    content: Build commercial lots + repair city pages + lists
    status: pending
    dependencies:
      - shared-setup
  - id: path-c
    content: Build removal/replacement + residential + sealcoating city pages + lists
    status: pending
    dependencies:
      - shared-setup
  - id: qa-checks
    content: Verify copy, links, lists, navigation removed
    status: pending
    dependencies:
      - path-a
      - path-b
      - path-c
---

# 3-Part Plan: Remaining City Service Pages (Parallel Paths)

## Part 1 — Shared Setup (All Agents)

- Service types to mirror (from Birmingham city pages): asphalt millings, asphalt resurfacing, commercial parking lots, parking lot repair, removal & replacement, residential paving, sealcoating & maintenance. Asphalt paving is already done.
- City slugs to use across all services: `walled-lake`, `wolverine-lake`, `berkley`, `oakland-township`, `madison-heights`, `dexter`, `brighton`.
- Templates in `src/pages/servicepages/cities/` (Birmingham pages):
- `asphalt-millings-in-birmingham.html`
- `asphalt-resurfacing-in-birmingham.html`
- `commercial-parking-lots-in-birmingham.html`
- `parking-lot-repair-in-birmingham.html`
- `removal-replacement-in-birmingham.html`
- `residential-paving-in-birmingham.html`
- `sealcoating-maintenance-in-birmingham.html`
- Shared update rules for every new city page:
- Update front matter: `description`, `metaTitle`, `tagTitle`, `title`, `permalink`.
- Replace city names in headings, paragraphs, CTA text, FAQ questions/answers, and image alt text.
- Remove `eleventyNavigation` blocks so pages stay out of the nav.
- “Areas We Serve” list includes the full city list (existing + new) with the current city highlighted; keep the same alphabetical-ish order used elsewhere.
- Work one page at a time; if using scripts/commands, redirect output to files.

## Part 2 — Parallel Build Paths (Agents Can Work Independently)

### Path A — Asphalt Surfaces

- Create 7 city pages each for:
- Asphalt millings (template: `asphalt-millings-in-birmingham.html`)
- Asphalt resurfacing (template: `asphalt-resurfacing-in-birmingham.html`)
- Update service-area lists on these service pages in `src/pages/servicepages/`:
- `asphalt-millings.html`, `asphalt-resurfacing.html`

### Path B — Commercial & Repair

- Create 7 city pages each for:
- Commercial parking lots (template: `commercial-parking-lots-in-birmingham.html`)
- Parking lot repair (template: `parking-lot-repair-in-birmingham.html`)
- Update service-area lists on these service pages in `src/pages/servicepages/`:
- `commercial-parking-lots.html`, `parking-lot-repair.html`

### Path C — Replacement & Maintenance

- Create 7 city pages each for:
- Removal & replacement (template: `removal-replacement-in-birmingham.html`)
- Residential paving (template: `residential-paving-in-birmingham.html`)
- Sealcoating & maintenance (template: `sealcoating-maintenance-in-birmingham.html`)
- Update service-area lists on these service pages in `src/pages/servicepages/`:
- `removal-replacement.html`, `residential-paving.html`, `sealcoating-maintenance.html`

## Part 3 — Final QA & Consistency

- Verify each new city page has:
- Correct city name in front matter, body copy, FAQ, CTA, and image alt text.
- Correct permalink and matching link in lists.
- `eleventyNavigation` removed.
- “Areas We Serve” list includes the full set and highlights the current city.