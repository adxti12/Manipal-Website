const container = document.getElementById('fastFoodContainer');
const searchBar = document.getElementById('searchBar');

function displayFastFood(places) {
  container.innerHTML = '';
  places.forEach(place => {
    const card = `
      <div class="col-md-4 mb-4">
        <div class="card shadow-sm">
          <img src="${place.image}" class="card-img-top" alt="${place.name}">
          <div class="card-body">
            <h5 class="card-title">${place.name}</h5>
            <p class="card-text">Open Hours: ${place.openHours}</p>
          </div>
        </div>
      </div>
    `;
    container.innerHTML += card;
  });
}

displayFastFood(fastFoodPlaces);

searchBar.addEventListener('input', e => {
  const query = e.target.value.toLowerCase();
  const filtered = fastFoodPlaces.filter(place =>
    place.name.toLowerCase().includes(query)
  );
  displayFastFood(filtered);
});
