import datetime

class CodeTracker:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start_coding(self):
        if self.start_time is not None:
            print("Coding session already started.")
        else:
            self.start_time = datetime.datetime.now()
            print("Coding session started at", self.start_time)

    def stop_coding(self):
        if self.start_time is None:
            print("No coding session in progress.")
        else:
            self.end_time = datetime.datetime.now()
            duration = self.end_time - self.start_time
            print("Coding session stopped at", self.end_time)
            print("Total coding time:", duration)

if __name__ == "__main__":
    code_tracker = CodeTracker()

    while True:
        print("\nOptions:")
        print("1. Start Coding")
        print("2. Stop Coding")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            code_tracker.start_coding()
        elif choice == "2":
            code_tracker.stop_coding()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
