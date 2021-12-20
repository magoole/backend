# Magoole Backend
The backend of Magoole Search Engine made with fastapi

# Try locally:
1. Install requirements
```shell
pip install -r requirements.txt
```
2. Set up your mongodb passwords/url<br>
    - If you have an account on Magoole Mongodb just do this
    ```shell
    touch .mongopass && echo "username:password" > .mongopass
    ```
    - Else modify MongoServer url on files main.py at line `client = pymongo.MongoClient(f"mongodb+srv://yourmongoserver")`
      <br>
      <br>
3. Run the backend
```shell
uvicorn main:app --reload
```