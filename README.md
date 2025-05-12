# Django Blog Platform

[![Django](https://img.shields.io/badge/Django-3.2-brightgreen)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://www.python.org/)

A full-featured blogging platform built with Django, featuring user authentication, CRUD operations, and responsive design.

## Features

✅ User Authentication System  
✅ Create/Edit/Delete Blog Posts  
✅ Responsive Bootstrap Design  
✅ Post Timestamps  
✅ Admin Dashboard  
✅ Search Optimization Ready  

## Installation

1. **Clone Repository**
```bash
git clone https://github.com/yourusername/django-blog.git
cd django-blog
```

2. **Set Up Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Database Setup**
```bash
python manage.py migrate
```

5. **Create Admin User**
```bash
python manage.py createsuperuser
```

6. **Run Development Server**
```bash
python manage.py runserver
```

## Usage

- Access admin panel at `/admin`
- Create new posts when logged in
- Public view shows all posts
- Responsive design works on mobile/desktop

## Project Structure
```
django-blog/
├── blog/               # Main application
├── blog_project/       # Project configuration
├── templates/          # HTML templates
├── requirements.txt    # Dependencies
└── manage.py           # Django CLI
```

## Screenshots

![Home Page](https://via.placeholder.com/800x400?text=Blog+Homepage)
![Admin Panel](https://via.placeholder.com/800x400?text=Admin+Dashboard)

## License
MIT License - See [LICENSE](LICENSE) for details

## Roadmap
- [ ] Add comment system
- [ ] Implement search functionality
- [ ] Add user profiles
- [ ] Deploy to cloud


## Author 
**Wambita Sheila Fana**
