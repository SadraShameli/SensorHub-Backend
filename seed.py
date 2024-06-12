import os

commands = [
    "python manage.py makemigrations api",
    "python manage.py migrate",
    "python manage.py migrate --run-syncdb",
    "python manage.py loaddata fixtures",
]


def main():
    print("Seeding database")

    for command in commands:
        os.system(command)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)