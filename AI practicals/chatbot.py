# Levenshtein distance function (edit distance)
def levenshtein(str1, str2):
    len_str1 = len(str1) + 1
    len_str2 = len(str2) + 1

    # Create a distance matrix
    matrix = [[0] * len_str2 for _ in range(len_str1)]

    # Initialize the matrix
    for i in range(len_str1):
        matrix[i][0] = i
    for j in range(len_str2):
        matrix[0][j] = j

    # Fill the matrix
    for i in range(1, len_str1):
        for j in range(1, len_str2):
            cost = 0 if str1[i - 1] == str2[j - 1] else 1
            matrix[i][j] = min(matrix[i - 1][j] + 1,
                               matrix[i][j - 1] + 1,
                               matrix[i - 1][j - 1] + cost)

    return matrix[len_str1 - 1][len_str2 - 1]

# Function to find closest keyword from user input
def get_closest_match(user_input, keywords):
    closest_match = None
    min_distance = float('inf')

    for keyword in keywords:
        distance = levenshtein(user_input, keyword)
        if distance < min_distance:
            min_distance = distance
            closest_match = keyword

    return closest_match

# Dictionary with predefined responses
responses = {
    "greetings": ["hello", "hi", "hey", "greetings"],
    "order_status": ["order status", "check order", "order tracking", "order status query"],
    "cancel_order": ["cancel order", "cancel my order", "order cancel", "cancel my order"],
    "returns": ["return product", "return", "product return", "return item"],
    "payment": ["payment", "refund", "refund status", "payment query"],
    "delivery": ["delivery", "shipping", "shipping status", "track delivery"],
    "product_query": ["product", "availability", "stock", "product query"],
    "default": ["sorry", "help", "rephrase", "unclear"]
}

# Define responses for each query
response_messages = {
    "greetings": "Bot: Hello! How can I help you today?",
    "order_status": "Bot: To check your order status, please log into your account and go to 'My Orders'.",
    "cancel_order": "Bot: To cancel your order, visit 'My Orders' and click on 'Cancel' next to the item.",
    "returns": "Bot: You can return a product within 7 days of delivery. Go to 'My Orders' and click 'Return'.",
    "payment": "Bot: Refunds are processed within 3–5 business days to your original payment method.",
    "delivery": "Bot: Standard delivery takes 3–7 business days. You can track it from 'My Orders'.",
    "product_query": "Bot: Can you please specify the product name? I can check if it's in stock.",
    "default": "Bot: I'm sorry, I didn't understand that. Could you please rephrase your question?"
}

# Function to get the best response
def get_response(user_input):
    user_input = user_input.lower().strip()
    best_match_category = "default"  # Default category for unmatched input
    min_distance = float('inf')

    # Iterate over the response categories to find the closest match
    for category, keywords in responses.items():
        for keyword in keywords:
            closest_match = get_closest_match(user_input, keywords)
            if closest_match and levenshtein(user_input, closest_match) < min_distance:
                min_distance = levenshtein(user_input, closest_match)
                best_match_category = category

    return response_messages[best_match_category]

# Chatbot function
def chatbot():
    print("Bot: Welcome to ShopEase Support Bot!")
    print("Type 'exit' to end the chat.\n")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "exit":
            print("Bot: Thank you for chatting with ShopEase. Have a great day!")
            break

        response = get_response(user_input)
        print(f"{response}")

# Run the chatbot
chatbot()
