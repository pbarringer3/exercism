from datetime import timedelta


def add_gigasecond(birth_date):
    return birth_date + timedelta(days=1000000000/(60*60*24.0))
