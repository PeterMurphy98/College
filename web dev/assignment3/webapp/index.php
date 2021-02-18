<?php
// Connect to database
$servername = "localhost";
$username = "root";
$password = "";
try {
    $conn = new PDO("mysql:host=$servername;dbname=classicmodels", $username, $password);
    // set the PDO error mode to exception
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    echo "Connected successfully" . '<br>';
}
catch(PDOException $e)
    {
        echo "Connection failed: " . $e->getMessage();
    }
// Store productLines and textDescription in arrays
$prodlines_query = $conn->query('SELECT * FROM productlines');
$prodlines = array();
$prodlines_count = 0;
$textDescription = array();
while($row = $prodlines_query->fetch(PDO::FETCH_ASSOC)){
    $prodlines[$prodlines_count] = $row['productLine'];
    $textDescription[$prodlines_count] = $row['textDescription'];
    $prodlines_count ++;
}
// Store products table in array
$products_query = $conn->query('SELECT * FROM products');
$products = array();
$products_count = 0;
while($row = $products_query->fetch(PDO::FETCH_ASSOC)){
    $products[$products_count] = $row;
    $products_count ++;
}
?>
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" type="text/css" href="index.css">
    <title>index</title>
</head>
<body onload="onLoad()">
    <!-- Navigation bar -->
    <?php include 'header.php' ?>
    <!-- Button to return from products table to product lines -->
    <button type="button" id="b01" onclick="returnProductLines()">Return to product lines</button>
    <!-- Divs for product lines, and products table -->
    <div id="prodlines"></div>
    <div id="products"></div>
    <?php include 'footer.php'; ?>
</body>
<script>
function onLoad(){
    // Convert productLine and textDescription to javascript variables
    <?php echo "var js_prodlines = ". json_encode($prodlines) . ";\n";
    echo "var js_textDescription = ". json_encode($textDescription) . ";\n" ?>
    // Add each productLine, textDescription and table link to a div
    for (i=0; i < js_prodlines.length; i++){
        document.getElementById('prodlines').innerHTML += 
        "<h3 class=h01>"+js_prodlines[i]+"</h3>" +
        "<a class=a01 onclick=viewProductLine(this) data-prodline="+ 
        js_prodlines[i]+" href=javascript:void(0)>Click to view prodcut line</a>" +
        "<p class = p01>" + js_textDescription[i] + "</p>";
    }
}
function viewProductLine(prod){    
    // Get productLine 
    var product_line = prod.dataset.prodline;
    // Convert products array to javascript
    <?php echo "var js_products = ". json_encode($products) . ";\n" ?>
    // Start table and add headings
    var table = "<table><tr>";
    for (column in js_products[0]){
        table += "<th>" + column + "</th>";
    }
    table += "</tr>"
    // Add rows
    for (i=0; i < js_products.length; i++){
        // Check productLine
        if (js_products[i]['productLine'].includes(product_line)){
            table += "<tr>";
            // Add column values
            for (column in js_products[i]){
                table += "<td>" + js_products[i][column] + "</td>";
            }
            table += "</tr>";
        }
    }
    table += "</table>";
    document.getElementById("products").innerHTML = table;
    document.getElementById("b01").style.display="block";
    document.getElementById("prodlines").style.display="none";
    document.getElementById("products").style.display="block"; 
}
function returnProductLines(){
    document.getElementById("b01").style.display="none";
    document.getElementById("prodlines").style.display="block";
    document.getElementById("products").style.display="none";
}
</script>
</html>