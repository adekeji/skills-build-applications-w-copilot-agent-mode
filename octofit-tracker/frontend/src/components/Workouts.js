import React from 'react';

function Workouts() {
  return (
    <div className="card">
      <div className="card-header">
        <h2 className="card-title">Workouts</h2>
      </div>
      <div className="card-body">
        <table className="table table-striped">
          <thead>
            <tr>
              <th>Workout</th>
              <th>Description</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Running</td>
              <td>5km run in the park</td>
            </tr>
            <tr>
              <td>Swimming</td>
              <td>30 laps in the pool</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Workouts;
