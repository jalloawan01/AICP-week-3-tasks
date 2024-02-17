# AICP Week 3 Tasks

class Cow:
    def __init__(self, cow_id):
        self.cow_id = cow_id
        self.yields = []

    def record_yield(self, yield_amount):
        self.yields.append(yield_amount)

    def total_weekly_yield(self):
        return sum(self.yields)

    def average_weekly_yield(self):
        return round(sum(self.yields) / len(self.yields), 1) if len(self.yields) > 0 else 0


class Farm:
    def __init__(self):
        self.herd = []

    def add_cow(self, cow):
        self.herd.append(cow)

    def calculate_statistics(self):
        total_volume = sum(cow.total_weekly_yield() for cow in self.herd)
        total_cows = len(self.herd)

        average_yield = total_volume / total_cows if total_cows > 0 else 0
        return total_volume, average_yield

    def identify_most_productive_cow(self):
        most_productive_cow = max(self.herd, key=lambda x: x.total_weekly_yield(), default=None)
        return most_productive_cow.cow_id if most_productive_cow else None, most_productive_cow.total_weekly_yield()

    def identify_low_yield_cows(self):
        low_yield_cows = [cow.cow_id for cow in self.herd if cow.average_weekly_yield() < 12 and len(cow.yields) >= 4]
        return low_yield_cows


def main():
    farm = Farm()

    # Task 1: Record the yield
    herd_size = int(input("Enter the size of the herd: "))

    for _ in range(herd_size):
        cow_id = input("Enter cow's 3-digit identity code: ")
        cow = Cow(cow_id)
        for _ in range(14):  # Twice a day for 7 days
            yield_amount = float(input(f"Enter the milk yield for cow {cow_id}: "))
            cow.record_yield(yield_amount)
        farm.add_cow(cow)

    # Task 2: Calculate statistics
    total_volume, average_yield = farm.calculate_statistics()
    print(f"\n Total weekly volume of milk: {round(total_volume)} litres")
    print(f"\n Average yield per cow: {round(average_yield)} litres")

    # Task 3: Identify the most productive cow and low yield cows
    most_productive_cow_id, max_yield = farm.identify_most_productive_cow()
    print(f"\n Most productive cow: {most_productive_cow_id} with {max_yield} litres")

    low_yield_cows = farm.identify_low_yield_cows()
    if low_yield_cows:
        print("\n Cows with low yield (less than 12 litres for 4 or more days):", low_yield_cows,"\n")
    else:
        print("\n No cows with consistently low yield found.")


if __name__ == "__main__":
    main()






