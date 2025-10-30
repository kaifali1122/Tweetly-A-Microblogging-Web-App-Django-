# ChaiHeadQ - Django Tweet Application

A Twitter-like social media application built with Django that allows users to create, edit, delete, and view tweets with image uploads.

## Features

- User authentication (login, register, logout)
- Create tweets with text and images
- View all tweets in a card-based layout
- Edit and delete own tweets
- User-specific tweet management
- Responsive design with Bootstrap

## Project Structure

```
chaiheadq/
├── chaiheadq/                    # Main project configuration
│   ├── settings.py               # Django settings
│   ├── urls.py                   # Main URL routing
│   └── views.py                  # Project-level views
├── tweet/                        # Tweet application
│   ├── models.py                 # Database models
│   ├── views.py                  # View functions
│   ├── forms.py                  # Django forms
│   ├── urls.py                   # App URL patterns
│   └── templates/                # App templates
├── templates/                    # Global templates
│   ├── registration/             # Auth templates
│   └── layout.html               # Base template
├── media/                        # User uploaded files
├── static/                       # Static files (CSS, JS)
└── db.sqlite3                    # SQLite database
```

## Models

### Tweet Model (`tweet/models.py`)
```python
class tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=240)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

## Views and Functionality

### Authentication Views

#### User Registration (`views.py`)
- **URL**: `/register/`
- **Function**: `register(request)`
- **Template**: `registration/register.html`
- **Purpose**: Handles user registration with custom form
- **Flow**: 
  1. GET: Display registration form
  2. POST: Validate form, create user, auto-login, redirect to tweet list

#### User Login (`views.py`)
- **URL**: `/login/`
- **Function**: `user_login(request)`
- **Template**: `registration/login.html`
- **Purpose**: Handles user authentication
- **Flow**:
  1. GET: Display login form
  2. POST: Authenticate user, login, redirect to tweet list

### Tweet Management Views

#### Tweet List (`views.py`)
- **URL**: `/` (root)
- **Function**: `tweet_list(request)`
- **Template**: `tweet_list.html`
- **Purpose**: Display all tweets in chronological order
- **Features**:
  - Shows all tweets with user info and timestamps
  - Displays tweet images if uploaded
  - Shows edit/delete buttons only for tweet owner
  - Responsive card-based layout

#### Create Tweet (`views.py`)
- **URL**: `/create/`
- **Function**: `tweet_created(request)`
- **Template**: `tweet_form.html`
- **Decorator**: `@login_required`
- **Purpose**: Create new tweets
- **Flow**:
  1. GET: Display empty tweet form
  2. POST: Validate form, associate with current user, save, redirect to list
- **Authentication**: Redirects to login if user not authenticated

#### Edit Tweet (`views.py`)
- **URL**: `/<int:tweet_id>/edit/`
- **Function**: `tweet_edit(request, tweet_id)`
- **Template**: `tweet_form.html`
- **Decorator**: `@login_required`
- **Purpose**: Edit existing tweets
- **Security**: Only tweet owner can edit (enforced by `user=request.user` filter)
- **Flow**:
  1. GET: Pre-populate form with existing tweet data
  2. POST: Update tweet, redirect to list

#### Delete Tweet (`views.py`)
- **URL**: `/<int:tweet_id>/delete/`
- **Function**: `tweet_delete(request, tweet_id)`
- **Template**: `tweet_confirm_delete.html`
- **Decorator**: `@login_required`
- **Purpose**: Delete tweets with confirmation
- **Security**: Only tweet owner can delete
- **Flow**:
  1. GET: Show confirmation page
  2. POST: Delete tweet, redirect to list

## Forms (`tweet/forms.py`)

### TweetForm
- **Fields**: `text`, `photo`
- **Widgets**: Custom styling with Bootstrap classes
- **Purpose**: Handle tweet creation and editing

### UserRegistrationForm
- **Inherits**: Django's `UserCreationForm`
- **Fields**: `username`, `email`, `password1`, `password2`
- **Purpose**: User registration with email field

## URL Routing

### Main URLs (`chaiheadq/urls.py`)
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tweet.urls')),
]
```

### App URLs (`tweet/urls.py`)
```python
urlpatterns = [
    path("", views.tweet_list, name='tweet_list'),
    path("create/", views.tweet_created, name='tweet_create'),
    path("<int:tweet_id>/edit/", views.tweet_edit, name='tweet_edit'),
    path("<int:tweet_id>/delete/", views.tweet_delete, name='tweet_delete'),
    path("login/", views.user_login, name='login'),
]
```

## Templates

### Base Template (`templates/layout.html`)
- Bootstrap 5 integration
- Navigation bar with auth status
- Common styling and scripts

### Tweet List (`tweet/templates/tweet_list.html`)
- Extends base template
- Card-based responsive layout
- Conditional edit/delete buttons
- Image display support

### Tweet Form (`tweet/templates/tweet_form.html`)
- Form for creating/editing tweets
- File upload support for images
- CSRF protection

### Authentication Templates (`templates/registration/`)
- `login.html`: User login form
- `register.html`: User registration form
- `logged_out.html`: Logout confirmation

## Authentication & Security

### Login Required Decorator
- Applied to: `tweet_created`, `tweet_edit`, `tweet_delete`
- **Behavior**: Redirects unauthenticated users to login page
- **Settings**: `LOGIN_URL = 'login'` in `settings.py`

### User Authorization
- Users can only edit/delete their own tweets
- Enforced by filtering: `get_object_or_404(tweet, pk=tweet_id, user=request.user)`

### CSRF Protection
- All forms include `{% csrf_token %}`
- Prevents cross-site request forgery attacks

## Database Configuration

### SQLite Database
- **File**: `db.sqlite3`
- **Location**: Project root
- **Purpose**: Development database

### Media Files
- **URL**: `/media/`
- **Path**: `media/photos/`
- **Purpose**: Store uploaded tweet images

## Settings Configuration (`settings.py`)

### Key Settings
```python
# Authentication
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'tweet_list'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Static files
STATIC_URL = "static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
```

## Installation & Setup

1. **Clone the repository**
2. **Create virtual environment**:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirement.txt
   ```
4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```
5. **Create superuser**:
   ```bash
   python manage.py createsuperuser
   ```
6. **Run development server**:
   ```bash
   python manage.py runserver
   ```

## Usage Flow

### For New Users
1. Visit `/register/` to create account
2. Auto-login after registration
3. Redirected to tweet list

### For Existing Users
1. Visit `/login/` to authenticate
2. Redirected to tweet list after login

### Tweet Management
1. **View Tweets**: Visit `/` (root) to see all tweets
2. **Create Tweet**: Click "Create a Tweet" button (requires login)
3. **Edit Tweet**: Click "Edit" on your own tweets
4. **Delete Tweet**: Click "Delete" on your own tweets (with confirmation)

### Security Features
- Unauthenticated users redirected to login for protected actions
- Users can only modify their own tweets
- CSRF protection on all forms
- Secure file upload handling

## Dependencies

- Django 5.2.7
- Pillow (for image handling)
- Bootstrap 5 (via CDN)

This application demonstrates a complete Django web application with user authentication, CRUD operations, file uploads, and responsive design.