from fastapi import FastAPI, HTTPException

app = FastAPI(title="User Profile (Vulnerable)")

# demo users
users = {
  1: {"username": "aman", "email": "aman.dev@gmail.com"},
  2: {"username": "admin", "email": "admin.dev@gmail.com"}
}

@app.get("/users/{user_id}")
def get_user(user_id: int):
  user = users.get(user_id)

  if user is None:
    raise HTTPException(status_code=404, detail="User not Found")

  return user
