
from amazon.api import AmazonAPI

amazon=AmazonAPI("AKIAI6DA7AZ35GPPONJQ", "lngMtLZjOI+k3zrmGqXeck5cyuNJXoMnbyIhyI8Q", "hat07c-20")
product = amazon.lookup(ItemId='B00EOE0WKQ')
product.title
