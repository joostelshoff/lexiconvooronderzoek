---
title: Graph
layout: page
---

# Termengrafiek

Een netwerkweergave van alle termen en hun onderlinge `[[wikilink]]`-relaties, vergelijkbaar met de graph-view in Obsidian. Sleep nodes om te herschikken, scroll om te zoomen, en klik op een term om naar de bijbehorende pagina te gaan.

<div id="graph-container" style="width:100%; height:75vh; border:1px solid #e1e1e1; border-radius:4px;"></div>

<script src="https://cdn.jsdelivr.net/npm/d3@7"></script>
<script>
(function () {
  fetch("{{ '/assets/graph-data.json' | relative_url }}")
    .then(function (r) { return r.json(); })
    .then(renderGraph)
    .catch(function (err) {
      document.getElementById("graph-container").textContent =
        "Kon graph-data.json niet laden: " + err;
    });

  function renderGraph(data) {
    var container = document.getElementById("graph-container");
    var width = container.clientWidth;
    var height = container.clientHeight;

    var svg = d3.select(container).append("svg")
      .attr("width", width)
      .attr("height", height);

    var g = svg.append("g");

    svg.call(d3.zoom().scaleExtent([0.2, 5]).on("zoom", function (event) {
      g.attr("transform", event.transform);
    }));

    var simulation = d3.forceSimulation(data.nodes)
      .force("link", d3.forceLink(data.links).id(function (d) { return d.id; }).distance(90))
      .force("charge", d3.forceManyBody().strength(-180))
      .force("center", d3.forceCenter(width / 2, height / 2))
      .force("collide", d3.forceCollide(34));

    var link = g.append("g")
      .attr("stroke", "#999")
      .attr("stroke-opacity", 0.6)
      .selectAll("line")
      .data(data.links)
      .join("line")
      .attr("stroke-width", 1.5);

    var node = g.append("g")
      .selectAll("g")
      .data(data.nodes)
      .join("g")
      .call(drag(simulation));

    node.append("circle")
      .attr("r", 7)
      .attr("fill", "#2a6df5")
      .attr("stroke", "#fff")
      .attr("stroke-width", 1.5)
      .style("cursor", "pointer")
      .on("click", function (event, d) { window.location.href = d.url; });

    node.append("text")
      .text(function (d) { return d.label; })
      .attr("x", 11)
      .attr("y", 4)
      .style("font-size", "11px")
      .style("font-family", "sans-serif")
      .style("pointer-events", "none");

    node.append("title").text(function (d) { return d.label; });

    simulation.on("tick", function () {
      link
        .attr("x1", function (d) { return d.source.x; })
        .attr("y1", function (d) { return d.source.y; })
        .attr("x2", function (d) { return d.target.x; })
        .attr("y2", function (d) { return d.target.y; });

      node.attr("transform", function (d) { return "translate(" + d.x + "," + d.y + ")"; });
    });

    function drag(simulation) {
      function dragstarted(event, d) {
        if (!event.active) simulation.alphaTarget(0.3).restart();
        d.fx = d.x; d.fy = d.y;
      }
      function dragged(event, d) {
        d.fx = event.x; d.fy = event.y;
      }
      function dragended(event, d) {
        if (!event.active) simulation.alphaTarget(0);
        d.fx = null; d.fy = null;
      }
      return d3.drag().on("start", dragstarted).on("drag", dragged).on("end", dragended);
    }
  }
})();
</script>
