from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
    movie: str,
    customers: list,
    hall_number: int,
    cleaner: str,    
) -> None:    
    result_customers = [Customer(name=customer["name"], food=customer["food"]) for customer in customers]
    for c in result_customers:
        CinemaBar.sell_product(product=c.food, customer=c)
    cleaning_staff = Cleaner(name=cleaner)
    hall = CinemaHall(hall_number)
    hall.movie_session(
        movie_name=movie,
        customers=result_customers,
        cleaning_staff=cleaning_staff
    )
