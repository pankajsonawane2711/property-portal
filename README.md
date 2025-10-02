# Property Portal (Complete)
Includes:
- Buyer + Builder + Admin roles
- Auth (email/password; Google optional via allauth stub)
- Builder Dashboard (CRUD) with approval flow
- Listings + Detail with Leaflet map
- Leads (enquiry), Save Property (login required)
- Sitemap/robots/OG meta
- CSV/JSON fixtures for 10 properties
- Dockerfile + Railway config

## Quick start
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py loaddata properties/fixtures/properties.json
python manage.py runserver
```
