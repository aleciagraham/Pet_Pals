function buildPlot() {
  /* data route */
  const url = "/api/pals";
  d3.json(url).then(function(response) {

    console.log(response);

    trace = {
      "type": "scattergeo",
      "locationmode": "USA-states",
      "lat": response["latitude"],
      "lon": response["longitude"],
      "text": response["hover_text"],
      "hoverinfo": "text",
      "marker": {
          "size": 50,
          "line": {
              "color": "rgb(8,8,8)",
              "width": 1
          },
      }
    }

    data = [trace]  

    const layout = {
      scope: "usa",
      title: "Pet Pals",
      showlegend: false,
      height: 600,
            // width: 980,
      geo: {
        scope: "usa",
        projection: {
          type: "albers usa"
        },
        showland: true,
        landcolor: "rgb(217, 217, 217)",
        subunitwidth: 1,
        countrywidth: 1,
        subunitcolor: "rgb(255,255,255)",
        countrycolor: "rgb(255,255,255)"
      }
    };

    Plotly.newPlot("plot", data, layout);
  });
}

buildPlot();
