from fastapi import FastAPI, UploadFile, File, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import os
import shutil

from database import files_collection
from auth import create_token, verify_token, router as auth_router
from ai.search import search_files
from ai.tagging import generate_tags

# ✅ Create app FIRST
app = FastAPI()

# ✅ CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Include routes
app.include_router(auth_router)

# ✅ Upload folder
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ✅ Static files
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# ✅ Model
class FileInput(BaseModel):
    filename: str
    content: str

# ✅ Home
@app.get("/")
def home():
    return {"message": "Cloud Storage Backend Running"}

# ✅ Upload
@app.post("/upload/")
async def upload_file(file: UploadFile = File(...), authorization: str = Header(None)):
    user = verify_token(authorization)

    if not user:
        return {"error": "Unauthorized"}

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    if file.filename.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    else:
        content = file.filename

    tags = generate_tags(content)

    files_collection.insert_one({
        "filename": file.filename,
        "path": file_path,
        "tags": tags,
        "user": user
    })

    return {"message": "File uploaded successfully"}

# ✅ Search
@app.get("/search/")
async def search(query: str, authorization: str = Header(None)):
    user = verify_token(authorization)

    if not user:
        return {"error": "Unauthorized"}

    results = search_files(query)

    return {"results": results}

# ✅ Download
@app.get("/download/{filename}")
def download_file(filename: str):
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    return FileResponse(file_path, filename=filename)

# ✅ Delete
@app.delete("/delete/{filename}")
def delete_file(filename: str):
    file_path = os.path.join(UPLOAD_FOLDER, filename)

    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        raise HTTPException(status_code=404, detail="File not found")

    files_collection.delete_one({"filename": filename})

    return {"message": "File deleted successfully"}
