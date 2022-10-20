function toggleText1() {
    // Get all the elements from the page
    var points1 = document.getElementById("points1");
    var showMoreText1 = document.getElementById("moreText1");
    var buttonText1 = document.getElementById("textButton1");
    if (points1.style.display === "none") {
        showMoreText1.style.display = "none";

        points1.style.display = "inline";

        buttonText1.innerHTML = "Show More";
    } else {
        showMoreText1.style.display = "inline";

        points1.style.display = "none";

        buttonText1.innerHTML = "Show Less";
    }
}

function toggleText2() {
    var points2 = document.getElementById("points2");
    var showMoreText2 = document.getElementById("moreText2");
    var buttonText2 = document.getElementById("textButton2");
    if (points2.style.display === "none") {
        showMoreText2.style.display = "none";

        points2.style.display = "inline";

        buttonText2.innerHTML = "Show More";
    } else {
        showMoreText2.style.display = "inline";

        points2.style.display = "none";

        buttonText2.innerHTML = "Show Less";
    }
}