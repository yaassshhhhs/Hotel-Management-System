
---

## 3. `statement.md`

```markdown
# Problem Statement & Project Scope

## Problem Statement

Small hotels and lodges often manage bookings, room availability, and guest billing manually using paper registers or simple spreadsheets. This manual process is error-prone, time-consuming, and does not scale well as the number of guests increases.

There is a need for a simple, easy-to-use desktop application that helps hotel staff manage guest bookings, track room availability, and generate basic bills in a structured way.

---

## Scope of the Project

The scope of this project is to build a **desktop-based Hotel Lodge Management System** that supports:

- Guest registration and room booking
- Room inventory tracking (by room type)
- Simple billing for each booking
- Checkout operations that free up rooms

The project is designed for **single-system usage** at the front desk (no networking, no multi-user support) and uses **in-memory data storage** (no external database).

---

## Target Users

- Receptionists / front-desk staff of small hotels and lodges
- Students and educators who want to understand basic hotel management workflows using Python and Tkinter

---

## High-Level Features

1. **Guest Registration & Booking**
   - Capture guest details (name, phone)
   - Select room type and number of nights
   - Automatic check-in/check-out date calculation
   - Input validation and error messages

2. **Room Inventory Management**
   - Maintain available room counts for Single, Double, and Suite
   - Automatic adjustment of availability on booking and checkout
   - Prevent bookings when no rooms are available for a selected type

3. **Billing**
   - Calculate total bill based on room type and stay duration
   - Display bill summary for selected guest

4. **Checkout**
   - Remove guest on checkout
   - Release room back into available inventory

5. **User-Friendly GUI**
   - Intuitive Tkinter interface with labeled sections
   - Simple navigation and clear instructions/messages
