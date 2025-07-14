# Quizera

A Django-based web application featuring a blog module, demonstrating core Django concepts such as models, views, templates, static files, and custom management commands. This project is ideal for learning or teaching Django fundamentals and serves as a solid foundation for more advanced web development.


## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features
- User authentication (login/logout required for most pages)
- List of quizzes with pagination
- Individual quiz/practice pages
- About and contact pages
- Responsive design using Bootstrap
- Custom static styling
- Modular template structure (header, footer, base)
- MySQL database integration (optional)
- Custom management commands for data population

## Project Structure
```
myapp/
├── manage.py                  # Django project entry point
├── db.sqlite3                 # SQLite DB (default, not used if MySQL configured)
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
├── myapp/                     # Django project settings and URLs
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── blog/                      # Main Django app (quizzes, users, etc.)
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/            # Database migrations
│   │   ├── __init__.py
│   │   ├── 0001_initial.py
│   │   ├── ...                # Other migration files
│   ├── management/
│   │   └── commands/
│   │       ├── __init__.py
│   │       └── populate_dat.py
│   ├── static/
│   │   └── css/
│   │       └── style.css
│   └── templates/
│       ├── about.html
│       ├── base.html
│       ├── contact.html
│       ├── detail.html
│       ├── index.html
│       ├── login.html
│       ├── register.html
│       └── [other html files]
├── templates/
│   └── 404.html               # Custom error page
```

## Main Components
**models.py:**
- `Post`: Represents a quiz post with title, content, image, and slug for URLs.
- `AboutUs`: Stores about/mission content for the About page.

**views.py:**
- `index`: Home page (requires login).
- `list`: Paginated list of quizzes.
- `detail`/`practice`: Individual quiz/practice page.
- `about`: About Us page.
- `contact`: Contact form (with validation).
- `login/logout`: User authentication.

**forms.py:**
- `ContactForm`: Simple form for name and message.

**templates/:**
- Modular HTML using Bootstrap, with reusable header/footer.
- Pages: Home, List, Practice, About, Contact, Login, Register, Detail.

**static/css/style.css:**
- Custom styles for background and pagination.

**management/commands/populate_dat.py:**
- Custom Django management command for populating the database with sample data.

## Setup Instructions
1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd myapp
   ```
2. **Create and activate a virtual environment**
   ```bash
   python -m venv tutorialenv
   tutorialenv\Scripts\activate  # On Windows
   # or
   source tutorialenv/bin/activate  # On Mac/Linux
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure the database (optional for MySQL)**
   Edit `myapp/settings.py` with your MySQL credentials:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'courses',
           'USER': 'root',
           'PASSWORD': 'your_password',
           'HOST': '127.0.0.1',
           'PORT': '3306'
       }
   }
   ```
5. **Apply migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
6. **Create a superuser (for admin access)**
   ```bash
   python manage.py createsuperuser
   ```
7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

## Usage
- **Login:** Use your Django superuser or any created user.
- **View Quizzes:** After login, see the list of quizzes and click "Read" for details.
- **About/Contact:** Learn about the project or send a message via the contact form.
- **Logout:** Use the header button to log out.

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License
This project is for learning and demonstration purposes. 
