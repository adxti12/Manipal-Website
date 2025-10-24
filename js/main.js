// Fetch and display featured places
fetch('data/places.json')
  .then(response => response.json())
  .then(places => {
    const container = document.getElementById('featured-places');
    places.forEach(place => {
      container.innerHTML += `
        <div class="col-md-4 mb-4">
          <div class="card h-100 shadow">
            <img src="${place.image}" class="card-img-top" alt="${place.name}">
            <div class="card-body">
              <h5 class="card-title">${place.name}</h5>
              <p class="card-text">${place.description}</p>
              <span class="badge bg-info text-dark">${place.category}</span>
            </div>
          </div>
        </div>
      `;
    });
  });
