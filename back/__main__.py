
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("back.main:app", host="127.0.0.1", port=8080, reload=True)