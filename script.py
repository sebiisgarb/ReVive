import boto3
import json
import base64
import logging
from botocore.config import Config

config = Config(
    read_timeout=300,
    connect_timeout=300,
    retries={
        "max_attempts": 10,
    }
)
client = boto3.client("sagemaker-runtime", region_name="eu-central-1", config=config)
boto3.set_stream_logger("botocore", level=logging.DEBUG)

with open("poza_test.jpg", "rb") as f:
    img_b64 = base64.b64encode(f.read()).decode("utf-8")


response = client.invoke_endpoint(
    EndpointName="sp-deoldify",
    ContentType="application/json",
    Body=json.dumps({"image_base64": img_b64}),
)

result = json.loads(response["Body"].read().decode("utf-8"))
color_img_bytes = base64.b64decode(result["image_base64"])

with open("rezultat_color.jpg", "wb") as f:
    f.write(color_img_bytes)

