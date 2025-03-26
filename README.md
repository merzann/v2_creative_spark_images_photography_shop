# Creative Spark Images – Photography Shop

## Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Features Left to Implement](#features-left-to-implement)
- [The Admin Panel](#the-admin-panel)
- [Security Features and Error Handling](#security-features-and-error-handling)
- [Testing](#testing)
- [Technology Stack](#technology-stack)
- [Deployment](#deployment)
- [Usage](#usage)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)
- [Author](#author)
- [License](#license)

---

## About the Project

**Creative Spark Images** is a feature-rich eCommerce web application built for photographers to sell digital and printed artworks.

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

> Live site: [Add your live Heroku or production link here]

---

## Features

### Existing Features

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
- Admin control via Django backend

### Shopping Bag Functionality

- Real-time cart updates
- Session persistence
- Remove items with composite keys (product ID, format, license/print type)
- Frontend UI feedback with toast messages
- Dropdown cart preview (like modern eCommerce platforms)

### Checkout Flow

- Stripe Checkout Session with dynamically populated line items
- Success page clears cart and saves order
- Orders are saved with full metadata (user, total price, status)
- Secure webhook for Stripe confirmations

---

### Features Left to Implement

- User profiles with order history
- Rating and comment system for products
- Image zoom/lightbox on product detail
- SEO optimization and sitemap auto-generation
- Instagram feed integration

---

## The Admin Panel

Admins can:
- Add/edit products, licenses, and print types
- View and manage orders via OrderModel
- Manage stock levels
- Add featured products and promotions

Admin is enhanced with:
- Crispy forms
- Status filters
- Automated `order_number` generation

---

## Security Features and Error Handling

- CSRF protection on all POST requests
- Cleaned and validated form inputs
- Graceful fallback for missing data
- Django messages framework to inform users
- Proper use of Django’s ORM to prevent SQL injection
- Restriction of checkout success/order creation to authenticated users
- Secure Stripe key handling via environment variables
- Admin login restricted to staff/superusers

---

## Testing

### Manual Testing

- Add to cart (with/without license or print type)
- Remove from cart
- Quantity updates
- Stripe checkout end-to-end
- Webhook confirmation with test payloads
- Error message display for edge cases
- Missing print type/stock/out of range conditions

### Automated Testing

- Pylint/Flake8 compliance (PEP8 style fixes implemented)
- Unit tests on views and utility functions (`calculate_total_price`)
- Repeated regression testing after bag and checkout integration

---

## Technology Stack

- **Backend:** Python 3, Django 4.2
- **Frontend:** HTML5, CSS3, Bootstrap 5, JavaScript
- **Database:** PostgreSQL
- **Media Hosting:** Cloudinary
- **Payment Integration:** Stripe
- **Email Notifications:** Zapier + SendGrid
- **Deployment:** Heroku

---

## Deployment

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/creative-spark-images
   cd creative-spark-images

2. If using VS Code, create a virtual environment:
   python3 -m venv .venv
   source .venv/bin/activate

3. Install dependencies:
   pip install -r requirements.txt

4. Set up .env with:
   SECRET_KEY=
   DEBUG=False
   DATABASE_URL=
   STRIPE_PUBLIC_KEY=
   STRIPE_SECRET_KEY=
   STRIPE_ENDPOINT_SECRET=
   CLOUDINARY_URL=

5. Apply migrations:
   python3 manage.py migrate

6. Collect static files:
   python3 manage.py collectstatic

7. Deploy to Heroku or similar:
   Set up environment variables in Heroku dashboard
   Link GitHub repo
   Enable automatic deploys

## Usage

  - Launch the site and browse the gallery
  - Select a product, choose format and quantity
  - Add to cart and proceed to secure checkout
  - Receive confirmation and follow-up via email

## Contributing

  - Fork the repo
  - Create a new branch (git checkout -b feature-name)
  - Make your changes
  - Commit (git commit -m 'Add feature')
  - Push to branch (git push origin feature-name)
  - Open a Pull Request

## Acknowledgements

- Stripe Docs for checkout and webhooks
- Stack Overflow and Django community for troubleshooting
- Code Institute project templates for structure inspiration
- Freepik for placeholder images

## Author

- [merzann](https://github.com/merzann)

## License
[![MIT License](https://img.shields.io/badge/License%20-%20MIT-olivgreen)](LICENSE.md)