import csv

def main():
    filename = input()
    movie_data = {}
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        
        for row in reader:
            showtime, title, rating = row
            
            if title not in movie_data:
                movie_data[title] = {"rating": rating, "showtimes": []}

            movie_data[title]["showtimes"].append(showtime)

    for title, data in movie_data.items():
        title = title[:44]
        showtimes = " ".join(data["showtimes"])
        print(f"{title:<44} | {data['rating']:>5} | {showtimes}")

if __name__ == "__main__":
    main()
