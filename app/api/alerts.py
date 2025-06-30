


This router handles user-related endpoints. You’ll need to define:

Endpoint	Purpose
POST /users/register	Allows a new user to register (customer only)
GET /users/me	Returns the current user info (based on JWT token)
GET /users/ (admin only)	Admin-only route to list all users

📌 These routes will depend on:

Input Pydantic schemas (UserCreate, UserRead)

JWT token parsing

Calling logic in user_service.py

from fastapi import FastAPI


app = FastAPI()

@app.get("/register")
async def 