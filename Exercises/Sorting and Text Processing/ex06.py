votes = [
    ('Alice', 'French', 'Amélie'),
    ('Bob', 'French', 'Les Choristes'),
    ('Charlie', 'French', 'Amélie'),
    ('Alice', 'English', 'Inception'),
    ('Bob', 'English', 'Inception'),
    ('Charlie', 'English', 'The Matrix'),
    ('Alice', 'History', 'The Pianist'),
    ('Bob', 'History', 'The Pianist'),
    ('Charlie', 'History', 'Jojo Rabbit')
]

results = {}

for student, subject, movie in votes:
    if subject not in results:
        results[subject] = {}
    if movie not in results[subject]:
        results[subject][movie] = 0
    results[subject][movie] += 1

print("Results: ")
for subject in results:
    print(f"{subject}:")
    for movie in results[subject]:
        print(f" {movie} : {results[subject][movie]} votes")

print("Winner: ")
for subject, movie_votes in results.items():
    winner = max(movie_votes.items(), key=lambda x: x[1])
    print(f"{subject}: {winner[0]} ({winner[1]} votes)")


purchases = [
    ('Alice', 'snacks', 'chips'),
    ('Bob', 'snacks', 'chocolate'),
    ('Alice', 'snacks', 'chips'),
    ('Charlie', 'drinks', 'soda'),
    ('Alice', 'drinks', 'juice'),
    ('Bob', 'drinks', 'juice'),
    ('Charlie', 'snacks', 'chocolate'),
    ('Charlie', 'snacks', 'chips'),
    ('Alice', 'drinks', 'soda')
]

client_data = {}

for client, category, product in purchases:
    if client not in client_data:
        client_data[client] = {}
    if category not in client_data[client]:
        client_data[client][category] = {}
    if product not in client_data[client][category]:
        client_data[client][category][product] = 0
    client_data[client][category][product] += 1


print("purchases :")
for client in client_data:
    print(f"\nClient : {client}")
    for category in client_data[client]:
        print(f"  Catégorie : {category}")
        for product in client_data[client][category]:
            count = client_data[client][category][product]
            print(f"    {product} : {count} fois")


print("\nFavorite :")
for client, categories in client_data.items():
    product_counter = {}
    for products in categories.values():
        for product, count in products.items():
            product_counter[product] = product_counter.get(product, 0) + count
    favorite = max(product_counter.items(), key=lambda x: x[1])
    print(f"{client} : {favorite[0]} ({favorite[1]} fois)")