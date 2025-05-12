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
git clone https://github.com/Wambita/Django-blog.git
cd Django-blog
```
2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Apply Migrations:**
   ```bash
   python manage.py migrate
   ```

4. **Create Superuser (Optional):**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the Application:**
   - Open your web browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to view the homepage.
   - Access the admin panel at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) to manage users and articles (requires superuser credentials).
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
