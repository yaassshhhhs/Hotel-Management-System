# Hotel Lodge Management System

## Overview
The **Hotel Lodge Management System** is a Python-based desktop application designed to simplify day-to-day hotel operations. It allows staff to register guests, manage room bookings, track room availability, generate bills, and perform guest checkouts efficiently. Built using Tkinter and a modular Python architecture, it demonstrates practical software development principles such as separation of concerns, GUI programming, input validation, and maintainability.

## Features
### ✔ Guest Registration & Booking  
- Enter guest name, phone number, room type, and number of nights  
- Auto-calculates check-in and check-out dates  
- Input validation to prevent incorrect data  
- Prevents overbooking by checking room availability  

### ✔ Room Inventory Management  
- Tracks available rooms for Single, Double, and Suite  
- Updates room count on booking and checkout  

### ✔ Billing  
- Calculates bill using room type and nights stayed  
- Displays a formatted bill when a guest is selected  

### ✔ Guest Checkout  
- Removes guest from active list  
- Restores room availability  

### ✔ GUI Interface  
- Clean Tkinter interface  
- Table view of current guests  
- Real-time bill display  

## Project Structure


```text
hotel-management-system/
├── README.md
├── statement.md
├── src/
│   ├── main.py
│   └── hotel_management/
│       ├── __init__.py
│       ├── models.py
│       ├── storage.py
│       ├── validation.py
│       ├── booking.py
│       ├── billing.py
│       └── ui.py
├── tests/
│   └── test_validation.py
└── docs/
    └── Project_Report.md

```



## Installation
### Requirements
- Python **3.8+**  
- No external libraries required  

### Steps  
1. Download or clone the project  
2. (Optional) Create a virtual environment:  



3. Navigate to the `src` folder and run:  



## How to Use
1. Enter guest details in the **Guest Registration** section  
2. Click **Book Room** to create a booking  
3. View all active guests in the **Current Guests** table  
4. Select a guest to view their bill in the **Billing** section  
5. Click **Check Out Guest** to complete checkout and free the room  

## Module Description
### `models.py`
Defines the `Guest` dataclass, room types, room rates, and default availability.

### `storage.py`
Handles in-memory storage of all guest bookings and room inventory.

### `validation.py`
Validates phone numbers and nights; raises errors for incorrect inputs.

### `booking.py`
Contains logic for booking guests and checking out.

### `billing.py`
Computes total bill and returns formatted bill text.

### `ui.py`
Tkinter-based GUI that integrates all modules and handles UI events.

### `main.py`
Application entry point.

## Testing
Unit tests ensure validation functions behave correctly.  
Run tests using:




## Design Decisions
- Tkinter chosen for zero external dependencies  
- Modular architecture increases readability and maintainability  
- In-memory storage used for simplicity and academic demonstration  
- Separation of UI, logic, and storage allows future extension  

## Future Improvements
- Add SQLite database support  
- Generate downloadable PDF invoices  
- Add search and filter options for guests  
- Implement role-based login system  
- Add reports: daily revenue, occupancy chart  

## Limitations
- No persistent storage (data resets after program closes)  
- Not intended for multi-user systems  
- Basic billing (no taxes or extra services)

## Author
**Yash Pratap Singh**  
**25MIM10193**

Hotel Lodge Management System Project  

---

