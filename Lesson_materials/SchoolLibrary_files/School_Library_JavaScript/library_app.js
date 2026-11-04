// Run this JavaScript in a browser console, or load it from an HTML script tag.
// The JavaScript below follows the structure of the Python version.
// Browser equivalents: prompt = input, alert = print,
// localStorage + JSON = saving and loading the book data.

const FILE = "school_library_books";
let books;

function load_books() {
    const saved = localStorage.getItem(FILE);
    if (saved !== null) {
        return JSON.parse(saved);
    }
    // Starter books for the first run.
    return {
        "1": { title: "The Hobbit", borrowed_by: null },
        "2": { title: "Matilda", borrowed_by: null },
        "3": { title: "The Hunger Games", borrowed_by: null }
    };
}

function save_books() {
    localStorage.setItem(FILE, JSON.stringify(books, null, 4));
}

function show_books() {
    let output = "--- LIBRARY BOOKS ---\n";
    for (const [book_id, book] of Object.entries(books)) {
        const status = book.borrowed_by === null
            ? "Available" : "Borrowed by " + book.borrowed_by;
        output += book_id + " - " + book.title + " - " + status + "\n";
    }
    alert(output);
}

function add_book() {
    const answer = prompt("Book title:");
    if (answer === null) return;
    const title = answer.trim();
    if (!title) {
        alert("Title cannot be empty.");
        return;
    }
    const book_id = String(Math.max(0, ...Object.keys(books).map(Number)) + 1);
    books[book_id] = { title: title, borrowed_by: null };
    save_books();
    alert("Book added!");
}

function borrow_book() {
    show_books();
    const answer = prompt("Book ID:");
    if (answer === null) return;
    const book_id = answer.trim();
    if (!Object.prototype.hasOwnProperty.call(books, book_id)) {
        alert("Book does not exist.");
    } else if (books[book_id].borrowed_by !== null) {
        alert("Book is already borrowed.");
    } else {
        const answer = prompt("Student name:");
        if (answer === null) return;
        const name = answer.trim();
        if (!name) {
            alert("Name cannot be empty.");
            return;
        }
        books[book_id].borrowed_by = name;
        save_books();
        alert("Book borrowed!");
    }
}

function return_book() {
    const answer = prompt("Book ID to return:");
    if (answer === null) return;
    const book_id = answer.trim();
    if (!Object.prototype.hasOwnProperty.call(books, book_id)) {
        alert("Book does not exist.");
    } else if (books[book_id].borrowed_by === null) {
        alert("Book was not borrowed.");
    } else {
        books[book_id].borrowed_by = null;
        save_books();
        alert("Book returned!");
    }
}

function search_book() {
    const answer = prompt("Search title:");
    if (answer === null) return;
    const query = answer.trim().toLowerCase();
    let found = false;
    let output = "";
    for (const [book_id, book] of Object.entries(books)) {
        if (book.title.toLowerCase().includes(query)) {
            output += book_id + " - " + book.title + "\n";
            found = true;
        }
    }
    alert(found ? output : "No books found.");
}

function main() {
    try {
        books = load_books();
        const actions = {
            "1": show_books, "2": add_book, "3": borrow_book,
            "4": return_book, "5": search_book
        };
        while (true) {
            const answer = prompt(
                "===== SCHOOL LIBRARY =====\n" +
                "1. Show all books\n2. Add a book\n3. Borrow a book\n" +
                "4. Return a book\n5. Search for a book\n6. Exit\n\nChoose 1-6:"
            );
            if (answer === null) break;
            const choice = answer.trim();
            if (choice === "6") {
                break;
            } else if (Object.prototype.hasOwnProperty.call(actions, choice)) {
                actions[choice]();
            } else {
                alert("Invalid option.");
            }
        }
    } catch (error) {
        alert("Could not load or save the books. Check that browser storage is allowed.\n" + error.message);
    }
}

