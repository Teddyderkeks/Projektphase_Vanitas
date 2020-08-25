<!DOCTYPE html>

<html>
	<head>
		<link rel="stylesheet" href="style.css" type="text/css">
		<title>HOME - Vanitas</title>
		<meta charset = "utf-8">
	</head>
	<body>
		<h1>Senden</h1>
		<?php
			$name = $_POST["name"];
			$kommentar = $_POST["kommentar"];

			if ($name =="" or $kommentar == ""){
			echo "Du musst zuerst beide Felder ausfüllen.";}
		?>
	</body>
</html>