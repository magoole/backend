![Banner](https://repository-images.githubusercontent.com/421378452/7aaab2c1-c081-452e-b741-e6da0d37997b)
<div align="center">

# Magoole backend
The official API of Magoole.

</div>

## Table of content
- [Credits](#credits-and-acknowledgement)
- [About](#about-magoole-backend)
- [Try it locally](#try-locally-)

## Credits and acknowledgement
- Source code under [CeCLL Licence V2.1](https://github.com/magoole/backend/tree/main/LICENSE?raw=true) by [@camarm](https://github.com/camarm-dev).
- Brand and logos under [CC BY-NC-ND 3.0 FR](https://creativecommons.org/licenses/by-nc-nd/3.0/fr/) by [@camarm](https://github.com/camarm-dev).
- Icon from [Fontawesome V5.15.4](https://fontawesome.com/v5/icons/brain?f=classic&s=solid).
- Font "League Spartan".

## About Magoole backend
The Magoole backend uses datas that are provided by [Magoole scanner](https://github.com/magoole/scanner) and deliver a search engine through a Fastapi API.

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