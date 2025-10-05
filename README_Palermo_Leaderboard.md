# Palermo Scale Leaderboard - File Package

This zip file contains all the necessary files to create and run the Palermo Scale Leaderboard functionality.

## 📁 Files Included

### Core Files (Essential)
- **`helpers.py`** - Main data processing functions
  - `get_palermo_leaderboard()` - Fetches and sorts asteroids by Palermo Scale
  - `get_vi_data()` - Gets virtual impactor data for individual asteroids
  - `get_high_risk_asteroid_data()` - Fetches high-risk asteroid data from NASA APIs

- **`sites.py`** - Flask routes
  - `/leaderboard` route that renders the leaderboard page

- **`templates/leaderboard.html`** - Frontend template
  - Complete HTML page with Tailwind CSS styling
  - Displays the leaderboard table with educational content

- **`app.py`** - Flask application setup
  - Main application entry point
  - Registers blueprints and configures caching

### Supporting Files
- **`extensions.py`** - Flask extensions configuration
- **`api.py`** - API endpoints for data fetching
- **`orbit.py`** - Orbital calculations and 3D point generation

## 🚀 How to Run

1. **Install Dependencies:**
   ```bash
   pip install flask flask-caching flask-cors requests numpy
   ```

2. **Run the Application:**
   ```bash
   python app.py
   ```

3. **Access the Leaderboard:**
   - Open browser to `

## 🔧 Data Flow

```
NASA Sentry API → helpers.py → sites.py → leaderboard.html
     ↓              ↓           ↓           ↓
  Raw Data → Processed Data → Flask Route → HTML Template
```

## 📊 Features

- **Real-time NASA data** from Sentry API
- **Performance caching** (10-hour timeout)
- **Responsive design** with Tailwind CSS
- **Educational content** explaining Palermo Scale
- **Top 10 most dangerous asteroids** ranked by Palermo Scale

## 🎯 Key Functions

- `get_palermo_leaderboard(limit=10)` - Main function that creates the leaderboard
- `get_vi_data(des)` - Gets detailed data for individual asteroids
- `/leaderboard` route - Flask endpoint that serves the leaderboard page

## 📝 Notes

- The leaderboard shows asteroids sorted by Palermo Scale (descending)
- Data is cached for 10 hours to improve performance
- All data comes from NASA's official Sentry API
- The system includes fallback error handling for API failures

## 🔗 Dependencies

- Flask (web framework)
- Flask-Caching (performance caching)
- Flask-CORS (cross-origin requests)
- Requests (HTTP API calls)
- NumPy (mathematical calculations)

---

**Created:** October 5, 2025  
**Purpose:** NASA NEO Impact Risk Assessment Tool  
**Data Source:** NASA JPL Sentry API
