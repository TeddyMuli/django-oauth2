# Django OAuth2 Example

This project is a basic example of how to implement OAuth2 authentication in a Django application. It demonstrates the use of a third-party OAuth2 provider (e.g., Google, GitHub) to authenticate users and access their protected resources.

## Project Structure

- `oauth2_app/`: This Django application handles the OAuth2 client-side logic, including initiating the authorization flow, handling callbacks, and exchanging authorization codes for access tokens.
- `oauth2_project/`: This is the main Django project directory, containing settings, URLs, and other project-wide configurations.
- `factory.py`: This file likely contains factory definitions for creating test data or mock objects.
- `db.sqlite3`: The default SQLite database file for the Django project.
- `manage.py`: Django's command-line utility for administrative tasks.
- `requirements.txt`: Lists the Python dependencies required for this project.

## Getting Started

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd django-oauth2-example
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```
   On macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a Superuser:
   ```bash
   python manage.py createsuperuser
   ```

### Configuration

1. **OAuth2 Provider Setup**:
 - You will need to register your application with an OAuth2 provider (e.g., Google Developers Console, GitHub Developer Settings) to obtain a Client ID and Client Secret.
 - Create a social application in django admin with the client id and client secret.
 - Ensure to uses the site as localhost.


### Running the Application

1. Start the Django development server:
   ```bash
   python manage.py runserver
   ```

2. Open your web browser and navigate to `http://127.0.0.1:8000/`.

3. You should see a link or button to initiate the OAuth2 authentication flow (e.g., "Login with Google").

## Usage

- **Login/Registration**: Users can log in or register using their chosen OAuth2 provider.
- **Access Protected Resources**: After successful authentication, the application can access user information or perform actions on behalf of the user, depending on the scopes requested during the authorization process.

## Technologies Used

- Django
- Python
- `django-oauth-toolkit`
