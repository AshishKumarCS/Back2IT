from p4print import p
import random

def SecretLang_coding():
    msg = input("Enter your message: ")
    msg = msg[::-1] if len(msg) <=3  else msg[3:] + msg[:3] + random.choice(["ohdf", "pwdt", "exwr"])  
    p(f"Encoded Message is: {msg}")
    SecretLang_decoding(msg)

def SecretLang_decoding(msg):
    msg = msg[::-1] if len(msg) <=3 else msg[4: -4] + msg[:4]   # Shift back

    p(f"Decoded Message is: {msg}")

SecretLang_coding()
