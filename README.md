# YouTube Mp3 Converter API

A Python-based API that interacts with y2mate.lol to convert YouTube videos to downloadable audio files. This service is deployed on Vercel and provides a simple endpoint to convert YouTube videos to MP3 format.

## 🌟 Features

- **YouTube to MP3**: Convert any YouTube video to MP3 format
- **Simple JSON API**: Easy-to-use REST endpoint
- **Serverless Architecture**: Deployed on Vercel for reliability
- **Direct Download URLs**: Get direct download links for converted files
- **Automatic File Naming**: Preserves original video title in filename

## 📚 API Documentation

### Base URL
```
https://y2-indol.vercel.app
```

### Endpoint

#### Convert Video
```http
POST /api/convert
```

##### Request Format
Content-Type: application/json

```json
{
    "link": "https://youtu.be/YOUR_VIDEO_ID"
}
```

##### Example Request
```bash
curl -X POST 'https://y2-indol.vercel.app/api/convert' \
     -H 'Content-Type: application/json' \
     -d '{"link": "https://youtu.be/f5-IY_Ja1RM?si=KUTcO5FmX-AE8lmP"}'
```

##### Response Format
```json
{
    "filename": "JVKE - her (official lyric video) - JVKE.mp3",
    "status": "tunnel",
    "url": "https://dl25.yt-dl.click/tunnel?id=..."
}
```

## 🚀 Getting Started

### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)
- Node.js and npm (for Vercel CLI)

### Local Development

1. **Clone the Repository**
   ```bash
   git clone <your-repo-url>
   cd y2mate-converter
   ```

2. **Create and Activate Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Development Server**
   ```bash
   vercel dev
   ```

## 📦 Deployment

### Deploying to Vercel

1. **Install Vercel CLI**
   ```bash
   npm install -g vercel
   ```

2. **Configure Vercel Project**
   ```bash
   vercel login
   vercel link
   ```

3. **Deploy**
   ```bash
   vercel --prod
   ```

## ⚡ Response Details

The API response includes:
- `filename`: Name of the converted audio file
- `status`: Current status of the conversion
- `url`: Direct download URL for the converted file

## 🛠️ Error Handling

| Status Code | Description                                    |
|-------------|------------------------------------------------|
| 200         | Successful conversion                          |
| 400         | Bad request (invalid URL)                      |
| 404         | Video not found                               |
| 500         | Internal server error                         |

Error Response Format:
```json
{
    "error": "Error message description"
}
```

## ⚠️ Rate Limiting

To prevent abuse, the API implements rate limiting. Please be mindful of the following limits:
- Maximum of 100 requests per hour per IP
- Maximum video length: 2 hours



## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This project is not affiliated with, endorsed by, or sponsored by y2mate.lol or YouTube. Users are responsible for ensuring compliance with YouTube's Terms of Service and local copyright laws.

## 🚫 Legal Notice

This tool should only be used for converting videos that you have the right to download and convert. Do not use this service for any copyright-infringing purposes.

## 📮 Support

For issues, feature requests, or questions:
- Open an issue in the GitHub repository
  

---

Made with ❤️ 
