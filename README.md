 Personal Cloud Storage with AI Optimization

 Project Overview

This project is a **web-based personal cloud storage system** enhanced with **AI-based optimization techniques**. It allows users to securely upload, store, search, and manage files efficiently.

Unlike traditional systems, this project provides **smart search functionality** using AI-based tagging and keyword matching.

Features

* 🔐 Secure User Authentication (JWT-based)
* 📤 File Upload & Storage
* 🔍 AI-based Smart Search
* 🗑️ File Deletion
* ⬇️ File Download
* 🖼️ Image Preview
* 📄 PDF Preview
* 📊 MongoDB Integration


Tech Stack

#Frontend

* React.js
* HTML, CSS, JavaScript

#Backend

* FastAPI (Python)

#Database

* MongoDB

# AI Logic

* Keyword-based tagging (extendable to ML models)

Project Structure

```
cloud_storage_project/
│
├── backend/
│   ├── main.py
│   ├── auth.py
│   ├── database.py
│   ├── upload.py
│   ├── search.py
│   └── uploads/
│
├── frontend/
│   ├── src/
│   │   ├── App.js
│   │   ├── components/
│   │   └── styles/
│   └── package.json
│
├── requirements.txt
└── README.md
```


##  Installation & Setup

Clone Repository

```
git clone https://github.com/TEJASWINI-2804/cloud_storage_project.git
cd cloud_storage_project
```

Backend Setup

```
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

👉 Runs on: http://127.0.0.1:8000


### 🔹 Frontend Setup

```
cd frontend
npm install
npm start
```

👉 Runs on: http://localhost:3000

 MongoDB Setup

* Install MongoDB OR use MongoDB Atlas
* Update connection string in backend

 API Endpoints

| Endpoint             | Method | Description   |
| -------------------- | ------ | ------------- |
| /signup              | POST   | Register user |
| /login               | POST   | Login         |
| /upload              | POST   | Upload file   |
| /search              | GET    | Search files  |
| /delete/{filename}   | DELETE | Delete file   |
| /download/{filename} | GET    | Download file |

Screenshots


* Login Page
  <img width="940" height="384" alt="image" src="https://github.com/user-attachments/assets/2897740a-2334-4b2c-a7b5-afdce59caae4" />

* Dashboard
  <img width="940" height="533" alt="image" src="https://github.com/user-attachments/assets/a0a0011f-0ea8-4fae-b99f-4a42b87acf6e" />

* Upload Screen
  <img width="940" height="499" alt="image" src="https://github.com/user-attachments/assets/2720073f-af9c-4987-8b04-cb9a4809cd87" />

* Search Results
  <img width="940" height="499" alt="image" src="https://github.com/user-attachments/assets/e1db0fde-df14-41c6-b161-387f0dd8b759" />


Results

* Faster search compared to traditional systems
* Improved efficiency using AI tagging
* Reduced manual file management

 Limitations

* Basic AI implementation
* Local file storage

Future Scope

* Advanced AI models (CLIP, NLP)
* Cloud deployment (AWS, GCP)
* Mobile app integration
* Voice-based search

 Author

**Tejaswini Kattamanchi**
MCA Final Year Project

License

This project is developed for academic purposes.


