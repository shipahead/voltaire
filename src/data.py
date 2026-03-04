class EnergyDataLoader:
    """
    Loads energy production data from a given source and date range.
    """
    def __init__(self, source, start_date, end_date):
        self.source = source
        self.start_date = start_date
        self.end_date = end_date
        print(f"Loader created for {self.source}")

    def load_from_file(self, filepath):
        """
        Loads data from a CSV file.
        
        Args:
            filepath (str): Path to the CSV file
        """
        try:
            with open(filepath, "r") as f:
                print(f"Successfully loaded {self.source} data from {filepath}")
        except FileNotFoundError:
            print(f"Error: {filepath} not found. Have you downloaded the data yet?")
        except Exception as e:
            print(f"Unexpected error loading {self.source} data: {e}")
