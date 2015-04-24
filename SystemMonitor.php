<?php

$db_host = "localhost";
$db_user = "root";
$db_pass = "hp36565a";




$db_connection = mysql_connect($db_host,$db_user,$db_pass) or die ("could not connect");

$selct_db = mysql_select_db('location_id') or die ('database not found');



    if ($db_connection && $selct_db) {

        $query = "SELECT * FROM  `assosiate_location_with_id`";

        $fetch = mysql_query($query) or die ('fant ikke bruker');

        while ($row = mysql_fetch_assoc($fetch)) {

            echo "<br>";
            echo "<br>";
            echo "Lokasjon: ";
            echo $row['location'];
            echo "<br>";
            echo "Id: ";
            echo $row['id'];
            echo "<br>";
            echo "Status PC: ";
            if ($row['computer_status'] == '1') {
                echo "OPPE";
            } else {
                echo "NEDE";
            }
            echo "<br>";
            echo "Status SOFTWARE: ";
            if ($row['program_status'] == '1') {
                echo "OPPE";
            } else {
                echo "NEDE";
            }
        }

}
?>