from cinema.bar import CinemaBar
from cinema.hall import CinemaHall
from people.customer import Customer
from people.cinema_staff import Cleaner


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    result_customers = [
        Customer(name=customer["name"], food=customer["food"])
        for customer in customers
    ]
    for customer in result_customers:
        CinemaBar.sell_product(product=customer.food, customer=customer.name)
    CinemaHall.movie_session(
        CinemaHall(hall_number),
        movie_name=movie,
        customers=result_customers,
        cleaning_staff=Cleaner(cleaner)
    )
