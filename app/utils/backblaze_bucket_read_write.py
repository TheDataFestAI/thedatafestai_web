import os
from pathlib import Path
import b2sdk.v2 as b2
from b2sdk.v1 import DownloadDestBytes
from reportlab.pdfgen import canvas
from dotenv import load_dotenv

load_dotenv()

info = b2.InMemoryAccountInfo()
b2_api = b2.B2Api(info)

application_key_id = os.getenv("B2_KEY_ID")
application_key = os.getenv("B2_APPLICATION_KEY")

b2_api.authorize_account("production", application_key_id, application_key)

def upload_file_into_backblaze(file_name, content, bucket_name="tdf-app-bucket"):
    a4_page_size = (595.27, 841.89)   
    file_path = "./assets/temp_dumps/" + file_name
    c = canvas.Canvas(file_path, pagesize=a4_page_size)
    if type(content) == list:
        for i in content:
            c.drawString(50, 780, i)
    else:
         c.drawString(50, 780, content)
    c.showPage()
    c.save()
    
    local_file = Path(file_path).resolve()
    print(f"local_file: {local_file}")
    metadata = {"writer": "TheDataFestAI"}
    bucket = b2_api.get_bucket_by_name(bucket_name)
    uploaded_file = bucket.upload_local_file(
        local_file=local_file,
        file_name=file_name,
        file_infos=metadata,
    )
    print(f"b2 file url: {b2_api.get_download_url_for_fileid(uploaded_file.id_)}")
    # os.remove(file_path)
    return file_path

def download_file_from_backblaze(file_name="sample_cv.pdf", bucket_name="tdf-app-bucket"):
    file_path = "./assets/temp_dumps/" + file_name
    download_dest = DownloadDestBytes()
    bucket = b2_api.get_bucket_by_name(bucket_name)
    bucket.download_file_by_name(file_name, download_dest)
    content_as_bytes = download_dest.get_bytes_written()
    
    with open(file_path, "wb") as file:
        file.write(content_as_bytes) 
    return content_as_bytes