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
// Store offices table in array
$offices_query = $conn->query('SELECT * FROM offices');
$offices = array();
$offices_count = 0;
while($row = $offices_query->fetch(PDO::FETCH_ASSOC)){
    $offices[$offices_count] = $row;
    $offices_count ++;
}
// Store employees table in array
$employ_query = $conn->query('SELECT * FROM employees ORDER BY jobTitle');
$employ = array();
$employ_count = 0;
while($row = $employ_query->fetch(PDO::FETCH_ASSOC)){
    $employ[$employ_count] = $row;
    $employ_count ++;
}
?>
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" type="text/css" href="index.css">
    <title>index</title>
</head>
<body onload="officesLoad()">
    <!-- Navigation bar -->
    <?php include 'header.php' ?>     
    <!-- Button to return from products table to product lines -->
    <button type="button" id="b02" onclick="returnOffices()">Return to offices</button>
    <!-- Divs for offices and employees tables -->
    <div id="offices"></div>
    <div id="employees"></div>
    <!-- Include footer -->
    <?php include 'footer.php'; ?>
</body>
<script>
function officesLoad(){    
    // Convert offices array to javascript
    <?php echo "var js_offices = ". json_encode($offices) . ";\n" ?>
    // Start table and add headings
    var table2 = "<table><tr><th>city</th><th>phone</th><th>addressLine1</th><th>addressLine2</th><th>employees info</th></tr>";
    // Add rows
    for (i=0; i < js_offices.length; i++){
        table2 += "<tr>";
        // Add column values
        for (column in js_offices[i]){
            if (column == 'city' || column == 'phone' || column == 'addressLine1' || column == 'addressLine2'){
                table2 += "<td>" + js_offices[i][column] + "</td>";
                continue;
            }
        }
        table2 += "<td><button id=empbutton type=button onclick=employeeInfo(this) value="+js_offices[i]['officeCode']+">employees info</button></td></tr>";
    }
    table2 += "</table>";
    document.getElementById("offices").innerHTML = table2;
}
function employeeInfo(office){
    // Get office code
    var off_Code = office.value;
    // Convert employees array to javascript
    <?php echo "var js_employees = ". json_encode($employ) . ";\n" ?>
    // Start table and add headings
    var table3 = "<table><tr><th>full name"+"</th><th>job title</th><th>employee number</th><th>email address</th></tr>"
    for (i=0; i < js_employees.length; i++){
        table3 += "<tr>";
        // Add column values
        if (js_employees[i]['officeCode'] == off_Code){
            table3 += "<td>" + js_employees[i]['firstName'] + 
            " " + js_employees[i]['lastName'] + "</td>" + 
            "<td>" + js_employees[i]['jobTitle'] + "</td>" + 
            "<td>" + js_employees[i]['employeeNumber'] + "</td>" + 
            "<td>" + js_employees[i]['email'] + "</td>";
        }
        table3 += "</tr>";
    }
    document.getElementById("employees").innerHTML = table3;
    document.getElementById("b02").style.display="block";
    document.getElementById("offices").style.display="none";
    document.getElementById("employees").style.display="block"; 
}
function returnOffices(){
    document.getElementById("b02").style.display="none";
    document.getElementById("offices").style.display="block";
    document.getElementById("employees").style.display="none"; 
}
</script>
</html>