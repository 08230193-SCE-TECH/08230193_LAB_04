# Personal Learning Journey Web Application

**Student ID:** 08230193  
**Name:** Sonam Choden  
**Lab:** 04 - Django MVT Architecture  
**Course:** Web Application Development  

## Project Overview

This Django web application demonstrates the Model-View-Template (MVT) architecture by creating a personalized learning journey website. The application showcases my progress in web development and provides information about my background.

## Features

### 🏠 **Index Page (Learning Journey)**
- Displays my personal learning journey and experiences
- Shows dynamic learning milestones from the database
- Responsive design with modern styling
- Navigation to About Me page

### 👤 **About Me Page**
- Personal information and biography
- Contact details
- Professional background
- Clean, modern interface

### 🔧 **Admin Interface**
- Django admin panel for content management
- Easy addition of learning milestones
- Personal information management
- User-friendly interface for data entry

## Technical Implementation

### **Models (Data Layer)**
- `AboutMe`: Stores personal information (name, bio, email)
- `LearningJourney`: Stores learning milestones (title, description, date)

### **Views (Logic Layer)**
- `Index`: Displays learning journey with dynamic content
- `aboutMe`: Shows personal information

### **Templates (Presentation Layer)**
- `Index.html`: Main learning journey page
- `aboutMe.html`: Personal information page
- Responsive CSS styling
- Modern UI/UX design

### **URL Configuration**
- Clean URL routing
- RESTful URL patterns
- Proper navigation between pages

## Installation & Setup

### Prerequisites
- Python 3.8+
- Django 5.2.7
- SQLite database

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/08230193_Lab4.git
   cd 08230193_Lab4
   ```

2. **Install dependencies:**
   ```bash
   pip install django
   ```

3. **Run migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create superuser:**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the application:**
   - Main site: `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

## Usage

### Adding Content

1. **Access Admin Panel:**
   - Go to `http://127.0.0.1:8000/admin/`
   - Login with your superuser credentials

2. **Add Personal Information:**
   - Navigate to "Personal Information"
   - Add your name, bio, and email

3. **Add Learning Milestones:**
   - Navigate to "Learning Milestones"
   - Add titles and descriptions of your achievements

### Viewing the Site

- **Homepage:** Displays your learning journey with dynamic milestones
- **About Me:** Shows your personal information
- **Navigation:** Easy navigation between pages

## Project Structure

```
08230193_LAB_04/
├── myJourney/                 # Django project
│   ├── myJourney/            # Project settings
│   │   ├── __init__.py
│   │   ├── settings.py       # Django configuration
│   │   ├── urls.py           # Main URL configuration
│   │   └── wsgi.py
│   ├── scJourney/            # Main application
│   │   ├── models.py         # Data models
│   │   ├── views.py          # View functions
│   │   ├── urls.py           # App URL patterns
│   │   ├── admin.py          # Admin configuration
│   │   ├── templates/       # HTML templates
│   │   │   ├── Index.html
│   │   │   └── aboutMe.html
│   │   └── static/           # Static files
│   └── db.sqlite3           # SQLite database
├── Pipfile                   # Python dependencies
└── README.md                # Project documentation
```

## Key Learning Outcomes

### **Django MVT Architecture**
- **Models:** Defined data structures for personal info and learning milestones
- **Views:** Created view functions to handle HTTP requests
- **Templates:** Designed responsive HTML templates with dynamic content

### **Database Integration**
- SQLite database for data persistence
- Model relationships and data validation
- Admin interface for content management

### **Web Development Skills**
- HTML5 and CSS3 for modern styling
- Django template language for dynamic content
- URL routing and navigation
- Responsive web design

### **Code Quality**
- Comprehensive code documentation
- Clean, readable code structure
- Proper error handling
- Professional development practices

## Screenshots

### Admin Interface
*[Screenshots of admin interface will be added here]*

### Website Pages
*[Screenshots of website pages will be added here]*

## Future Enhancements

- User authentication system
- Comment system for learning milestones
- Image upload functionality
- Advanced styling with CSS frameworks
- API endpoints for mobile app integration

## Author

**Sonam Choden**  
Student ID: 08230193  
Email: [your.email@example.com]  
Course: Web Application Development  

## License

This project is created for educational purposes as part of Lab 04 - Django MVT Architecture.

---

*This project demonstrates proficiency in Django web development, MVT architecture, and modern web design principles.*
