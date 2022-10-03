"""Restaurant rating lister."""


scores_file = open("scores.txt")


def make_restaurant_ratings_dict(scores_file):
    """"Returns a list of tuples (restaurant_name, restaurant_rating)"""
    
    restaurant_ratings = {}
    scores_file = open(scores_file)

    for line in scores_file:
        restaurant_name, restaurant_rating = line.strip().split(":")
        restaurant_ratings[restaurant_name] = restaurant_rating

    # print(restaurant_ratings.items())

    return restaurant_ratings

print(make_restaurant_ratings_dict("scores.txt"))
ratings = make_restaurant_ratings_dict("scores.txt")
sorted_restaurant_ratings = sorted(ratings.items())

print(sorted_restaurant_ratings)
print(type(sorted_restaurant_ratings))
for tup in sorted_restaurant_ratings:
    restaurant_name = tup[0]
    restaurant_rating = tup[1]
    print(f'{restaurant_name} is rated at {restaurant_rating}.')

user_restaurant = input("Restaurant name: ")
user_restaurant_rating = input("Restaurant rating: ")
while user_restaurant_rating is not int:
       input("Restaurant rating: ") # This does not work yet! 
[user_restaurant] = user_restaurant_rating
