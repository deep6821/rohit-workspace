from pipelines.dataload import process_data
from pipelines.prepare import preprocess_data


class Main:
    def main(self):
        process_data()
        preprocess_data()


if __name__ == "__main__":
    Main().main()
