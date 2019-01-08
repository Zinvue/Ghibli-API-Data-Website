// functions that contain plotly documentation (table and bar graph) and return them
function tableGraph (arr) {
  var name = [];
    var score = [];
    for (data of arr) {
    name.push(data[0]);
    score.push(data[1]); 
}
  var tableData = [{
    type: 'table',
    columnorder: [1,2],
    columnwidth: [20, 20], 
    header: {
      values: [["<b>Films</b>"], ["<b>Rotten Tomato Scores</b>"]],
    align: ["center", "center"],
    height: 40,
      line: {width: 1, color: '#506784'},
      fill: {color: '#119DFF'},
      font: {family: "Georgia", size: 14, color: "white"}
    },
    cells: {
      values: [name, score],
      align: ["center", "center"],
    height: 30,
      line: {color: "#506784", width: 1},
    fill: {color: ['#25FEFD', 'white']},
      font: {family: "Georgia", size: 11, color: ["black"]} 
    }
  }]
  return tableData;
}

// BAR GRAPH
function barGraph(arr) {
  var name = [];
  var score = [];
  for (data of arr) {
    name.push(data[0]);
    score.push(data[1]);
//    console.log(name)
//    console.log(score)
}
  var barData = [
  {
    x: name,
    y: score,
    type: 'bar',
  }
];
return barData;
}

// puts functions into an object that AJAX later calls
function theGraphs(jason) {
    var a = {};
    var json = JSON.parse(jason);
    a['bar'] = barGraph(json);
    a['table'] = tableGraph(json); //return dictionary with json and data
    console.log(tableGraph(json)) //ignore
  return a;
}

//AJAX that gets information from films
function loadGraph() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function(){
    if (this.readyState === 4 && this.status === 200){
        var _theGraphs = theGraphs(this.response);
        Plotly.newPlot('myDiv', _theGraphs.bar);
        Plotly.plot('graph', _theGraphs.table);
        };
    }

     xhttp.open("GET", "/films");
     xhttp.send();
    
}
