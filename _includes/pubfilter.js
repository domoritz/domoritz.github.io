(function() {
  var elements = document.querySelectorAll(".publication, h2, .stop-marker");

  function showAll() {
    document.querySelectorAll(".hidden-pub-placeholder").forEach(function(element) {
      element.remove();
    });

    document.querySelectorAll(".hidden").forEach(function(element) {
      element.classList.remove("hidden");
    });
  };

  document.querySelector(".show-all").onclick = showAll;

  var counter = 0;
  elements.forEach(function(element) {
    if (element.tagName === "H2" || element.classList.contains("stop-marker")) {
      if (counter > 0) {
        var div = document.createElement("div");
        div.classList.add("hidden-pub-placeholder");
        var button = document.createElement("button");
        div.appendChild(button);
        button.innerHTML = "<div>" + counter + " hidden publications.</div><a href=\"#all\">Show all...</a>"
        button.onclick = showAll;

        element.parentNode.insertBefore(div, element);
        counter = 0;
      }
    } else if (!element.classList.contains("highlight")) {
      element.classList.add("hidden");
      counter++;
    }
  });
})();
