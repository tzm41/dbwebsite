<h1>Database Test</h1>
<?php
$servername = "localhost";
$username = "ztan";
$password = "ztan";
$dbname = "ztan";

try {
    $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
    // set the PDO error mode to exception
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    echo "Connected successfully"; 
    }
catch(PDOException $e)
    {
    echo "Connection failed: " . $e->getMessage();
    }


$sql = "SELECT id, name FROM test";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    echo "<table><tr><th>ID</th><th>Name</th></tr>";
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo "<tr><td>".$row["id"]."</td><td>".$row["name"]." </td></tr>";
    }
    echo "</table>";
} else {
    echo "<br>0 results";
}
$conn->close();
?>
