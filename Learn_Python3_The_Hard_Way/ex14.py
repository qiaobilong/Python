from sys import argv
script,user_name = argv
prompt = '>'

print(f"Hi {user_name}, i'm the {script} script.")
print("i'd like to ask you a few questions.")
print(f"do you like mo {user_name}?")
likes = input(prompt)

print(f"where do you live {user_name}")
lives = input(prompt)

print("what kind of computer do you have")
computer = input(prompt)

print(f"""
alright, so you said {likes} about liking meself.
you live in {lives}. not sure where that is
and you have a {computer} computer. nice.
""")
