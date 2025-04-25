# app/s3_utils.py
import base64
import uuid


def upload_to_s3(image_bytes: bytes, s3_client, bucket: str, region: str) -> str:
    s3_key = f"{uuid.uuid4().hex}.png"

    s3_client.put_object(
        Bucket=bucket,
        Key=s3_key,
        Body=image_bytes,
        ACL='public-read',
        ContentType="image/png"
    )

    return f"https://{bucket}.s3.{region}.amazonaws.com/{s3_key}"
