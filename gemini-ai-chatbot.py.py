from google import genai
import os
from dotenv import load_dotenv
import time


load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

def get_gemini_response(input,max_tries = 3):
    for attempts in range(max_tries):
        try:
            client = genai.Client(api_key=api_key)

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents= input
            )

            print("*" * 25)
            print(str(f"Gemini: {response.text}"))
            print("*" * 25)
            break
        except Exception as error:
            print(f"⚠️ Attempt {attempts + 1}.Error: {error}")

            if attempts < max_tries - 1:
                print(f"🔄 Retrying in 3 seconds")
                time.sleep(3)
            else:
                    print("❌ All retry attempts failed. Please check your internet connection.")

def main():
    conversation = 0
    while True:
        try:
            user_input = input("You: ")
            
            if user_input.lower() in ["quit", "exit", "bye"]:
                print(f"Gemini: Goodbye.\nWe had {conversation} Exchanges.")
                break
            get_gemini_response(user_input)
            conversation += 1
        except Exception as error:
            print(f"Error: {error}")
            
        




if __name__ == "__main__":
    main()