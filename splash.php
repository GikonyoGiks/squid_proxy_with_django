<html>

...omitted HTML head and title...

<body>

 

...omitted Content...

n" value="Put Your Text Here" onclick="window.location.href='http://proxy.12contacts.io/manage/'" />
</form>
	 

<!--Accept Form -->

<h4>By clicking accept you accept the terms of usage explained below of WiFi Usage:</h4>

<?php

echo '<form action="' . htmlspecialchars($_GET["url"])  . '" target="_blank">

<input type="submit" value="Accept">

</form>'

?>

 

<body>

</html>
