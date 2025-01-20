from googleapiclient.discovery import build

def extract_video_id(url):
    """Extract the video ID from a YouTube URL."""
    if "v=" in url:
        # Handle URLs like https://www.youtube.com/watch?v=Qx6-SXQYuoc
        return url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        # Handle shortened URLs like https://youtu.be/Qx6-SXQYuoc
        return url.split("youtu.be/")[1].split("?")[0]
    else:
        return None

def scrape_url(url):
    try:
        # Extract video ID from the URL
        video_id = extract_video_id(url)
        if not video_id:
            print(f"Invalid YouTube URL: {url}")
            return None

        # Initialize the YouTube Data API client
        api_key = "AIzaSyBnnQQm7bVtQYcApLn4GRTVTqaeLHkNr9Q"  # Replace with your API key
        youtube = build("youtube", "v3", developerKey=api_key)

        # Fetch video details
        request = youtube.videos().list(
            part="snippet",
            id=video_id
        )
        response = request.execute()

        # Extract title and description
        if response.get("items"):
            snippet = response["items"][0]["snippet"]
            title = snippet["title"]
            description = snippet["description"]
            return {
                'title': title,
                'content': description
            }
        else:
            print(f"No data found for video ID: {video_id}")
            return None

    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None