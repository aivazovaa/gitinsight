# GitInsight

**GitInsight** is a web application for analyzing GitHub user activity. It allows users to visualize statistics related to commits, repositories, programming languages, and other GitHub metrics using the GitHub API.

**Live demo**: [https://gitinsight-02z2.onrender.com](https://gitinsight-02z2.onrender.com)

---

## Features

- 🔎 Search by GitHub username
- 📊 Retrieve and display user data:
  - Number of repositories
  - Number of followers / following
  - Most active repositories
  - Commit distribution over time
  - Programming language usage breakdown
- 📈 Text-based statistics and summaries rendered via server-side templates

---

## Technologies Used

### Backend
- **Python 3** — primary language for application logic and data fetching
- **Flask** — micro web framework used to handle routing, views, and HTTP logic
- **GitHub REST API v3** — used to retrieve live user and repository data from GitHub
- **Requests** — Python library for making HTTP calls to GitHub's API

### Templating and UI
- **Mako** — Python templating engine used for generating dynamic HTML content server-side
- **HTML5 / CSS3** — for markup and styling

### Deployment
- **Docker / Docker Compose** — containerized setup for local development and deployment
- **Render** — used for live cloud hosting

> Note: No JavaScript or frontend charting libraries are currently used. All analytics and visual representations are handled on the server and rendered as static HTML.

---

## Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/aivazovaa/gitinsight.git
cd gitinsight
```

### 2. Create a virtual environment & install dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file in the root directory and add your GitHub personal access token (optional but recommended):

```env
GITHUB_TOKEN=your_github_token_here
```

### 4. Run the server

```bash
python app.py
```

The application will be accessible at: [http://localhost:5000](http://localhost:5001)

---

## Usage

1. Visit the app in your browser.
2. Enter a GitHub username (e.g., `torvalds`, `aivazovaa`).
3. Click the "Search" button.
4. View detailed analytics:
   - User profile info
   - Public repositories and language usage
   - Summary tables for commits and activity

---

## Docker Deployment

To run GitInsight in a Docker container:

```bash
docker-compose up --build
```

This will start the service at [http://localhost:5000](http://localhost:5001)

---

## Project Structure

```
gitinsight/
├── app.py              # Main application logic
├── templates/          # Mako HTML templates
├── static/             # CSS files
├── requirements.txt    # Python dependencies
├── docker-compose.yml  # Docker setup for development
├── .env                # Environment variables (excluded from Git)
└── README.md           # Project documentation
```

---

## Roadmap / Future Improvements

- Support for GitHub organization-level analytics
- User comparison and ranking dashboard
- Improved error handling and loading states
- GitHub OAuth authentication
- Data caching to reduce API usage
- Metrics for pull requests, issues


