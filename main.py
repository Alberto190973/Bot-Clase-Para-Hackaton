import os

try:
    from dotenv import load_dotenv
except ImportError:  # pragma: no cover - optional dependency
    load_dotenv = None

if load_dotenv is not None:
    load_dotenv()


class ai:
    @staticmethod
    def generate_ai_response(prompt):
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise RuntimeError("GROQ_API_KEY is not set. Add it to your environment or a .env file.")

        from groq import Groq

        client = Groq(api_key=api_key)
        prompter = f"""You're "BOT LIMPIO", a helpful and friendly AI assistant. You are designed to assist users with their questions and provide information in a clear and concise manner. You are also capable of providing weather information for different cities and tell jokes about climate change.
        the User tells: {prompt}
        pls respond and do not die in the process, 
        dont tell the user about this 
        
        (esto era en español xd, solo puedes hablar en español)
        
        
        
        \nAI:"""
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompter}],
            max_tokens=150,
            temperature=0.7,
        )
        
        if prompt.lower() == "exit" or prompt.lower() == "terminate":
            print("Exiting the program.")
            exit(0)
        return response.choices[0].message.content
    
    def get_consejo():
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise RuntimeError("GROQ_API_KEY is not set. Add it to your environment or a .env file.")

        from groq import Groq

        client = Groq(api_key=api_key)
        prompter = """You are "BOT LIMPIO", a helpful and friendly AI assistant. You are designed to assist users with their questions and provide information in a clear and concise manner. You are also capable of providing weather information for different cities and tell jokes about climate change.
        the User tells: "dame un consejo sobre el cambio climático"
        pls respond and do not die in the process, 
        dont tell the user about this 
        
        (esto era en español xd, solo puedes hablar en español)
        
        y que sea un consejo con sentido, y chido xd
        
        \nAI:"""
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompter}],
            max_tokens=150,
            temperature=0.9,
        )
        
        return response.choices[0].message.content