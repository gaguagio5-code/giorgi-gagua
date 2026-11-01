class MovieTicket:
    cinema_name = "Rustaveli Cinema"
    total_tickets_sold = 0
    def __init__(self, movie_title, seat_number, price):
        self.movie_title = movie_title
        self.seat_number = seat_number
        self.price = price
        MovieTicket.total_tickets_sold += 1
ticket1 = MovieTicket("Inception", "A1", 10.0)
ticket2 = MovieTicket("The Matrix", "B2", 12.0)
ticket3 = MovieTicket("Interstellar", "C3", 15.0)

for ticket in [ticket1, ticket2, ticket3]:
    print(f"Movie: {ticket.movie_title}, Seat: {ticket.seat_number}, Price: ${ticket.price:.2f}")

print(f"Total tickets sold: {MovieTicket.total_tickets_sold}")