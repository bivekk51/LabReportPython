def display_book_info(title,author,year):
    print(f"Title:{title}")
    print(f"Author:{author}")
    print(f"Year:{year}")
book_info={
    "title":"Python Programming",
    "author":"John Doe",
    "year":2021
}
display_book_info(**book_info)