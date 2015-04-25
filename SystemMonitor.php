<?php

$db_host = "localhost";
$db_user = "root";
$db_pass = "***";

$db_connection = mysql_connect($db_host,$db_user,$db_pass) or die ("could not connect");

$selct_db = mysql_select_db('location_id') or die ('database not found');

    if ($db_connection && $selct_db) {

        $query = "SELECT * FROM  `assosiate_location_with_id`";

        $fetch = mysql_query($query) or die ('fant ikke bruker');

        while ($row = mysql_fetch_assoc($fetch)) {


            if ($row['computer_status'] == '1' && $row['program_status'] == '1'){

                echo "<div class='location_area_green'>";

            }

            if ($row['computer_status'] == '1' && $row['program_status'] == '0'){

                echo "<div class='location_area_yellow'>";

            }

            if ($row['computer_status'] == '0' && $row['program_status'] == '0'){

                echo "<div class='location_area_red'>";

            }



            echo "Lokasjon: ";
            echo $row['location'];
            echo "<br>";
            echo "Id: ";
            echo $row['id'];
            echo "<br>";
            echo "Status pc: ";
            if ($row['computer_status'] == '1') {
                echo "OPPE";
            } else {
                echo "NEDE";
            }
            echo "<br>";
            echo "Status software: ";
            if ($row['program_status'] == '1') {
                echo "OPPE";
            } else {
                echo "NEDE";
            }
            echo "</div>";
        }


}
?>

