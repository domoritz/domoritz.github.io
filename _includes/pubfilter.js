(function() {
  var pubs = document.querySelectorAll(".publication");
  var yearElements = document.querySelectorAll(".pub-year");

  var clear = document.getElementById("clear-filters");

  var data = [];
  var allYears = {};

  pubs.forEach(function(element) {
    var item = JSON.parse(element.getAttribute("data-pub"));

    item.highlight = item.highlight ? "Yes" : "No";

    allYears[item.year] = 1;

    item.element = element;

    item.authors = (item.authors || []).filter(function(d) {
      return d !== "Dominik Moritz";
    });

    data.push(item);
  });

  var engine = itemsjs(data, {
    aggregations: {
      venue_tags: {
        size: 5
      },
      authors: {
        size: 6
      },
      awards: {
        size: 5
      },
      highlight: {
        size: 2
      },
      tags: {
        size: 6
      }
    }
  });

  var query = { filters: {} };

  function setAggs(aggs) {
    document.querySelectorAll("#facets > .facet").forEach(function(facet) {
      var id = facet.getAttribute("id");

      var buckets = aggs[id].buckets;

      var el = facet.querySelector("ul");
      if (buckets.length === 0) {
        el.innerHTML = "Empty";
      } else {
        el.innerHTML = "";

        buckets.forEach(function(bucket) {
          if (query.filters[id] && query.filters[id].indexOf(bucket.key) >= 0) {
            bucket.in_query = true;
          }
        });

        var maxDocCount = Math.max.apply(
          null,
          buckets.map(function(bucket) {
            return bucket.doc_count;
          })
        );

        buckets.forEach(function(bucket) {
          var child = document.createElement("li");

          var wrap = document.createElement("span");
          child.appendChild(wrap);

          var text = document.createElement("span");
          text.classList.add("limited");
          text.innerText = bucket.key;
          text.setAttribute("title", bucket.key);
          var number = document.createElement("span");
          number.classList.add("cnt");
          number.innerText = " (" + bucket.doc_count + ")";
          wrap.appendChild(text);
          wrap.appendChild(number);

          var barFull = document.createElement("div");
          barFull.classList.add("bar-full");
          child.append(barFull);

          var bar = document.createElement("div");
          bar.classList.add("bar");
          bar.style.width = "" + (bucket.doc_count / maxDocCount) * 100 + "%";
          barFull.append(bar);

          if (bucket.in_query) {
            child.classList.add("in-query");

            // remove filter
            child.onclick = function() {
              query.filters[id].splice(
                query.filters[id].indexOf(bucket.key),
                1
              );
              if (query.filters[id].length === 0) {
                delete query.filters[id];
              }
              search(query);
            };
          } else {
            // add to filter
            child.onclick = function() {
              if (query.filters[id]) {
                query.filters[id].push(bucket.key);
              } else {
                query.filters[id] = [bucket.key];
              }
              search(query);
            };
          }

          el.appendChild(child);
        });
      }
    });
  }

  // full text search is broken
  // var ftSearch = document.getElementById("ft-search");
  // ftSearch.oninput = function() {
  //   var val = ftSearch.value;

  //   if (val) {
  //     query.query = val;
  //   } else {
  //     delete query.val;
  //   }

  //   console.log(query);
  //   search(query);
  // }

  function search(query) {
    console.time("Search");

    var result = engine.search(Object.assign({ per_page: 1000 }, query));

    setAggs(result.data.aggregations);

    var counter = pubs.length - result.data.items.length;

    document.getElementById("count_hidden").innerText = counter;
    document.getElementById("count_total").innerText = pubs.length;

    pubs.forEach(function(element) {
      element.classList.add("hidden");
    });

    var visibleYears = {};
    result.data.items.forEach(function(item) {
      item.element.classList.remove("hidden");
      visibleYears[item.year] = 1;
    });

    yearElements.forEach(function(element) {
      element.classList.add("hidden");
    });
    Object.keys(allYears).forEach(function(year) {
      if (year in visibleYears) {
        document.getElementById("y" + year).classList.remove("hidden");
      }
    });

    // show or hide notification about filtered papers
    if (Object.keys(query.filters).length || query.query) {
      clear.classList.remove("hidden");
    } else {
      clear.classList.add("hidden");
    }

    console.timeEnd("Search");
  }

  clear.onclick = function() {
    query = { filters: {} };
    search(query);
  };

  search(query);

  document.getElementById("facets").classList.remove("hidden");
})();
