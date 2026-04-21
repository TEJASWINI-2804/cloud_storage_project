Personal Cloud Storage with AI Optimization

Overview

This project is a **web-based personal cloud storage system** enhanced with **AI optimization**. It allows users to securely upload, store, search, and manage files efficiently using intelligent search techniques.

Unlike traditional storage systems, this project introduces **AI-based search and optimization**, making file retrieval faster and smarter.



Features

*  User Authentication (Signup/Login using JWT)
*  File Upload to Cloud Storage
*  AI-based Smart Search
*  File Delete Functionality
*  File Download Support
*  Image Preview
*  PDF Preview
*  MongoDB Integration for Metadata Storage



 Tech Stack

Frontend:

* React.js
* HTML, CSS, JavaScript

 Backend:

* FastAPI (Python)

 Database:

* MongoDB (NoSQL)

AI / Optimization:

* Keyword-based search (extendable to ML models)


Installation & Setup

 1. Clone Repository


git clone https://github.com/your-username/cloud-storage-project.git
cd cloud-storage-project




2. Backend Setup (FastAPI)


cd backend
pip install -r requirements.txt
uvicorn main:app --reload


 Backend runs at:


http://127.0.0.1:8000




 3. Frontend Setup (React)


cd frontend
npm install
npm start


Frontend runs at:


http://localhost:3000




 4. MongoDB Setup

* Install MongoDB locally OR use MongoDB Atlas
* Update connection string in backend code



API Endpoints

| Endpoint             | Method | Description   |
| -------------------- | ------ | ------------- |
| /signup              | POST   | Register user |
| /login               | POST   | Login user    |
| /upload              | POST   | Upload file   |
| /search              | GET    | Search files  |
| /delete/{filename}   | DELETE | Delete file   |
| /download/{filename} | GET    | Download file |



How AI Optimization Works

* Files are tagged or indexed during upload
* Search uses keyword matching (can be extended to embeddings)
* Improves file retrieval speed and accuracy


 Screenshots (Add your images)

* Login Page
* Dashboard
* Upload Screen
* Search Results



Deployment

 Backend:

* Render / Railway

Frontend:

* Netlify / Vercel

Replace API URLs in frontend after deployment.



 Limitations

* Basic AI search (not deep learning-based yet)
* Local file storage (can be extended to cloud storage like AWS S3)



uture Improvements

* Advanced AI (CLIP, NLP search)
* Voice-based search
* Cloud storage integration (AWS/GCP)
* Mobile app development



 Author

**Tejaswini Kattamanchi**
MCA Final Year Project



 License

This project is for academic purposes only.

