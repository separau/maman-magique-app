import replicate
import os
import uuid

# Assure-toi d’avoir défini REPLICATE_API_TOKEN dans tes variables d’environnement
replicate_client = replicate.Client(api_token=os.getenv("REPLICATE_API_TOKEN"))

def generate_image(prompt: str) -> str:
    """
    Generates an image from a text prompt using Stable Diffusion.
    Returns the local image path.
    """
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    # Appel au modèle stable-diffusion
    model = replicate.models.get("stability-ai/stable-diffusion")
    version = model.versions.get("db21e45e7b571e5aa3bcd0f375fb1a4cabfc23ecb167b612740202612c6210c0e")

    output_url = version.predict(prompt=prompt)[0]

    # Télécharger l’image
    image_path = os.path.join(output_dir, f"{uuid.uuid4().hex}.png")
    os.system(f"wget {output_url} -O {image_path}")

    return image_path
