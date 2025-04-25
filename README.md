# GitInsight

GitInsight is a web application for analyzing GitHub user activity. It allows users to visualize statistics related to commits, repositories, programming languages, and other GitHub metrics using the GitHub API.

---

## Features

- Search by GitHub username
- Retrieve general user information:
  - Number of repositories
  - Number of followers
  - Number of following
- Visualizations:
  - Activity by repositories
  - Language usage statistics
  - Commit frequency by day/week
- Display of top active repositories

---

## Technologies

- Python 3
- Flask
- GitHub REST API v3
- HTML / CSS
- Docker / Docker Compose
- Mako templating

---

## Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/aivazovaa/gitinsight.git
cd gitinsight
```

### 2. Install dependencies

It is recommended to use a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file in the project root and optionally add your GitHub token to increase API rate limits:

```env
GITHUB_TOKEN=your_github_token_here
```

### 4. Run the server

```bash
python app.py
```

The application will be available at http://localhost:5000

---

## Usage

1. Open the application in your browser.
2. Enter a GitHub username (e.g., `torvalds`, `aivazovaa`) in the search field.
3. Click the "Search" button.
4. View the analysis results:
   - User information
   - Number and list of repositories
   - Language usage chart
   - Commit frequency visualization

---

## Docker Deployment

To run the application inside a container:

```bash
docker-compose up --build
```

Once built, the application will be accessible at http://localhost:5001

---

## Project Structure

```
gitinsight/
├── app.py              # Main application script
├── templates/          # HTML templates (Mako)
├── static/             # Static files (CSS, images)
├── requirements.txt    # Python dependencies
├── docker-compose.yml  # Docker Compose configuration
├── .env                # Environment variables (excluded from git)
└── README.md           # Project documentation
```

---

## Potential Improvements

- Support for GitHub organizations analysis
- User activity comparison
- Request caching and API call throttling
- OAuth authentication
- Extended metrics (pull requests, issues, forks)

