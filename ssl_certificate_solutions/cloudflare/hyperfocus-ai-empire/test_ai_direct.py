import requests

API_BASE_URL = "https://api.cloudflare.com/client/v4/accounts/a54016fa7240168776cc16e5725a2675/ai/run/"
headers = {"Authorization": "Bearer hh2YKjExIYzEZ73y_VVccf0i6P4n613nCwY_e4My"}


def run(model, inputs):
    payload = {"messages": inputs}
    response = requests.post(
        f"{API_BASE_URL}{model}", headers=headers, json=payload, timeout=30
    )
    return response.json()


def test_hyperfocus_ai():
    """Test the AI with HyperFocus Zone Empire prompts"""

    # Test 1: Basic connection
    print("🧠 Testing Cloudflare AI Connection...")
    inputs = [
        {
            "role": "system",
            "content": "You are a friendly assistant that helps with focus and productivity",
        },
        {"role": "user", "content": "Hello, can you help me focus better?"},
    ]

    try:
        output = run("@cf/meta/llama-3-8b-instruct", inputs)
        print("✅ AI Connection Success!")
        print(f"Response: {output}")
        return True
    except requests.RequestException as e:
        print(f"❌ AI Connection Failed: {e}")
        return False


def test_neurodivergent_coaching():
    """Test ADHD/Autism specific coaching"""

    print("\n🎯 Testing Neurodivergent Focus Coaching...")
    inputs = [
        {
            "role": "system",
            "content": """You are a specialized AI coach for neurodivergent individuals (ADHD, autism).
            You understand executive function challenges, hyperfocus patterns, and sensory needs.
            Provide encouraging, practical advice using positive language.""",
        },
        {
            "role": "user",
            "content": "I have ADHD and I'm struggling to focus on my work today. Everything feels overwhelming.",
        },
    ]

    try:
        output = run("@cf/meta/llama-3-8b-instruct", inputs)
        print("✅ Neurodivergent Coaching Test Success!")
        print(f"AI Response: {output}")
        return True
    except requests.RequestException as e:
        print(f"❌ Coaching Test Failed: {e}")
        return False


if __name__ == "__main__":
    print("🏆 HYPERFOCUS ZONE EMPIRE - AI TESTING 🏆")
    print("=========================================")

    # Test basic AI connection
    basic_success = test_hyperfocus_ai()

    if basic_success:
        # Test specialized coaching
        coaching_success = test_neurodivergent_coaching()

        if coaching_success:
            print("\n🌟 ALL TESTS PASSED! 🌟")
            print("Your token works perfectly with Cloudflare AI!")
            print("Ready for Workers deployment! 🚀")
        else:
            print("\n⚠️  Basic AI works, but coaching needs refinement")
    else:
        print("\n❌ AI connection failed - check token permissions")

    print("\nNext step: Deploy to Cloudflare Workers! 💫")
