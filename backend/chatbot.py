"""
chatbot.py

Main chatbot application.
"""

from config import get_gemini_client
from prompts import SHOPPING_SYSTEM_PROMPT


def chat():
    """
    Runs the chatbot continuously until the user types 'exit'.
    """

    try:
        # Initialize Gemini client
        client = get_gemini_client()

        print("=" * 50)
        print("         BuySense AI")
        print("  AI Shopping Decision Assistant")
        print("=" * 50)
        print("I can help you:")
        print("✔ Compare Products")
        print("✔ Recommend Alternatives")
        print("✔ Explain Specifications")
        print("✔ Make Better Buying Decisions")
        print("\nType 'exit' anytime to quit.")
        print("=" * 50)
        

        while True:

            # Take input from user
            user_input = input("\nYou : ")

            # Exit condition
            if user_input.lower() == "exit":
                print("\nGoodbye! 👋")
                break

            # Combine the system prompt with the user's question
            full_prompt = f"""
             {SHOPPING_SYSTEM_PROMPT}

             User Question:
             {user_input}
             """

             # Generate response from Gemini
            response = client.models.generate_content(
             model="gemini-2.5-flash",
             contents=full_prompt
             )

            # Print AI response
            print(f"\n🤖 BuySense AI: {response.text}")

    except ValueError as error:
        print(f"\nConfiguration Error: {error}")

    except Exception as error:
        print(f"\nSomething went wrong: {error}")


if __name__ == "__main__":
    chat()