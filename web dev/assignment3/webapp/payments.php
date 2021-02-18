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
// Store payments table in array
$payments_query = $conn->query('SELECT * FROM payments ORDER BY paymentDate DESC;');
$payments = array();
$payments_count = 0;
while($row = $payments_query->fetch(PDO::FETCH_ASSOC)){
    $payments[$payments_count] = $row;
    $payments_count ++;
}
// Store customers table in array
$customers_query = $conn->query('SELECT * FROM customers');
$customers = array();
$customers_count = 0;
while($row = $customers_query->fetch(PDO::FETCH_ASSOC)){
    $customers[$customers_count] = $row;
    $customers_count ++;
}
?>

<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" type="text/css" href="index.css">
    <title>index</title>
</head>
<body onload="paymentsLoad()">
    <!-- Navigation bar -->
    <?php include 'header.php' ?>     
    <!-- Button to return from products table to product lines -->
    <!-- Divs for payments and customer tables -->
    <div id="payments"></div>
    <div id="customer"></div>
    <div id="customerpay"></div>
    <!-- Include footer -->
    <?php include 'footer.php'; ?>
</body>

<script>
function paymentsLoad(){    
    // Convert payments array to javascript
    <?php echo "var js_payments = ". json_encode($payments) . ";\n" ?>
    // Start table
    var table4 = "<table><tr><th>customer no.</th><th>check number</th><th>payment date</th><th>amount</th></tr>";
    // Add rows
    for (i=0; i < 20; i++){
        table4 += "<tr>";
        // Add column values
        for (column in js_payments[i]){
            if (column == 'customerNumber'){
                table4 += "<td><a onclick=viewCustomer(this) href=javascript:void(0)>" + js_payments[i][column] + "</a></td>";
                continue;
            }
            table4 += "<td>" + js_payments[i][column] + "</td>";    
        }
        table4 += "</tr>";
    }
    table4 += "</table>";
    document.getElementById("payments").innerHTML = "<h3 class=h02 >Recent Payments</h3>" + table4;
}
function viewCustomer(customer){
    // Convert customers array and payments array to javascript
    <?php echo "var js_customers = ". json_encode($customers) . ";\n"; 
    echo "var js_payments = ". json_encode($payments) . ";\n" ?>
    // Display customer payment history
    var table6 = "<table><tr><th>customer no.</th><th>check number</th><th>payment date</th><th>amount</th></tr>";
    var total_amount = 0;
    for (i=0; i < js_payments.length; i++){
        if (js_payments[i]['customerNumber'] == customer.innerHTML){
            table6 += "<tr>";
            // Add column values
            for (column in js_payments[i]){
                table6 += "<td>" + js_payments[i][column] + "</td>";  
                if (column == 'amount'){
                    total_amount += parseFloat(js_payments[i][column]);
                }  
            }
            table6 += "</tr>";
        }
    }
    table6 += "</table>";    
    // Display customer info
    var table5 = "<table><tr><th>customer no.</th><th>phone</th><th>slaes rep</th><th>credit limit</th><th>total payments</th></tr>";
    for (i=0; i < js_customers.length; i++){
        if (js_customers[i]['customerNumber'] == customer.innerHTML){
            table5 += "<tr><td>" + js_customers[i]['customerNumber'] + 
            "</td><td>" + js_customers[i]['phone'] + 
            "</td><td>" + js_customers[i]['salesRepEmployeeNumber'] + 
            "</td><td>"  + js_customers[i]['creditLimit'] + 
            "</td><td>"  + total_amount.toFixed(2) + "</td></tr></table";
            break;
        }
    }
    document.getElementById("customer").innerHTML = "<h3 class=h02 >Customer Details</h3>" + table5;
    document.getElementById("customerpay").innerHTML = "<h3 class=h02 >Customer Payment History</h3>" + table6;
}
</script>
</html>