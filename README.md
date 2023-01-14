
# Fampay_backend_Assignment

an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

## Basic Requirements:
- [X]   Server should call the YouTube API continuously in background (async) with some interval (say 10 seconds) for fetching the latest videos for a predefined search query and should store the data of videos (specifically these fields - Video title, description, publishing datetime, thumbnails URLs and any other fields you require) in a database with proper indexes.
- [X]   A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.
- [X]  A basic search API to search the stored videos using their title and description.
- [X]  Dockerize the project.
- [X]  It should be scalable and optimised.

## Additional

- [X]  Add support for supplying multiple API keys so that if quota is exhausted on one, it automatically uses the next available key.
- [X]  Optimise search api, so that it's able to search videos containing partial match for the search query in either video title or description.
    - Ex 1: A video with title *`How to make tea?`* should match for the search query `tea how`


## Environment Variables

To run this project, you will need to add the following environment variables.

1. Create `fampay.env` and add the following environment variables
- `DB_HOST` (Domain name for Postgres)  
- `ADMINER_HOST` (Domain name for Adminer)
- `POSTGRES_USER` (Username for Postgres)
- `POSTGRES_PASSWORD` (Password for Postgres user)
- `POSTGRES_DB` (Database name)
- `TZ` (Timezone)
- Place this file in the root folder of the project

2. Create `.env` and add the following environment variables
- `NUM_KEYS` (Number of Youtube API KEYS)
- `DEV_KEY_{i}` (Youtube API Developer key)
- you can add multiple keys just replace `i` with the next key in serial. Ex : `DEV_KEY_1`
- `DB_NAME` (Database Name)
- `DB_USER` (Postgres Username)
- `DB_PASS` (Postgres Password)
- `DB_HOST` (Domain name for Postgres)
- `DB_PORT` (Postgres Port) (Default is `5432`)
- `PAGE_LIMIT` (Pagination limit on 1 page)
- `DEFAULT_QUERY` (Search query)
- `CELERY_BROKER_URL='redis://redis:6379'` (You can change it and set it to local redis server) (Redis server url)
- `CELERY_RESULT_BACKEND='redis://redis:6379'`
- `INTERVAL` (Celery Scheduele interval)
- place this file in ./youtubeApiFetch, since it'll be used by Django server




## Installation (Docker)

1. Place the enviroment variable files in the correct folders (See Enviroment Variables Section).
2. Install Docker and Docker compose on your system.
3. Navigate to the root of the project. 
4. Run the following commands in your `CLI`
```bash
 $ docker compose --env-file .\fampay.env up
```

## Working

1. Tasks are schedueled every given minute intervals.
2. These tasks are responsible for fetching data from Youtube search API and storing it in the Database.
3. Celery schedueler data is stored in the redis.
4. Django handles Client search query requests and responses with JSON serialized paginated data.

## API Reference

- Django server is hosted on port `8000`.
- client can access using url `localhost:8000`.

#### Get search query result.

- Get search query results

```http
  GET /api/videos
```

| Query | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `search` | `string` | **Required**. Search query|
| `page`   | `Int`    |    Pagination page                       |

- Example usage `http://localhost:8000/api/videos?search=crick`

- Example Result 
```JSON

{
    "count": 16,
    "next": "http://localhost:8000/api/videos?page=2&search=crick",
    "previous": null,
    "results": [
        {
            "id": 15,
            "video_id": "sZb6PF9PPo0",
            "title": "Cricket fanny 😀 | IND vs SL 2nd ODI highlights | Kl Rahul, Rohit Sharma, kuldeep yadav |",
            "description": "Cricket fanny | IND vs SL 2nd ODI highlights | Kl Rahul, Rohit Sharma, kuldeep yadav |",
            "published_on": "2023-01-14T00:55:56Z",
            "thumbnail_url": "https://i.ytimg.com/vi/sZb6PF9PPo0/default.jpg"
        },
        {
            "id": 16,
            "video_id": "QIzhY3Hi6Ow",
            "title": "#shorts #youtubeshorts #viralshorts #cricket #cricketshorts #cricketvideo #realcricket22 #sayristatu",
            "description": "shorts #youtubeshorts #viralshorts #viralvideos #viralshort #sayristatus #realcricket22 #cricket #sayristatusvideo #cricketshorts ...",
            "published_on": "2023-01-14T00:55:55Z",
            "thumbnail_url": "https://i.ytimg.com/vi/QIzhY3Hi6Ow/default.jpg"
        },
        {
            "id": 14,
            "video_id": "ibNJdHAP4SY",
            "title": "goat😱of india#cricket #ipl2023 #viratkohli #trending #t20worldcup #shortvideo",
            "description": "goat  of india#cricket #ipl2023 #viratkohli #trending #t20worldcup #shortvideo.",
            "published_on": "2023-01-14T00:55:00Z",
            "thumbnail_url": "https://i.ytimg.com/vi/ibNJdHAP4SY/default.jpg"
        },
        {
            "id": 13,
            "video_id": "CA5Sve62YjA",
            "title": "The #Virat Kohli Chesh 🔥 Master New #Cricket# Video ((2023)) Cricket Reels #Shorts# #shorts#",
            "description": "",
            "published_on": "2023-01-14T00:53:26Z",
            "thumbnail_url": "https://i.ytimg.com/vi/CA5Sve62YjA/default.jpg"
        },
        {
            "id": 12,
            "video_id": "WSNX0m0nyY0",
            "title": "World Cricket के सबसे शानदार विकेट कीपर बल्लेबाज़ #msdhoni #viral #shorts @cricketkingAk",
            "description": "World Cricket के सबसे शानदार विकेट कीपर बल्लेबाज़ #cricket #crickethistory #wicketkeeper ...",
            "published_on": "2023-01-14T00:52:43Z",
            "thumbnail_url": "https://i.ytimg.com/vi/WSNX0m0nyY0/default.jpg"
        }
    ]
}

```
## Additional Hosted Services
- `Adminer` at `localhost:8080`. Which can be used to access the database from browser.
- `Flower` at `localhost:8888`. Which is used to monitor celery tasks.
