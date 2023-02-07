import os
os.environ["REPLICATE_API_TOKEN"] = "86377e4e9bebeced337fc97bc8e83b74ca06dd45"

import replicate
from name_generator import nombre
model = replicate.models.get("lambdal/text-to-pokemon")
version = model.versions.get("3554d9e699e09693d3fa334a79c58be9a405dd021d3e11281256d53185868912")

from stats import Tipo
nombre2 = Tipo()
nombre2 = nombre2 + " pokemon"
def pokefeo():
    # https://replicate.com/lambdal/text-to-pokemon/versions/3554d9e699e09693d3fa334a79c58be9a405dd021d3e11281256d53185868912#input
    inputs = {
        # Input prompt
        'prompt': nombre2,

        # Number of images to output
        'num_outputs': 1,

        # Number of denoising steps
        # Range: 1 to 50
        'num_inference_steps': 25,

        # Scale for classifier-free guidance
        # Range: 1 to 20
        'guidance_scale': 7.5,

        # Random seed. Leave blank to randomize the seed
        # 'seed': ...,
    }

    # https://replicate.com/lambdal/text-to-pokemon/versions/3554d9e699e09693d3fa334a79c58be9a405dd021d3e11281256d53185868912#output-schema
    output = version.predict(**inputs)
    print(output)
    v = str(output)
    v = v.replace("[", "")
    v = v.replace("]", "")
    v = v.replace("'", "")
    v = v.replace(" ", "")
    v = v.replace(",", "")
    #guardamos la imagen
    print(v)
    return v

if __name__ == "__main__":
   pokefeo()
