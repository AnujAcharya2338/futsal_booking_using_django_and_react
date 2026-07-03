import { useState, useEffect } from 'react'

function App() {
  const [courts, setCourts] = useState([])

  useEffect(() => {
    fetch('http://localhost:8000/api/courts/')
      .then(res => res.json())
      .then(data => setCourts(data))
  }, [])

  return (
    <>
    <div>
      {courts.map(court => (
        <div key={court.id}>
          <h2>{court.court_name}</h2>
          <h2>{court.location}</h2>
          <h2>{court.price_per_hour}</h2>
        </div>
      ))}
    </div>
    </>
  )
}

export default App