# Creative Spark Images – Photography Shop

## Table of Contents

- [About the Project](#about-the-project)
- [Responsive Mock-up View](#responsive-mock-up-view)
- [Business Plan](#business-plan)
- [Design & Planning](#design--planning)
- [Agile Methology](#agile-methology)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Features Left to Implement](#features-left-to-implement)
  - [404 Page](#404-page)
- [The Admin Panel](#the-admin-panel)
- [Security Features and Error Handling](#security-features-and-error-handling)
- [Page performance](#page-performance)
- [Testing](#testing)
  - [Test Matrix](#test-matrix)
- [Version Control](#version-control)
- [Sitemaps](#sitemaps)
- [Technology Stack](#technology-stack)
- [Deployment](#deployment)
- [Usage](#usage)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)
- [Author](#author)
- [License](#license)

---
---

## About the Project

**Creative Spark Images** is a feature-rich eCommerce web application built for photographers to sell digital and printed artworks.

Photography has always been more than just a hobby for me — it’s how I pause time, soak in the stillness of a landscape, and capture fleeting moments of beauty in nature that speak louder than words ever could. It’s a way of reconnecting with myself, especially when life feels loud. The quiet detail in a morning mist or the vibrant warmth of golden hour light — those are the moments that move me. After years of collecting these snapshots of the world around me, it felt like the right time to bring them together and share them with others who see the world a little more tenderly too. That’s how Creative Spark Images came to life.

This project is my take on a curated online photography shop — clean, modern, and calm — built with the same level of care and attention to detail I put into each image. Visitors can browse a growing gallery of images that reflect a deep love for the outdoors, and purchase either digital versions (complete with licensing) or printed formats like canvas, posters, or framed art to bring the essence of nature into their own spaces.

The entire site is crafted with intention — not just in functionality, but in feel. The interface is designed to be intuitive and clutter-free, allowing the work itself to breathe. There’s a deep sense of rhythm in the visuals and structure, making browsing feel like a meditative experience. It’s a space that feels human — made for nature lovers, fellow photographers, and anyone who finds joy in the quiet magic of the natural world.

Creative Spark Images isn’t just a portfolio or a shop — it’s a visual love letter to the world we live in. Built for explorers, artists, and nature seekers alike, this project is where tech and creativity meet in quiet harmony.

>  The live site can be found here – [https://creative-spark-images-shop-6e4790dd908e.herokuapp.com/]

---
---

## Responsive Mock-up View

![Responsive Mock-up View](README_Media/responsive_mockup.png)

---
---

## Business Plan

# Creative Spark Images  
### *A Digital & Printed Photography eCommerce Platform*

---

## Executive Summary

**Creative Spark Images** is a refined online photography shop blending nature-inspired visual storytelling with seamless eCommerce functionality. Designed for nature lovers, designers, and art collectors, the platform offers both digital and physical art prints via a serene, cinematic user experience. With active social media presence on Facebook and Instagram over the past five years, the brand already enjoys an engaged following and visual credibility that accelerates market entry.

---

## Business Objectives

- Monetize a curated portfolio of photography through digital licenses and fine-art print sales
- Leverage an existing social media audience to drive store traffic and brand loyalty
- Expand into multilingual European markets
- Launch targeted campaigns for seasonal collections and limited editions
- Build a sustainable digital art brand with potential for future scaling

---

## Business Strategy: B2C First, B2B Expansion Later

Creative Spark Images will begin as a **B2C-focused business**, selling digital downloads and printed artworks directly to individual customers through the online store. This approach allows for organic brand growth, leveraging existing audiences on Facebook and Instagram, and refining the user experience based on real-time customer feedback.

### Why B2C First?
- Immediate revenue potential with lower operational complexity
- Builds brand credibility and community
- Allows refinement of product-market fit before scaling operations
- Capitalizes on 5 years of social media presence and personal brand recognition

---

## Transitioning to B2B (While Retaining B2C)

The long-term strategy includes developing a **B2B offering in parallel**, without compromising the existing B2C channel. The two segments will complement each other — B2C remains the foundation, while B2B becomes a scalable revenue stream through licensing, bulk orders, and collaborations with businesses.

### B2B Target Segments
- Interior designers and decorators
- Hospitality (hotels, spas, cafés)
- Marketing and media agencies
- Publishers and corporate offices

### Key B2B Offerings
- Commercial licensing tiers
- Bulk print orders at volume pricing
- Custom-curated collections for business interiors
- Subscription-based access to digital assets
- Invoicing and VAT-compliant workflows

---

## Timeline: B2C to B2B Expansion

| Timeline | Strategy Focus                        |
|----------|----------------------------------------|
| Months 0–3  | Launch B2C shop, promote via social media |
| Months 4–6  | Set up B2B page, licenses, and inquiry flow |
| Months 6–12 | Begin B2B outreach, secure pilot clients    |
| Months 12–18| Offer curated business packages, scale B2B |

---

### Maintaining Both Channels

- B2C remains active and prioritized in UX and marketing
- Separate navigation and content will be provided for B2B customers (e.g., “For Businesses” page)
- Cross-promotional opportunities will allow existing fans to refer or introduce B2B leads
- Systems will be built to support both streams: dynamic pricing, order management, and customer segmentation

> This dual-channel approach ensures long-term sustainability, diversified income, and broader reach — all while staying true to the heart of Creative Spark Images: connecting people to nature through visual art.

---

## Products & Services

### Digital Photography Downloads
- Editorial & Personal License
- Commercial License
- Advertising License

### Printed Formats
- Posters
- Canvas Prints
- Framed Art

### Value-Added Features
- Dynamic special offers (e.g., Free Shipping, Buy X Get Y)
- Curated gallery by theme
- Licensing transparency through a structured license info page
- Contact and support form
- Future roadmap: ratings, SEO enhancements, and social media integrations

---

## Target Market

### Primary Audience
- Nature and landscape photography collectors
- Interior decorators and design studios
- Content creators, marketers, and advertisers
- Tourists and expats nostalgic for Irish/European landscapes

### Geographic Focus
- English-speaking Europe (UK, Ireland)
- DACH region (Germany, Austria, Switzerland)
- France and Spain (planned language rollouts)

---

## Unique Value Proposition (UVP)

**Creative Spark Images** is not only a thoughtfully crafted store — it’s the digital extension of an already-recognized visual brand. With a **5-year presence on Instagram and Facebook**, it offers a familiar and authentic connection for followers now able to support the artist directly through secure and beautiful purchases.

---

## Business Model

### Revenue Streams
1. **Digital Downloads** – High-margin, low-overhead
2. **Print Sales** – Print-on-demand or in-house fulfillment
3. **Limited Editions / Promotions** – Seasonal exclusives
4. **Future: Commissioned Work** – Premium, bespoke options

### Cost Structure
- Hosting & domain
- Transaction fees (Stripe, Zapier)
- Printing & shipping
- Visual asset creation
- Marketing (ads, tools, partnerships)

---

## Technology Stack

- **Backend:** Django, PostgreSQL
- **Frontend:** HTML5, CSS3, Bootstrap, JavaScript
- **eCommerce:** Stripe Integration
- **Admin Tools:** Django Admin, Crispy Forms
- **Email Automation:** Zapier
- **Media Storage:** Cloudinary
- **Testing/CI:** Automated test scripts, user flow testing
- **Security:** CSRF, session handling, validation

---

## Operations Plan

### Order Fulfillment
- Digital: Instant download post-payment
- Prints: Partner or manual fulfillment

### Customer Support
- Contact form (form validation and feedback)
- Admin message handling

### Inventory Management
- Controlled through Django Admin
- Dynamic product, license, and print type settings

---

## Marketing & Growth Strategy

### Phase 1: Foundation (0–3 months)
- Announce store launch to existing Facebook/Instagram followers
- Use organic posts and story features
- Add bio links and product tags where applicable
- Begin collecting emails for newsletters

### Phase 2: Expansion (3–12 months)
- Boost high-performing posts via Meta Ads
- Launch targeted Instagram/Facebook ads
- Collaborate with photographers and lifestyle influencers
- Promote seasonal offers and UGC stories

### Phase 3: Scale (12+ months)
- Embed Instagram feed on the homepage
- Run giveaways and contests to boost engagement
- Launch a referral program

---

## SWOT Analysis

### Strengths
- Established social media presence
- Emotionally resonant brand story
- Fully functional multilingual store
- High-quality visuals and UX

### Weaknesses
- Limited initial SEO/social integrations
- Manual fulfillment overhead
- No current user-generated content system

### Opportunities
- Convert loyal followers into customers
- Partner with design/lifestyle influencers
- Expand into Instagram Shopping
- Monetize storytelling and UGC

### Threats
- Competition from larger photo marketplaces
- Changes to social platform algorithms
- Image piracy/digital license abuse

---

## Financial Projections (Year 1 Estimate)

| Metric                         | Value                  |
|--------------------------------|------------------------|
| Avg. Digital Product Price     | €10                   |
| Avg. Printed Product Price     | €20                   |
| Assumed Sales Mix              | 60% digital / 40% printed |
| Avg. Order Value (blended)     | €14 (0.6×10 + 0.4×20)  |
| Monthly Orders Estimate        | 150                   |
| Annual Orders                  | 1,800                 |
| **Annual Revenue**             | €25,200 (1,800 × €14) |

### Estimated Costs

| Cost Category                  | Estimate (EUR)         |
|--------------------------------|------------------------|
| COGS (prints & shipping, ~35%) | €8,820                |
| Stripe & Ops Fees (~15%)       | €3,780                |
| **Net Revenue**                | **€12,600**            |

---

## Milestones & Timeline

| Quarter | Goal |
|--------|------|
| Q1     | Launch store, promote on social media |
| Q2     | Start ad campaigns, build email list |
| Q3     | Run seasonal limited edition promos |
| Q4     | Launch Instagram integration and referral program |

---

## Team & Roles

| Role       | Responsibility |
|------------|----------------|
| Founder    | Photography, design, development, customer support |
| (Future) Assistant | Fulfillment and email responses |
| (Future) Marketing | Paid ads, SEO, influencer partnerships |

---

## Risk Management

- Regular platform backups
- Stripe keys stored securely
- CSRF, input, and session protection
- GDPR-compliant user deletion
- Email send error catching via Zapier and Django messages

---

## Exit Strategy

- License the platform to other creators
- Expand into multi-artist marketplace
- Potential acquisition by photography or art platforms

---

## Appendices

- Live Site: [https://creative-spark-images-shop-6e4790dd908e.herokuapp.com](https://creative-spark-images-shop-6e4790dd908e.herokuapp.com)
- Instagram: [https://www.instagram.com/irelandinsunset/](https://www.instagram.com/irelandinsunset/)

![Instagram](README_Media/instagram.png)

- Facebook: [https://www.facebook.com/profile.php?id=61574557148446](https://www.facebook.com/profile.php?id=61574557148446)

![Facebook](README_Media/fb_business_page.png)

- Tech Stack Summary
- Licensing Examples
- Admin Panel Capabilities

---
---

## Design & Planning

### Wireframes

#### Homepage

  ![Homepage Wireframe](README_Media/wireframe-homepageUpper.png)
  ![Homepage Wireframe](README_Media/wireframe-homepageLower.png)

#### Profile Section
  ![Checkout Order Summary Wireframe](README_Media/wireframe_profile_card.png)
  ![Checkout Order Summary Wireframe](README_Media/wireframe_order_history_card.png)

#### Gallery

  ![Gallery Wireframe](README_Media/wireframe_gallery_sm-md-screens.png)
  ![Gallery Wireframe](README_Media/wireframe_gallery_l-xl-screens.png)

#### Images by Theme
  
  ![Images by Theme Wireframe](README_Media/wireframe_images_by_theme_sm-screens.png)
  ![Images by Theme Wireframe](README_Media/wireframe_images_by_theme_md-l-screens.png)
  ![Images by Theme Wireframe](README_Media/wireframe_images_by_theme_xl-screens.png)

#### Product Customization Page

  ![Product Wireframe](README_Media/wireframe_product_sm-screens.png)
  ![Product Wireframe](README_Media/wireframe_product_md-l-xl-screens.png)

#### Shopping Bag
  ![Shopping Bag Wireframe](README_Media/wireframe_shopping_bag_sm-md-screens.png)
  ![Shopping Bag Wireframe](README_Media/wireframe_shopping_bag_l-xl-screens.png)

#### Checkout Page - Customer Data
  ![Checkout Customer Wireframe](README_Media/wireframe_CO_customer.png)

#### Checkout Page - Order Confirmation Page
  ![heckout Order Confirmation Wireframe](README_Media/wireframe_order_confirmation.png)

### Mockups
- Page mockups are displayed in the [Existing Features](#existing-features) sections.

### Diagrams

#### Key Entities and Relationships

  ![ERD Diagram](README_Media/erd_e-commerce.png)

  Users & Profiles
  - User (Django auth)
    ↔ OneToOne → UserProfile
    ↔ OneToMany → OrderModel

Orders
  - OrderModel
    - belongs to User (ForeignKey)
    - has many Products (ManyToManyField)

Products & Metadata
  - Product
    - ForeignKey → ImageTheme
    - ManyToMany → ProductType
    - ManyToMany → LicenseType
    - ManyToMany → PrintType
    - ManyToMany → Tag

Tag
  - ForeignKey → TagGroup

PrintType
  - ForeignKey → ProductType

Shop
  - ImageTheme
    - linked to Product (ForeignKey)
    - linked to SpecialOffer

PolicyPage: standalone (Privacy, Cookies, Terms)

Shipping & VAT
  - ShippingRate
    - ForeignKey → Shipper
    - Country as CharField (not FK)
    - CountryVAT: standalone, per country

Marketing
  - NewsletterSignup: standalone.
  - SpecialOffer
    - may apply to an ImageTheme.

AboutUs: standalone content

---

#### Checkout Flow Chart

![Checkout Flow Chart](README_Media/checkout_flow_chart.jpg)

---
---

## Agile Methology

This project was developed using Agile methodology, with a strong focus on iterative development, user stories, and continuous testing.  
A GitHub Kanban board was used to manage the project, track progress, and ensure transparency in the workflow.  
The board was divided into the columns **Ready**, **In Progress**, **In Review**, **Done**, and **Will Not Be Implemented**, enabling clear sprint planning and prioritisation of tasks.  

### Key Points of Agile Usage in this Project

- **User Stories**: Each feature was captured as a user story (e.g., *User Registration & Login*, *Wishlist*, *Downloading Purchased Images*).  
  This ensured that all functionality was tied directly to user needs and business goals.  

- **Incremental Delivery**: Features were built, tested, and moved through the board step by step.  
  For example: *Adding items to shopping cart* → *Checkout & making a purchase* → *Checkout progress tracker*.  

- **Backlog & Scope Control**: Non-essential features (*Custom Music Player*, *Admin Dashboard for Sales Insights*) were explicitly marked under *Will Not Be Implemented*.  
  This demonstrates prioritisation and scope management.  

- **Completed User Stories (Done)**:  
  - **Authentication & Profiles**: User registration, login, and profile management were implemented successfully.  
  - **Shopping Flow**: Viewing products, adding to cart, checkout process, checkout tracking, and downloading purchased images are complete.  
  - **Admin Functionality**: Managing user data, license options, orders, images, and website content (text, footer, SEO).  
  - **Marketing Features**: Newsletter signup and Facebook Business Page setup were added.  
  - **Enhancements**: Order history, immersive UX improvements, and site monitoring completed.  

- **Agile Transparency**: All tasks were visible on the Kanban board and tracked from *Ready* to *Done*.  
  This ensured progress could be reviewed at any time.  

- **Review & Testing**: Items moved through an *In Review* column before being marked as *Done*, aligning with Agile’s focus on validation and feedback.  


The Agile methodology ensured:
- Features were developed in line with user stories.  
- Project scope was managed realistically.  
- Progress was documented and traceable via the Kanban board.  
- The final product reflects both user needs and continuous iteration.  

link to the Kanban board for transparency:  

https://github.com/users/merzann/projects/8

The Kanban Board

![Kanban Board](README_Media/kanban_board.png)

---
---

## Existing Features

### Summary

  Users can:
  - Browse curated photographic works
  - Choose between **digital formats with licenses** or **printed formats** like canvas, poster, or framed print
  - Add products to a dynamic **shopping cart** with instant summary updates
  - Checkout securely via **Stripe**, with **automated order processing**
  - Receive confirmation emails via **Zapier** integration

  Admin users can:
  - Manage products, print types, and license types
  - Track orders via a robust **OrderModel**
  - Use Django Admin for full backend control

### Existing Features Summary

- Full product catalog and detail pages
- Format selection toggle (Digital vs Printed)
- License and print type options
- Dynamic price calculations (VAT, shipping, total)
- Custom Django template tags (`get_range`)
- Session-based shopping cart
- AJAX-based cart updates and feedback
- Stripe integration for payments
- Zapier email notifications on purchase
- Order management with unique `order_number`
- Extendable language selection menu (currently implemented: EN/planned: DE,ES,FR)
- Admin control via Django backend

---
---

## Color Palette:

The color palette reflects the deep connection to nature:

- Soft sand beige (#ddd), Sonic Silver (#7c7575)and warm earth brown (#333) echo tree bark and stone
- Cool slate gray for shadows and depth
- Hints of forest green and gentle sky blue across UI highlights

Balanced by off-white tones to make every page easy on the eyes and accessible across devices
These nature-inspired hues create a grounded, peaceful atmosphere — mirroring the very environments these images come from. The goal? To invite people in, let them slow down, and experience photography the way it was meant to be felt: personally.

Behind the scenes, the project is backed by a robust Django framework — dynamic shopping bag functionality, Stripe integration, Zapier automation for email confirmations, and a thoughtfully designed order system with metadata-rich order tracking. For photographers and creators like me, the Django Admin panel is a dream to work with — intuitive, powerful, and secure.

---
---

## Fonts

In designing Creative Spark Images, the selection of Poiret One and Montserrat fonts aligns seamlessly with the project's ethos. Poiret One's sleek, geometric elegance mirrors the refined simplicity of the platform, adding a touch of sophistication that resonates with the artistic nature of the showcased photography. Its graceful curves echo the organic forms found in nature, enhancing the visual narrative of each captured moment.​

Complementing this, Montserrat's modern, geometric structure offers exceptional readability across various devices and screen sizes, ensuring a smooth and engaging user experience. Its design, rooted in urban typography, brings a contemporary flair that balances the natural themes of the artwork, bridging the gap between the digital interface and the organic subjects of the photographs.​

Together, Poiret One and Montserrat create a harmonious typographic duo that embodies the essence of Creative Spark Images—a platform where technology and creativity converge to celebrate the quiet magic of the natural world.​

---
---

## The Logo

The Creative Spark Images logo is more than just a visual mark — it's a reflection of the soul behind the lens. The sketched figure of a woman holding a camera isn't just any figure; it's a stylized self-portrait — a symbolic representation of the creator herself.

With flowing hair and a quiet, focused gaze, the woman in the logo captures the meditative stillness that defines much of my photography. The camera in hand is both a tool and a metaphor — a means of connection, presence, and storytelling. This artistic sketch bridges the digital and natural worlds, just as Creative Spark Images blends technology with emotion and intention.

The elegant, handwritten-style typography of Creative Spark Images mirrors the thoughtful and creative nature of the work — soft, expressive, and inviting. It evokes a personal signature, reminding viewers that this isn’t just a brand — it’s an extension of a lived artistic journey.

Everything about the logo — from its monochrome simplicity to the organic curves — echoes the brand's core philosophy: to create a space that feels both curated and deeply human. It's a gentle nod to the artist behind the scenes, her relationship with nature, and the quiet beauty captured through the lens.

This logo is not just a visual identity — it's a moment, a mood, and a mirror of the artist's spirit. It invites the viewer into a world where photography becomes more than images — it becomes experience, reflection, and connection.

![Logo Mobile](README_Media/creative_spark_images_photography_shop(logo).png) ![Logo Desktop](README_Media/creative_spark_images_photography_shop_logo.png)

---
---

## The Homepage

The homepage of Creative Spark Images acts as a narrative-driven landing page blending visual storytelling, interactive transitions, and practical navigation. It sets the tone for the brand’s aesthetics while guiding users towards the gallery, store, or About-Us-section with cinematic flair and UX clarity.


### Features & Functionality

#### Homepage part 1: Hero Section with Background Video
- Full-screen looping background video (`sunny_day_in_waterville.mp4`) of Ballinskelligs Bay.
- Overlay text highlights:
  - `Nature & Wildlife Photography`
  - `Experimental Photography`
  - `Landmarks`
  - `Historical Sites`

**Newsletter Signup Modal**
- Immediately below the catch phrase, users are invited to **sign up for the newsletter** via a reusable modal.
- Key features include:
  - Fields for First Name, Last Name, Email Address
  - Client-side validation with required fields
  - Real-time success and error messages (Bootstrap alerts)
  - Duplicate email prevention
  - Styled with rounded corners and smooth transitions
  - Fully integrated with Django backend via `NewsletterSignup` model and `newsletter_signup` view

**Special Offer Display**
- A **wooden signboard** graphic shows the current `SpecialOffer`, conveying a feeling of actually being at a real location in Ireland.
- Dynamically rendered using:
  - **Offer Text** (`safe`-rendered HTML from admin input)
  - **Countdown Timer** (`data-expiry` handled via JS)
- Logic managed in `apply_special_offer()` from `checkout/views.py`:
  - Free Shipping
  - % General discounts
  - % Discount on products of a specific theme
  - Buy X Get Y Free

**Road Signs Navigation**
- The two interactive road signs further support the feeling of actually being at a real location.
  - **Gallery**: triggers animation and redirect
  - **About Us**: scrolls smoothly to the about section

![Upper Homepage part1](README_MEDIA/homepage_upper_pt.1.png)


**Fallback Image**
- A fallback image is implemented via the .video-container's background style to ensure the overlay content remains visible even if the video fails to load.

![Fallback Image](README_Media/sunny_day_at_ballinskelligsbay.jpg)

**Homepage part 2: Animated Gallery Entrance (initially hidden)**
  - Clicking “Gallery” fades out the intro section and plays `cottage-animation.mp4`.
  - Overlay welcome message appears and fades.
  - After ~6 seconds, user is redirected to `/shop/gallery/`.
  - The animation can be skipped by selecting 'Gallery -> Images by Theme' from the Menu in the Navbar which takes the User directly to the gallery room

![Upper Homepage Animation](README_Media/homepage_animation.png)

**Audio Toggle**
  - Walking sound plays during animation (`walking-on-gravel.mp3`).
  - Easy accessible toggle button (🔇 / 🔊).

---

#### Navigation & UX Considerations

| Element               | Destination / Functionality                                     |
|-----------------------|-----------------------------------------------------------------|
| **Gallery Sign**      | Triggers animation, redirects to `/shop/gallery/`               |
| **Newsletter Modal**  | Opens popup for name/email submission                           |
| **About Us Sign**     | Scrolls smoothly to `#about-section`                            |
| **Back to Top Button**| Scrolls to `#intro` section                                     |
| **Navbar Links**      | Skip animation, direct access to views like "Gallery by Theme"  |
| **Accessibility**     | Aria-label and aria-labledby attributes on all main sections and clickable elements ensure accessibilty requirements are met |

---

#### UX Design Principles

- Cinematic animation enhances storytelling.
- Scroll interactions guide users naturally through content.
- Real-world visual metaphors for signs and boards.
- Newsletter modal prioritizes unobtrusive engagement.
- All interactions remain accessible and responsive.

---

#### Backend Integration

- Homepage content is fully dynamic:
  - `AboutUs` content via Django Admin + Summernote.
  - `SpecialOffer` logic includes:
    - Expiry date filtering
    - Conditional display
    - Bag-level modifications during checkout
- Newsletter data is saved to the `NewsletterSignup` model with:
  - Unique email constraint
  - Admin CSV export action
- Countdown managed with JavaScript using `data-expiry` rendered server-side.

---

### About us section

The About section tells a heartfelt story of chasing golden light, capturing nature’s beauty, and transforming those moments into prints and calendars — blending art, adventure, and authenticity. A warm, sunset-lit profile photo the owner of the shop, the passionate eye behind Creative Spark Images.

#### Features

  - Dynamically displays content from the Django Admin (`AboutUs` model).
  - Responsive card layout with image and rich text formatting.
  - Positioned directly below the intro section.
  - Clean separation of layout and behavior via HTML, CSS, and JS.
  - CSS handles animations and positioning.
  - JavaScript uses `DOMContentLoaded` to ensure timing and availability of DOM elements.
  - Fully responsive and mobile-compatible design.

**About Us Navigation (Road Sign)**
  - Clickable **“About Us” road sign** on the homepage scrolls the user smoothly to the About section.
  - Uses `scrollIntoView` for a polished UX.
  - Provides intuitive and quick access without reloading or navigating away.

**Back to Top Button**
  - Smoothly scrolls the user back to the top of the page.
  - Fully accessible with `aria-label` and hover state.

**content Management**
  - profile image and content are managed from the Backend through the Admin Panel

---

**UX Considerations**
  - Consistent scrolling behavior for both the About and Back-to-Top buttons.
  - Intro section reappears on scroll-up if it was previously hidden (e.g., by gallery animation).
  - Elegant appearance matching the site's brand — including text shadow, elegant fonts, and card layout.
  - Fallback image used when no About image is provided.
  - The installation of summernote allows users to include rel-attributes into their content

![About us Homepage scetion](README_Media/about_us_section.png)

---
---

## Newsletter Signup

A globally accessible, reusable modal component that enables visitors to subscribe to a newsletter with instant feedback and admin-side export functionality.

---

### Summary

- **Modal-based signup form** that can be injected anywhere in the project.
- **Fields collected**:
  - First Name
  - Last Name
  - Email Address
- **Client-side validation** for all required fields.
- **Django messages framework** provides real-time user feedback on form submission.
- **Duplicate signup prevention**: Warns if email is already registered.
- **Success and error messages** styled with Bootstrap alerts and dismissible buttons.
- **Admin-side export**: Staff can export selected newsletter signups to CSV.
- Fully integrated with Django Admin, using the `NewsletterSignup` model.

---

### Structure & Components

#### From the User’s Perspective

- Clicking newsletter opens as a **modal popup**, styled with Bootstrap, rounded corners, and centered.

- Users can interact with:
  - First Name input field
  - Last Name input field
  - Email Address input (with placeholder and email validation)
  - Submit button (`Sign Up`)
  - Dismissal link (`Not now`)
  - Close (×) button in the top-right
- **Feedback**:
  - Success message: “Thank you for signing up!”
  - Duplicate email warning: “⚠ You have already signed up...”
  - Validation error: “⚠ There was a problem...”

- The newwsletter has been implemented in 3 key areas: 
  - center of the homepage (Signup via popup-modal)
  - order confirmation page (Signup via popup-modal)
  - order confirmation email (signup via link)

#### From the Admin’s Perspective

- Admin interface for `NewsletterSignup` shows:
  - Email
  - First Name
  - Last Name
  - Signup Timestamp
- Searchable and sortable in the admin dashboard.
- **CSV export feature via custom action**:
  - Download email, name, and signup time with one click.
  - Filename defaults to `newsletter_signups.csv`.

---

### Technical Structure & Functionalities

- **Model**: `NewsletterSignup` includes unique email constraint and auto timestamp.
- **Form**: Uses `ModelForm` with field-level validation and custom placeholders.
- **View**: `newsletter_signup()` handles POST requests only and redirects back.
- **Message handling**: Feedback via Django’s built-in messaging system.
- **Template**: Newsletter modal styled with Bootstrap, can be reused site-wide.

---

### Security & UX Defenses

| Type                   | Feature                                                                 |
|------------------------|-------------------------------------------------------------------------|
| CSRF Protection        | All forms protected using `{% csrf_token %}`                           |
| Duplicate Detection    | Prevents multiple subscriptions using `.filter(email=email).exists()`  |
| Required Fields        | All fields are marked `required` and validated both client- and server-side |
| Admin Export Restriction | CSV export only available to logged-in admin users                   |
| Modal Dismissal Options| Users can opt out via "Not now" link or close button                   |

---
---

## Navbar

### Menu

---

### Logo

The 'home'-url anchored to logo allows the user to return to the home page from any point within the web application.

---

### User dropdown menu

<u>Dropdown States:</u>

When no user is signed the following options are displayed:

- **Create an account:** Allows the user to to create an account using the customised Django Sign up template.

- **Login:** Allows the user to log in using the customised Django Login Template.

![No user signed in](README_Media/user_logged_out.png)

When the user is logged in the following options are displayed:

- **My Profile**: allows the user to access their user profile and update their information or delete their profile or view their order history
- **Order History:** provides direct access to the order history
- **My Wishlist:** provides direct access to the wishlist
- **Logout:** allows the user to log out and continue to browse the page as guest

![User signed in](README_Media/user_logged_in.png)

---

### Access to Shopping Cart

The shopping cart allows the user to access their shopping bag from any point within the application. Added items are counted in realtime and the counter updates accordingly informing the user about the number of items currently added to the bag.

![Real Time Quantity Counter](README_Media/real_time_quantity_counter.png)

---

### Extendable language selection dropdown menu

The language menu includes four of the most commonly understood languages in Europe, the future target market of Creative Spark Images: English, French, German and Spanish. Currently fully implmeneted is English.

A dynamic multilingual placeholder page was implemented to inform users when a language-specific version of the site is not yet available.

<u>Languages Supported:</u>
  - English (default fallback)
  - German
  - French
  - Spanish

![Language Menu](README_Media/language_menu.png)

---
---

### Footer

The website footer is fully responsive, accessible, and legally comprehensive, built to reinforce trust, provide clear navigation, and comply with modern data protection and e-commerce standards.

**Summary**
- **Centralized social section** with accessible social media links (Facebook, Instagram, YouTube).
- **Grouped legal/documentation links**:
  - Privacy Policy
  - Cookie Policy
  - Licenses (digital use rights overview)
  - Terms & Conditions
  - Contact Page
- **Dynamically rendered links** using Django's `{% url %}` template tag.
- **Responsive structure** with split layout for mobile and desktop views.
- **Clean and modern styling** using the global `Poiret One` (headings) and `Montserrat` (text) font stack.

---

### From the User’s Perspective

The footer is elegant, functional, and consistent with the site's design language:

- **Header ("Find us on social media")**: centered and styled with global heading font.
- **Social Icons**:
  - Font-Awesome-Icons for **Facebook**, **Instagram**, and **YouTube**
  - Each opens in a new tab with `target="_blank"` and includes `aria-labels` for screen readers.
- **Legal & Navigation Links**:
  - Positioned side-by-side on desktop, stacked on mobile.
  - Includes all necessary legal documents plus a Contact Page.
- **Copyright**
  - Automatically updates year (manual in current setup)
  - Located on the bottom right of desktop view, centered on mobile

---

### Technical Structure & Functionalities

- **Templates**:
  - The footer is included via a shared template: ```django {% include 'includes/footer_links.html' %}
  - Loaded into `base.html` under both mobile and desktop containers.
- **Routing**:
  - All links use `{% url %}` tags and rely on named views:
    - `policy_page` for privacy, cookies, terms (uses `PolicyPage` model)
    - `contact_page` for contact form
    - `license_info` for license overview (`products.views.image_licenses`)
- **Models Involved**:
  - `PolicyPage` (shop)
  - `LicenseType` (products)
- **Dynamic content**:
  - Policies and licenses are rendered from database-controlled models.
  - Content is editable via Django admin interface.

---

### Security & UX Defenses

| Type                          | Feature                                                                 |
|-------------------------------|-------------------------------------------------------------------------|
| Accessible Icons              | Social media icons have `aria-label` for screen reader support          |
| Secure External Links         | All external links use `rel="noopener"` and `target="_blank"`           |
| View Protection               | Licenses and policies pulled only if `is_active=True`                   |
| URL Resolution Safety         | All internal links use named routes (`{% url %}`) to prevent breakage   |
| Mobile UX                     | Uses `d-md-flex`/`d-md-none` for mobile/desktop layout separation       |
| Consistent Typography         | Applies global fonts via base CSS and maintains visual identity         |
| Error Prevention              | 404-safe: reverse routing avoids hardcoded URLs                         |

![Footer desktop](README_Media/footer_desktop.png)  ![Footer Mobilel](README_Media/footer_mobile.png)

---

### Contact Page

A user-friendly, styled contact form designed to facilitate customer inquiries and support, particularly related to orders, while maintaining accessibility, usability, and security.
The addition of the shop's logo further supports the personal note of the contact form.

**Summary**
- **Three essential input fields**: Name, Email, and Message.
- Integrated with Django’s `FormView` for clean separation of logic and display.
- **Server-side validation** using Django’s form API with detailed constraints:
  - Name: required, max 100 characters
  - Email: required, valid email format
  - Message: required, max 1000 characters
- Real-time **HTML5 email validation** plus visual feedback for error cases.
- Custom error feedback using Django’s messages framework.
- On successful submission, email is sent to the administrator using `send_mail`.
- On failure (e.g., SMTP error), user is notified with a styled error message.

---

### Structure & Components

- **Form Fields**:
  - `Name`: standard text field
  - `Email`: HTML5 email input with browser-native validation and red border on error
  - `Message`: textarea, capped at 1000 characters
- **Submission Button**:
  - Centrally aligned
  - Styled with `.btn-custom` and `px-5` for visual consistency
- **Feedback**:
  - Success: confirmation displayed above the form
  - Error: styled error message appears on top if message fails to send

#### Visual and UX Features

- **Elegant styling** aligned with global design system:
  - Fonts: `Poiret One` (headings), `Montserrat` (body)
  - Padding, margins, and form control spacing harmonized
- **Accessibility**:
  - Proper `label` elements linked via `for`/`id`
  - Focusable fields
  - Semantic HTML5 markup
- **Error Highlighting**:
  - Django adds `is-invalid` class automatically for erroneous inputs
  - Custom CSS displays red border for error states
- **Cross-Device Compatibility**:
  - Fully responsive layout with stacked fields and button on mobile

---

### Technical Structure & Functionalities

- **Form Class**:
  - `ContactForm` in `forms.py`
  - Uses built-in Django form fields with `max_length`, `required`, and `EmailField` constraints
- **View Logic**:
  - `ContactPage` class-based view extends `FormView`
  - Emails are sent using `send_mail()` from Django’s email backend
  - Errors like `BadHeaderError` and `SMTPException` are caught and handled gracefully
- **Message Framework**:
  - `messages.success()` for successful sends
  - `messages.error()` for email send failures
- **Security**:
  - CSRF protection enabled by default
  - Validations prevent invalid or malicious input

---

### Security & UX Defenses

| Type                     | Feature                                                                 |
|--------------------------|-------------------------------------------------------------------------|
| HTML5 Input Validation   | Browser detects invalid email addresses in real-time                    |
| Max Length Constraints   | Prevents overly long names or messages via server-side form limits      |
| Red Border on Error      | Inputs dynamically styled using `.is-invalid` for clear visual cues     |
| SMTP Error Handling      | Graceful user message if email backend is unavailable                   |
| CSRF Protection          | Enabled through `{% csrf_token %}` in the form                          |
| Feedback System          | Uses `messages` framework to avoid silent failures                      |
| Input Sanitization       | Relies on Django's built-in validators and HTML escaping                |

![Contact Page](README_Media/contact_form.png)

---
---

### Licenses Page

A well-structured, accessible page presenting key licensing options for digital image downloads. Designed for clarity and usability, this page helps customers understand usage rights and choose the appropriate license with confidence.

**Summary**
- **Three licensing options**, each represented as a uniform card:
  - **Editorial & Personal License**
  - **Commercial License**
  - **Advertising License**
  
- **Expandable card interface**:
  - Cards show title and short label by default.
  - Clicking a card reveals full license terms.
  - Only one card can expand at a time.
- **Equal height and spacing** across all cards for a visually cohesive layout.
- **Safe HTML rendering** of license descriptions stored in the database.
- **Fully responsive design** for desktop and mobile.
- **Click pointer cursor** reinforces interactivity.

- **Content**: The page content is managed through **License types** in the Products Section of the Admin Panel.

---

### Structure & Components

The Licenses Page is accessible from the footer and delivers three clearly labeled license options, each within an elegant card. 

Each card includes:
- A **heading** with the license type.
- A **subtitle**: "Overview".
- **Expandable content**: full license details slide open below on click.
- A **cursor pointer** indicating interactivity.

**User Experience Highlights:**
- Only the selected card expands — others remain collapsed.
- Expanded content may include:
  - Legal terms and notes on license transfer.
- Clean presentation with **consistent spacing**.
- Design matches the branding and aesthetics of the shop.
- Visually intuitive, with zero reloads or distractions.

---

### Technical Structure & Functionalities

- **Model**: `LicenseType` model includes `name`, `description`, `is_active`.
- **View**: `image_licenses` view filters active licenses and passes them to the template.
- **Template**: `products/includes/image_licenses.html`
  - Uses Django templating with `{{ license.description|safe }}` for HTML content.
  - Cards are styled via a custom CSS file `licenses.css`.
- **JavaScript Behavior**:
  - Each card toggles its content section independently.
  - Clicking a second card closes the previous one.
  - Transition is handled using Bootstrap `d-none` utility class.
- **Responsiveness**: Implemented using Bootstrap grid (`col-lg-4`) with custom shadow, spacing, and padding.

![Licenses Page](README_Media/licenses_page.png)

---
---

### Shopping Bag 

A polished, user-friendly feature that dynamically adapts to product configurations, provides transparency in costs, and enforces validation to reduce user error or skipped inputs.

**Summary**
- **Display of cart items** including image, title, pricing, format, and either license or print type.
- **Real-time cart updates** without page reloads, thanks to smart JavaScript event listeners.
- **Transparent pricing structure**:
  - Subtotal (excl. VAT)
  - VAT (dynamically fetched from `CountryVAT`)
  - Shipping (based on `ShippingRate` model)
  - Grand total (incl. VAT and shipping)
- **Country-specific VAT** and **shipper-specific shipping costs** handled dynamically via Admin Panel.
- **Session-based persistence** of bag items and totals.
- **Composite key system** ensures unique identification of item configurations (e.g. same product with different formats or licenses).
- **Form-based cart item updates**, including quantity, format, and print type.
- **Responsive layout** with special UX handling on small screens (buttons stacked vertically).

---

### Structure & Components

#### From the User's perspective

Upon opening the shopping cart, users are greeted with a clean, visually structured layout that displays every product they’ve added to their bag. Each item is accompanied by:

- A **thumbnail image** (takes up 50% of form height),
- The **product title**,
- A **Format dropdown** (Digital or Printed),
- A **Quantity selector** (1–10),
- A **Print Type selector** (if Printed is chosen),
- A **Subtotal display** (based on quantity × unit price),
- **two buttons for making changes to the shopping cart content**: `Update` and `Remove`.
- **two buttons to navigate back to the gallery and checkout**: `Continue Shopping` and `Proceed to Checkout`

**Smart Behavior:**
- If the user switches from Digital to Printed, the *Print Type* dropdown appears automatically.
- The **Update** and **Proceed to Checkout** buttons are automatically disabled when necessary **preventing the user from proceeding** until all changes made to items in the bag are confirmed
- An inline warning informs users if any updates still need confirmation.

This provides clarity and control while avoiding any accidental submissions with incomplete data.

**User Experience Highlights:**
- Immediate visual feedback on updates.
- No reloads needed to change format, quantity, or type.
- Responsive layout: buttons adapt on mobile and desktop.
- Intuitive validation logic — the user is guided without error popups.
- Checkout is blocked until all edits are finalized, reducing potential errors and mismatched pricing.
- Easy navigation back to Gallery Page and Checkout
- Real-time count of items in the shopping bag displayed by item counter in Navbar

---

### Technical Structure & Functionalities

- **Session Management:** All bag data is stored in `request.session`, with `view_bag`, `add_to_bag`, `update_bag_item`, and `remove_from_bag` views handling logic.
- **Composite Keys:** Each bag item is uniquely identified by a key composed of `product_id`, `format`, and either `license` or `print_type`, ensuring no collisions between digital and printed variants.
- **Country-Specific VAT:** Pulled from `CountryVAT` model using session-stored country; fallback to 21% VAT.
- **Shipping Lookup:** Pulled dynamically from the `ShippingRate` model using mappings like `PRINT_TYPE_TO_SHIPPING_TYPE`.
- **JS Logic:** Enables/disables buttons based on form state and input changes using `data-` attributes and live listeners.

---

### Security & UX Defenses

| Type                          | Feature                                                                 |
|-------------------------------|-------------------------------------------------------------------------|
| Input Validation              | Ensures quantity is within 1–10 and format is selected correctly        |
| Disabled Buttons              | Prevents proceeding to checkout without confirmed changes               |
| Conditional Logic             | Print types only shown if format is `printed`                           |
| Server-Side Validation        | Final `POST` checks in views for invalid data before updating session   |
| Session Integrity             | Session-based cart data avoids DB bloat and maintains user state        |

---

![Cart Preview](README_Media/cart_preview.png)

---
---

### User Profile Management

The User Profile section of the application provides a clean and intuitive interface for users to manage their personal data, preferences, and order history. It complements the authentication flow handled by Django AllAuth and is visually consistent with the rest of the application’s natural and sophisticated design.

When a user signs up, a UserProfile instance is automatically created via signals (not shown here but assumed to be implemented).
The profile page is protected and only accessible to authenticated users.
Data is editable in place and saved via standard Django form POST requests.
Carousel-based layout ensures a clean, mobile-responsive way to switch between profile info and order history.

### Extended User Model:
Built using a OneToOneField relationship with Django’s built-in User model. This allows storing additional profile information such as:
- Profile picture (via Cloudinary)
- Language preference
- Full address details (country, city, street, postcode)
- Phone number

### Dynamic Carousel View

Users can toggle between:
- My Profile Details – A comprehensive form to edit personal and shipping information
- My Order History – Displays all past purchases linked to the user (fetched via reverse relation to OrderModel)

### Image Upload Support

Users can upload and update their profile picture with a custom preview display using Cloudinary and Bootstrap styling.

### Language Preference Selector

Users can choose from a list of predefined languages (English, German, French, Spanish), which can be used in the future to customize app behavior or email notifications.

### Data Validation & UX

The form uses placeholder text, Bootstrap styling, and server-side form validation to ensure clean data entry and a pleasant user experience.

### Account Deletion Request Flow

A two-step modal confirmation allows users to request account deletion while optionally submitting feedback. This is handled securely via POST requests. In additioin to the success message the user receives and automated email confirming the request has been rceived and will be processed within 48 hours.

### Order History Integration

The UserProfile model includes a get_order_history() method to fetch related orders from the OrderModel, making integration with the checkout system seamless.

![User Profile Card](README_Media/user_profile_card.png)
![Create Account](README_Media/user_create_account.png) ![Sign up error](README_Media/user_sign_up_error.png)
![Order History Card](README_Media/order_history_card.png)
![My Wishlist Card](README_Media/my_wishlist_card.png)

---
---

## Wishlist  
A streamlined feature that allows customers to save products for later purchase, enhancing engagement and providing flexibility in the shopping journey.  

---

### Summary  

- Display of wishlist items including product thumbnail, title, and the date added.  
- Clear action buttons for **View**, **Remove**, and **Move to Cart**.  
- Items are stored at the user level, ensuring persistence across sessions (not tied to cookies).  
- Duplicate prevention: products already in the wishlist cannot be added twice, with inline feedback messages for clarity.  
- Responsive layout with proper stacking of buttons on small screens.  

---

### Access My Wishlist

- **Profile Dropdown Access**:  
  The wishlist can be accessed conveniently via the profile dropdown menu when the user is logged in, ensuring quick navigation without needing to go through the profile page manually.  

- **Part of Profile Carousel**:  
  Similar to **Order History**, the Wishlist is fully integrated into the User Profile Carousel.  
  This provides a consistent user experience where users can seamlessly switch between their Profile, Order History, and Wishlist sections within the same carousel component.  

---

### Adding Products to the Wishlist
Users can add products to their wishlist directly from two key touchpoints in the shopping journey:

- **Product Detail Page**:  
  Each product has a prominent **♡ Add to Wishlist** button.  
  Clicking this saves the product in its current configuration (digital license or print type, etc.) to the user’s wishlist.

- **Shopping Bag Page**:  
  For products already in the bag, a **♡ Add to Wishlist** button is also available.  
  This allows customers to move items they aren’t ready to purchase yet into the wishlist for safekeeping.

---

### Structure & Components  

**From the User’s perspective**  
When navigating to their profile and selecting the Wishlist tab, users are presented with a clean, card-based layout. Each saved product includes:  

- A thumbnail preview image,  
- The product title,  
- A timestamp of when the product was added,  
- Buttons for:  
  - **View** (opens product detail page),  
  - **Remove** (deletes the product from wishlist),  
  - **Move to Cart** (adds the product to the shopping bag and removes it from wishlist).  

---

### Smart Behavior  

- If a product is already in the wishlist, the user receives an **informative message** instead of a duplicate entry.  
- Using **Move to Cart**, items seamlessly transfer into the shopping bag session while simultaneously being removed from the wishlist.  
- All feedback is provided via **Django’s messaging system**, ensuring real-time confirmation of user actions.  

---

### User Experience Highlights  

- **Consistency**: Buttons share the same responsive behavior and alignment rules as the Shopping Bag.  
- **Clarity**: Inline success and info messages notify the user when items are added, already exist, or moved.  
- **Persistence**: Unlike the bag, wishlist items are stored in the database, allowing retrieval across devices and sessions.  
- **Responsiveness**: On mobile, buttons stack vertically and shrink proportionally to fit inside the white card area.  

---

### Technical Structure & Functionalities  

- **Database Model**:  
  - Each wishlist entry links a `User` with a `Product`.  
  - Optional fields for `quantity`, `license_type`, `print_type`, and `price_at_time` provide flexibility for future expansion.  

- **Views**:  
  - `add_to_wishlist`: Adds items with duplicate prevention and user messaging.  
  - `remove_from_wishlist`: Removes items safely.  
  - `move_to_cart`: Transfers items into session-based shopping bag.  
  - `wishlist_view`: Renders the user’s wishlist card in profile.  

- **Session Integration**: Items moved to cart are structured correctly for the session-based bag logic.  

- **Security & UX Defenses**:  

  | Type              | Feature                                                                 |  
  |-------------------|-------------------------------------------------------------------------|  
  | Duplicate Handling| Prevents same product being saved multiple times, shows info message.   |  
  | Feedback          | Success/info/error messages always shown after actions.                 |  
  | DB Persistence    | Stored in `Wishlist` model → user’s data is safe and retrievable later. |  
  | Responsiveness    | Bootstrap grid + custom media queries ensure clean layout on all screens.|  

---
---

### Secure Checkout Flow

**UX Highlights**
  - Intuitive Progress Tracker: Clearly indicates the current step and overall progress.
  - Auto-Fill & Change Detection: Ensures returning users see their stored details while also tracking unsaved edits.
  - Modal Dialog: Reduces accidental overwrites by confirming save actions.
  - Graceful Fallback: Users can cancel edits and revert to original data without reloading the page.
  - Responsive & Accessible: Form labels, ARIA attributes, and input feedback ensure accessibility compliance.

---

### Step 1: Contact details

**User Path:**
  - Checkout now requires authentication: all orders are tied to a registered user account.
  - When proceeding to checkout, unauthenticated visitors are redirected to the login/registration page.
  - Contact details (first name, last name, email) are always loaded from or saved into the user’s profile.
  - This change ensures a consistent link between orders, invoices, and customer profiles.

**Profile Management:**
  - Authenticated users can update their first name, last name, and email directly from the checkout form.
  - First time users need to create a user profile first in order to be able to complete a purchase

**Modal Confirmation:**
  - Users are prompted with a modal asking whether to save changes before proceeding.
  - Options: Save, Don't Save, or Cancel, giving users full control over profile updates.

**Dynamic Form Behavior:**
 - the Continue button is disabled until all form fields are valid (including correct email format).
 - For returning users, changes are tracked and compared to original data to detect modifications.
 - Real-time visual feedback allows user to easily identify errors in data provided 

**Security & UX Defenses**

| Type                          | Feature                                                                 |
|-------------------------------|-------------------------------------------------------------------------|
| CSRF Protection               | All form submissions include CSRF tokens and are verified server-side.  |
| Backend Validation            | All submitted data is sanitized and validated before saving.            |
| Frontend Validation           | Email field uses regex and required attributes for early validation.    |
| Live Feedback	                | Real-time visual validation with Bootstrap classes (is-valid/is-invalid).|
| Modal Confirmation            | Users must confirm intent before profile data is changed.               |
| Revert Unsaved Edits          | Canceling/discarding changes reverts fields to their original values.   |
| Disabled Buttons              | "Continue" is only enabled when inputs are valid and complete.          |
| ARIA & Label Compliance       | All fields include ARIA attributes for better accessibility.            |

![Checkout Step 1](README_Media/co_step1.png)

---

### Step 2: Billing Information

**Form Behavior:**

  - Fields are auto-filled for authenticated users using their saved profile data.
  - Form is loaded dynamically via AJAX to reflect real-time profile updates.


**Live Validation:**

  - All required fields are validated in real time as the user types.
  - Country-specific postcode formats are validated using regex.
  - The Continue button remains disabled until all fields are valid.
  - Security & UX Defenses


**Security & UX Defenses**

| Type                    | Feature                                                                       |
|-------------------------|-------------------------------------------------------------------------------|
| CSRF Protection	        | All billing form submissions include CSRF tokens.                             |
| Backend Validation	    | Billing fields are validated and sanitized before saving.                     | 
| Frontend Validation	    | Includes field-specific error messages and visual validation feedback.        |
| Regex Postcode          | Validation	Validates postcode based on selected country (e.g., IE, GB, DE    |
|                         | etc.).                                                                        |
| Disabled Buttons	      | Continue button only activates if all fields are valid.                       |
| Dynamic Rendering	      | Billing form is only injected at the billing step via AJAX.                   |
| Modal Confirmation	    | Save/discard prompt shown if user attempts to proceed after changes.          |
| Revert Unsaved Edits	  | Users can cancel and restore original field values.                           |
| ARIA & Label Compliance |	Each input has aria-labelledby for screen reader accessibility.               |

![Checkout Billing Form checked](README_Media/billing_form_checked.png) ![Checkout Billing Form empty](README_Media/billing_form_empty.png)

---

### Step 3: Order Summary

**Form Behavior:**

Structured Summary View:
  - Displays entered Contact Details and Billing Information, each with a Change button that redirects back to Step 1 for real-time editing.
  - Dynamically pulls contact and billing info from session data or authenticated user's profile (UserProfile model).

Bag Contents lists all cart items from the session-stored bag with:
  - Product image (on the left)
  - Product title, format (digital/printed), license, print type, and quantity (on the right)
  - Responsive layout with image next to content from min-width: 400px+

Special Offer Display:
  - Dynamically fetches and displays the most recent active special offer (if one exists) from the SpecialOffer model.
  - Highlighted in a green alert box.

Price Breakdown:
  - Shows a clear breakdown of:
  - Subtotal (excl. VAT)
  - VAT (based on user’s billing country)
  - Shipping (based on printed product type and location)

Total (calculated and rounded consistently)
  - Responsive UI
  - Product image and text adapt across breakpoints.
  - Responsive margin utilities like me-md-3 ensure clean layouts on larger screens.

Navigation:
  - ⬅ Go back button redirects to shopping bag.
  - Proceed to Secure Payment ➡ leads to Step 4: Payment.

Responsive Layout:
  - The order summary is split into a left (form data) and right (summary) column inside a Bootstrap card. On smaller screens, it stacks vertically.

Individual Line Totals and Per-Unit Price Indication:
  - Each product row shows the per-unit-price as well as the line total ensures price transparency and make it easy for the customer to identify and check their order's eligibilty for a discount.

Discount Block Styling:	
  - Special offers are shown in banner-style including a row clearly stating the value saved.

Responsive Layout with flex-wrap:
  - The .flex-wrap class ensures that the summary adapts cleanly across screen sizes and prevents layout breakage.

Subtotal, VAT, Shipping, and Total:
  - Financial breakdown shown with precision (floatformat:2) and are visually separated for better readability.

Floating "Secure Payment" Button:
  - Final CTA button updates dynamically via JS, gets styling and icon to indicate secure checkout visually.

Live Step Transition via AJAX: 
  - All content (including summary) is loaded using asynchronous requests (fetch()), allowing faster interaction without full reloads.

### Security & UX Defenses

| Type                    | Feature                                                                       |
|-------------------------|-------------------------------------------------------------------------------|
| CSRF Protection         | CSRF tokens included in all forms via `RequestContext` and `{% csrf_token %}` |
| Session Handling        | Contact, billing, and cart data stored in session or pulled from authenticated user |
| Progress Indicator      | Visual progress bar guides user through multi-step process                    |
| Change Buttons          | Allow users to return and edit previous steps without losing form state       |
| Responsive Layout       | Bootstrap grid ensures mobile-friendly alignment of images and form fields    |
| Validation (Client)     | JavaScript validation for email, phone number, and country-specific postcodes |
| Validation (Server)     | Django form and model validation for contact, billing, and bag data integrity |
| Fallback Mechanisms     | VAT and shipping defaults applied if no user country or matching rate found   |
| Error Handling          | AJAX and form errors surfaced clearly with `alert` messages or modals         |
| Number Formatting       | Prices consistently formatted with 2 decimal places for clarity and trust     |
| DOM Sanitization        | All order summary content rendered server-side and loaded via AJAX for safety |
| Live Step Transitions   | Prevents data duplication or stale state using dynamic step loading (AJAX)    |
| Accessibility Support   | ARIA roles and labels improve usability for screen readers and keyboard users |
| Discount Integrity      | Discount and total amounts are re-validated server-side at summary stage      |
| Secure Payment Feedback | Final CTA labeled clearly and styled with lock icon to indicate HTTPS trust   |


![Checkout Order Summary](README_Media/order_summary.png)

---

### Step 4: Payment

**Features**
- Integrated [Stripe Checkout](https://stripe.com/docs/checkout) to handle secure payments.
- Product data (title, quantity, price, image) dynamically passed to Stripe session.
- Stripe session created server-side and client is redirected to hosted payment page.
- Payment confirmation handled via a secure webhook.
- Checkout success clears cart and renders a thank-you page.

**Form Behaviour**
  - The “Continue” button becomes the **Secure Payment** button on the order summary step.
  - Stripe public key passed to JS using `<body data-stripe-public-key="{{ STRIPE_PUBLIC_KEY }}">`.
  - `checkout_script.js`:
    - Initializes Stripe
    - Handles the final payment step
    - Redirects users on session creation
    - Stripe session is initiated via AJAX (`fetch('/checkout/create-checkout-session/')`).
    - Stripe success and cancel URLs are dynamically built and defined in the session.
  - 

**Stripe Form Customisation**
Stripe Checkout was styled to visually match the project using:
  - Logo: Custom store logo added
  - Colors: Brand primary and accent colors set to match the site palette
  - Font: Montserrat (same as site typography)
  - Shape: Rounded buttons for consistency with UI elements

**⬅ Cancel Button Behavior :**
  - Customized default Stripe “←” back links to redirect users to the Order Summary page for a seamless experience.

**Confirmation Email**
- Triggered immediately after successful payment via the webhook.
- Uses `send_order_email()` to generate and send a rich HTML confirmation email.
- Includes:
  - Product list with titles, quantity, format/license, price
  - Billing summary (subtotal, VAT, shipping, discounts, grand total)
  - Secure download links (if digital products were purchased)
  - Personal thank-you note from the brand
- **Fallback Logic:**
  - If rich HTML email template fails to load (e.g., missing template or SMTP error), the system sends a **plain-text fallback email** using Django's `send_mail()` function.
  - Ensures that users always receive confirmation, even if formatting fails.

---

### Security & UX Defenses

| Type                      | Feature                                                                                     |
|---------------------------|---------------------------------------------------------------------------------------------|
| Secret Management         | Stripe secret keys and webhook secrets stored securely in `env.py` and Heroku Config Vars. |
| Webhook Verification      | Incoming webhooks validated with `stripe.Webhook.construct_event()` to prevent forgery.     |
| Cancel Button UX          | Stripe cancel button redirects back to the Order Summary instead of default fallback page.  |
| Local Webhook Testing     | Ngrok tunnel used for secure HTTPS testing with static authenticated domain.                |
| Visual Consistency        | Stripe Checkout branded with same fonts, colors, rounded shapes, and logo as store UI.      |
| Fallback Email Delivery   | If the HTML confirmation email fails, a plain-text backup is sent using Django's `send_mail()`.|


![Stripe Pay-Portal](README_Media/stripe_pay-portal.png)

---

### Step 5: Confirmation

A standalone confirmation screen rendered after Stripe payment completes successfully. Fully decoupled from earlier checkout steps to ensure security, visual consistency, and seamless download delivery for digital purchases.

 ### Features
 
  - **Standalone Django template (`checkout_success.html`)** triggered via Stripe’s `success_url` with `session_id`.
  - **Secure fetching of order** via Stripe session ID and matching `User` email.
  - Displays full **order summary**, including:
    - Order number
    - Billing address (from user profile)
    - Product list with titles, pricing, quantity, and format/license
    - Subtotals, VAT, shipping, discount, and grand total
  - **Dynamic progress tracker** hardcoded with `.success-wrapper` classes to mimic live step progress without relying on `currentStep` logic.
  - If digital files were purchased:
    - Automatically fetches **secure Cloudinary download links**.
    - Provides **1-click download buttons** for each file.
  - Clears the bag session after confirmed payment.

---

### Page Behavior & Display Logic

  - Confirmation page is **not part of the step-based dynamic flow** but styled to feel consistent.
  - Uses:
    - `session_id` from Stripe to retrieve order and bag data.
    - Stored `request.session["bag"]` data to reconstruct bag item details (e.g. print type vs. license).
  - Billing info is dynamically mapped from the user’s `UserProfile` model if available.
  - **Responsive Layout**:
    - Product thumbnails on left (for large screens)
    - Details (title, format/license, pricing, quantity) on right
    - Summary bar at the bottom with VAT and discounts
  - **Order Summary** at the bottom details all costs including discount and VAT.

---

### Template-Driven Structure**

  - Renders dynamic content with:
    - `order`, `bag_items`, `download_links`, `billing_info`, `shipping_total`, `discount`, `vat`, `grand_total`
  - Fully integrates with `CountryVAT`, `ShippingRate`, and `SpecialOffer` models.
  - Session-clearing logic ensures cart is reset after success.
  - Uses a fallback plain-text confirmation email if the HTML version fails.
  - `send_order_email()` handles both rich HTML and fallback text for confirmation.

---

### UX Highlights

  - **Consistent UI experience** with earlier checkout steps via `.success-step` styling
  - **1-click digital download buttons** auto-generated for eligible products
  - **Billing info and product list** mimic invoice formatting for transparency
  - **No page reloads or session exposure** — all data comes via secure Stripe webhooks and authenticated views
  - **Order ID included** to reassure users of successful processing
  - **Thanks note from the artist** at the bottom of the confirmation screen

---

### Security & UX Defenses

| Type                      | Feature                                                                                       |
|---------------------------|-----------------------------------------------------------------------------------------------|
| Secure Order Lookup       | Order is fetched via Stripe `session_id` to prevent unauthorized access                       |
| Session Bag Reset         | Clears `request.session["bag"]` only after Stripe confirms the payment                        |
| Dynamic Content Rendering | All amounts, addresses, and titles are passed through context—no manual interpolation         |
| Conditional Download UX   | Download buttons are only shown for products with valid Cloudinary files                      |
| Access Verification       | Tied to user's email on the order and session to prevent spoofing of success URL              |
| Layout Resilience         | Confirmation page styled using separate classes to prevent interference with checkout flow    |
| Email Fallback Mechanism  | Fallback plain-text email is sent if HTML template fails or SMTP errors occur                 |
| Webhook Signature Check   | Stripe webhook payload is verified using `construct_event` and Stripe’s secret key            |

---

![Confirmation Page](README_Media/checkout_confirmation.png)

---
---

### Confirmation Email

### Features
  - Sent via send_order_email() upon verified Stripe payment and order creation.
  - Dual-format delivery: Rich HTML email with fallback to plain-text.
  - Includes full order summary, featuring:
  - Order number (e.g. ORD-556445)
  - Product title(s), license type, quantity, and individual pricing
  - Subtotal, VAT breakdown, discount, shipping, and grand total
  - Dynamic download section for digital files:
  - Secure Cloudinary link(s) per item
  - 1-click download prompts
  - Clear support instructions in case of download issues

---

### Email Display & Structure
  Clean, readable layout designed for email clients.

  Includes:
  - Personalized thank-you greeting
  - Prominent order ID
  - Simple product list with license details
  - Breakdown of pricing (subtotal, VAT, discount, total)
  - Conditional section: Download button/link appears only for digital items
  - Friendly closing message and support fallback instructions
  - Styled with minimal formatting for email client compatibility

---

### Template-Driven Logic
  - Renders dynamic fields from the Order model:
    - order_number, lineitems, total, vat, shipping, discount
  - Accesses Cloudinary download links using item metadata
  - Plain-text fallback ensures delivery even if HTML fails
  - Sent to the customer’s email via Django's SMTP setup after checkout

---

### UX Highlights
  - Instant confirmation gives peace of mind post-purchase
  - Download access inline in the email (no login required)
  - Clear, invoice-style layout for transparency
  - Contact option via “reply to this email”
  - Personal thank-you note signed by the artist
  - Promotional CTA to subscribe to the newsletter

---

### Security & UX Defenses

| Type                    | Feature                                                          |
| ----------------------- | ---------------------------------------------------------------- |
| Verified Email Delivery | Sent only after successful Stripe session confirmation           |
| Digital Access Control  | Links only included for digital products and expire securely     |
| Fallback Compatibility  | Plain-text version ensures receipt across all email clients      |
| Friendly Recovery Path  | Users can reply directly to request alternate download link      |
| Branded Closure         | Email closes with signature from Creative Spark Images for trust |

---
---

## The Admin Panel

### Features

The Django Admin Panel provides a secure and intuitive interface for staff members to manage backend data. It is styled with the default Django admin theme and includes custom admin classes for model management across all core apps.

---

### Data Management

Below is an overview of what admins can manage, grouped by Django app:

#### Accounts & Users

  - **Users**: View, search, add, edit, or delete registered users.
  - **Groups**: Assign permissions and manage user roles.
  - **Email Addresses**: Linked to Django AllAuth for email verification.

#### User Profiles

  - View, filter, and search user profiles.
  - Export selected user profiles as CSV.
  - Fields include:
    - First/Last Name
    - Language preference
    - Email
    - Country

#### Shop

  - **Image Themes**: Create/edit themes with slug auto-generation.
  - **Order History**: Manage customer orders, including status and user.
  - **Policy Pages**: Manage editable site policies using a WYSIWYG editor (Summernote).

#### Products

  - **Products**: CRUD management with advanced filters (tags, themes, types).
  - **Product Types**: Related to print types, searchable.
  - **Print Types**: Simple list with name and search support.
  - **License Types**: Summernote editor for license descriptions.
  - **Tags & Tag Groups**: SEO and categorization tools with slug support.
  - **Country VAT**: View/edit country-specific VAT rates.
  - **Shippers & Shipping Rates**:
    - Manage shippers with tracking URLs.
    - Shipping rates by product type, country, and shipper.

#### Home

  - **About Us**: Rich text editing via Summernote.
  - **Special Offers**: Manage marketing content with expiry and filtering.

#### Site & Social Accounts

  - Manage:
    - Social login providers & tokens
    - Site domain configuration

---

### UX Highlights

  - Fully responsive admin layout
  - Logical grouping and section headers (e.g., SHOP, HOME)
  - Real-time filtering and searching
  - Dropdown filters (e.g., Country filter via DropdownFilter)
  - Admin actions like “Export as CSV”
  - WYSIWYG editing with Summernote
  - Slug auto-generation for SEO consistency
  - Recent activity panel on right sidebar
  - Field-level customization (displaying user info from related models)

---

### Security & UX Defenses

| Type                        | Feature                                                                                             |
|-----------------------------|-----------------------------------------------------------------------------------------------------|
| Admin Access Restriction    | Only superusers or staff members can access the Django `/admin/` panel                             |
| CSRF Protection             | All admin and form views are protected by Django’s built-in CSRF middleware                        |
| Confirmation Prompts        | Export actions like "Export as CSV" require explicit selection and action confirmation             |
| Field-Level Permissions     | Sensitive fields like email and phone are only editable based on user role and form configuration  |
| Scoped Data Export          | Export CSV functionality is limited to the specifically selected user profile records              |
| Authenticated Email Control | Social account and email management are gated through Django AllAuth with proper verification      |
| Permission Checks           | Admin views use Django’s built-in object-level and group permission checks                         |
| Secure Filter Controls      | Dropdown filters for data fields (e.g., country) prevent unrestricted data exposure via URL params |

---
---

### Sales Dashboard

The Dashboard provides staff members with a comprehensive overview of store performance.  
It is an **admin-only view** (restricted with `@staff_member_required`) that aggregates sales data into clear KPIs and interactive charts.

#### Key Features
  - KPIs at a glance:
    - Total Sales (number of completed orders).
    - Total Revenue (sum of all order totals).
    - Top Product (the most frequently ordered product).

  - Sales Trends Visualization:
    - **Daily Trends**: Shows short-term fluctuations and recent activity.
    - **Monthly Trends**: Highlights medium-term growth and seasonal patterns.
    - **Yearly Trends**: Provides a high-level overview of long-term performance.

  - Interactive Chart Toggle:
    - A single Chart.js graph updates dynamically when switching between *Daily*, *Monthly*, and *Yearly* views.
    - Users can analyze trends without reloading or switching pages.

  Technical Notes
  - Built with Django and Chart.js.
  - Sales data is aggregated via `TruncDate`, `TruncMonth`, and `TruncYear` annotations on the `OrderModel`.
  - Context data is serialized as JSON (`labels` + `data`) and injected into the template for Chart.js rendering.
  - Integrated into the `shop` app under the `/shop/dashboard/` route.

---
---

### 404 Page

The project includes two custom 404 pages:

- **404.html** is rendered when a requested route does not match any defined URL pattern, or when an error occurs preventing a view from responding correctly, resulting in a "Page Not Found" response. Clicking the **Back-to-Gallery** allows the user to return to the shop.

![404 Page](README_Media/404_page.png)

- **page_under_construction.html** 
  - A single 404-style “Coming Soon” page is shared across all languages.
  - Language is determined via ?lang= query string (e.g. ?lang=de, ?lang=fr, ?lang=es).
  - Translations are handled on the client-side using JavaScript.
  - The feature includes a language dropdown in the navbar that links users to the under-construction page with the correct language flag and content.

![404 Page under construction](README_Media/404_page_under_construction.png)

---
---

## Features Left to Implement

  - option to checkout as a guest without creating an account
  - Rating and comment system for products
  - Image zoom/lightbox on product detail
  - Image catalogue displaying all images
  - SEO optimization and sitemap auto-generation

---
---

## Security Features and Error Handling

## Security Features

Security has been a central concern in the development of this application — especially given that it involves user authentication, digital transactions through Stripe, and sensitive user data. The system is built using Django's robust security tools, enhanced with thoughtful implementation to create a secure, trustworthy, and seamless shopping experience.

This project adopts a defensive development strategy, focusing on data integrity, user protection, and controlled access throughout the site. Sensitive workflows such as checkout, Stripe payments, and account handling are fortified with proven security best practices.

### Authentication & Authorization

- **Django's built-in authentication system** is used to enforce user authentication.
- Role-based access control (**RBAC**) differentiates **normal users, staff, and superusers** to limit permissions accordingly.
- **Session expiration & inactivity logout** prevent unauthorized access if a session remains idle for too long.
- **Two-factor authentication (2FA)** can be integrated for additional security.

### **User Management & Account Security**
- **Password hashing using Django’s PBKDF2 algorithm** (configurable with bcrypt, Argon2, or SHA-256) to secure stored credentials.
- **Brute-force protection** via login attempt throttling to prevent repeated unauthorized login attempts.
- Users must use **strong passwords**, enforced through Django’s built-in **password validators**.
- **Email verification** is required for new account activation and password resets.
- **Cross-Site Request Forgery (CSRF) protection** is enabled for all sensitive user actions.

### Form & Input Validation

- All form inputs are cleaned and validated before saving to the database.
- CSRF protection is enforced via Django’s automatic CSRF token inclusion on all forms to prevent cross-site attacks.
- The system uses try-except blocks to gracefully catch and handle edge cases like invalid quantity or missing data during form submission.

### Stripe Integration Security

- The Stripe payment gateway is integrated using environment variables to protect secret keys.
- Stripe checkout sessions are server-side generated, ensuring users cannot manipulate payment data client-side.
- All sensitive payment interactions happen on Stripe’s secure hosted pages, reducing PCI compliance risks.

### Data Protection & ORM Use

- **Form validation** prevents SQL injection, XSS (Cross-Site Scripting), and malicious inputs.
- All input fields are sanitized before being stored in the database.
- **Django ORM (Object-Relational Mapping)** is used instead of raw SQL queries to prevent SQL injection attacks.
- **File uploads are restricted** to specific formats, and **size limits** are set to prevent abuse.
- **Sensitive data is encrypted** before being stored, using Django’s **encrypted fields** or third-party libraries like **Fernet encryption**.

### Admin Panel Security

- **Admin panel access is restricted** to superusers and staff members.
- **Recent admin actions are logged**, allowing audits for tracking changes.
- **Bulk actions (delete, approve, mark verified)** require confirmation to prevent unintended modifications.
- **Only verified email addresses** can be assigned as primary to prevent account impersonation.
- **Superusers receive notifications for suspicious activity** within the admin panel.

### **Database Integrity Protection**
- **Foreign key constraints** ensure related data is properly linked and prevent orphan records.
- **Transactional integrity** is enforced using Django’s **atomic transactions** to prevent partial data updates in case of failure.
- **Backups & automatic rollbacks** are scheduled to recover from accidental data loss or corruption.

### **Logging & Monitoring**
- **Django’s logging framework** is configured to track authentication attempts, errors, and suspicious activity.
- **Error logs are monitored in real-time**, and alerts are triggered for repeated failed login attempts or unusual API usage.
- **Third-party security monitoring tools**, such as Sentry, can be integrated to capture and analyze security breaches.

### Other Protections

- Hidden form fields are validated server-side to ensure users don’t manipulate hidden product configuration values like license type or print format.
- Checkout sessions are cleared immediately after successful order placement, preventing re-submission or reuse of the cart.
- Null-safe access to all optional values (e.g., license or print_type) prevents unexpected crashes in cart or checkout logic.

---

## Error Handling

This project uses clear, user-friendly messaging and fallback logic to maintain a smooth experience, even when unexpected errors occur.


### **Form & Input Validation Errors**

- User input validation provides **real-time feedback** to prevent incorrect submissions.
- Custom **error messages** guide users toward resolving input issues.
- **Try-except blocks** handle unexpected form errors gracefully.

### **Authentication & Access Errors**

- Unauthorized users attempting to access restricted pages are **redirected to the login page with an error message**.
- **403 Forbidden and 401 Unauthorized responses** are properly returned in the API when access is denied.
- **Invalid login attempts are logged**, and users are notified of suspicious login activity.
- **Attempts to bypass restrictions** are gracefully denied with messages, not crashes.

### **Database & Model Errors**

- **Atomic transactions** prevent database corruption by rolling back failed operations.
- **Custom error handlers** catch and display meaningful error messages when database operations fail.
- **Graceful handling of missing database records**, preventing "DoesNotExist" exceptions.

### Fallback for Missing Data

- If product data or stock details are missing, users are shown friendly warnings rather than raw errors.
- The system validates session data before using it, preventing “NoneType” or invalid cast exceptions.

---
---

## Page Performance

### Desktop

  - Home Page
  ![Home page](readme_media/homepage_dtest.png)

  - Gallery Page
  ![Category page](readme_media/gallery_page_dtest.png)

  - Images by Theme Page
  ![Recipe detail page](readme_media/images_by_theme_dtest.png)

  - Product Detail Page
  ![About page](readme_media/product_detail_dtest.png)

  - Shopping Cart Page
  ![Contact Page](readme_media/shopping_cart_dtest.png)

  - Checkout Choice Page
  ![Checkout Choice Page](readme_media/checkout_choice_dtest.png)

  - Checkout Contact Details Page
  ![Checkout Contact Details Page](readme_media/contact_details_dtest.png)

  - Checkout Billing Address Page
  ![Checkout Billing Address Page](readme_media/billing_address_dtest.png)

  - Checkout Summary Page
  ![Checkout Summary Page](readme_media/checkout_summary_dtest.png)

  - Checkout Confirmation Page
  ![Checkout Confirmation Page](readme_media/checkout_confirmation_dtest.png)

  - Privacy Policy Page
  ![Privacy Policy Page](readme_media/privacy_policy_dtest.png)

  - Cookies Policy Page
  ![Cookies Policy Page](readme_media/cookies_policy_dtest.png)

  - Licenses Page
  ![Licenses Page](readme_media/licenses_dtest.png)

  - Terms & Conditions Page
  ![Terms & Conditions Page](readme_media/tc_dtest.png)

  - Contact Page
  ![Contact Page](readme_media/contact_dtest.png)

  - User Profile Page
  ![User Profile Page](readme_media/user_profile_dtest.png)

  - Order History Page
  ![Order History Page](readme_media/order_history_dtest.png)

---

### Mobile

  - Home Page
  ![Home page](readme_media/homepage_mtest.png)

  - Gallery Page
  ![Category page](readme_media/gallery_page_mtest.png)

  - Images by Theme Page
  ![Recipe detail page](readme_media/images_by_theme_mtest.png)

  - Product Detail Page
  ![About page](readme_media/product_detail_mtest.png)

  - Shopping Cart Page
  ![Contact Page](readme_media/shopping_cart_mtest.png)

  - Checkout Choice Page
  ![Checkout Choice Page](readme_media/checkout_choice_mtest.png)

  - Checkout Contact Details Page
  ![Checkout Contact Details Page](readme_media/contact_details_mtest.png)

  - Checkout Billing Address Page
  ![Checkout Billing Address Page](readme_media/billing_address_mtest.png)

  - Checkout Summary Page
  ![Checkout Summary Page](readme_media/checkout_summary_mtest.png)

  - Checkout Confirmation Page
  ![Checkout Confirmation Page](readme_media/checkout_confirmation_mtest.png)

  - Privacy Policy Page
  ![Privacy Policy Page](readme_media/privacy_policy_mtest.png)

  - Cookies Policy Page
  ![Cookies Policy Page](readme_media/cookies_policy_mtest.png)

  - Licenses Page
  ![Licenses Page](readme_media/licenses_mtest.png)

  - Terms & Conditions Page
  ![Terms & Conditions Page](readme_media/tc_mtest.png)

  - Contact Page
  ![Contact Page](readme_media/contact_mtest.png)

  - User Profile Page
  ![User Profile Page](readme_media/user_profile_mtest.png)

  - Order History Page
  ![Order History Page](readme_media/order_history_mtest.png)

---
---

## Testing

### Manual Testing

To catch and be able to reverse an action before being forced to wipe the database I made sure to strictly following the concept of model first and test the functionality with print statements to the terminal and compiling a tests file for each app.

I confirmed that all errors caused by user action are handeled the expected way and the corresponding feedback messages are given to the user by entering invalid inputs

- Add to cart (with/without license or print type)
- Remove from cart
- Quantity updates
- Stripe checkout end-to-end
- Webhook confirmation with test payloads
- Error message display for edge cases
- Missing print type/stock/out of range conditions

I had content reviewed by test users so I catch and fix typos and/or grammar errors.

I thoroughly tested all buttons, carousel and scroll-down-icon on both mobile devices, tablets and desktop.

Together with my test users (age 25 - 74) I reviewed the content on different devices to ensure all of the content is displayed as expected.

---

## Test Matrix

### Hompage

| Test Case ID | Description                      | Steps to Reproduce                                      | Expected Result                             | Actual Result | Pass/Fail | Notes                     |
|--------------|----------------------------------|----------------------------------------------------------|----------------------------------------------|---------------|-----------|---------------------------|
| TC001        | Check homepage loads             | Open browser → Go to homepage URL                        | Homepage loads successfully                  |               | Pass      |                           |
| TC002        | Responsive design                | Resize browser to mobile width                          | Layout adjusts without breaking              |               | Pass      | Test on real device too   |
| TC003        | Navbar: Image Catalogue link functionality    | Open homepage → Click 'Gallery' dropdown → Select 'Image Catalogue'| Navigates to image catalogue page                    | Link is not wired up (empty href)              | Fail        | Needs URL implementation          |
| TC004        | Menu Navigation Links (Gallery Dropdown)   | Open homepage → Hover over "Gallery" in menu → Click each dropdown item            | Each link navigates to its respective gallery section         | All links work except Image Catalogue         | Partial   | "Image Catalogue" has no href set          |
| TC005        | Language selector: English version            | Open homepage → Click language selector → Select English            | Reloads page with English content                    | Page loads successfully in English             | Pass        |                                   |
| TC006        | Language selector: Other languages            | Open homepage → Click language selector → Select non-English option | 404 or under construction message page               | Custom 404 under construction page shown       | Partial Pass | Intentional placeholder behavior  |
| TC007        | Navbar collapses on mobile                    | Open on mobile → Tap menu button                                   | Navbar expands and shows dropdown links              | Menu expands correctly                         | Pass        |                                   |
| TC008        | User Account Dropdown                         | Open homepage → Click user icon → Check options based on auth status| Login/Signup or Profile/Logout shown                | Options shown correctly                        | Pass        |                                   |
| TC009        | User icon behavior (unauthenticated)       | Open homepage → Not logged in → Click user icon → Check dropdown links              | Links: Create account → signup, Login → login                 | `{% url 'account_signup' %}` and `account_login` | Pass      | Correctly routes to auth pages             |
| TC010        | User icon behavior (authenticated)         | Log in → Click user icon → Check dropdown links                                     | Links: My Profile → profile, Order History → profile?slide=history, Logout | All URLs resolve as expected                  | Pass      | Uses Django auth routing                   |
| TC012        | Successful login                 | Go to login page → Enter valid credentials → Submit     | Redirected to dashboard                      |               | Pass      | Use test credentials      |
| TC013        | Logout functionality             | While logged in → Click logout button                   | Redirects to login page                      |               | Pass      | Session should be cleared |
| TC014        | Shopping cart icon navigation              | Click cart icon in navbar                                                           | Redirects to view bag/cart page                               | `{% url 'view_bag' %}`                         | Pass      | Cart count badge updates dynamically       |
| TC015        | Background video on intro section       | Open homepage → Wait for video to load                      | Video plays automatically as background                   | Sometimes fallback image shown after login/logout| Partial Pass | Intermittent load failure for video        |
| TC016        | Catchphrase text visibility             | Open homepage → Observe overlay text on video               | Catchphrase headings are displayed over video             | Displays correctly                               | Pass        |                                            |
| TC017        | Special offer text and countdown        | Open homepage → Look at digital sign area                   | Displays dynamic offer text and countdown timer           | Displays correctly                               | Pass        |                                            |
| TC018        | Gallery sign (image button)             | Click 'This way to gallery' sign                            | Navigates to gallery section/page                         | Navigates correctly                              | Pass        | Bypasses animation if accessed directly    |
| TC019        | About sign (image button)               | Click 'About Us' road sign                                  | Scrolls or navigates to About section                     | Navigates correctly                              | Pass        |                                            |
| TC020        | Cottage animation video loads           | Wait for animation trigger (or simulate it)                 | Short animation video plays showing entrance              | Plays correctly when shown                       | Pass        |                                            |
| TC021        | Audio toggle for walking sound          | Click speaker icon during animation                         | Toggle walking sound on/off                               | Audio toggles as expected                        | Pass        | Initially muted                            |
| TC022        | About section profile image display     | Scroll to About section                                     | Shows image if available, fallback image otherwise         | Image displays or fallback shown                 | Pass        |                                            |
| TC023        | About section content                   | Scroll to About section                                     | Renders title and text content                            | Displays correctly or fallback message           | Pass        | Handles empty content gracefully           |
| TC024        | Back to Top button functionality        | Scroll down → Click 'Back to Top' button                    | Scrolls back to top of homepage                           | Works as expected                                | Pass        |                                            |

---

### Footer

| Test Case ID | Description                    | Steps to Reproduce                        | Expected Result                                             | Actual Result                                     | Pass/Fail | Notes                      |
|--------------|--------------------------------|--------------------------------------------|--------------------------------------------------------------|--------------------------------------------------|-----------|----------------------------|
| TC001        | Privacy Policy link            | Click 'Privacy Policy' in footer           | Navigates to privacy policy page with correct content        | Page loads correctly with policy content         | Pass      |                            |
| TC002        | Cookie Policy link             | Click 'Cookie Policy' in footer            | Navigates to cookie policy page with correct content         | Page loads correctly with policy content         | Pass      |                            |
| TC003        | Licenses link                  | Click 'Licenses' in footer                 | Navigates to licenses page                                   | Page loads correctly with licenses content       | Pass      |                            |
| TC004        | Terms & Conditions link        | Click 'Terms & Conditions' in footer       | Navigates to terms and conditions page with content          | Page loads correctly with policy content         | Pass      |                            |
| TC005        | Contact page link              | Click 'Contact' in footer                  | Navigates to contact form/page                               | Page loads correctly                             | Pass      |                            |
| TC006        | Policy page fallback (missing) | Navigate to a policy page with no content  | Displays fallback message: "Document Not Available"          | Fallback message shown when content is missing   | Pass      | Graceful fallback is present|
| TC007        | Clickable shop logo on contact form        | Open contact form page → Click logo                         | Navigates to shop homepage                                   | Redirects to `{% url 'shop' %}`                  | Pass      |                                    |
| TC008        | Form field: Name input                     | Open contact form page → Check for name input field         | Input field for name is present                              | Displays correctly                               | Pass      |                                    |
| TC009        | Form field: Email input (with validation)  | Submit form with invalid email                              | Displays error with red border and feedback                  | Shows invalid feedback on error                  | Pass      | Conditional error block works     |
| TC010        | Form field: Message textarea               | Open contact form → Check for message field                 | Textarea field for user message is shown                     | Displays correctly                               | Pass      |                                    |
| TC011        | Send button functionality                  | Fill out form → Click 'Send'                                | Form is submitted to server                                  | Submits form (if valid)                          | Pass      |                                    |
| TC012        | License cards display title and description| Open licenses page → View license cards                     | Each license card shows title and hidden description         | All display correctly with hidden descriptions   | Pass      |                                    |
| TC013        | Read more interaction on license cards     | Click license card → Toggle description                     | Description toggles visibility                               | Works as expected using JS                       | Pass      | JS toggle for overview             |
| TC014        | Fallback for missing license description   | Open page with license having no description                | Shows placeholder message                                    | Displays 'This license is currently not available.' | Pass      |                                    |

---

### Global Newsletter Modal

| Test Case ID | Description                          | Steps to Reproduce                                                              | Expected Result                                                  | Actual Result                                                  | Pass/Fail | Notes                                                  |
|--------------|--------------------------------------|----------------------------------------------------------------------------------|------------------------------------------------------------------|----------------------------------------------------------------|-----------|--------------------------------------------------------|
| TC001        | Load modal via homepage              | Visit any page where modal is included; modal may open on a delay or trigger    | Modal displays newsletter signup form                            | Modal visible with expected fields and styles                 | Pass      | Can be reused across multiple templates               |
| TC002        | Responsive design                    | Resize browser window to mobile, tablet, desktop                                | Modal scales correctly                                            | Modal and form remain accessible and legible                  | Pass      | Bootstrap handles modal layout                        |
| TC003        | Input required validation            | Submit form with one or more fields blank                                       | Form rejected with client-side validation                        | Browser blocks submission and shows validation messages       | Pass      |                                                          |
| TC004        | Email format validation              | Submit an invalid email format                                                  | Form rejected before submission                                  | Browser prevents submission                                   | Pass      |                                                          |
| TC005        | Valid signup                         | Submit valid first name, last name, and unique email                            | Success message shown and user redirected                        | Message: ✅ Thank you for signing up!                          | Pass      |                                                          |
| TC006        | Duplicate email                      | Try to submit a second time with same email                                     | Warning message shown                                             | Message: ⚠ You have already signed up...                      | Pass      | Server-side check for duplicates                       |
| TC007        | Message display                      | Submit form with error or success                                               | Alert box shown at top of page                                   | Styled using Bootstrap alerts                                | Pass      | Supports success, warning, and error tags             |
| TC008        | Dismiss modal                        | Click close (×) button or “Not now” link                                        | Modal closes without submission                                  | Modal dismissed as expected                                  | Pass      | UX-friendly opt-out options                           |
| TC009        | Admin view                           | Visit /admin/newsletter/newslettersignup/                                      | Admin shows email, name, timestamp                               | Table rendered as expected                                   | Pass      | Uses `list_display` fields                            |
| TC010        | Admin CSV export                     | Select entries in admin → use “Export selected to CSV”                         | File downloads as newsletter_signups.csv                         | File includes header and rows                                | Pass      | Uses custom admin action                              |
| TC011        | Server-side validation fallback      | Submit tampered POST data bypassing frontend                                   | Form invalid, error message shown                                | Form revalidated, error handled                              | Pass      | Safe against tampering                                |

---

### Gallery Page

| Test Case ID | Description                                      | Steps to Reproduce                             | Expected Result                                             | Actual Result                        | Pass/Fail | Notes |
|--------------|--------------------------------------------------|-------------------------------------------------|--------------------------------------------------------------|-------------------------------------|-----------|-------|
| TC001        | Check gallery page loads             | On homepage → click on Gallery 'Road Sign' at the bottom right or chose 'Images by theme' in the navbar dropdown        | Gallery page loads successfully                  |               | Pass                                 |
| TC002        | Page title and heading                           | Open gallery page → View heading                | Gallery title is displayed prominently                       | Displayed as expected                | Pass      |       |
| TC003        | Search bar functionality                         | Enter text in search bar → Click 'Search'       | Search submits query via GET method                          | Works as expected                    | Pass      |       |
| TC004        | Theme card displays title, short description, image | Open gallery page → View a theme card        | Each card shows title, short description, and an image       | Displays correctly                   | Pass      |       |
| TC005        | Fallback image for missing theme image           | View card with no theme image                   | Shows default placeholder image                              | Placeholder displays correctly       | Pass      |       |
| TC006        | Read More button expands full text               | Click 'Read More' on any card                   | Reveals full description content                             | Expands text as expected             | Pass      |       |
| TC007        | View Images button navigation                    | Click 'View Images' on a theme card             | Navigates to images filtered by theme slug                   | Links resolve and load content       | Pass      |       |
| TC008        | No themes available message                      | Load page with no themes                        | Displays 'No themes available.' message                      | Fallback message appears             | Pass      |       |
| TC009        | Back to Top button                               | Scroll down → Click 'Back to Top'               | Scrolls to top of gallery page                               | Scrolls smoothly as expected         | Pass      |       |
| TC010        | Responsive design                | Resize browser to mobile width                          | Layout adjusts without breaking              |               | Pass      | Test on real device too   |

---

### Images by theme

| Test Case ID | Description                              | Steps to Reproduce                                      | Expected Result                                          | Actual Result                          | Pass/Fail | Notes |
|--------------|------------------------------------------|----------------------------------------------------------|-----------------------------------------------------------|-----------------------------------------|-----------|-------|
| TC001        | Load page via View Images button         | On gallery page → Click 'View Images' on any theme card | Loads page with images filtered by theme                 | Loads filtered images as expected       | Pass      |       |
| TC002        | Responsive design for image grid         | Resize browser window → Observe image layout            | Image cards adjust layout for screen size                | Responsive layout works correctly       | Pass      |       |
| TC003        | Theme title heading                      | Open theme page → View heading at top                   | Displays current theme title                             | Displays as expected                    | Pass      |       |
| TC004        | Image card link to product detail        | Click on any image preview                              | Navigates to image's product detail page                 | Correctly routes to product detail      | Pass      |       |
| TC005        | Image card displays title and price      | Scroll through images                                   | Each card shows title and starting price                 | Displays correctly                      | Pass      |       |
| TC006        | License tags under image card            | View image cards with licenses                          | Each license appears as a tag                            | Displays license tags as expected       | Pass      |       |
| TC007        | Fallback for no images in theme          | Open theme with no images assigned                      | Message shown and button to return to gallery            | Fallback message and button display     | Pass      |       |
| TC008        | Back to Gallery button (bottom of page)  | Scroll to bottom → Click 'Back to Gallery'              | Navigates to gallery page                                | Redirects correctly                     | Pass      |       |
| TC009        | Back to Top button                       | Scroll down → Click 'Back to Top'                       | Scrolls smoothly to top of page                          | Works as expected                       | Pass      |       |

---

### Product detail page

| Test Case ID | Description                                 | Steps to Reproduce                                                | Expected Result                                           | Actual Result                              | Pass/Fail | Notes                                 |
|--------------|---------------------------------------------|--------------------------------------------------------------------|------------------------------------------------------------|---------------------------------------------|-----------|----------------------------------------|
| TC001        | Load page from image grid                   | On 'Images by Theme' page → Click on any image                    | Product detail page for selected image loads              | Loads correct product page                  | Pass      |                                                    |
| TC002        | Responsive design layout                    | Resize browser window                                              | Product image and form layout adjusts to screen size      | Responsive layout works correctly           | Pass      |                                                    |
| TC003        | Product image display                       | View product detail page                                           | Main preview image displays                               | Image renders as expected                   | Pass      |                                                    |
| TC004        | Toggle format between Digital and Printed   | Click format toggle buttons                                        | Form fields update accordingly                            | Toggles work correctly                      | Pass      |                                                    |
| TC005        | License select dropdown (digital)           | Choose Digital format → Open license dropdown                      | License options are shown                                 | Dropdown displays license types             | Pass      |                                                    |
| TC006        | Print type select dropdown (printed)        | Choose Printed format → Open print type dropdown                   | Print options are shown                                   | Dropdown displays print types               | Pass      |                                                    |
| TC007        | Quantity selector (1–10)                    | Open quantity dropdown                                             | Dropdown shows 1 to 10 values or restricted if at limit   | Displays dynamically based on remaining qty | Pass      | Uses dynamic server-side enforcement   |
| TC008        | Add to Cart button                          | Fill form and click 'Add to Cart'                                 | Item is added to cart                                     | Cart updates                                | Pass      | Disabled if limit is reached                       |
| TC009        | Price summary updates on input change       | Change quantity/print type/format                                 | Price, VAT, and total update correctly                    | Summary updates dynamically                 | Pass      |                                                    |
| TC010        | Back to Gallery button                      | Click '⬅ Back to Gallery'                                         | Redirects to gallery page                                 | Navigates correctly                         | Pass      |                                                    |
| TC011        | Quantity over 10 via continue shopping  | Add 10 items → click Continue Shopping → attempt to add more      | Max 10 items enforced and UI prevents further addition     | Quantity restricted; add to cart disabled   | Pass      | Bug fixed with dynamic server-side enforcement     |
| TC012        | Fallback for missing license options        | Open product with no digital licenses                             | Shows disabled `<option>` with "No license available"     | Disabled message displays correctly         | Pass      | Uses `{% empty %}` block                           |
| TC013        | Fallback for missing print type options     | Switch to Printed → Open dropdown on product with no prints       | Shows disabled `<option>` with "No print option available"| Disabled message displays correctly         | Pass      | Uses `{% empty %}` block                           |

---

### Shopping cart

| Test Case ID | Description                              | Steps to Reproduce                                      | Expected Result                                              | Actual Result                          | Pass/Fail | Notes                                |
|--------------|------------------------------------------|----------------------------------------------------------|----------------------------------------------------------------|-----------------------------------------|-----------|----------------------------------------|
| TC001        | Access shopping bag page after adding item | Go to product detail → Select options → Click 'Add to Cart' → Open bag | Item appears in bag with correct details and configurations    | Item displays correctly in bag         | Pass      |                                        |
| TC002        | Responsive design adapts to screen size  | Open shopping bag page on different screen sizes             | Layout adjusts appropriately (mobile vs desktop)              | Responsive layout works correctly       | Pass      |                                        |
| TC003        | Shopping bag loads with added items      | Add items to cart → Open shopping bag page               | Shopping bag displays all items with configuration options    | Displays correctly                      | Pass      |                                        |
| TC004        | Product image and details in cart        | Open cart with items                                     | Product image, title, format, and subtotal are visible        | All details are visible                 | Pass      |                                        |
| TC005        | Format select (Digital/Printed)          | Change format dropdown on an item                        | UI updates accordingly (show/hide print options)              | Format toggles correctly                | Pass      |                                        |
| TC006        | Quantity selector updates subtotal       | Change quantity → Click update                           | Subtotal recalculates per item                                | Subtotal updates correctly              | Pass      |                                        |
| TC007        | Print type dropdown shown conditionally  | Select Printed format                                    | Print type dropdown becomes visible                           | Appears correctly                       | Pass      |                                        |
| TC008        | Update button state logic                | Change format/quantity/print type                        | Update button enables only when valid                         | Button enables/disables correctly       | Pass      |                                        |
| TC009        | Remove button functionality              | Click remove on a cart item                              | Item removed from bag                                         | Item is removed successfully            | Pass      |                                        |
| TC010        | Total cost breakdown                     | View totals at bottom of bag                             | Accurate breakdown is shown                                   | Correct totals displayed                | Pass      |                                        |
| TC011        | Checkout eligibility enforcement         | Make changes → Try to proceed without updating           | Warning shown, checkout disabled until update                 | Checkout disabled and warning shown     | Pass      | Uses JS to enforce update before checkout |
| TC012        | Continue shopping button                 | Click 'Continue shopping'                                | Navigates back to gallery page                                | Navigates correctly                     | Pass      |                                        |
| TC013        | Fallback for empty bag                   | Ensure cart is empty → Open bag page                     | Message shown with link to continue shopping                  | Fallback message and button shown       | Pass      |                                        |

---

### Checkout Flow

| Test Case ID | Description                                 | Steps to Reproduce                                                   | Expected Result                                                  | Actual Result                                                           | Pass/Fail | Notes                                                   |
|--------------|---------------------------------------------|------------------------------------------------------------------------|------------------------------------------------------------------|---------------------------------------------------------------------------|-----------|---------------------------------------------------------|
| TC001        | Load checkout page from bag                 | Click "Proceed to Checkout" on shopping bag page                     | Login Screen if user is not logged in and checkout step 1 if user is logged in                       | Page loads with checkout step                         | Pass      |                                                         |
| TC002        | Responsive Design                           | Resize window across mobile/tablet/desktop                           | Layout adjusts accordingly                                       | Layout responsive at all breakpoints                                    | Pass      | Bootstrap-based layout                                  |
Correct section is shown based on choice                                | Pass      | Conditional render based on user state                 |
| TC003 | Checkout Progress Bar Display | Open checkout and proceed through steps | Progress bar updates to highlight the current step and completed steps | Visual step tracker reflects accurate step progression | Pass | Consistent across all steps and visible on confirmation page |
| TC004        | Contact Details Form                        | Proceed past choice (authed users)                                   | Form is displayed, fields are pre-filled if user is authed       | User info correctly shown or fields empty when user data is incomplete                    | Pass      |                                                         |
| TC005        | Real-time JS form validation – user form    | Enter invalid and then valid data in user form fields                | Invalid: red border + error message. Valid: green border + tick  | Real-time validation with visual indicators works correctly             | Pass      | Email, first/last name validated                        |
| TC006        | Real-time JS form validation – billing form | Enter invalid ZIP/email/phone/country fields                         | Red border and inline feedback if invalid, green + tick if valid | Fields respond immediately to user input                                | Pass      | Includes postcode validation by country                 |
| TC007        | Block progress with invalid input           | Leave required fields empty or invalid                               | “Continue” button remains disabled                               | Continue button greyed out until all validations pass                   | Pass      | Button stays inactive with any error                    |
| TC008        | Modal trigger on continue                   | Fill forms and click “Continue”                                      | Modal pops up asking to confirm profile save                     | Modal appears with correct user-specific message                        | Pass      | User see tailored prompt               |
| TC009        | Modal cancel option                         | In modal, click “Cancel”                                             | Modal closes, no form progression                                | Modal dismissed and stays on current step                               | Pass      |                                                         |
| TC010        | Modal confirm save                          | In modal, click “Save”                                               | Proceeds to next step, saves data                                | Successfully proceeds to billing step                                   | Pass      |                                                         |
| TC011        | Invalid form blocks modal                   | Leave required form fields invalid and click “Continue”              | Modal does not open                                              | Modal prevented by disabled button                                      | Pass      | JS validation ensures pre-check conditions              |
| TC012        | Billing Form validation flow                | Fill billing form with correct/incorrect data                        | Input validated in real time                                     | All fields provide accurate feedback                                    | Pass      | Country and postcode validation tied                    |
| TC013        | Stripe SDK & Checkout Script load           | Open browser console, observe JS loading                             | No errors; Stripe and custom checkout script loaded              | Scripts load successfully                                               | Pass      | `checkout_script.js` must be present                    |
| TC014        | Stripe payment success                        | Complete Stripe payment with valid card                                                               | Redirects to confirmation page `/checkout/success/`                             | Success page loads with order summary                                     | Pass      | Stripe webhook correctly triggers backend logic                      |
| TC014        | Stripe payment fails                          | Use a declined test card (e.g., `4000000000000002`)                                                   | Stripe shows error, no redirection to success page                              | Error handled gracefully                                                   | Pass      | Stripe’s fail cases tested                                          |
| TC016        | 2FA verification flow                         | Use a 3DS test card (`4000002760003184`)                                                              | 2FA modal shown, user confirms → redirect to success                            | Works as expected                                                          | Pass      | Confirms 3DS secure cards                                            |
| TC017        | Email sent after payment                      | Complete checkout → check inbox of test user                                                          | Confirmation email with order summary is received                               | Email received with correct formatting and data                           | Pass      | Includes download links for digital items                          |
| TC018        | Email fallback on error                       | Simulate template failure (e.g., remove HTML template) → complete checkout                            | Plain text fallback email sent                                                  | Fallback plain email is sent                                              | Pass      | Verified by removing HTML template temporarily                     |
| TC019        | Email includes download links                 | Buy a digital product → complete checkout → open confirmation email                                  | Email contains links to download purchased files                                | Links present and working                                                 | Pass      | Secure Cloudinary links expire after 1 hour                        |
|
| TC020        | Proceed through checkout steps              | Login, fill all fields, continue step-by-step   | Each step appears sequentially with validation                   | All steps function as designed                                          | Pass      | Steps are conditionally visible and sequential          |
| TC021        | Summary “Change” buttons                    | On summary step, click “Change” for contact/billing                  | Returns user to appropriate form step                            | Takes user back to input step                                           | Pass      | Could be improved by targeting correct step directly    |
| TC022        | Summary info formatting                     | Confirm correct formatting of displayed address and user info        | Proper field spacing and content                                 | Summary matches entry fields                                            | Pass      |                                                         |
| TC023        | Order Item Details                          | View items listed in summary                                         | Product, format/license, qty, unit price shown                   | Items displayed with preview, names, and pricing                        | Pass      | Responsive layout                                        |
| TC024        | Order Price Breakdown                       | Review order totals                                                  | Subtotal, VAT, shipping, discount, total shown                   | Pricing is calculated and formatted correctly                           | Pass      | Includes special offer if present                      |
| TC025        | Stripe Payment Page Customization           | Proceed to Stripe hosted checkout page                               | Stripe page matches site design, includes image & item breakdown | Colors, logo, product image, title, quantity, and price shown correctly | Pass      | Matches project branding; enhances trust & UX          |
| TC026        | Stripe Valid/Invalid Payment Test           | Use valid and invalid Stripe test card numbers                       | Valid cards complete payment; invalid ones are rejected          | Stripe handles both correctly and shows appropriate messages            | Pass      | Used test cards from official Stripe docs              |
| TC027        | Stripe 2-Way Verification Handling          | Use cards requiring 3D Secure (SCA) authentication                   | Authentication screen shown; passes/fails based on input         | Verification screen shows; outcome behaves as expected                  | Pass      | Simulated authentication with 3D Secure test cards     |
| TC028        | Checkout Success Display                    | Complete checkout through Stripe                                     | Confirmation page shown with order number and summary            | Confirmation section includes all expected messages                     | Pass      |                                                         |
| TC029        | Checkout Success Summary                    | View bottom of confirmation page                                     | Final price breakdown shown (same as step 3)                     | All amounts match pre-checkout summary                                  | Pass      | Summary consistent with order                          |
| TC030        | Downloadable Items Section                  | Checkout includes digital items                                      | Shows “Download” buttons with file titles                        | Buttons download items directly                                         | Pass      | Uses `download` attribute                              |
| TC031        | Modal Save Error Handling                   | Simulate failed save (e.g., disconnect network before clicking Save) | Error message shown in modal                                     | Error alert is shown in red within modal                                | Pass      | Simulated by console error override or server intercept |
| TC032        | Navigation Flexibility                      | Use browser back/forward or revisit form steps                       | Page resets correctly and sections toggle                        | Sections show/hide correctly with JS                                    | Pass      | State resets properly with re-entry                    |
| TC033        | Spinner on slow transition          | Proceed through checkout with simulated network lag or slow connection           | Loading spinner appears when submitting form or progressing to next checkout step | Spinner is shown until next step loads, giving visual feedback during delay         | Pass      | Prevents user confusion or multiple submissions        |


---

### User Profile Form

| Test Case ID | Description                                       | Steps to Reproduce                                                   | Expected Result                                                       | Actual Result                                                          | Pass/Fail | Notes                                                         |
|--------------|---------------------------------------------------|------------------------------------------------------------------------|------------------------------------------------------------------------|------------------------------------------------------------------------|-----------|---------------------------------------------------------------|
| TC001        | Load profile page from navbar icon               | Click user icon in navbar and choose 'Profile'                        | Profile page opens showing profile details                            | Page opens with profile carousel active                               | Pass      | Includes carousel for toggling between views                 |
| TC002        | Responsive design                                | Resize viewport across mobile/tablet/desktop                          | Layout adapts correctly to screen size                                | Responsive at all breakpoints                                          | Pass      | Bootstrap grid and container used                            |
| TC003        | Display and update user profile picture          | View or upload profile picture via 'Upload New Picture'              | Picture updates or defaults shown if not set                          | Image display logic works, upload input functions                     | Pass      | Supports upload and preview                                  |
| TC004        | Contact and address input fields                 | Enter data in each form input                                         | All form fields are shown and editable                                | Inputs populate from profile or stay empty                            | Pass      | Language preference, phone and address included              |
| TC005        | Real-time JS form validation on all fields       | Try valid and invalid data in inputs (e.g., email, phone, postcode)  | Invalid input: red + error message, valid: green + tick               | Visual feedback responds correctly to input                           | Pass      | All fields respond dynamically to input                      |
| TC006        | Profile Save functionality                       | Edit data and click 'Save Changes'                                   | Profile data is submitted and saved                                   | Save works and persists data                                          | Pass      | No page reload required                                      |
| TC007        | Profile Carousel navigation                      | Click carousel indicators or prev/next controls                       | Carousel switches between Profile and Order History                   | Smooth switching between two views                                    | Pass      | Accessible via buttons and indicators                        |
| TC008        | Order history display                            | Scroll to order history section of carousel                           | Past orders are listed or a message is shown                          | Correct message or orders shown                                       | Pass      | Includes order meta and status                               |
| TC009        | Order product details shown with images          | View listed products under each order                                 | Products display with image and info                                  | Product preview and metadata rendered                                | Pass      | Loop through order.products.all                              |
| TC010        | Delete account: trigger modal                    | Click 'Delete my account' button                                      | First modal appears requesting feedback                               | Bootstrap modal opens with form                                       | Pass      | Textarea accepts feedback                                    |
| TC011        | Delete account: modal confirm cancellation       | Click 'Cancel' in deletion modal                                      | Modal closes, stays on profile page                                   | Dismissal works without issue                                         | Pass      | No state lost on dismiss                                     |
| TC012        | Delete account: second modal confirmation        | Click 'Submit Request' then 'Yes, I'm sure'                           | Second modal confirms deletion request                                | Confirms and submits deletion form                                    | Pass      | Two-step confirmation prevents accidental deletion           |
| TC013        | All form data validated before submission        | Submit form with and without valid data                               | Form blocked from submitting if any errors                            | JS validation blocks invalid form state                               | Pass      | Enhances UX; prevents bad data                               |
| TC014        | User profile & order history via navbar icon     | Click user icon → Profile                                             | User can access profile from any page                                 | Icon routes to profile successfully                                   | Pass      | Same icon links to checkout and profile                      |

---

### Wishlist  

| Test Case ID | Description                                      | Steps to Reproduce                                                                 | Expected Result                                                                 | Actual Result                                                                 | Pass/Fail | Notes                                                                 |
|--------------|--------------------------------------------------|------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|--------------------------------------------------------------------------------|-----------|----------------------------------------------------------------------|
| TC001        | Access wishlist from profile dropdown            | Log in → click user icon in navbar → select “Wishlist”                             | Profile carousel opens on “Wishlist” card                                       | Carousel opens and loads wishlist tab                                          | Pass      | Integrated into profile dropdown & carousel                          |
| TC002        | Wishlist empty state                             | Access wishlist with no saved products                                             | Message “Your wishlist is empty.” is shown                                      | Message is displayed correctly                                                 | Pass      | Clear empty state feedback                                           |
| TC003        | Wishlist populated with products                 | Add product via “Add to Wishlist” button on product detail page                     | Product shows in wishlist card with thumbnail, title, date added                | Card layout renders with product info                                          | Pass      | Uses product.image_preview and added_at fields                      |
| TC004        | Add product to wishlist from shopping bag        | In bag view → click “♡ Add to Wishlist”                                            | Product is added to wishlist and confirmation message displayed                | Works as expected                                                              | Pass      | Prevents duplicates with feedback                                    |
| TC005        | Product thumbnail loads correctly                | View wishlist with saved products                                                  | Thumbnail image visible with alt text describing product                        | Images render with `alt="Preview of {{ item.product.title }}"`                 | Pass      | Lazy loading improves performance                                   |
| TC006        | View product details from wishlist               | Click **View** button on wishlist item                                             | Redirects to product detail page of selected product                            | Navigates to `product_detail` view                                             | Pass      | `aria-label` used for accessibility                                 |
| TC007        | Remove product from wishlist                     | Click **Remove** button on wishlist item                                           | Item removed from wishlist and confirmation message displayed                   | Product disappears from list                                                   | Pass      | Correct feedback via Django messages                                |
| TC008        | Move product from wishlist to cart               | Click **Move to Cart** on wishlist item                                            | Item removed from wishlist, added to bag (session-based cart)                   | Item shows in bag, disappears from wishlist                                    | Pass      | Confirms success with user message                                  |
| TC009        | Prevent duplicate additions                      | Add same product twice via product detail page                                     | Second attempt prevented; inline info message displayed                         | Message: “Product is already in your wishlist.”                               | Pass      | Duplicate defense implemented                                       |
| TC010        | Responsive layout                                | Resize viewport across mobile/tablet/desktop                                       | Cards and buttons stack appropriately on smaller screens                        | Buttons stack vertically on mobile, align horizontally on desktop              | Pass      | Bootstrap grid + utility classes ensure responsiveness              |
| TC011        | Accessibility of wishlist buttons                | Navigate using keyboard and screen reader                                          | Buttons focusable with keyboard; labels announced by screen reader              | `aria-label`s applied to View, Remove, Move to Cart buttons                    | Pass      | Meets WCAG guidelines                                                |
| TC012        | Wishlist persistence across sessions             | Log out and back in → navigate to wishlist                                         | Wishlist items still stored and displayed                                       | Items persist, tied to user in database                                       | Pass      | Unlike bag, wishlist is DB-based not session-based                  |


---

### Newsletter Page & Modal

| Test Case ID | Description                        | Steps to Reproduce                                              | Expected Result                                                | Actual Result                                                | Pass/Fail | Notes                                               |
|--------------|------------------------------------|------------------------------------------------------------------|----------------------------------------------------------------|--------------------------------------------------------------|-----------|-----------------------------------------------------|
| TC001        | Load the Admin Panel               | Navigate to `/admin/`                                           | Admin login screen is displayed                               | Admin panel loads and user can log in if credentials valid  | Pass      | Used to test admin access for newsletter data       |
| TC002        | Responsive Design                  | Resize browser or simulate device                               | Layout and inputs adjust on all screen sizes                  | Form and modal remain fully accessible                       | Pass      | Verified on mobile, tablet, desktop                 |
| TC003        | Logo Visibility                    | Open `/newsletter/` page                                        | Logo is displayed above form                                  | Logo loads and displays as expected                         | Pass      | Branding check                                      |
| TC004        | Headings Render                    | View newsletter page                                            | “Like my work?” + subheading visible                          | Headings are correctly styled and placed                    | Pass      | Typography check                                    |
| TC005        | First Name Input                   | Type into first name field                                      | Input is accepted                                              | Input accepted and styled                                   | Pass      | Required field                                      |
| TC006        | Last Name Input                    | Type into last name field                                       | Input is accepted                                              | Input accepted and styled                                   | Pass      | Required field                                      |
| TC007        | Email Input                        | Enter valid email                                               | Accepted, with email validation                               | Format validated via HTML5 and form logic                   | Pass      | Placeholder and styling correct                     |
| TC008        | Required Field Validation          | Submit form without one or more fields                          | Browser prevents submission                                   | HTML5 form validation blocks submit                         | Pass      | Verified in all browsers                            |
| TC009        | Sign-Up Button Works               | Click “Sign Up” after entering valid info                       | Submits form and shows success message                        | Data sent, green success message shown                      | Pass      | Backend + frontend form link works                  |
| TC010        | Duplicate Email Warning            | Submit form with an already registered email                    | Warning message appears                                       | “You have already signed up…” message visible               | Pass      | Server filters duplicates                           |
| TC011        | “Not now” Page Link                | Click link under the form                                       | Redirects to homepage                                         | Link works and routes to homepage                          | Pass      | Passive opt-out                                     |
| TC012        | Modal Displays                     | Trigger modal on any page                                       | Modal pops up centered                                        | Modal appears and can be interacted with                   | Pass      | Bootstrap modal test                                |
| TC013        | Modal Form Inputs                  | Type into modal’s form fields                                   | Fields accept input, validate same as page version            | Same behavior confirmed                                     | Pass      | Duplicate of main form                              |
| TC014        | Modal Close Button                 | Click “×” in top right                                          | Modal closes                                                   | Modal dismissed                                              | Pass      | UI interaction functional                           |
| TC015        | Modal “Not Now” Link               | Click under modal form                                          | Modal closes                                                   | Same as close button                                        | Pass      | User opt-out confirmed                              |
| TC016        | Feedback: Success Message          | Submit new valid email                                          | “✅ Thank you for signing up!” shown                          | Message shown in alert div                                 | Pass      | Alert is dismissible                                |
| TC017        | Feedback: Duplicate Email Message  | Resubmit with same email                                        | Warning message in yellow alert box                           | Correct warning visible                                     | Pass      | Alert color + copy verified                         |
| TC018        | Feedback: General Error Message    | Submit invalid or broken form                                   | Error message in red shown                                    | “There was a problem…” appears                            | Pass      | JS and backend paths tested                         |
| TC019        | CSRF Token Exists                  | Inspect source of newsletter form                               | {% csrf_token %} present                                      | Token rendered inside form tag                             | Pass      | Security test                                       |
| TC020        | Accessibility: Field Inputs        | Use keyboard and screen reader                                  | Labels read, tab order logical                                | Fields accessible and usable via keyboard                  | Pass      | Manual screen reader test                           |
| TC021        | Accessibility: Modal Compliance    | Open modal and test ARIA + keyboard nav                         | Modal fully accessible, closeable                            | Keyboard nav and screen reader compliance confirmed        | Pass      | Meets WCAG AA                                       |

---

### AllAuth templates

| Test Case ID | Description                         | Steps to Reproduce                                                                 | Expected Result                                                               | Actual Result                                                                  | Pass/Fail | Notes                                                             |
|--------------|-------------------------------------|------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|----------------------------------------------------------------------------------|-----------|-------------------------------------------------------------------|
| TC001        | Load login/signup/reset flow        | Click user icon → Login / Create account / Forgot Password                        | Correct page loads with proper forms                                          | Correct templates rendered, URL routes valid                                   | Pass      | Includes forgot password, signup paths                         |
| TC002        | Responsive Design                   | Resize window to test layout across breakpoints                                   | Layout adapts cleanly across devices                                          | Cards and forms reflow correctly                                               | Pass      | Tested on Chrome dev tools                                       |
| TC003        | Login Form Submission               | Enter credentials and submit form                                                 | User is logged in and redirected                                              | Redirect to homepage/profile after login                                       | Pass      | Redirect handles redirect_field correctly                       |
| TC004        | Login Form - Invalid Feedback       | Submit empty or invalid credentials                                               | Feedback shown near problematic input                                        | Inline error messages appear correctly                                        | Pass      | Form binds error styles correctly                              |
| TC005        | Signup Form Validation              | Enter invalid/valid data in signup form                                           | Red border & error for invalid input, green on valid                          | Real-time feedback responds as expected                                       | Pass      | Form loops + errors handled in template                         |
| TC006        | Signup Form Submission              | Submit complete signup form                                                       | User is created, email sent for verification                                 | New user account created                                                       | Pass      | CSRF protected, errors styled                                   |
| TC007        | Password Reset Request Form         | Access forgot password and submit valid email                                     | Email submission acknowledged, notice shown                                  | Message confirms reset email sent                                             | Pass      | No email leakage; masked success                                |
| TC008        | Password Reset Email Confirmation   | Check reset confirmation screen after submission                                  | Message indicating email has been sent                                       | Displays informational message as expected                                   | Pass      | No back button redirect, just info shown                        |
| TC009        | Password Reset Form (via token)     | Click reset link in email and change password                                     | Form accepts new password and redirects                                      | Password changed, user redirected to login                                   | Pass      | Token used in reset URL                                         |
| TC010        | Password Reset - Invalid Token      | Click expired/invalid reset link                                                  | Shows error about invalid link with reset suggestion                         | Fallback message and reset link shown                                         | Pass      | Tested with expired token link                                  |
| TC011        | Password Change - Logged in User    | Access password change from authenticated user                                    | Change password form is shown                                                 | Form accepts and validates input                                              | Pass      | No template logic errors                                        |
| TC012        | Password Change - Feedback Display  | Submit valid password change                                                      | Success message appears after change                                          | Notification displayed on form submission                                    | Pass      | Bootstrap cards used                                             |
| TC013        | Logout Confirmation Flow            | Click 'Logout' in UI                                                               | Logout modal/confirmation page is displayed                                  | Logout occurs, session cleared                                                | Pass      | CSRF, styled card, form works                                   |
| TC014        | Email Verification Notice           | Signup and check post-submission verification notice                              | Notice and email verification instructions shown                             | Template with instructions shown                                              | Pass      | Custom instructions clearly written                             |
| TC015        | Email Confirmation via Link         | Click confirmation link in email                                                  | Confirms user email and updates status                                       | Email address is verified                                                     | Pass      | Both success & failure paths covered                            |
| TC016        | Manage Email Address Page           | Go to Manage Email page under account settings                                    | Email list displayed with actions                                             | Correct UI and email status indicators shown                                 | Pass      | Includes Add, Remove, Re-send buttons                           |
| TC017        | Email Change and Resend Verification| Attempt to change or verify a new email                                           | Pending email shown, option to resend                                        | Re-send and switch primary email options available                           | Pass      | Form and buttons work with JS confirm                           |
| TC018        | Email Confirmation Failure Flow     | Try confirming expired/invalid email link                                         | Fails gracefully with a fallback option                                      | Fallback UI message shown with resend link                                   | Pass      | Covers expired confirmation use-case                            |
| TC019        | All Buttons Trigger Expected Actions| Click any button in forms/modals                                                  | Each button triggers correct form logic                                      | All inputs functional and interactive                                        | Pass      | Submit, cancel, resend, etc., all testable                     |
| TC020        | Navigation Links (Login <-> Signup) | Click provided navigation links (e.g., 'Sign in here')                            | Link routes correctly to login/signup                                        | Navigation works without error                                               | Pass      | Clear flow between login/signup pages                          |
| TC021        | All Pages Inherit Custom Base Styling | Open any AllAuth view and check style match                                      | Card layout and buttons match overall site style                             | All pages use custom base and classes                                        | Pass      | Base extends layout with branding and CSS                      |

---

### Admin Panel

| Test Case ID | Description                               | Steps to Reproduce                                                                 | Expected Result                                                       | Actual Result                                                         | Pass/Fail | Notes                                                         |
|--------------|-------------------------------------------|------------------------------------------------------------------------------------|------------------------------------------------------------------------|------------------------------------------------------------------------|-----------|---------------------------------------------------------------|
| TC001        | Load Admin Panel                          | Visit `/admin` in browser, login as superuser                                     | Admin dashboard loads                                                  | Admin interface with model sections displayed                         | Pass      | Requires superuser login                                      |
| TC002        | Responsive Design                         | Resize admin interface window across devices                                      | Admin layout adjusts to screen sizes                                  | Interface remains usable on all breakpoints                           | Pass      |                                                              |
| TC003        | UserProfile list display                  | Go to User Profiles section                                                       | Table lists user data: name, language, email, country                 | All columns are visible                                               | Pass      | Uses custom display functions                                 |
| TC004        | UserProfile search                        | Use search bar with name or email                                                 | Matching users appear                                                  | Search returns expected results                                       | Pass      | Custom search_fields                                          |
| TC005        | UserProfile filter                        | Use dropdown for language or country filters                                      | Filters update user list                                               | Filtered list updates as expected                                     | Pass      | Uses DropdownFilter                                           |
| TC006        | Export user data as CSV                   | Select users and use “Export as CSV” from admin actions                           | CSV file downloads with user data                                      | File contains correct headers and values                              | Pass      | Custom admin action                                           |
| TC007        | ImageTheme slug auto-population           | Add a new ImageTheme and type a title                                             | Slug field is auto-filled                                              | Slug is generated from title                                          | Pass      | Uses `prepopulated_fields`                                    |
| TC008        | Order list view                           | Visit Orders section in admin                                                     | Orders listed with number, user, status, total                        | All relevant data displayed                                           | Pass      |                                                              |
| TC009        | Order search and filter                   | Use search bar or filters (status, date)                                          | Results update to match query                                          | Correct filtering and search                                         | Pass      |                                                              |
| TC010        | PolicyPage WYSIWYG                        | Edit policy content                                                               | Summernote editor appears                                               | Rich text editor loads                                                | Pass      | Uses `SummernoteModelAdmin`                                   |
| TC011        | PolicyPage list view                      | Visit Policies section                                                            | Lists policy pages and update times                                    | Correctly sorted and displayed                                       | Pass      |                                                              |
| TC012        | Tag slug auto-population                  | Add/edit tag and type name                                                        | Slug is generated automatically                                        | Slug field updates instantly                                          | Pass      |                                                              |
| TC013        | Product list display                      | View Product admin section                                                        | Product titles, prices, dates listed                                   | Proper list rendering                                                 | Pass      |                                                              |
| TC014        | Product search/filter                     | Search or filter by theme, tag, type, license                                     | Resulting list matches criteria                                        | Functional and fast                                                  | Pass      | Uses `filter_horizontal` for M2M fields                       |
| TC015        | ProductType with PrintType display        | Visit Product Types list                                                          | Print types shown as comma-separated list                             | Shows correct M2M data                                               | Pass      | Uses custom method `print_types_list`                         |
| TC016        | LicenseType WYSIWYG editor                | Edit license description                                                          | Summernote WYSIWYG loads                                               | Text formatting supported                                            | Pass      |                                                              |
| TC017        | ShippingRate admin                        | Visit Shipping Rates section                                                      | Lists shipper, product type, country, price                            | Correct fields and filters                                            | Pass      |                                                              |
| TC018        | ShippingRate filter/search                | Use filters or search for country                                                 | Matching rates displayed                                                | Filters and search functional                                        | Pass      |                                                              |
| TC019        | CountryVAT list display                   | Visit VAT settings                                                                | Country and VAT rate listed                                             | Accurate table view                                                  | Pass      |                                                              |
| TC020        | CountryVAT search                         | Search by country name                                                            | Matching result displayed                                               | Search works with partial country names                              | Pass      |                                                              |
| TC021        | Shipper admin interface                   | Open Shipper admin section                                                        | Lists shipper names and tracking URLs                                   | All entries display correctly                                        | Pass      |                                                              |
| TC022        | Shipper search                            | Search by shipper name                                                            | Matches found and shown                                                | Case-insensitive match                                               | Pass      |                                                              |
| TC023        | TagGroup admin                            | View Tag Groups                                                                   | Lists group names                                                      | Admin page loads                                                     | Pass      |                                                              |
| TC024        | SpecialOffer admin display                | Visit Special Offers section                                                      | List shows offer text, type, expiry                                    | Sorted by expiry date                                                | Pass      |                                                              |
| TC025        | SpecialOffer filter/search                | Use sidebar filters and top search                                                | Filters results                                                        | Fast and accurate                                                    | Pass      |                                                              |
| TC026        | AboutUs WYSIWYG editing                   | Edit About Us section                                                             | Summernote editor loads                                                | Rich text editing functional                                         | Pass      |                                                              |
| TC027        | Navigation between admin sections         | Use left sidebar or breadcrumbs                                                   | Navigation updates main content pane                                   | Seamless navigation                                                  | Pass      |                                                              |
| TC028        | Form field validation in admin            | Submit form with required fields empty                                            | Form shows inline errors                                                | Proper error messages shown                                          | Pass      | Django admin default behavior                                 |

---

### Dashboard Test Matrix

| Test Case ID | Description                          | Steps to Reproduce                                                              | Expected Result                                                                 | Actual Result                                                                  | Pass/Fail | Notes                                                  |
|--------------|--------------------------------------|----------------------------------------------------------------------------------|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------|-----------|--------------------------------------------------------|
| TC041        | Dashboard Access (Staff Only)        | Log in as a staff user and navigate to `/shop/dashboard/`                        | Dashboard loads successfully with sales KPIs and charts                         | Dashboard loads correctly with metrics and empty charts (if no data available)   | Pass      | Staff-only view works with `@staff_member_required`   |
| TC042        | Dashboard Access (Non-Staff)         | Log in as a normal user and try to open `/shop/dashboard/`                       | Access denied, redirected to login or error page                                | Redirected to login page with proper message                                    | Pass      | Access control enforced                              |
| TC043        | KPI Totals Display                   | Place orders and check dashboard                                                 | Total Sales, Total Revenue, and Top Product display correct values              | KPIs update correctly with orders                                               | Pass      | Values aggregate using ORM `Sum` and `Count`         |
| TC044        | Daily Sales Trends                   | Place multiple orders across different days, view dashboard                      | Daily sales chart shows separate bars/points for each day                       | Daily chart updates as expected                                                 | Pass      | Uses `TruncDate` aggregation                         |
| TC045        | Monthly Sales Trends                 | Place orders in different months, view dashboard                                 | Monthly sales chart groups totals per month                                     | Monthly chart groups correctly                                                  | Pass      | Uses `TruncMonth` aggregation                        |
| TC046        | Yearly Sales Trends                  | Place orders in different years, view dashboard                                  | Yearly sales chart groups totals per year                                       | Yearly chart groups correctly                                                   | Pass      | Uses `TruncYear` aggregation                         |
| TC047        | Toggle Between Views (Daily/Monthly/Yearly) | Use dropdown toggle to switch between datasets                                   | Chart updates instantly when switching views                                    | Toggle switches chart data correctly                                            | Pass      | Implemented in JavaScript toggle logic               |
| TC048        | Empty Dataset Handling               | Open dashboard when no orders exist                                              | KPIs show 0, charts remain empty without error                                  | Works as expected — no crashes                                                  | Pass      | Gracefully handles empty data                        |


---

### 404 Page & Custom 404_Page_under_construction Page

| Test Case ID | Description                                | Steps to Reproduce                                                                                   | Expected Result                                                  | Actual Result                                                   | Pass/Fail | Notes                                                                                   |
|--------------|--------------------------------------------|--------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|------------------------------------------------------------------|-----------|-----------------------------------------------------------------------------------------|
| TC001        | Load 404 error page                        | Manually enter a non-existent route (e.g., /nonexistent-page)                                         | Custom 404 page is shown with branding and return button        | Custom 404 with logo, message, and return button shown          | Pass      | Designed for general 404 errors                                                       |
| TC002        | Load "Under Construction" language error   | Click language selector → choose a non-English language                                                | 404 under construction page is shown with coming soon message   | "Coming Soon" page shown for unsupported languages              | Pass      | Soft fallback UX for i18n not yet implemented                                          |
| TC003        | Responsive Design check                    | Resize browser across mobile/tablet/desktop breakpoints                                                | Layout adjusts for all devices                                  | Images and buttons scale correctly                              | Pass      | Uses Bootstrap grid system                                                              |
| TC004        | View shop logo                             | Load any error page                                                                                    | Logo is visible                                                  | Logo displayed with appropriate alt text                        | Pass      | In `404.html`, large logo shown via static image                                       |
| TC005        | Error explanation message (404.html)       | Load `404.html`                                                                                        | Message explains the page is not available                      | Text shown: “The page you are looking for is not available.”   | Pass      | Clear user direction                                                                  |
| TC006        | Error explanation message (under construction) | Load `404_page_under_construction.html`                                                                 | Message explains page is coming soon                            | Text shown: “This section isn’t quite ready yet.”               | Pass      | Includes language-related explanation                                                  |
| TC007        | Navigation button (404.html)               | Load 404 and click “Return to shop” button                                                             | Redirects to gallery page                                       | Button redirects user to `gallery_page`                         | Pass      | Prevents dead-end navigation                                                          |
| TC008        | Navigation button (under construction)     | Load under-construction page and click “Back to Creative Spark Images” button                         | Redirects to homepage                                            | Button correctly links to `/`                                   | Pass      | Button styled as `.btn` and functional                                                |
| TC009        | Branding display                           | Load both pages                                                                                        | “Creative Spark Images” branding shown                          | Branding text shown prominently on both pages                   | Pass      | Reinforces site identity even during errors                                           |
| TC010        | JS + CSS loading check (under construction)| Inspect source, view `<head>` section                                                                  | CSS/JS loaded as expected                                       | `style.css` and `script.js` included                           | Pass      | `/css/style.css` & `/js/script.js` included via `{% static %}`                        |
| TC011        | Accessibility tags                         | Inspect semantic HTML and ARIA attributes                                                              | Sections labeled for screen readers                             | `aria-label`, `alt`, `section`, and heading tags used correctly | Pass      | Basic ARIA and semantic tags in place                                                 |

---
---

### Automated Testing

Automated testing was initiated but could not be fully completed due to time constraints from an approaching deadline.

- Pylint/Flake8 compliance (PEP8 style fixes implemented)
- Unit tests on views and utility functions (`calculate_total_price`)
- Repeated regression testing after bag and checkout integration

#### Code Style and Linting (PEP8)

- Installed and ran `.flake8` to identify PEP8 violations.
- Used `autopep8` to automatically correct issues. All were resolved except one (`line too long`).
- Manually fixing that issue caused a functional error, so it was left as-is to preserve functionality.

#### Tests Implemented

Automated unit tests were written and run for various modules with successful results. Below is a breakdown of the test reports:

- **shop/tests/test_models.py**: 6 tests – all passed  
- **user_profiles/tests/test_models.py**: 3 tests – all passed  
- **user_profiles/tests/test_admin.py**: 1 test – passed  
- **user_profiles/tests/test_form.py**: 2 tests – all passed  
- **user_profiles/tests/test_views.py**: 2 tests – all passed  
- **user_profiles/tests/test_signals.py**: 2 tests – all passed  

**Final test suite run** (after implementing all features):  
- **10 tests run** – all passed

All test runs completed with no issues reported by the Django system check. Overall, the foundational test coverage is in place and functioning correctly.

---

### Test Report Django

  ```bash
  shop/tests/test_models.py
  Found 6 test(s).
  Creating test database for alias 'default'...
  System check identified no issues (0 silenced).
  ......
  ----------------------------------------------------------------------
  Ran 6 tests in 3.395s

  OK


  user_profiles/tests/test_models.py

  Found 3 test(s).
  Creating test database for alias 'default'...
  System check identified no issues (0 silenced).
  ...
  ----------------------------------------------------------------------
  Ran 3 tests in 1.575s

  OK


  user_profiles/tests/test_admin.py

  Found 1 test(s).
  Creating test database for alias 'default'...
  System check identified no issues (0 silenced).
  .
  ----------------------------------------------------------------------
  Ran 1 test in 1.659s

  OK


  user_profiles/tests/test_form.py

  Found 2 test(s).
  Creating test database for alias 'default'...
  System check identified no issues (0 silenced).
  ..
  ----------------------------------------------------------------------
  Ran 2 tests in 0.451s

  OK


  user_profiles/tests/test_views.py

  Found 2 test(s).
  Creating test database for alias 'default'...
  System check identified no issues (0 silenced).
  ..
  ----------------------------------------------------------------------
  Ran 2 tests in 2.647s

  OK

  user_profiles/tests/test_signals.py

  Found 2 test(s).
  Creating test database for alias 'default'...
  System check identified no issues (0 silenced).
  ..
  ----------------------------------------------------------------------
  Ran 2 tests in 0.987s

  OK


  Final test after implementing all features

  Found 10 test(s).
  Creating test database for alias 'default'...
  System check identified no issues (0 silenced).
  ..........
  ----------------------------------------------------------------------
  Ran 10 tests in 8.551s

  OK
  ```

---
---

### Validator testing

## Known HTML Validation Issues

During W3C HTML validation, several warnings and errors were identified across multiple pages of the site. However, due to strict time constraints nearing the end of development, these issues were not resolved in the current version, as changes could have compromised page layout and functionality.

**Validation examples**

- **Gallery / Images by Theme Page:**  
  Semantic elements such as `<section>` and `<article>` were deliberately used with `aria-label` attributes to improve accessibility, despite validation warnings related to improper use of `id` attributes and heading structure. The use of a single `<h1>` tag for the “Gallery” title was retained to ensure proper screen reader support, overriding the validator’s recommendation for demotion to `<h2>`.

- **Product Detail Page:**  
  The use of `autocomplete="off"` on `<input type="radio">` elements was intentional and aimed at ensuring consistent user experience. This prevents browsers from auto-selecting previously chosen options, which could override default selections and cause visual or functional inconsistencies upon page reload.

- **Shopping Bag Page:**  
  A validation error flagged an incorrectly typed attribute `aria-disbaled`, which was intended to be `aria-disabled`. This attribute was used on an anchor tag styled as a button to improve accessibility by communicating a disabled state to assistive technologies, since `<a>` elements do not support the native `disabled` attribute.

---

In summary, while these validation issues are acknowledged, they were consciously deprioritized due to time limitations and the potential impact on layout stability and user experience.

---

### CSS Validation:

[![Valid CSS!](https://jigsaw.w3.org/css-validator/images/vcss)](https://jigsaw.w3.org/css-validator/check/referer)

no CSS errors detected
Additionally, a list with warning was displayed resulting from outdated style elements due to teh use of Bootstrap and webkits.

---

### Javascript

Javascript errors detected and fixed
used tool: JSHint
no errors detected
warning caused by the use of arrow functions only avaialbale in ES6

---
---

### Bugs and Resolutions

  | Bug / Issue | Description | Resolution |
  |-------------|-------------|------------|
  | `ModuleNotFoundError` for `bag.context_processors` | Typo in the context processor path led to an internal server error on homepage load. | Corrected the import path in `settings.py` to properly reference `bag.context_processors.bag_contents`. |
  | Quantity was not passed in `POST` request | Resulted in `NoneType` error during `add_to_bag` view. | Added a hidden quantity field and ensured `name="quantity"` was included in the form. |
  | Incorrect `if` template logic in `bag.html` | Used `{% elif %}` without a condition, causing a TemplateSyntaxError. | Replaced `{% elif %}` with `{% else %}` to correctly handle the conditional. |
  | Printed product was added as digital | Format input was not updated when selecting "Printed Product". | Ensured `formatInput.value` is updated in the JS toggle logic and added the `formatInput` field inside the `<form>`. |
  | Remove button in bag failed | Reverse URL lookup for `remove_from_bag` failed due to incorrect argument. | Updated `remove_from_bag` view to use composite `item_key` and passed it correctly in the template with `{% url 'remove_from_bag' key %}`. |
  | Print type showed as "None" | Printed product selection was not saved properly. | Corrected logic in view to capture and store the print type string instead of its raw or empty value. |
  | Duplicate field assignments | Variables like `product_format`, `license_id` were declared twice. | Cleaned up `add_to_bag` view to assign each value once and added necessary try-except blocks for safety. |
  | Quantity not accumulating | Items were overwritten instead of updated when re-added. | Switched from product ID key to composite `item_key` in the session to distinguish variations. |
  | Facebook page not linked correctly in Instagram | Page didn’t show under Accounts in Instagram. | Resolved via Meta’s **Accounts Center** by properly connecting Facebook Page under "Connected Experiences". |
  | Stripe `checkout_success` crashed on OrderModel save | `user_id` was missing due to anonymous session. | Required login before checkout and passed `request.user` when saving the order. |
  | `product_format` showed as `None` in bag | JS toggle logic did not update hidden input properly. | Ensured `formatInput.value` is correctly set on both radio button changes. |
  | Shopping bag displayed nothing after adding product | Key logic broke due to mismatch between view and template. | Made sure both view and template used the same composite `item_key` structure. |
  | View crashed due to `b` typo | Typo in `remove_from_bag` function: `b else:` instead of `else:`. | Fixed syntax error by removing stray character and fixing indentation. |
  | Shipping costs not appearing | Incorrect `product_type` used for ShippingRate query| Mapped `print_type` to correct lowercase keys using `PRINT_TYPE_TO_SHIPPING_TYPE` |
  | Shipping displayed as €0.00 despite valid config | Print type defaulted silently to first in list | Added `---` placeholder and enforced user selection |
  | VAT always showed 0% | VAT lookup failed due to missing country session value | Added fallback and ensured country is set in session |
  | Buttons didn’t disable after selection changes | No JS logic tracking pending updates | Introduced `data-pending-update` attributes and validation logic |
  | Proceed to Checkout remained active | JS didn’t sync with all forms | Check across all forms before enabling the checkout button |
  | Buttons misaligned on mobile | Layout didn’t account for responsive wrapping | Used Bootstrap classes to stack buttons on small screens |
  | Image not resizing | Fixed height and inline styles limited image height | Replaced inline styles and used flexbox with min-height |
  | Order total recalculated incorrectly in checkout | View re-calculated totals instead of using pre-calculated bag data. | Added session-level calculation and passed it to OrderModel creation. |
  | `request.user` not passed in `OrderModel` | Attempted to save an order without an authenticated user. | Added `login_required` decorator to ensure only logged-in users can complete checkout. |
  | Stripe webhook email not received | Email address was missing from test payload. | Ensured `customer_email` was included in Stripe session and template. |
  | `Uncaught TypeError: Cannot read properties of null (reading 'style')` | JavaScript attempted to access `.style` on DOM elements that were not present on some pages (e.g., `#backToTop`, `#message-container`). | Added `if (element)` checks before accessing `.style` or attaching event listeners to ensure scripts run safely across all pages. |
  | `NoReverseMatch at /` | `{% url 'page_under_construction' %}` was used without registering the corresponding view in `urls.py`. | Created a Django view for `page_under_construction` and added a named URL pattern. |
  | `Uncaught ReferenceError: Cannot access 'translations' before initialization` | JavaScript attempted to access the `translations` object before it was defined using `const`. | Reordered code to define `translations` before using it. |
  | Language selection always showed English | Language was hardcoded in JavaScript (`const lang = 'en'`) instead of being dynamically detected. | Re-enabled `detectLang()` to read from `?lang=` query parameter or browser settings. |
  | `Uncaught TypeError: Cannot set properties of null (setting 'textContent')` | JavaScript tried to update elements that didn’t exist in the DOM because `{% block content %}` was missing or script ran before DOM loaded. | Wrapped content in `{% block content %}` and deferred DOM updates using `DOMContentLoaded`. |
  | Flag icon didn't match selected language | The navbar flag was hardcoded to the UK flag. | Added logic to update the flag image based on selected language using JavaScript and query parameters. |
  | UK flag disappeared from language dropdown | English was only used in the toggle button, not listed as an option. | Added English back into the dropdown list with the appropriate flag and label. |
  | Bug / Issue | Description | Resolution |
  | Modal infinite loop | Clicking "Continue" after a cancelled or skipped save reopened the modal | Tracked user intent using flags and dataset attributes to conditionally redirect |
  | Modal not closing | Clicking "Save" did not close modal despite successful save | Refactored save handler to close modal on successful response |
  | Error displayed despite success | Modal still showed "Unable to save profile" even when save succeeded | Ensured error alert is cleared upon success and modal is hidden |
  | Profile changes not reverted | Authenticated users clicking "Don't Save" saw their edits remain in the form | Reset form fields to original values by re-inserting captured initial data |
  | Pre-filled data not displayed | Billing form did not display saved profile data for authenticated users  | Used `initial.billing_*` context properly in the template                 |
  | No field-level error feedback | Form didn’t provide immediate input feedback                             | Added `invalid-feedback` elements and real-time input validation          |
  | Continue enabled on invalid input | Button could activate before form was valid                          | Bound validation logic to real-time listeners and checked on render       |
  | Country select didn’t persist | Selected country not marked as `selected` in dropdown                    | Used `{% if initial.billing_country == 'IE' %}selected{% endif %}`        |
  | Missing Template Filter | Template filter `get_item` caused `TemplateSyntaxError` in `checkout_summary.html`.            | Removed or replaced `get_item` usage with direct dictionary access or correct filter logic. |
  | No Timestamp on Request | AttributeError: `'WSGIRequest' object has no attribute 'timestamp'` during offer lookup.       | Replaced `request.timestamp` with `timezone.now()` from Django utilities.                   |
  | Favicon 404             | Browser auto-requested `/checkout/favicon.ico`, resulting in a 404 error.                      | Added a `favicon.ico` in the static directory and linked it via `<link rel="icon">`.        |
  | Price Format Inconsistency | Some totals were displayed as `€0` instead of `€0.00`.                                         | Applied `floatformat:2` in the Django template to ensure all monetary values show two decimals. |
  | `get_item` filter error             | Template error due to undefined custom filter `get_item`                                    | Removed custom template logic and used native Django context rendering                       |
  | `request.timestamp` not found       | Attempted to access non-existent attribute `request.timestamp`                              | Replaced with `timezone.now()` in views.py to fetch current timestamp reliably              |
  | `{% csrf_token %}` warning          | Warning shown due to missing `RequestContext` when rendering user form                     | Ensured all form views use `RequestContext` and context processors properly configured       |
  | Favicon 404                         | Missing `favicon.ico` request caused 404 errors in dev logs                                 | Added a `favicon.ico` static file and linked it in base template                            |
  | Missing card layout in summary      | Order Summary section lacked consistent visual card styling used in previous steps          | Wrapped entire summary content inside Bootstrap `.card` container with padding and shadow   |
  | Buttons breaking layout             | Proceed/Back buttons appeared too large or shared borders on small screens                  | Updated with responsive width classes and spacing utilities (`w-auto`, `gap-2`, etc.)       |
  | Progress bar hidden at Step 3       | Summary step loaded via AJAX but didn’t re-render the tracker                               | Extracted progress markup to a shared include and injected with context-aware highlighting   |
  | Buttons not responsive              | Buttons didn’t resize proportionally or maintain readability on smaller screens             | Used flexbox (`d-flex`, `gap-2`, `w-auto`) and removed fixed sizing                         |
  | AJAX missing on Step 3              | Step 3 (summary) was previously rendered via redirect, losing dynamic step state            | Implemented full AJAX loading of Step 3 with updated progress and button handling           |
  | Webhook failures          | 400/404 errors in Stripe dashboard when using dynamic Ngrok URLs           | Replaced with a static Ngrok domain and re-authenticated the tunnel       |
  | Stripe session unverified | Webhook didn’t validate signature on localhost                             | Correct `STRIPE_WH_SECRET` used and token passed securely                 |
  | Print statement silent    | `print('Payment received:', session)` not visible in production logs     | Print removed, replaced with proper logging and DB order creation routine  |
  | Cards open all at once | Clicking one license card caused all cards to expand simultaneously on large and extra-large screens. | Updated the JavaScript to target the clicked `.license-card`'s specific `.license-description` element using `querySelector` instead of relying on duplicate IDs. |
| Duplicate `id` values | All `.license-description` divs shared the same `id`, causing conflicts and invalid HTML. | Switched to using unique identifiers by dynamically appending `license.pk` in the `id` attribute. |
| Script error: `addEventListener` of null | JS tried to bind `addEventListener` on an element that didn't exist when `emailInput` was missing from the DOM. | Renamed `emailInput` to the actual Django-generated `id_email` and added a `null` check in JS before attaching the listener. |
| Back-to-gallery button not visible on empty pages | On pages with no content and no scroll, the button relying on scroll detection never became visible. | Replaced dynamic JS logic with a hardcoded fallback button in the HTML template for empty pages. |
| JavaScript event listener conflict | `shop_script.js` and inline scripts created overlapping behavior on elements like `.read-more-btn` and `.license-card`. | Removed no-longer-needed inline JS blocks and scoped `shop_script.js` to handle only its designated classes. |
| Progress Bar Not Highlighting Step 5 | When reaching the `checkout_success.html` confirmation page, the progress bar does not visually highlight the final step (Step 5: Confirmation), breaking consistency with the rest of the checkout flow.| Replaced dynamic JavaScript-based tracker with a **static progress bar** using `.success-wrapper`, `.success-step`, and `.success-step-active` classes, styled to visually match earlier steps but without depending on JS logic or `currentStep` state.|
| Progress Bar Not Centered on Large Screens | On screens ≥768px, the custom confirmation progress bar appeared off-center, breaking the alignment consistency set in global checkout steps. | Wrapped confirmation step in a `.success-wrapper` div and applied targeted media queries (from `1024px` and up) with `margin: 0 auto; width: 60%` to match `.progress-wrapper` from the main checkout styles. |
| Order Line Items Missing Quantity or Type Info | The initial order summary showed only the product title without print type, license, or quantity, causing ambiguity in confirmation details for digital or printed items.| `checkout_success` view reconstructs order line items from the bag stored in the Stripe session metadata, allowing `bag_items` to include `quantity`, `format`, `print_type` or `license`, and pricing for complete and clear display. |
| Responsive Layout Broken on Mobile | Product image and details were stacked horizontally even on small screens, making it hard to read or scroll on phones. | Used Bootstrap’s grid system (`col-md-2`, `d-none d-md-block`, etc.) to **hide image on small screens** and maintain a stacked layout. Product details are shown below image on mobile and side-by-side on desktop, mimicking cart styling for consistency.|
| Inconsistent VAT/Shipping/Discount Calculation  | VAT and shipping were not properly recalculated on the confirmation page, leading to mismatches between payment totals and display.| VAT, shipping, and discounts are recomputed in `checkout_success()` based on Stripe’s `session.metadata`, ensuring display values match those used in payment.|
| Confirmation Page Not Integrated with Main Flow | `checkout_success.html` was originally standalone and excluded from the linear checkout logic, causing confusion and progress tracking issues.| Used `step=5` context variable to match UI logic and hardcoded a non-interactive progress bar using shared visual styles, creating continuity without JavaScript reliance.|
| Bag Not Reset After Order | The cart remained full after completing the checkout, potentially confusing users and allowing accidental repeat purchases. | `request.session["bag"] = {}` is explicitly reset in the view only **after** Stripe payment is confirmed and the order is successfully fetched, preventing premature clearing or skipped payments. | 
| Duplicate email confirmations sent | When `send_order_email()` failed (due to template or context issues), the fallback plain text email was always triggered, resulting in **two confirmation emails** being sent to the customer. | Updated the exception handling to only trigger fallback email when specific errors (e.g. `TemplateDoesNotExist`, `TemplateSyntaxError`, `SMTPException`) occur during the rich email rendering or sending process. |
| `'str' object is not a mapping` error | `send_order_email()` expected a `summary` dictionary, but was incorrectly passed a `session_id` string instead, causing unpacking (`**summary`) to fail. | Ensured that `send_order_email()` either accepts a `summary` dict (with values like `bag_items`, `vat`, etc.) or is modified to rebuild context from `session_id`. Consistently used one strategy across all views. |
| Incorrect shipping cost in confirmation email | The email summary used hardcoded or incomplete shipping calculations, resulting in the wrong shipping total (e.g. 0€ instead of 6.60€). | Aligned email view logic with `checkout_success`, using full bag data and correct shipping rates per item. |
| Missing digital download links in confirmation email | Digital products with attached files weren’t showing download links in the email. | Re-added logic to loop over products and generate secure download links for those with associated files. |
| Template rendering failed silently | Errors in the HTML/text email templates weren't clearly surfaced, making debugging difficult. | Added logging for `TemplateDoesNotExist` and `TemplateSyntaxError` to help identify rendering issues without affecting the customer experience. |
| Image download not working        | Download links for digital products were not functioning in either the confirmation page or email. | Changed `resource_type='raw'` in `build_url()` in Product model to match how the images were uploaded to Cloudinary. |
| Chrome blocking download          | Downloads worked in Safari and email but failed in Chrome due to mixed content (HTTP download URL).| Added `secure=True` to `build_url()` to enforce HTTPS and avoid Chrome’s mixed content blocking.  |
| Image download links not working     | Initially, download links in both the browser and confirmation email failed, especially in Chrome. Some files gave 400 errors after restart, especially `.heic` images auto-converted to `.jpeg` by macOS. | Switched `resource_type` to `'image'`, added `secure=True`, and sanitized file names to remove problematic characters. Identified `.heic`-to-`.jpeg` conversion issue—resolved by batch converting files manually before re-uploading. |
| Download link shown for all products | The download button was appearing even for printed products,which shouldn't be downloadable. |
| In the browser view (`checkout_success`), filtered out printed products using the session’s bag data. For email, reused `bag_items` passed via context and skipped items with `print_type`.|
| Session unavailable in email context | The session-based product format check was not accessible when sending email.
| Passed enriched product data (`bag_items`) with format info into the email context, then filtered for digital products only in the email logic.|
| Special Offer application stopped working | The `apply_special_offer` function stopped applying discounts, even when valid offers existed. The logic was intact, but it wasn’t integrated correctly into the updated checkout flow (e.g., `create_checkout_session`, `checkout_summary`, and `checkout_success`). This caused the special offer to silently fail. | Re-integrated the `apply_special_offer` function into all key checkout steps, ensuring discount calculation is applied consistently. Verified that discounts now flow correctly from checkout summary → Stripe session → order confirmation. |
| Free Shipping Discount Not Applied Correctly | Customers saw `-€0.00` in the discount field, even when the total order value exceeded the minimum threshold for free shipping. The logic only checked the **subtotal** (`bag_total`) against the threshold, ignoring shipping. | Updated `apply_special_offer` to check the **order total excluding VAT** (`bag_total + shipping_total`) against the threshold. Now, when free shipping is applied, the discount equals the deducted shipping cost (e.g., `-€22.00`), clearly showing the benefit. Verified locally and in production. |
| Checkout flow – Server 500 error during Stripe webhook | The server crashed with a 500 error after Stripe’s `checkout.session.completed` webhook because the session metadata stored the entire cart (`bag`) JSON. This caused payload bloat, and decoding errors during webhook processing. It also created discrepancies when orders were being reconstructed from that metadata. | Implemented a `bag_ref` approach: instead of storing the full `bag` JSON in the Stripe session, a unique `bag_ref` UUID is generated and mapped to the session bag in Django. Stripe metadata now only includes this lightweight reference. The webhook retrieves the original bag via `bag_ref`, eliminating payload size issues and JSON decoding failures. This stabilized order creation | Orders with more than 3–4 items could not complete checkout and failed with a 500 error, blocking users from purchasing larger or multiple-item orders until resolved. |
| Stripe checkout: product image not showing & cancel redirect not working | During Stripe Checkout, product images were missing and the cancel button redirected to a non-existent `/bag/view_bag/` path. This caused broken UX when customers abandoned payment. | Fixed by adding absolute image URLs (`request.build_absolute_uri(product.image_preview.url)`) to Stripe line items and correcting the cancel URL to use Django’s `reverse("view_bag")`, ensuring images display properly and cancel redirects to the shopping bag. |
| Discount and Subtotal Missing in Confirmation Email | The order confirmation email was not displaying the discount or subtotal values because `send_order_email()` was not passing these fields correctly to the email templates. | Updated `send_order_email()` in `checkout_success` to include `bag_total` and `discount` in the summary context, ensuring both HTML and plain-text emails render the full pricing breakdown accurately |
| Checkout "Change" link caused 404 | The "Change" link in the **Billing Information** section pointed to `/checkout/billing/`, which does not exist in the Django URLconf. This resulted in a *Page not found (404)* error. | Replaced the hardcoded link with `/checkout/?step=billing` and added a query-string handler in `checkout_script.js` to load the billing form directly when `?step=billing` is present. |
| Jumping back to Checkout Summary | Users had no way to jump back directly to the order summary step from intermediate steps, forcing them to restart the checkout flow. | Introduced a `?step=summary` query parameter and updated `checkout_script.js` to detect it, allowing the summary template to be loaded immediately without restarting the checkout flow. |
| Missing Live Validation on Profile Step | The checkout profile form lacked real-time validation, allowing users to progress with incomplete or invalid fields. This was highlighted as a weakness during assessment. | Implemented **live validation** for `first_name`, `last_name`, and `email` fields in `checkout_script.js`. Fields are validated on input and blur events, disabling the "Continue" button until all fields are valid. |
| Checkout success redirect not working for new users | The `{CHECKOUT_SESSION_ID}` placeholder in the success URL was being escaped by `build_absolute_uri()` into `%7B...%7D`, preventing Stripe from replacing it with the actual session ID. This caused `checkout_success` to fail for non-admin users. | Build the success URL with `reverse("checkout_success")` and append the raw query string: `...?session_id={CHECKOUT_SESSION_ID}` so Stripe receives the correct placeholder and substitutes it properly. |
| Account deletion request not working | Initially, the “Delete my account” link did not trigger any action. After fixing the connectioin between modals and Javascript, the process stalled after the first step and no confirmation email was sent. The backend only notified the admin, leaving the user without feedback. | Fixed by wiring up the button to the modal flow, implementing a two-step confirmation process, and updating the `request_account_deletion` view to send **two emails**: one to the site admin with the user’s request, and one to the user confirming receipt of the request. |

---
---

### Bugs remaining:

  - clicking the **Back**-button on the Stripe payment field returns the user to a order summary page with broken styling

  ---
  
  - Image catalogue link is currently not active; reason: filter functionality could not be implemented due to deadline reached

---
---

## Code Quality and Version Control

- PEP8 Compliance: The code has been checked against PEP8 standards using .Flake8, .autopep8 and Pylint

- Comments: Functions and classes include docstrings to describe their purpose, inputs, and outputs.

- Version control is managed using Git and GitHub, with a focus on maintaining a clean and organized history. Regular commits follow a consistent format and describe the features implemented and/or reasons for changes made to existing features.

---
---

## Sitemap

Creative Spark Images uses a dynamically generated `sitemap.xml` to improve SEO and help search engines crawl the most relevant content.

### Features

- Auto-generated sitemap via Django’s `django.contrib.sitemaps` framework.
- Accessible at [`/sitemap.xml`](https://creativesparkimages.com/sitemap.xml).
- Covers all key public-facing routes:
  - Homepage and static pages (via `StaticViewSitemap`)
  - Individual product detail pages (via `ProductSitemap`)
  - Theme-specific gallery views (via `ThemeSitemap`)
  - About Us content (via `AboutUsSitemap`)
- Custom priorities and change frequencies defined for each section.

### Setup Highlights

- A single `sitemaps.py` file is located at project level (`my_shop/sitemaps.py`).
- Registered in `urls.py` using Django’s built-in `sitemap` view.
- Automatically updated as products or themes are added via the admin panel.

---
---

## Technology Stack

- **Backend:** Python 3, Django 4.2
- **Frontend:** HTML5, CSS3, Bootstrap 5, JavaScript
- **Database:** PostgreSQL
- **Media Hosting:** Cloudinary
- **Payment Integration:** Stripe
- **Email Notifications:** Django Email Host + Gmail
- **Deployment:** Heroku

---
---

## Deployment

This project is hosted on Heroku

  **Fork or Clone the repository**

1. Clone the repo:
    ```bash
    git clone https://github.com/yourusername/creative-spark-images
    cd creative-spark-images

2. Create a virtual environment:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate

3. Install dependencies:
    ```bash
    pip install -r requirements.txt

    # List of dependencies
    asgiref==3.8.1
    bleach==6.2.0
    certifi==2025.1.31
    cffi==1.17.1
    charset-normalizer==3.4.1
    cloudinary==1.36.0
    crispy-bootstrap5==0.7
    cryptography==44.0.2
    defusedxml==0.7.1
    dj-database-url==0.5.0
    dj3-cloudinary-storage==0.0.6
    Django==4.2.20
    django-admin-list-filter-dropdown==1.0.3
    django-allauth==0.57.2
    django-countries==7.2.1
    django-crispy-forms==2.3
    django-summernote==0.8.20.0
    gunicorn==20.1.0
    idna==3.10
    oauthlib==3.2.2
    packaging==24.2
    psycopg2-binary==2.9.10
    pycparser==2.22
    PyJWT==2.10.1
    python3-openid==3.2.0
    requests==2.32.3
    requests-oauthlib==2.0.0
    setuptools==75.8.2
    six==1.17.0
    sqlparse==0.5.3
    stripe==11.6.0
    typing_extensions==4.12.2
    urllib3==1.26.20
    webencodings==0.5.1
    whitenoise==6.5.0


4. Set up .env with:
    ```bash
    SECRET_KEY=
    DEBUG=False
    DATABASE_URL=
    STRIPE_PUBLIC_KEY=
    STRIPE_SECRET_KEY=
    STRIPE_ENDPOINT_SECRET=
    CLOUDINARY_URL=

5. Apply migrations:
    ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate

6. Collect static files:
    ```bash
    python3 manage.py collectstatic

7. Create a PPROCFILE:
    ```bash
    python manage.py > Procfile

8. in settings.py
    ```bash
    DEBUG = FALSE

8. Deploy to Heroku or similar:
    ```bash
    Set up environment variables in Heroku dashboard
    Link GitHub repo
    Enable automatic deploys

> The live link can be found here: https://creative-spark-images-shop-6e4790dd908e.herokuapp.com/

---
---

## Usage

  - Launch the site and browse the gallery
  - Select a product, choose format and quantity
  - Add to cart and proceed to secure checkout
  - Receive confirmation and follow-up via email

---
---

## Contribution

  - Fork the repo
  - Create a new branch (git checkout -b feature-name)
  - Make your changes
  - Commit (git commit -m 'Add feature')
  - Push to branch (git push origin feature-name)
  - Open a Pull Request

---
---

## Acknowledgements

### Content

- Stripe Docs for checkout and webhooks
- all legal documents, T&C and policy documents are taken from my existing shop with Picfair whcih this new shop is going to replace
- Stack Overflow and Django community for troubleshooting
- Code Institute project templates for structure inspiration [p3-template](https://github.com/Code-Institute-Org/p3-template)

### Media
- placeholder images:  Freepik https://www.freepik.com/free-photos-vectors
- Icons from my Icon Kit on [font-awesome](https://fontawesome.com/icons)
- all images and videos are my own

---
---

## Author

- [merzann](https://github.com/merzann)

---
---

## License
[![MIT License](https://img.shields.io/badge/License%20-%20MIT-olivgreen)](LICENSE.md)