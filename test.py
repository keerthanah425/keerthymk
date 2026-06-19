from fastapi import FastAPI, Header, HTTPException, Depends

app = FastAPI(
    title="FastAPI KT",
    description="This is a test FastAPI application.",
    version="1.0.0"
)

def verify_token(token: str = Header(None)):
    # Token verification logic
    if token != "3242423":
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    return {
        "user": "authorised_user"
    }


@app.get("/secure-data")
def get_secure_data(user=Depends(verify_token)):
    return {
        "message": "This is secure data",
        "user": user
    }