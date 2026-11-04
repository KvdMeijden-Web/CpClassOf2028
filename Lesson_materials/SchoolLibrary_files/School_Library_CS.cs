
#nullable enable
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.Json;
using System.Text.Json.Serialization;

class Book
{
    [JsonPropertyName("title")]
    public string Title { get; set; } = "";

    [JsonPropertyName("borrowed_by")]
    public string? BorrowedBy { get; set; }
}

class Program
{
    static readonly string FilePath =
        Path.Combine(Directory.GetCurrentDirectory(), "books.json");

    static Dictionary<string, Book> books = new Dictionary<string, Book>();

    static string Input(string prompt)
    {
        Console.Write(prompt);
        return (Console.ReadLine() ?? "").Trim();
    }

    static Dictionary<string, Book> LoadBooks()
    {
        if (!File.Exists(FilePath))
        {
            Console.WriteLine("No books.json found. Creating a new library.");
            return new Dictionary<string, Book>();
        }

        string json = File.ReadAllText(FilePath);

        return JsonSerializer.Deserialize<Dictionary<string, Book>>(json)
            ?? throw new InvalidDataException("Invalid book data.");
    }

    static void SaveBooks()
    {
        string json = JsonSerializer.Serialize(books, new JsonSerializerOptions
        {
            WriteIndented = true
        });

        File.WriteAllText(FilePath, json);
    }

    static void ShowBooks()
    {
        Console.WriteLine("\n--- LIBRARY BOOKS ---");

        if (books.Count == 0)
        {
            Console.WriteLine("No books in the library.");
            return;
        }

        foreach (var entry in books)
        {
            string bookId = entry.Key;
            Book book = entry.Value;

            string status = book.BorrowedBy is null
                ? "Available"
                : "Borrowed by " + book.BorrowedBy;

            Console.WriteLine($"{bookId} - {book.Title} - {status}");
        }
    }

    static void AddBook()
    {
        string title = Input("Book title: ");

        if (title == "")
        {
            Console.WriteLine("Title cannot be empty.");
            return;
        }

        int nextId = books.Keys
            .Select(id => int.TryParse(id, out int number) ? number : 0)
            .DefaultIfEmpty(0)
            .Max() + 1;

        string bookId = nextId.ToString();

        books[bookId] = new Book
        {
            Title = title,
            BorrowedBy = null
        };

        SaveBooks();
        Console.WriteLine("Book added!");
    }

    static void BorrowBook()
    {
        ShowBooks();

        string bookId = Input("Book ID: ");

        if (!books.ContainsKey(bookId))
        {
            Console.WriteLine("Book does not exist.");
        }
        else if (books[bookId].BorrowedBy is not null)
        {
            Console.WriteLine("Book is already borrowed.");
        }
        else
        {
            string name = Input("Student name: ");

            if (name == "")
            {
                Console.WriteLine("Name cannot be empty.");
                return;
            }

            books[bookId].BorrowedBy = name;
            SaveBooks();

            Console.WriteLine("Book borrowed!");
        }
    }

    static void ReturnBook()
    {
        ShowBooks();

        string bookId = Input("Book ID: ");

        if (!books.ContainsKey(bookId))
        {
            Console.WriteLine("Book does not exist.");
        }
        else if (books[bookId].BorrowedBy is null)
        {
            Console.WriteLine("Book is not borrowed.");
        }
        else
        {
            books[bookId].BorrowedBy = null;
            SaveBooks();

            Console.WriteLine("Book returned!");
        }
    }

    static void MainMenu()
    {
        while (true)
        {
            Console.WriteLine("\n--- LIBRARY MENU ---");
            Console.WriteLine("1. Show books");
            Console.WriteLine("2. Add book");
            Console.WriteLine("3. Borrow book");
            Console.WriteLine("4. Return book");
            Console.WriteLine("5. Exit");

            string choice = Input("Choose an option: ");

            switch (choice)
            {
                case "1":
                    ShowBooks();
                    break;

                case "2":
                    AddBook();
                    break;

                case "3":
                    BorrowBook();
                    break;

                case "4":
                    ReturnBook();
                    break;

                case "5":
                    Console.WriteLine("Goodbye!");
                    return;

                default:
                    Console.WriteLine("Invalid option.");
                    break;
            }
        }
    }

    static void Main()
    {
        try
        {
            books = LoadBooks();
        }
        catch (Exception ex) when (
            ex is IOException ||
            ex is JsonException ||
            ex is UnauthorizedAccessException)
        {
            Console.WriteLine("Could not load books: " + ex.Message);
            return;
        }

        MainMenu();
    }
}
