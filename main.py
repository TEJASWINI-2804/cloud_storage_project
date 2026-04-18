from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later restrict
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
from fastapi import Header
from auth import create_token, verify_token
from auth import router as auth_router
import os
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
import os
import shutil
from fastapi import FastAPI, UploadFile, File
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from database import files_collection, users_collection

from ai.search import search_files
from ai.tagging import generate_tags
from fastapi import FastAPI

# ✅ Create app ONLY ONCE
app = FastAPI()
from auth import router as auth_router

app.include_router(auth_router)
app.mount("/files", StaticFiles(directory="uploads"), name="files")
from fastapi.staticfiles import StaticFiles

app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")
# ✅ CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Model
class FileInput(BaseModel):
    filename: str
    content: str

# ✅ Home Route
@app.get("/")
def home():
    return {"message": "Cloud Storage Backend Running"}

# ✅ Upload API
@app.post("/upload/")
async def upload_file(file: UploadFile = File(...), authorization: str = Header(None)):
    user = verify_token(authorization)

    if not user:
        return {"error": "Unauthorized"}
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # FIX HERE
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
        "user": user  # ✅ ADD THIS LINE
    })

    return {"message": "File uploaded successfully"}
    # ✅ Search API
from ai.search import search_files   # already added above

@app.get("/search/")
async def search(query: str, authorization: str = Header(None)):
    user = verify_token(authorization)

    if not user:
        return {"error": "Unauthorized"}
    files = list(collection.find({"user": user}))
    results = search_files(query)

    output = []
    for item in results:
        output.append({
            "filename": item.get("filename", ""),
            "tags": item.get("tags", [])
        })

    return {"results": output}
from fastapi.responses import FileResponse

@app.get("/download/{filename}")
def download_file(filename: str):
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    return FileResponse(file_path, filename=filename)
from fastapi import HTTPException
import os

@app.delete("/delete/{filename}")
def delete_file(filename: str):
    file_path = os.path.join("uploads", filename)

    # Delete file from folder
    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        raise HTTPException(status_code=404, detail="File not found")

    # Delete from MongoDB
    files_collection.delete_one({"filename": filename})

    return {"message": "File deleted successfully"}