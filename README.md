# LJ Transport Services Web Platform

[](https://ljtransport.pythonanywhere.com/)
[](https://www.python.org/)

A modern, responsive web application developed for **LJ Transport Services**, a company specializing in bus rentals, haulage, and logistics solutions. This platform serves as the digital storefront for the business, allowing clients to explore services, view the vehicle fleet, and submit booking inquiries.

The live application is currently deployed at: **[https://ljtransport.pythonanywhere.com/](https://ljtransport.pythonanywhere.com/)**

-----

## 📖 Table of Contents

  * [About the Project](https://www.google.com/search?q=%23about-the-project)
  * [Key Features](https://www.google.com/search?q=%23key-features)
  * [Screenshots](https://www.google.com/search?q=%23screenshots)
  * [Technologies Used](https://www.google.com/search?q=%23technologies-used)
  * [Local Development Setup](https://www.google.com/search?q=%23local-development-setup)
  * [Usage](https://www.google.com/search?q=%23usage)
  * [Future Roadmap](https://www.google.com/search?q=%23future-roadmap)
  * [Contact](https://www.google.com/search?q=%23contact)

-----

## 🧐 About the Project

LJ Transport Services needed a reliable online presence to showcase their diverse transportation offerings, ranging from corporate bus rentals to heavy-duty haulage.

This web application was built to solve the problem of manual booking inquiries and lack of digital visibility. It provides potential customers with detailed information about the company's fleet and services, building trust and streamlining the initial contact process through integrated inquiry forms.

-----

## ✨ Key Features

  * **Service Showcase:** Detailed breakdowns of core offerings: Bus Rentals (Corporate/Social), Haulage & Logistics, and Driver-for-Hire services.
  * **Fleet Gallery:** A visual catalog of available vehicles, including cars, vans, buses, and trucks, allowing clients to see what they are booking.
  * **Booking Inquiry System:** Integrated contact forms that allow users to specify their needs (service type, date) and send inquiries directly to the administration.
  * **Responsive Design:** Fully optimized interface that provides an excellent user experience on mobile devices, tablets, and desktops.
  * **Company Information:** Sections for "About Us" and clear contact details to establish trust and reliability.

-----

## 📸 Screenshots

*(Please add actual screenshots of your website here to make the README visually appealing. You can drag and drop images into GitHub issues to generate URLs for them.)*

| Home Page |

<img width="1680" height="895" alt="Screenshot 2025-11-20 at 6 00 56 PM" src="https://github.com/user-attachments/assets/7d7809c1-7210-41ef-b972-0771aaec44de" />

| Services Page | 

<img width="1674" height="887" alt="Screenshot 2025-11-20 at 5 58 24 PM" src="https://github.com/user-attachments/assets/483f90c8-d468-47c2-b52c-1157145a0f8a" />
| Contact Form |


-----

## 🛠️ Technologies Used

This project was built using the following technologies:

**Backend:**

  * [Python 3.x](https://www.python.org/)
  * **[INSERT YOUR FRAMEWORK HERE: e.g., Django 4.x OR Flask]** - The core web framework used for routing and backend logic.
  * **[INSERT YOUR DATABASE HERE: e.g., SQLite (development), PostgreSQL (production)]**

**Frontend:**

  * HTML5 & CSS3
  * JavaScript
  * **[INSERT CSS FRAMEWORK IF USED: e.g., Bootstrap 5 / Tailwind CSS]** - Used for responsive layout and styling components.

**Deployment:**

  * [PythonAnywhere](https://www.pythonanywhere.com/) - Hosting platform.

-----

## 💻 Local Development Setup

To run this project locally on your machine, follow these steps:

### Prerequisites

  * Python 3.8 or higher installed.
  * Git installed.

### Installation Steps

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/[your-username]/[your-repo-name].git
    cd [your-repo-name]
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up Environment Variables (If applicable):**

      * *Create a `.env` file in the root directory and add necessary secrets (database URLs, secret keys, email host users, etc.). See `.env.example` for reference.*

5.  **Database Migration:**

    ```bash
    # If using Django:
    python manage.py migrate
    # python manage.py createsuperuser (optional, if you have an admin panel)

    # If using Flask (commands may vary based on your setup):
    # flask db upgrade
    ```

6.  **Run the development server:**

    ```bash
    # If using Django:
    python manage.py runserver

    # If using Flask:
    # flask run
    ```

7.  Access the application at `http://127.0.0.1:8000/` (or the port specified in your terminal).

-----

## 🚀 Future Roadmap

The following features are planned for future updates to enhance the platform:

  * **Admin Dashboard:** A secure backend for LJ Transport staff to manage incoming booking requests, update fleet availability, and edit site content.
  * **Real-time Availability Checker:** allowing users to see if specific vehicles are free on chosen dates.
  * **Customer Accounts:** allowing returning clients to view past bookings and save contact details.
  * **Integration with Maps API:** To show service area coverage dynamically.

-----

## 🤝 Contact

**LJ Transport Services**

  * **Live Website:** [ljtransport.pythonanywhere.com](https://ljtransport.pythonanywhere.com/)
  * **Developer GitHub:** [@YourUsername](https://github.com/QwuophyRain)
  * **Email:** senamqwuophy@gmail.com
