import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';
import './App.css';
import logo from './octofitapp-small.png';

function App() {
  return (
    <div className="App">
      <header className="logo">
        <img src={logo} alt="Octofit Logo" />
        <h1>Welcome to Octofit</h1>
      </header>
      <Router>
        <div>
          <nav>
            <ul>
              <li><Link to="/activities">Activities</Link></li>
              <li><Link to="/leaderboard">Leaderboard</Link></li>
              <li><Link to="/teams">Teams</Link></li>
              <li><Link to="/users">Users</Link></li>
              <li><Link to="/workouts">Workouts</Link></li>
            </ul>
          </nav>
          <Routes>
            <Route path="/activities" element={<Activities />} />
            <Route path="/leaderboard" element={<Leaderboard />} />
            <Route path="/teams" element={<Teams />} />
            <Route path="/users" element={<Users />} />
            <Route path="/workouts" element={<Workouts />} />
          </Routes>
        </div>
      </Router>
    </div>
  );
}

export default App;
