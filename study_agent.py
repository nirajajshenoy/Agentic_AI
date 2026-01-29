from googleapiclient.discovery import build

# --------------------------------
# YOUTUBE CONFIG
# --------------------------------
API_KEY = "AIzaSyBUNu1CNoXzydIYydbmFF-s7eIznOloyBc"
YOUTUBE_SERVICE_NAME = "youtube"
YOUTUBE_VERSION = "v3"

# --------------------------------
# STUDY ACTION
# --------------------------------
def study_topic(topic):
    print(f"\n📘 Studying topic: {topic}")

    youtube = build(
        YOUTUBE_SERVICE_NAME,
        YOUTUBE_VERSION,
        developerKey=API_KEY
    )

    request = youtube.search().list(
        q=f"{topic} explained for beginners",
        part="snippet",
        type="video",
        maxResults=1
    )

    response = request.execute()

    for item in response["items"]:
        video_id = item["id"]["videoId"]
        title = item["snippet"]["title"]
        link = f"https://www.youtube.com/watch?v={video_id}"

        print("▶ Recommended Video:", title)
        print("🔗 Link:", link)
