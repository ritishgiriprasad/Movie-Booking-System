# 🎬 Movie Booking System

## Project Overview

This repository contains the source code for our **Movie Booking System**, developed in **Python** with a **MySQL** backend using **PyMySQL** for database connectivity.

The goal is to build a fully functional application that allows users to browse movies, view show timings, book tickets, and manage bookings while providing an admin interface to manage the system.

---

# Current Status

* ✅ Database schema completed
* 🔄 Python backend under development
* ⏳ User interface to be implemented

---

# Tech Stack

* **Language:** Python 3
* **Database:** MySQL
* **Database Connector:** PyMySQL
* **Version Control:** Git & GitHub

---

# Planned Repository Structure

```text
movie-booking-system/
│
├── README.md                 # Project overview and documentation
├── requirements.txt          # Python dependencies
├── .gitignore
│
├── database/
│   └── schema.sql            # Database schema
│
├── src/
│   ├── main.py               # Entry point of the application
│   │
│   ├── config.py             # Database configuration
│   ├── db.py                 # PyMySQL connection setup
│   │
│   ├── auth.py               # User/Admin login & registration
│   ├── movies.py             # Movie-related operations
│   ├── shows.py              # Show scheduling
│   ├── booking.py            # Ticket booking logic
│   ├── payment.py            # Payment handling
│   ├── admin.py              # Admin functions
│   │
│   └── utils.py              # Helper functions
│
└── docs/                     # Documentation (optional)
```

---

# Module Responsibilities

### `database/`

Contains the SQL schema used to create the database.

### `config.py`

Stores database configuration such as host, username, password, and database name.

### `db.py`

Creates and manages the PyMySQL database connection.

### `auth.py`

Handles:

* User registration
* User login
* Admin login

### `movies.py`

Handles:

* View movies
* Add movies
* Update movies
* Delete movies

### `shows.py`

Handles:

* Add shows
* Update show timings
* View available shows

### `booking.py`

Handles:

* Book tickets
* Cancel bookings
* View booking history
* Seat availability checks

### `payment.py`

Handles:

* Recording payment details
* Payment status updates

### `admin.py`

Contains administrator-specific operations and controls.

### `utils.py`

Reusable helper functions shared across multiple modules.

---

# Development Plan

### Phase 1

* [x] Design database
* [ ] Connect Python to MySQL
* [ ] Test database connection

### Phase 2

* [ ] User authentication
* [ ] Movie management
* [ ] Show management

### Phase 3

* [ ] Booking system
* [ ] Payment module
* [ ] Booking history

### Phase 4

* [ ] Testing
* [ ] Bug fixes
* [ ] Documentation

---

# Notes

* Keep functions modular.
* Avoid writing SQL queries in multiple places—reuse functions where possible.
* Commit changes frequently with meaningful commit messages.
* Update this README if the project structure changes.
