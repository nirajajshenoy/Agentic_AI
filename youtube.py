from googleapiclient.discovery import build

# ---------------------------------
# AGENT GOAL
# ---------------------------------
GOAL = "Help me study the latest AI trends using YouTube videos"

# ---------------------------------
# YOUTUBE API CONFIG
# ---------------------------------
API_KEY = "AIzaSyBUNu1CNoXzydIYydbmFF-s7eIznOloyBc"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# ---------------------------------
# PERCEPTION MODULE
# ---------------------------------
def perceive_latest_ai_trends():
    """
    In a real system, this list could come from:
    - AI news
    - Research papers
    - Trend analysis
    """
    return [
        "Agentic AI",
        "Multimodal AI",
        "Retrieval Augmented Generation",
        "Open Source LLMs",
        "Responsible AI"
    ]

# ---------------------------------
# PLANNING MODULE
# ---------------------------------
def plan_search_queries(trends):
    """
    Convert topics into YouTube-friendly search queries
    """
    return [f"{trend} explained for beginners" for trend in trends]

# ---------------------------------
# ACTION MODULE
# ---------------------------------
def fetch_youtube_videos(search_query, max_results=1):
    youtube = build(
        YOUTUBE_API_SERVICE_NAME,
        YOUTUBE_API_VERSION,
        developerKey=API_KEY
    )

    request = youtube.search().list(
        q=search_query,
        part="snippet",
        type="video",
        maxResults=max_results
    )

    response = request.execute()

    videos = []
    for item in response["items"]:
        video_id = item["id"]["videoId"]
        title = item["snippet"]["title"]
        link = f"https://www.youtube.com/watch?v={video_id}"
        videos.append({"title": title, "link": link})

    return videos

# ---------------------------------
# AGENT LOOP
# ---------------------------------
def study_agent():
    print("🎯 Agent Goal:", GOAL)

    trends = perceive_latest_ai_trends()
    search_queries = plan_search_queries(trends)

    print("\n📚 AI Study Plan (YouTube Links):\n")

    for trend, query in zip(trends, search_queries):
        print(f"🔹 Topic: {trend}")
        videos = fetch_youtube_videos(query)

        for video in videos:
            print(f"   ▶ {video['title']}")
            print(f"     🔗 {video['link']}")
        print()

# ---------------------------------
# RUN AGENT
# ---------------------------------
if __name__ == "__main__":
    study_agent()
