---
name: Add Asphalt Paving Cities
overview: Create asphalt paving city pages for the new locations and add them to the service-area lists on the homepage and the asphalt paving service page, while keeping them out of the navigation.
todos:
  - id: audit-cities
    content: Confirm which requested cities already exist and define slugs
    status: pending
  - id: create-city-pages
    content: Create new asphalt paving city pages with the template
    status: pending
    dependencies:
      - audit-cities
  - id: update-lists
    content: Add new city links to homepage and asphalt paving lists
    status: pending
    dependencies:
      - audit-cities
  - id: sync-city-lists
    content: Ensure new city pages include full Areas We Serve list
    status: pending
    dependencies:
      - create-city-pages
---

# Add Asphalt Paving City Pages

## Context

- Homepage service-area list lives in `src/index.html` under the `service-area-map` section.
- Asphalt paving service page list lives in `src/pages/servicepages/asphalt-paving.html` under `service-area-map`.
- City page template is in existing pages like `src/pages/servicepages/cities/asphalt-paving-in-birmingham.html` (static HTML with an “Areas We Serve” list).

## Plan

- Audit requested cities against existing asphalt paving pages in `src/pages/servicepages/cities/` to avoid duplicates. Current list already includes `Sterling Heights` and `Warren`.
- Define slugs using the existing pattern `/asphalt-paving-in-<city-slug>/` for the new pages: `walled-lake`, `wolverine-lake`, `berkley`, `oakland-township`, `madison-heights`, `dexter`, `brighton`.
- Create new city pages in `src/pages/servicepages/cities/` by copying `asphalt-paving-in-birmingham.html` and updating:
- Front matter fields (`description`, `metaTitle`, `tagTitle`, `title`, `permalink`).
- City names in headings, paragraphs, CTA text, FAQ questions/answers, and image alt text.
- The highlighted city in the “Areas We Serve” list for each page.
- Remove the `eleventyNavigation` block so pages stay out of the nav.
- Update the homepage “Areas We Serve” list in `src/index.html` to add links for the new city pages, keeping the list in the same alphabetical-ish order as the existing list.
- Update the asphalt paving service page list in `src/pages/servicepages/asphalt-paving.html` to include the same new city links.
- Keep the “Areas We Serve” lists consistent across the new city pages by including the full list (existing + new) with the current city highlighted.

## Notes on the requested list