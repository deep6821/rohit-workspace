"""
Kafka Producer Utility

This module provides functions for producing messages to a Kafka topic.
"""
import json
from confluent_kafka import Producer

# Create Producer instance
producer = Producer({'bootstrap.servers': 'localhost:9092'})

# Define your payload
payload = {
    "name": "French Onion Soup Stuffed Mushrooms",
    "ingredients": "2 Tablespoons Butter\n2 whole Large Onions, Halved And Sliced Thin\n1/4 cup Beef Broth\n7 dashes Worcestershire Sauce\n Splash Of Red Or White Wine\n1/2 cup Grated Gruyere Cheese (can Use Swiss)\n Kosher Salt\n24 whole White Or Crimini Mushrooms, Washed And Stems Removed\n Minced Parsley",
    "url": "http://thepioneerwoman.com/cooking/2010/11/french-onion-soup-stuffed-mushrooms/",
    "image": "http://static.thepioneerwoman.com/cooking/files/2010/11/5200405868_e86da8e6e8_o.jpg",
    "cookTime": "PT30M",
    "recipeYield": "8",
    "datePublished": "2010-11-23",
    "prepTime": "PT20M",
    "description": "Important note: this recipe has absolutely nothing to do with Thanksgiving.     I'm so glad I got that out. I feel cleansed! ..."
}

# Serialize payload to JSON
message_value = json.dumps(payload)
# Produce message to topic
TOPIC = 'quickstart-events'
producer.produce(TOPIC, value=message_value)

# Produce message to topic
# message = "This is test event"
# TOPIC = 'quickstart-events'
# producer.produce(TOPIC, value=message)

# Flush messages
producer.flush()
