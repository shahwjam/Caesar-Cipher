# Name: Shahwan Alchomer
# Project: Caesar Cipher 
# Description: Encrypt and decrypt messages using the Caesar Cipher algorithm,
# including automatic deciphering using English letter frequency scoring.

def shift1(c):
    """Shift a single letter forward by 1 (A→B, z→a). Non-letters stay the same."""
    if c.isalpha():
        base = ord('A') if c.isupper() else ord('a')
        return chr((ord(c) - base + 1) % 26 + base)
    return c


def shiftn(lett, n):
    """Shift a single character n times."""
    for _ in range(n):
        lett = shift1(lett)
    return lett


def encipher(s, n):
    """Shift every letter in a string by n positions."""
    result = ''
    for char in s:
        result += shiftn(char, n)
    return result


def letProb(c):
    """Return the English letter probability for scoring during deciphering."""
    probs = {
        ' ': 0.1904, 'e': 0.1017, 't': 0.0737, 'a': 0.0661, 'o': 0.0610,
        'i': 0.0562, 'n': 0.0557, 'h': 0.0542, 's': 0.0508, 'r': 0.0458,
        'd': 0.0369, 'l': 0.0325, 'u': 0.0228, 'm': 0.0205, 'c': 0.0192,
        'w': 0.0190, 'f': 0.0175, 'y': 0.0165, 'g': 0.0161, 'p': 0.0131,
        'b': 0.0115, 'v': 0.0088, 'k': 0.0066, 'x': 0.0014, 'j': 0.0008,
        'q': 0.0008, 'z': 0.0005
    }
    return probs.get(c.lower(), 1.0)


def decipher(s):
    """Attempt to automatically decipher text using frequency analysis."""
    best_score = 0
    best_decoding = s

    for shift in range(26):
        decoded = encipher(s, 26 - shift)
        score = sum(letProb(c) for c in decoded)
        if score > best_score:
            best_score = score
            best_decoding = decoded

    return best_decoding


def jscore(S, T):
    """Compute similarity score between two strings."""
    score = 0
    T = list(T)
    for c in S:
        if c in T:
            score += 1
            T.remove(c)
    return score


if __name__ == "__main__":
    print("=== Caesar Cipher Tool ===")
    text = input("Enter text: ")
    shift = int(input("Enter shift (e.g., 3): "))

    encrypted = encipher(text, shift)
    decrypted = decipher(encrypted)

    print("\n--- Results ---")
    print(f"Encrypted: {encrypted}")
    print(f"Auto-Deciphered: {decrypted}")
