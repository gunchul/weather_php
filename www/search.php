<?php
$now = new DateTime;
$search_date=$_POST["search_date"];
$region=$_POST["region"];

if ( strlen($search_date) == 0 || strlen($region) == 0 ) {
    $search_date = $now->format('Y-m-d');
    $search_year = $now->format('Y');
    $region = "newcastle";
}
else {
    $search_year = sprintf("%.4s", $search_date);
}

$cmd = sprintf("cat data/%s/%s_%s.txt", $search_year, $search_date, $region);
$output = shell_exec($cmd);
if ($output == NULL)
{
   $output = sprintf("No data(%s)", $cmd);
}
?>

<!DOCTYPE html>
<html lang="ko">
<title>Search Weather</title>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.2/jquery.min.js"></script>
  <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
<body>
<?php
echo $_POST["search_date"];
echo "<p>";
echo $_POST["region"];
?>
<p>
<form action="search.php" id="search" method="post">
  지역: 
  <div class="btn-group">
    <button type="button" class="btn btn-primary" onclick="submit_by_region('newcastle')">뉴카슬</button>
    <button type="button" class="btn btn-primary" onclick="submit_by_region('bondi')">시드니</button>
    <button type="button" class="btn btn-primary" onclick="submit_by_region('wollongong')">울릉공</button>
  </div>
  <br><br>                         
  날짜:
  <input type="date" value="<?php echo $search_date ?>" name="search_date" onchange="submit()">
  <br><br>
  <input type="hidden" id="region" name="region" value="<?php echo $region?>">
</form>
<br>
<div class="form-group">
  <label for="result">날씨:</label>
  <textarea style="font-family:consolas" class="form-control" rows="120" id="comment"><?php echo $output;?></textarea>
</div>

<script>
function submit_by_region(region) {
  document.getElementById("region").value = region;
  document.getElementById("search").submit();
}
</script>
</body>
</html>
