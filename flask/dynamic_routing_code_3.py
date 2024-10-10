from flask import Flask

app = Flask(__name__)

# A dictionary to store book details by their IDs
systems = {
    mahalwari: {'name': 'mahalwari system', 'information': 'The Mahalwari system was introduced by Holt Mackenzie in 1822 and it was reviewed under Lord William Bentinck in 1833.
This system was introduced in North-West Frontier, Agra, Central Province, Gangetic Valley, Punjab, etc.
This had elements of both the Zamindari and the Ryotwari systems.
This system divided the land into Mahals. Sometimes, a Mahal was constituted by one or more villages.
The tax was assessed on the Mahal.
Each individual farmer gave his share.
Here also, ownership rights were with the peasants.
Revenue was collected by the village headman or village leaders.
It introduced the concept of average rents for different soil classes.
The state share of the revenue was 66% of the rental value. The settlement was agreed upon for 30 years.
This system was called the Modified Zamindari system because the village headman virtually became a Zamindar.'},
    ryotwari: {'name': 'ryotwari system', 'information': 'This system of land revenue was instituted in the late 18th century by Sir Thomas Munro, Governor of Madras in 1820.
This was practised in the Madras and Bombay areas, as well as Assam and Coorg provinces.
In this system, the peasants or cultivators were regarded as the owners of the land. They had ownership rights, could sell, mortgage or gift the land.
The taxes were directly collected by the government from the peasants.
The rates were 50% in dryland and 60% in the wetland.
The rates were high and unlike the Permanent System, they were open to being increased.
If they failed to pay the taxes, they were evicted by the government.
Ryot means peasant cultivators.
Here there were no middlemen as in the Zamindari system. But, since high taxes had to be paid only in cash (no option of paying in kind as before the British) the problem of moneylenders came into the show. They further burdened the peasants with heavy interests.'},
    permanent: {'name': 'permanent settlement', 'information': ''},
}

@app.route('/')
def home():
    return "Welcome to our bookstore!"

@app.route('/books/<int:book_id>')
def book_details(book_id):
    if book_id in books:
        book = books[book_id]
        title = book['title']
        author = book['author']
        return f"Displaying details for Book {book_id}: {title} by {author}"
    else:
        return "Book not found"