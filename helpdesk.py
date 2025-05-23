import sqlite3

# Connect to SQLite DB (creates one if it doesn't exist)
conn = sqlite3.connect("tickets.db")
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    status TEXT DEFAULT 'open'
)
''')
conn.commit()

def create_ticket():
    title = input("Enter ticket title: ")
    description = input("Enter ticket description: ")
    cursor.execute("INSERT INTO tickets (title, description) VALUES (?, ?)", (title, description))
    conn.commit()
    print("Ticket created successfully.")

def view_tickets():
    cursor.execute("SELECT * FROM tickets")
    tickets = cursor.fetchall()
    print("\n=== All Tickets ===")
    for t in tickets:
        print(f"ID: {t[0]} | Title: {t[1]} | Status: {t[3]}")
        print(f"Description: {t[2]}\n")

def update_ticket_status():
    ticket_id = input("Enter ticket ID to update: ")
    new_status = input("Enter new status (open, in progress, closed): ").lower()
    cursor.execute("UPDATE tickets SET status = ? WHERE id = ?", (new_status, ticket_id))
    conn.commit()
    print("Ticket status updated.")

def delete_ticket():
    ticket_id = input("Enter ticket ID to delete: ")
    cursor.execute("DELETE FROM tickets WHERE id = ?", (ticket_id,))
    conn.commit()
    print("Ticket deleted.")

def search_ticket():
    ticket_id = input("Enter ticket ID to search: ")
    cursor.execute("SELECT * FROM tickets WHERE id = ?", (ticket_id,))
    ticket = cursor.fetchone()
    if ticket:
        print(f"\nID: {ticket[0]} | Title: {ticket[1]} | Status: {ticket[3]}")
        print(f"Description: {ticket[2]}\n")
    else:
        print("Ticket not found.")

def show_menu():
    while True:
        print("\n=== Helpdesk Ticketing System ===")
        print("1. Create Ticket")
        print("2. View All Tickets")
        print("3. Search Ticket by ID")
        print("4. Update Ticket Status")
        print("5. Delete Ticket")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            create_ticket()
        elif choice == '2':
            view_tickets()
        elif choice == '3':
            search_ticket()
        elif choice == '4':
            update_ticket_status()
        elif choice == '5':
            delete_ticket()
        elif choice == '0':
            print("Exiting Helpdesk System.")
            break
        else:
            print("Invalid option. Try again.")
        input("Press Enter to continue...\n")

if __name__ == "__main__":
    show_menu()
    conn.close()
