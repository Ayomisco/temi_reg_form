# Temi Registration Form

Welcome to the Temi Registration Form project! This is a Django web application that allows users to submit their registration details through a form. The submitted data is stored in a SQL Server database.

## Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

Before running the project, ensure you have the following installed:

- Python (version 3.6 or higher)
- Django
- SQL Server (or another database supported by Django)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Ayomisco/temi_reg_form.git
   ```

2.  cd temi_reg_form

    ```bash
   cd temi_reg_form

   ```

3. Install the required Python packages:

```bash
   pip install -r requirements.txt

   ```
4. Run the Django development server:

```bash
   python manage.py runserver


   ```

5. Access the registration form in your web browser at 
``` http://localhost:8000/user-form/. ``` Fill in the required details and submit the form.

6. You can view the submitted data in the Django admin interface at ```http://localhost:8000/admin/.```

7. Create your custom admin details using the below command
``` python manage.py createsuperuser```