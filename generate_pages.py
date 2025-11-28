#!/usr/bin/env python3
"""
Script to generate all 56 service pages for the new cities.
"""

import os
import re

# City mappings: (display_name, url_slug)
new_cities = [
    ('Birmingham', 'birmingham'),
    ('Orchard Lake', 'orchard-lake'),
    ('Davisburg', 'davisburg'),
    ('Pontiac', 'pontiac'),
    ('Sterling Heights', 'sterling-heights'),
    ('Southfield', 'southfield'),
    ('Clarkston', 'clarkston'),
    ('Plymouth', 'plymouth'),
    ('Warren', 'warren'),
    ('Commerce', 'commerce')
]

# Existing cities list
existing_cities = [
    ('Wixom', 'wixom'),
    ('Highland', 'highland'),
    ('White Lake', 'white-lake'),
    ('West Bloomfield', 'west-bloomfield'),
    ('Bloomfield Hills', 'bloomfield-hills'),
    ('Farmington Hills', 'farmington-hills'),
    ('Farmington', 'farmington'),
    ('Rochester', 'rochester'),
    ('Troy', 'troy'),
    ('Howell', 'howell'),
    ('Holly', 'holly'),
    ('Novi', 'novi'),
    ('South Lyon', 'south-lyon'),
    ('New Hudson', 'new-hudson'),
    ('Rochester Hills', 'rochester-hills'),
    ('Fenton', 'fenton'),
    ('Pinckney', 'pinckney'),
    ('Hartland', 'hartland'),
    ('Livonia', 'livonia'),
    ('Waterford', 'waterford'),
    ('Northville', 'northville'),
    ('Lake Orion', 'lake-orion'),
    ('Ortonville', 'ortonville')
]

# All cities combined, sorted alphabetically
all_cities = sorted(new_cities + existing_cities, key=lambda x: x[0].lower())

# Service configurations: (service_name, service_display, banner_image, image_0, image_1, service_slug)
services = [
    ('asphalt-paving', 'Asphalt Paving', 'paving_banner.png', 'paving_0.png', 'paving_1.png', 'asphalt-paving'),
    ('residential-paving', 'Residential Paving', 'paving_banner.png', 'paving_0.png', 'paving_1.png', 'residential-paving'),
    ('commercial-parking-lots', 'Commercial Parking Lots', 'commercial_banner.png', 'commercial_0.png', 'commercial_1.png', 'commercial-parking-lots'),
    ('sealcoating-maintenance', 'Sealcoating & Maintenance', 'sealcoating_banner.png', 'sealcoating_0.png', 'sealcoating_1.png', 'sealcoating-maintenance'),
    ('asphalt-resurfacing', 'Asphalt Resurfacing', 'resurfacing_banner.png', 'resurfacing_0.png', 'resurfacing_1.png', 'asphalt-resurfacing'),
    ('parking-lot-repair', 'Parking Lot Repair', 'repair_banner.png', 'repair_0.png', 'repair_1.png', 'parking-lot-repair'),
    ('removal-replacement', 'Removal & Replacement', 'removal_banner.png', 'removal_0.png', 'removal_1.png', 'removal-replacement'),
    ('asphalt-millings', 'Asphalt Millings', 'millings_banner.png', 'millings_0.png', 'millings_1.png', 'asphalt-millings')
]

def generate_service_area_list(current_city_slug, service_slug):
    """Generate the service area list HTML with all cities, highlighting the current one."""
    html_lines = []
    for city_name, city_slug in all_cities:
        if city_slug == current_city_slug:
            html_lines.append(f'          <li class="cs-area-item" style="font-weight: 700; background: var(--primaryDark);"><a href="/{service_slug}-in-{city_slug}/" style="color: white; text-decoration: none;">{city_name}</a></li>')
        else:
            html_lines.append(f'          <li class="cs-area-item"><a href="/{service_slug}-in-{city_slug}/" style="color: white; text-decoration: none;">{city_name}</a></li>')
    return '\n'.join(html_lines)

def generate_page_content(city_name, city_slug, service_config):
    """Generate the complete HTML content for a service page."""
    service_name, service_display, banner_img, img_0, img_1, service_slug = service_config
    
    # Service-specific content variations
    service_variations = {
        'asphalt-paving': {
            'desc': 'Quality Materials • Expert Installation • Durable Results',
            'card1_title': 'Quality Materials',
            'card1_text': 'We use only the highest quality asphalt materials and expert installation techniques to ensure your new surface is durable, attractive, and long-lasting.',
            'card2_title': 'Expert Installation',
            'card2_text': 'Our experienced team provides professional installation with proper preparation, grading, and compaction to ensure optimal performance and longevity.'
        },
        'residential-paving': {
            'desc': 'Quality Materials • Expert Installation • Durable Results',
            'card1_title': 'Home Solutions',
            'card1_text': 'We specialize in residential driveway paving and installation, creating beautiful and durable surfaces that enhance your home\'s curb appeal.',
            'card2_title': 'Expert Installation',
            'card2_text': 'Our experienced team provides professional residential paving services with attention to detail and quality craftsmanship.'
        },
        'commercial-parking-lots': {
            'desc': 'Business Solutions • Professional Service • Reliable Results',
            'card1_title': 'Business Focused',
            'card1_text': 'We specialize in commercial parking lot solutions designed to meet the specific needs of businesses, ensuring minimal disruption to your operations.',
            'card2_title': 'Professional Service',
            'card2_text': 'Our experienced team provides professional commercial parking lot services with proper planning, execution, and cleanup to maintain your business operations.'
        },
        'sealcoating-maintenance': {
            'desc': 'Protection • Maintenance • Longevity',
            'card1_title': 'Surface Protection',
            'card1_text': 'Our professional sealcoating provides essential protection against weather, UV rays, and traffic wear, extending the life of your asphalt surfaces.',
            'card2_title': 'Preventive Maintenance',
            'card2_text': 'Regular sealcoating and maintenance prevents costly repairs by addressing issues early and maintaining the integrity of your asphalt surfaces.'
        },
        'asphalt-resurfacing': {
            'desc': 'Restoration • Quality • Value',
            'card1_title': 'Surface Restoration',
            'card1_text': 'Our resurfacing process restores your existing asphalt to like-new condition, extending its life and improving appearance.',
            'card2_title': 'Cost-Effective Solution',
            'card2_text': 'Resurfacing is a cost-effective alternative to complete replacement, providing excellent results while saving on material and labor costs.'
        },
        'parking-lot-repair': {
            'desc': 'Quick Response • Quality Repairs • Reliable Service',
            'card1_title': 'Quick Response',
            'card1_text': 'We provide fast and efficient parking lot repair services to address issues quickly and minimize disruption to your business operations.',
            'card2_title': 'Quality Repairs',
            'card2_text': 'Our professional repair services restore your parking lot to safe and functional condition using quality materials and proven techniques.'
        },
        'removal-replacement': {
            'desc': 'Complete Removal • Fresh Start • Quality Installation',
            'card1_title': 'Complete Removal',
            'card1_text': 'We provide comprehensive removal and replacement services, completely removing old asphalt and installing fresh, quality surfaces.',
            'card2_title': 'Fresh Installation',
            'card2_text': 'Our removal and replacement process ensures a clean slate for new asphalt installation, providing the best foundation for long-lasting results.'
        },
        'asphalt-millings': {
            'desc': 'Cost-Effective • Eco-Friendly • Durable',
            'card1_title': 'R.A.P. Installation',
            'card1_text': 'We provide professional installation of R.A.P. (Recycled Asphalt Pavement) millings for cost-effective and environmentally friendly paving solutions.',
            'card2_title': 'Sustainable Solution',
            'card2_text': 'Asphalt millings offer a sustainable paving solution by recycling existing asphalt materials while providing durable and functional surfaces.'
        }
    }
    
    variations = service_variations.get(service_name, service_variations['asphalt-paving'])
    
    service_area_list = generate_service_area_list(city_slug, service_slug)
    
    content = f'''---
layout: 'base.html'
description: 'Professional {service_display.lower()} service in {city_name}, Michigan. Asphalt Express LLC provides quality {service_display.lower()} throughout {city_name} with 30+ years of experience.'
metaTitle: '{service_display} in {city_name}, Michigan | Asphalt Express LLC'
tagTitle: '{service_display} in {city_name}'
title: '{service_display} in {city_name}'
preloadImg: '/images/{banner_img}'
preloadCSS: '/css/services.css'
permalink: '{service_slug}-in-{city_slug}/'
eleventyNavigation:
  key: {service_display} in {city_name}
  parent: Services
  order: 400
---
<!-- ============================================ -->
<!--                   Banner                     -->
<!-- ============================================ -->

<section id="int-hero">
  <h1 id="home-h">{service_display} in {city_name}</h1>
  {{% image './src/images/{banner_img}', 'professional {service_display.lower()} in {city_name}, Michigan by Asphalt Express LLC', '', 'lazy', '(max-width: 850px) 850px, 1920px' %}}
</section>

<!-- ============================================ -->
<!--                 Content Page                 -->
<!-- ============================================ -->

<section id="content-page-1402">
  <div class="cs-container">
    <div class="cs-image-group fx slide-top staggered-m" style="--i:1">
      <div class="cs-flex">
        <picture class="cs-background">
          <source media="(max-width: 600px)" srcset="/images/{img_0}">
          <source media="(min-width: 601px)" srcset="/images/{img_0}">
          <img loading="lazy" decoding="async" src="/images/{img_0}" alt="professional {service_display.lower()} in {city_name}, Michigan" width="542" height="728">
        </picture>
        <div class="cs-box">
          <img class="cs-box-icon" loading="lazy" decoding="async" src="https://csimg.nyc3.cdn.digitaloceanspaces.com/Icons/gear-white.svg" alt="service icon" width="60" height="60">
          <span class="cs-desc">
            {variations['desc']}
          </span>
        </div>
      </div>
      <ul class="cs-card-group fx slide-top staggered-m" style="--i:3">
        <li class="cs-item fx slide-top staggered-m" style="--i:4">
          <h3 class="cs-h3">
            <div style="width: 24px; height: 24px; flex-shrink: 0;">
                <svg class="cs-h3-icon" aria-hidden="true" viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="var(--primary)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"></path>
                    <path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"></path>
                    <path d="M4 22h16"></path>
                    <path d="M10 14.66V17c0 .55-.47.98-.97 1.21l-1.25.5c-.5.2-1.28.2-1.78 0l-1.25-.5A1.25 1.25 0 0 1 4 17v-2.34"></path>
                    <path d="M14 14.66V17c0 .55.47.98.97 1.21l1.25.5c.5.2 1.28.2 1.78 0l1.25-.5c.5-.23.97-.66.97-1.21v-2.34"></path>
                    <path d="M18 2H6l2 7h8l2-7Z"></path>
                    <path d="M12 9v4"></path>
                </svg>
            </div>
            {variations['card1_title']}
          </h3>
          <p class="cs-item-text">
            {variations['card1_text']}
          </p>
        </li>
        <li class="cs-item fx slide-top staggered-m" style="--i:5">
          <h3 class="cs-h3">
            <div style="width: 24px; height: 24px; flex-shrink: 0;">
                <svg class="cs-h3-icon" aria-hidden="true" viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="var(--primary)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <circle cx="12" cy="12" r="10"></circle>
                    <path d="m9 12 2 2 4-4"></path>
                </svg>
            </div>
            {variations['card2_title']}
          </h3>
          <p class="cs-item-text">
            {variations['card2_text']}
          </p>
        </li>
      </ul>
    </div>

    <div class="cs-content fx slide-top staggered-m" style="--i:2">
      <hr />
      <br /><br />

      <h1 class="cs-title">Professional {service_display} in <span class="cs-color">{city_name}, Michigan</span></h1>

      <br />
      <h3>Why Choose Asphalt Express LLC for {service_display} in {city_name}</h3>
      <br />
      <p>
        At Asphalt Express LLC, we're proud to serve the {city_name} community with professional {service_display.lower()} that enhance your property's value and functionality. Our experienced team understands the unique needs of {city_name} residents and businesses, delivering quality workmanship with over 30 years of experience and owner supervision on every jobsite.
      </p>

      <br />
      <hr />
      <br />

      <div class="desktop-only">
        <h3>Our {service_display} Services in {city_name}</h3>
        <ol>
          <li>Professional {service_display.lower()} installation and repair</li>
          <li>Quality materials and expert workmanship</li>
          <li>Owner supervised on every jobsite</li>
          <li>Free estimates for all services</li>
        </ol>

        <h4>Benefits of Professional {service_display} in {city_name}</h4>
        <ul>
          <li>Increases property value and curb appeal</li>
          <li>Expert installation with local knowledge</li>
          <li>Owner supervised on every jobsite</li>
          <li>Free estimates for all services</li>
          <li>Quality materials and professional service</li>
        </ul>
      </div>
    </div>
  </div>
  <div class="cs-bubbles" aria-hidden="true"></div>
</section>

<!-- ============================================ -->
<!--                  Services                    -->
<!-- ============================================ -->

<section id="services-563">
  <div class="cs-container">
    <picture class="cs-picture fx slide-top staggered-m" style="--i:1">
      <source media="(max-width: 600px)" srcset="/images/{img_1}">
      <source media="(min-width: 601px)" srcset="/images/{img_1}">
      <img loading="lazy" decoding="async" src="/images/{img_1}" alt="{service_display.lower()} consultation in {city_name}, Michigan" width="630" height="528" aria-hidden="true">
    </picture>
    <div class="cs-content fx slide-top staggered-m" style="--i:2">
      <span class="cs-topper">Featured Service</span>
      <br />
      <h3 class="cs-h3">Professional {service_display} in <span class="cs-color">{city_name}</span></h3>
      <p class="cs-text">
        Our comprehensive {service_display.lower()} services are designed to meet all your needs in {city_name}. We provide professional solutions with quality materials and expert workmanship.
      </p>
      <ul class="cs-ul">
        <li class="cs-li">
          <div style="width: 16px; height: 18px; flex-shrink: 0;">
              <svg class="cs-icon" aria-hidden="true" viewBox="0 0 24 24" width="16" height="18" fill="none" stroke="var(--primary)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M5 12h14"></path>
                  <path d="m12 5 7 7-7 7"></path>
              </svg>
          </div>
          Professional {service_display.lower()} installation and repair
        </li>
        <li class="cs-li">
          <div style="width: 16px; height: 18px; flex-shrink: 0;">
              <svg class="cs-icon" aria-hidden="true" viewBox="0 0 24 24" width="16" height="18" fill="none" stroke="var(--primary)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M5 12h14"></path>
                  <path d="m12 5 7 7-7 7"></path>
              </svg>
          </div>
          Quality materials and expert workmanship
        </li>
        <li class="cs-li">
          <div style="width: 16px; height: 18px; flex-shrink: 0;">
              <svg class="cs-icon" aria-hidden="true" viewBox="0 0 24 24" width="16" height="18" fill="none" stroke="var(--primary)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M5 12h14"></path>
                  <path d="m12 5 7 7-7 7"></path>
              </svg>
          </div>
          Owner supervised on every jobsite
        </li>
      </ul>
      <a href="/contact" class="cs-button-solid">Get Free Estimate in {city_name}</a>
    </div>
  </div>
</section>

<!-- ============================================ -->
<!--              Service Area Map                -->
<!-- ============================================ -->

<section id="service-area-map">
  <div class="cs-container">
    <div class="cs-content">
      <span class="cs-topper">Service Areas</span>
      <h2 class="cs-title">Proudly Serving Southeast Michigan</h2>
      <p class="cs-text">
        Asphalt Express LLC is your trusted local asphalt paving and maintenance expert, serving communities throughout Oakland, Livingston, Wayne, and Macomb Counties. Our experienced team delivers quality workmanship to both residential and commercial customers across the region.
      </p>
    </div>
    <div class="cs-map-wrapper">
      <div class="cs-map-container fx slide-top staggered-m" style="--i:1">
        <iframe
          src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d948481.7108714974!2d-84.28402282550397!3d42.59168454510316!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8824d23516b4c889%3A0xc7f96240f6e27736!2sOakland%20County%2C%20MI!5e0!3m2!1sen!2sus!4v1717259708888!5m2!1sen!2sus"
          width="100%"
          height="400"
          style="border:0;"
          allowfullscreen=""
          loading="lazy"
          referrerpolicy="no-referrer-when-downgrade"
          title="Asphalt Express LLC Service Area Map">
        </iframe>
      </div>
      <div class="cs-service-areas fx slide-top staggered-m" style="--i:2">
        <h3 class="cs-areas-title">Areas We Serve</h3>
        <ul class="cs-areas-list" style="grid-template-columns: repeat(2, 1fr);">
{service_area_list}
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- ============================================ -->
<!--                    FAQ                       -->
<!-- ============================================ -->

<section id="faq-254">
  <div class="cs-container fx fade-in">
    <div class="cs-content">
      <span class="cs-topper">FAQ's</span>
      <h2 class="cs-title">{service_display} in {city_name} FAQs</h2>
      <p class="cs-text">
        Answers to common questions about our {service_display.lower()} in {city_name}, Michigan by Asphalt Express LLC.
      </p>
    </div>
    <div class="cs-flex-group">
      <ul class="cs-faq-group fx slide-top staggered-m" style="--i:1">
        <li class="cs-faq-item active">
          <button class="cs-button">Do you serve {city_name}, Michigan?</button>
          <p class="cs-item-p">
            Yes! Asphalt Express LLC proudly serves {city_name} and surrounding communities. We provide comprehensive {service_display.lower()} throughout the area.
          </p>
        </li>
        <li class="cs-faq-item">
          <button class="cs-button">How long does {service_display.lower()} work take in {city_name}?</button>
          <p class="cs-item-p">
            Project timelines vary based on size and scope. Most projects take 1-3 days, while larger commercial projects may take longer. We work efficiently while ensuring quality results.
          </p>
        </li>
        <li class="cs-faq-item">
          <button class="cs-button">Do you provide free estimates in {city_name}?</button>
          <p class="cs-item-p">
            Yes. We provide free estimates on all our services in {city_name}. Our professional team members will come out and give you our recommendation for your project while keeping your budget in mind.
          </p>
        </li>
        <li class="cs-faq-item">
          <button class="cs-button">What is your satisfaction guarantee?</button>
          <p class="cs-item-p">
            We stand behind every job 100% with our commitment to quality and customer satisfaction. Owner supervised on every jobsite ensures the highest standards for {city_name} residents and businesses.
          </p>
        </li>
        <li class="cs-faq-item">
          <button class="cs-button">What {service_display.lower()} do you offer in {city_name}?</button>
          <p class="cs-item-p">
            We offer comprehensive {service_display.lower()} in {city_name} including installation, repair, and maintenance services with professional workmanship and quality materials.
          </p>
        </li>
      </ul>

      <div class="cs-cta fx slide-top staggered-m" style="--i:2">
        <h3 class="cs-h3">Ready for Professional {service_display} in {city_name}?</h3>
        <p class="cs-cta-p">
          Contact us today for your free estimate and experience quality service with our professional {service_display.lower()} in {city_name}, Michigan.
        </p>
        <a href="/contact" class="cs-button-solid">Contact Us Now</a>
      </div>
    </div>
  </div>

  <script>
    const faqItems = Array.from(document.querySelectorAll('.cs-faq-item'));
    for (const item of faqItems) {{
      const onClick = () => {{
        item.classList.toggle('active')
      }}
      item.addEventListener('click', onClick)
    }}
  </script>
</section>
'''
    return content

def main():
    """Generate all service pages for all cities."""
    base_dir = 'src/pages/servicepages/cities'
    
    # Create directory if it doesn't exist
    os.makedirs(base_dir, exist_ok=True)
    
    count = 0
    for city_name, city_slug in all_cities:
        for service_config in services:
            filename = f'{service_config[5]}-in-{city_slug}.html'
            filepath = os.path.join(base_dir, filename)
            
            content = generate_page_content(city_name, city_slug, service_config)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            count += 1
            print(f'Generated: {filename}')
    
    print(f'\nTotal pages generated: {count}')

if __name__ == '__main__':
    main()

