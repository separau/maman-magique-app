# utils/letter_generator.py

from datetime import datetime

def generate_letter(name: str, relationship: str, memories: list[str], language: str = "en") -> str:
    """Génère une lettre personnalisée pour la fête des mères."""

    if language == "fr":
        intro = f"Chère {name},\n\nEn cette fête des mères, je veux prendre un moment pour te dire combien tu comptes pour moi."
        body = "\n\n".join(f"Je me souviens de {memory.lower()}." for memory in memories)
        closing = f"\n\nMerci pour tout ce que tu fais. Je t’aime plus que les mots ne peuvent le dire.\n\nAvec tout mon amour,\n{relationship}"
    else:
        intro = f"Dear {name},\n\nOn this Mother’s Day, I want to take a moment to tell you how much you mean to me."
        body = "\n\n".join(f"I remember {memory.lower()}." for memory in memories)
        closing = f"\n\nThank you for everything you do. I love you more than words can say.\n\nWith all my love,\n{relationship}"

    return f"{intro}\n\n{body}{closing}\n\n({datetime.now().strftime('%Y')})"

