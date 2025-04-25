# app/process_image.py
from PIL import Image
from io import BytesIO
import base64
from app.uploadS3 import upload_to_s3


def process_image(img, s3_client, bucket: str, region: str):
    anchor = img.anchor._from
    row = anchor.row + 1
    col = anchor.col + 1

    img_bytes = BytesIO()
    pil_img = Image.open(img.ref)
    pil_img.save(img_bytes, format="PNG")

    encoded_str = base64.b64encode(img_bytes.getvalue()).decode()
    decoded_image = base64.b64decode(encoded_str)

    image_url = upload_to_s3(decoded_image, s3_client, bucket, region)

    return {
        "row": row,
        "col": col,
        "image_url": image_url,
    }
