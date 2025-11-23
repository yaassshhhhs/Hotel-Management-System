import tkinter as tk
from tkinter import ttk, messagebox

from . import storage
from .booking import book_guest, checkout_guest, BookingError
from .billing import format_bill_text
from .models import ROOM_TYPES


def run_app() -> None:
    """Create and run the Tkinter GUI application."""
    root = tk.Tk()
    root.title("Hotel Lodge Management System")

    # ----------------- Guest Registration Frame -----------------
    reg_frame = tk.LabelFrame(root, text="Guest Registration", padx=10, pady=10)
    reg_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    tk.Label(reg_frame, text="Name").grid(row=0, column=0, sticky="w")
    entry_name = tk.Entry(reg_frame)
    entry_name.grid(row=0, column=1)

    tk.Label(reg_frame, text="Phone").grid(row=1, column=0, sticky="w")
    entry_phone = tk.Entry(reg_frame)
    entry_phone.grid(row=1, column=1)

    tk.Label(reg_frame, text="Room Type").grid(row=2, column=0, sticky="w")
    combo_room = ttk.Combobox(reg_frame, values=list(ROOM_TYPES), state="readonly")
    combo_room.grid(row=2, column=1)
    combo_room.current(0)

    tk.Label(reg_frame, text="Nights").grid(row=3, column=0, sticky="w")
    entry_nights = tk.Entry(reg_frame)
    entry_nights.grid(row=3, column=1)

    # ----------------- Guests List Frame -----------------
    list_frame = tk.LabelFrame(root, text="Current Guests", padx=10, pady=10)
    list_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    guest_table = ttk.Treeview(
        list_frame,
        columns=("Name", "Phone", "Room", "Nights", "CheckIn", "CheckOut"),
        show="headings",
        height=6,
    )
    for col in guest_table["columns"]:
        guest_table.heading(col, text=col)
    guest_table.grid(row=0, column=0, sticky="nsew")

    # Add scrollbar
    scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=guest_table.yview)
    guest_table.configure(yscrollcommand=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky="ns")

    # ----------------- Billing Frame -----------------
    bill_frame = tk.LabelFrame(root, text="Billing", padx=10, pady=10)
    bill_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

    label_bill = tk.Label(bill_frame, text="Select a guest above to see their bill.")
    label_bill.pack()

    # ----------------- Helper functions (GUI layer) -----------------
    def refresh_table():
        """Reload the guest table from storage."""
        for row in guest_table.get_children():
            guest_table.delete(row)
        for idx, guest in enumerate(storage.get_guests()):
            guest_table.insert(
                "",
                "end",
                iid=str(idx),
                values=(
                    guest.name,
                    guest.phone,
                    guest.room_type,
                    guest.nights,
                    guest.check_in.isoformat(),
                    guest.check_out.isoformat(),
                ),
            )

    def on_book_room():
        """Handle Book Room button click."""
        name = entry_name.get()
        phone = entry_phone.get()
        room_type = combo_room.get()
        nights_str = entry_nights.get()

        try:
            guest = book_guest(name, phone, room_type, nights_str)
        except (BookingError) as ex:
            messagebox.showerror("Booking Error", str(ex))
            return
        except Exception as ex:
            # Catch-all for unexpected errors
            messagebox.showerror("Unexpected Error", f"An unexpected error occurred: {ex}")
            return

        # Clear inputs on success
        entry_name.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
        entry_nights.delete(0, tk.END)
        combo_room.current(0)

        refresh_table()
        messagebox.showinfo("Success", f"Room booked for {guest.name}!")

    def on_checkout_guest():
        """Handle Check Out Guest button click."""
        selected = guest_table.selection()
        if not selected:
            messagebox.showwarning("Select Guest", "No guest selected.")
            return

        try:
            idx = int(selected[0])
        except ValueError:
            messagebox.showerror("Error", "Invalid guest selection.")
            return

        try:
            guest = checkout_guest(idx)
        except IndexError:
            messagebox.showerror("Error", "Selected guest no longer exists.")
            refresh_table()
            return

        refresh_table()
        label_bill.config(text="Select a guest above to see their bill.")
        messagebox.showinfo("Checked Out", f"{guest.name} has checked out.")

    def on_show_bill(event=None):
        """Update bill label when a guest is selected."""
        selected = guest_table.selection()
        if not selected:
            label_bill.config(text="Select a guest above to see their bill.")
            return

        try:
            idx = int(selected[0])
        except ValueError:
            label_bill.config(text="Select a valid guest to see their bill.")
            return

        guests = storage.get_guests()
        if idx < 0 or idx >= len(guests):
            label_bill.config(text="Select a valid guest to see their bill.")
            return

        guest = guests[idx]
        label_bill.config(text=format_bill_text(guest))

    # Buttons in list frame
    btn_checkout = tk.Button(list_frame, text="Check Out Guest", command=on_checkout_guest)
    btn_checkout.grid(row=1, column=0, pady=5, sticky="w")

    btn_book = tk.Button(reg_frame, text="Book Room", command=on_book_room)
    btn_book.grid(row=4, column=0, columnspan=2, pady=5)

    # Bind selection event for bill display
    guest_table.bind("<<TreeviewSelect>>", on_show_bill)

    # Start the GUI event loop
    root.mainloop()
