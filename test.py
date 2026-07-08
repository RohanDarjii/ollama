from tools.TavilySearch import search_tavily
from tools.FlightSearch import search_flights
from backend import run_travel_agent

'''test_query = "Best hotels in India?"
results = search_tavily(test_query)
print(results)'''

'''print(search_flights("Plan a 7 days Japan trip from India"))'''

user_query = input("Enter your travel query: ")
response = run_travel_agent(user_query=user_query,
                            thread_id="test_thread")
print("\nFinal Itinerary:\n")
print(response["final_answer"]) 