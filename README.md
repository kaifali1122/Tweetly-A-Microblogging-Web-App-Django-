# Tweetly-A-Microblogging-Web-App-Django-
A Twitter-like platform built using Django where users can create, edit, and delete tweets with image uploads.  Includes authentication, user-specific dashboards, and a responsive card-based feed layout.

# 📸 PhotoHub – Django Photo Sharing App  

A simple yet powerful **photo-sharing web app** built using **Django**, where users can **upload, view, and manage photos** securely.  
This project helped me understand Django fundamentals like models, views, templates, static/media files, and authentication workflows.  

---

## 🚀 Features  

- 🧑‍💻 User Registration & Login (Django Authentication System)  
- 📤 Upload Photos with Captions  
- 🗂️ View All Photos in a Responsive Grid Layout  
- ✏️ Edit or Delete Own Uploads  
- 🧱 Modular Project Structure (apps, templates, static, media)  
- 🧾 Admin Panel for Easy Content Management  

---

## 🧰 Tech Stack  

| Component | Technology |
|------------|-------------|
| Backend | Django 5.x (Python 3) |
| Frontend | HTML, CSS, Bootstrap 5 |
| Database | SQLite3 |
| Hosting | Localhost / Future-ready for Render or PythonAnywhere |
| Tools | Git, VS Code |

---

## 🏗️ Project Structure  

PhotoHub/
│
├── photohub/             # 🔧 Main Django project folder (global settings & configs)
│ ├── init.py             # Makes folder a Python package
│ ├── settings.py         # ⚙️ Main configuration file (DB, static/media, installed apps)
│ ├── urls.py             # 🌐 Root URL mappings that connect apps to routes
│ ├── wsgi.py             # 🔌 For deployment (runs Django on web servers)
│ └── asgi.py             # ⚡ For async server support (optional)
│
├── photos/                        # 📸 Core app managing photos and related logic
│ ├── migrations/                  # 🗂️ Database schema migrations (auto-generated)
│ ├── templates/photos/            # 🖼️ HTML templates specific to the "photos" app
│ │ ├── photo_list.html            # 📜 Page showing all uploaded photos
│ │ ├── photo_form.html            # 📤 Page for uploading new photos
│ │ └── photo_delete.html          # 🗑️ Confirmation page for deleting a photo
│ ├── static/photos/               # 🎨 Static assets (CSS, JS, images) for photo app
│ ├── admin.py                     # 🧑‍💼 Registers Photo model in Django admin panel
│ ├── apps.py                      # ⚙️ App configuration file (auto-generated)
│ ├── forms.py                     # 📝 Defines form for photo upload (ModelForm)
│ ├── models.py                    # 🧱 Database structure for storing photo info
│ ├── urls.py                      # 🌍 App-level URL routes (photo_list, upload, delete)
│ └── views.py                     # 🧠 Logic for displaying, uploading, and deleting photos
│
├── templates/             # 🌐 Global HTML templates used across the project
│ ├── layout.html          # 🧩 Base HTML layout (Navbar + common structure)
│ └── registration/        # 🔑 Authentication templates
│ ├── login.html           # Login form page
│ └── register.html        # Signup form page
│
├── media/                        # 📂 Folder for user-uploaded photos
│
├── static/                       # 🌍 Global static files (CSS, JS)
│
├── db.sqlite3                    # 🗄️ SQLite database file
│
├── manage.py                     # ⚙️ Django’s command-line tool for managing a project
│
└── requirements.txt              # 📦 List of dependencies (Django etc.)
