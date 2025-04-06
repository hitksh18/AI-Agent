# main.py

from agents.summarizer import summarize
from agents.retriever import retrieve_similar_tickets
from agents.router import predict_routing
from agents.resolver import suggest_resolution
from agents.estimator import estimate_resolution_time

def main():
    print("🧠 Welcome to the AI Customer Support System!")
    print("Please describe your issue below:\n")

    # 📝 Accept user input dynamically
    user_input = input("✍️  Your Issue: ")

    print("\n📝 Summary:")
    summary = summarize(user_input)
    print(summary)

    print("\n🔍 Similar Historical Tickets:")
    similar_tickets = retrieve_similar_tickets(summary)
    for i, ticket in enumerate(similar_tickets, 1):
        description = ticket.get("description", "N/A")
        sentiment = ticket.get("sentiment", "N/A")
        team = ticket.get("team", "N/A")
        action = ticket.get("action", "N/A")

        print(f"{i}.  {description} | Sentiment: {sentiment}")
        print(f"   → Team: {team}")
        print(f"   → Action: {action}\n")

    print("📦 Routing Info:")
    routing = predict_routing(summary)
    print(routing)

    print("\n💡 Suggested Resolution:")
    resolution = suggest_resolution(summary, similar_tickets)
    print(resolution)

    print("\n⏱ Estimated Resolution Time:")
    print(estimate_resolution_time(summary))

if __name__ == "__main__":
    main()
