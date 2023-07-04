// Use URL pattern to call view rendering desired html
fetch('/guest/')

    // Convert fetched HTML file to text string.
    .then(response => response.text())

    // Parse string to HTML text
    .then(html => {
        const parser = new DOMParser();
        const doc = parser.parseFromString(html, 'text/html');

        const scrollableCards = doc.querySelector('.scrollable-cards');
        const containerCards = doc.querySelector('.container-cards');
        const prevButton = doc.querySelector('prev-button');
        const nextButton = doc.querySelector('next-button');
        const cardWidth = 320; // Including  margin
        const scrollSpeed = 200;
        
        // Listeners for button click
        prevButton.addEventListener('click', () => {
            containerCards.scrollBy({
                left: -cardWidth,
                behavior: 'smooth'
            });
        });

        nextButton.addEventListener('click', function() {
            containerCards.scrollBy({
                right: cardWidth,
                behavior: 'smooth'
            });
        });

        // listeners for arrow keys.
        scrollableCards.addEventListener('keydown', (event) => {
            if (event.key === 'ArrowLeft') {
                scrollableCards.scrollBy(-scrollSpeed, 0);
            } else if (event.key === 'ArrowRight') {
                scrollableCards.scrollBy(scrollSpeed, 0);
            }
        });

        // Append modified 'base.html' doc object to js doc body.
        document.body.appendChild(doc.documentElement)
    })

    .catch(error =>{
        console.log("Error fetching HTML file:", error)
    });
