// Define the search terms to test
const searchTerms = [
    "-failed",
    "n5",
    "n4",
    "n3",
    "n2",
    "n1",
    "on:shi",
    "kun:shi",
    "not",
    "test",
    "random"
];

// Add a random character to the search terms
const chars = "h";
const randomChar = chars.charAt(Math.floor(Math.random() * chars.length));
searchTerms.push(randomChar);

// Define a function to get the visible cells
function getVisibleCells() {
    return Array.from(document.querySelectorAll(".divTableCell"))
        .filter(cell => cell.style.display !== 'none')
        .map(cell => cell.textContent.trim());
}

// Run the tests
searchTerms.forEach(term => {
    // Set the search value
    document.querySelector("#mySearch").value = term;

    // Trigger the input event
    const event = new Event('input', {
        bubbles: true,
        cancelable: true,
    });
    document.querySelector("#mySearch").dispatchEvent(event);

    // Get the visible cells
    const visibleCells = getVisibleCells();

    // Log the results
    console.log(`Search term: ${term}`);
    console.log(`Visible cells: ${visibleCells.join(', ')}`);
});
